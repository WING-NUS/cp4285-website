#!/usr/bin/env python3
"""Credential-safe client for the fixed private YOURLS instance at soc-n.us."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Callable


BASE_URL = "https://soc-n.us"
API_URL = f"{BASE_URL}/yourls-api.php"
KEYCHAIN_SERVICE = "codex.yourls.soc-n.us"
KEYCHAIN_ACCOUNT = "api-signature"
ENV_SIGNATURE = "YOURLS_API_SIGNATURE"
DEFAULT_TITLE = "Short link"
DEFAULT_TIMEOUT_SECONDS = 20.0
MAX_RESPONSE_BYTES = 1_048_576
MAX_DESTINATION_CHARACTERS = 65_535


class YourlsError(Exception):
    def __init__(
        self,
        message: str,
        *,
        code: str = "error",
        exit_code: int = 2,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.exit_code = exit_code
        self.details = details or {}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        return None


@dataclass(frozen=True)
class ApiResponse:
    data: dict[str, Any]
    http_status: int


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))


def _contains_control(value: str) -> bool:
    return any(ord(char) < 32 or ord(char) == 127 for char in value)


def validate_destination(value: str) -> str:
    if not value or value != value.strip() or any(char.isspace() for char in value) or _contains_control(value):
        raise YourlsError("Destination URL contains whitespace or control characters", code="invalid_url")
    parsed = urllib.parse.urlsplit(value)
    if parsed.scheme.lower() not in {"http", "https"} or not parsed.hostname:
        raise YourlsError("Destination URL must use http or https and include a host", code="invalid_url")
    if parsed.username is not None or parsed.password is not None:
        raise YourlsError("Destination URL must not contain embedded credentials", code="invalid_url")
    try:
        _ = parsed.port
    except ValueError as exc:
        raise YourlsError("Destination URL contains an invalid port", code="invalid_url") from exc
    return value


def summarize_destination(value: str) -> dict[str, Any]:
    """Return a useful equality fingerprint without emitting secret-bearing URL components."""
    value = validate_destination(value)
    parsed = urllib.parse.urlsplit(value)
    hostname = parsed.hostname or ""
    display_host = f"[{hostname}]" if ":" in hostname else hostname
    port = parsed.port
    origin = f"{parsed.scheme.lower()}://{display_host}{f':{port}' if port is not None else ''}"
    return {
        "origin": origin,
        "path_segment_count": sum(1 for segment in parsed.path.split("/") if segment),
        "has_query": bool(parsed.query),
        "has_fragment": bool(parsed.fragment),
        "sha256": hashlib.sha256(value.encode("utf-8")).hexdigest(),
    }


def public_link_record(record: dict[str, Any]) -> dict[str, Any]:
    """Remove the exact destination before serializing a record to stdout."""
    public = {key: value for key, value in record.items() if key != "long_url"}
    if isinstance(record.get("long_url"), str):
        public["destination"] = summarize_destination(record["long_url"])
    return public


def read_destination_from_stdin(stream: Any | None = None) -> str:
    """Read one URL line without placing it in argv or echoing an interactive TTY."""
    stream = stream or sys.stdin
    terminal_state = None
    terminal_fd: int | None = None
    if stream is sys.stdin and getattr(stream, "isatty", lambda: False)():
        try:
            import termios

            terminal_fd = stream.fileno()
            terminal_state = termios.tcgetattr(terminal_fd)
            hidden_state = termios.tcgetattr(terminal_fd)
            hidden_state[3] &= ~termios.ECHO
            termios.tcsetattr(terminal_fd, termios.TCSADRAIN, hidden_state)
        except (ImportError, OSError):
            terminal_state = None
            terminal_fd = None
    try:
        line = stream.readline(MAX_DESTINATION_CHARACTERS + 2)
    finally:
        if terminal_state is not None and terminal_fd is not None:
            try:
                import termios

                termios.tcsetattr(terminal_fd, termios.TCSADRAIN, terminal_state)
            except (ImportError, OSError):
                pass
    if not line:
        raise YourlsError("Destination URL was not provided on standard input", code="missing_url")
    if len(line) > MAX_DESTINATION_CHARACTERS + 1:
        raise YourlsError("Destination URL is too long", code="invalid_url")
    if line.endswith("\n"):
        line = line[:-1]
    if line.endswith("\r"):
        line = line[:-1]
    if len(line) > MAX_DESTINATION_CHARACTERS:
        raise YourlsError("Destination URL is too long", code="invalid_url")
    return validate_destination(line)


def validate_keyword(value: str) -> str:
    if not value or value != value.strip() or len(value) > 100:
        raise YourlsError("Keyword must contain 1 to 100 non-whitespace characters", code="invalid_keyword")
    if _contains_control(value) or any(char.isspace() for char in value):
        raise YourlsError("Keyword must not contain whitespace or control characters", code="invalid_keyword")
    if any(char in value for char in "/?#"):
        raise YourlsError("Keyword must be one path segment without '/', '?', or '#'", code="invalid_keyword")
    return value


def parse_short_reference(value: str) -> str:
    if "://" not in value:
        return validate_keyword(value)

    parsed = urllib.parse.urlsplit(value)
    if parsed.scheme.lower() != "https" or (parsed.hostname or "").lower() != "soc-n.us":
        raise YourlsError("Short URL must use the https://soc-n.us origin", code="invalid_short_url")
    if parsed.username is not None or parsed.password is not None or parsed.query or parsed.fragment:
        raise YourlsError("Short URL must not contain credentials, a query, or a fragment", code="invalid_short_url")
    try:
        if parsed.port is not None:
            raise YourlsError("Short URL must not specify a port", code="invalid_short_url")
    except ValueError as exc:
        raise YourlsError("Short URL contains an invalid port", code="invalid_short_url") from exc
    path = parsed.path.removeprefix("/")
    if not path or "/" in path or parsed.path.endswith("/"):
        raise YourlsError("Short URL must contain exactly one keyword path segment", code="invalid_short_url")
    return validate_keyword(urllib.parse.unquote(path))


def canonical_short_url(keyword: str) -> str:
    keyword = validate_keyword(keyword)
    return f"{BASE_URL}/{urllib.parse.quote(keyword, safe='-._~')}"


def validate_returned_short_url(value: str) -> tuple[str, str]:
    keyword = parse_short_reference(value)
    canonical = canonical_short_url(keyword)
    if value != canonical:
        raise YourlsError(
            "YOURLS returned a non-canonical or unexpected short URL",
            code="unexpected_short_url",
            exit_code=6,
            details={"returned_short_url": value, "expected_origin": BASE_URL},
        )
    return keyword, canonical


def _keychain_item_exists() -> bool:
    security = shutil.which("security")
    if sys.platform != "darwin" or not security:
        return False
    try:
        result = subprocess.run(
            [security, "find-generic-password", "-a", KEYCHAIN_ACCOUNT, "-s", KEYCHAIN_SERVICE],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    return result.returncode == 0


def credential_status() -> dict[str, Any]:
    if os.environ.get(ENV_SIGNATURE, "").strip():
        return {"credential_available": True, "source": "environment"}
    if _keychain_item_exists():
        return {"credential_available": True, "source": "macos-keychain"}
    return {
        "credential_available": False,
        "source": None,
        "keychain_service": KEYCHAIN_SERVICE,
        "keychain_account": KEYCHAIN_ACCOUNT,
        "environment_fallback": ENV_SIGNATURE,
    }


def load_permanent_signature() -> tuple[str, str]:
    environment_value = os.environ.get(ENV_SIGNATURE, "").strip()
    if environment_value:
        if _contains_control(environment_value):
            raise YourlsError("Injected API signature is invalid", code="invalid_credential")
        return environment_value, "environment"

    security = shutil.which("security")
    if sys.platform == "darwin" and security:
        try:
            result = subprocess.run(
                [security, "find-generic-password", "-a", KEYCHAIN_ACCOUNT, "-s", KEYCHAIN_SERVICE, "-w"],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
                timeout=15,
                check=False,
            )
            value = result.stdout.strip() if result.returncode == 0 else ""
        except (OSError, subprocess.TimeoutExpired):
            value = ""
        if value and not _contains_control(value):
            return value, "macos-keychain"

    raise YourlsError(
        "YOURLS API credential is unavailable; configure Keychain or use the authenticated browser workflow",
        code="credential_unavailable",
        details={
            "keychain_service": KEYCHAIN_SERVICE,
            "keychain_account": KEYCHAIN_ACCOUNT,
            "environment_fallback": ENV_SIGNATURE,
        },
    )


def _numeric_status(data: dict[str, Any], fallback: int) -> int:
    candidate = data.get("statusCode", fallback)
    try:
        return int(candidate)
    except (TypeError, ValueError):
        return fallback


def _response_message(data: dict[str, Any]) -> str:
    message = data.get("message")
    return str(message) if message is not None else ""


def _is_not_found(data: dict[str, Any], http_status: int) -> bool:
    status = _numeric_status(data, http_status)
    message = _response_message(data).lower()
    return status == 404 or "not found" in message or "does not exist" in message


def _is_auth_error(data: dict[str, Any], http_status: int) -> bool:
    status = _numeric_status(data, http_status)
    message = _response_message(data).lower()
    return status in {401, 403} or any(
        marker in message for marker in ("authentication", "unauthorized", "invalid signature", "please log in")
    )


class ApiClient:
    def __init__(
        self,
        *,
        permanent_signature: str | None = None,
        opener: Any | None = None,
        clock: Callable[[], float] = time.time,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
    ) -> None:
        if permanent_signature is None:
            permanent_signature, source = load_permanent_signature()
        else:
            source = "injected-for-test"
        self._permanent_signature = permanent_signature
        self.credential_source = source
        self._opener = opener or urllib.request.build_opener(NoRedirect())
        self._clock = clock
        self._timeout = timeout

    def _auth_fields(self) -> dict[str, str]:
        timestamp = str(int(self._clock()))
        derived = hashlib.sha512(f"{timestamp}{self._permanent_signature}".encode("utf-8")).hexdigest()
        return {"timestamp": timestamp, "signature": derived, "hash": "sha512"}

    def request(self, action: str, parameters: dict[str, str] | None = None, *, mutation: bool = False) -> ApiResponse:
        payload = {"action": action, "format": "json", **self._auth_fields(), **(parameters or {})}
        encoded = urllib.parse.urlencode(payload).encode("utf-8")
        request = urllib.request.Request(
            API_URL,
            data=encoded,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "manage-socn-links/1.0",
            },
            method="POST",
        )

        http_status: int
        body: bytes
        final_url = API_URL
        try:
            with self._opener.open(request, timeout=self._timeout) as response:
                http_status = int(getattr(response, "status", response.getcode()))
                final_url = response.geturl()
                body = response.read(MAX_RESPONSE_BYTES + 1)
        except urllib.error.HTTPError as exc:
            http_status = int(exc.code)
            if 300 <= http_status < 400:
                if mutation:
                    raise YourlsError(
                        "The create request received a redirect and has an uncertain outcome; inspect server state before retrying",
                        code="mutation_uncertain",
                        exit_code=4,
                    ) from None
                raise YourlsError("YOURLS API redirect was blocked", code="redirect_blocked") from None
            try:
                body = exc.read(MAX_RESPONSE_BYTES + 1)
                final_url = exc.geturl()
            except (OSError, TimeoutError):
                if mutation:
                    raise YourlsError(
                        "The create error response could not be read and has an uncertain outcome; inspect server state before retrying",
                        code="mutation_uncertain",
                        exit_code=4,
                    ) from None
                raise YourlsError("Could not read the YOURLS API error response", code="connection_failed") from None
        except (urllib.error.URLError, TimeoutError, OSError):
            if mutation:
                raise YourlsError(
                    "The create request has an uncertain outcome; inspect server state before retrying",
                    code="mutation_uncertain",
                    exit_code=4,
                ) from None
            raise YourlsError("Could not connect to the YOURLS API", code="connection_failed") from None

        if final_url != API_URL and mutation:
            raise YourlsError(
                "The create request returned from an unexpected endpoint and has an uncertain outcome; inspect server state before retrying",
                code="mutation_uncertain",
                exit_code=4,
            )
        if final_url != API_URL:
            raise YourlsError("YOURLS API returned an unexpected origin or endpoint", code="unexpected_endpoint")
        if len(body) > MAX_RESPONSE_BYTES:
            if mutation:
                raise YourlsError(
                    "The create response exceeded the size limit and has an uncertain outcome; inspect server state before retrying",
                    code="mutation_uncertain",
                    exit_code=4,
                )
            raise YourlsError("YOURLS API response exceeded the size limit", code="response_too_large")

        try:
            parsed = json.loads(body.decode("utf-8-sig"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            if mutation:
                raise YourlsError(
                    "The create request returned malformed output and may have succeeded; inspect server state before retrying",
                    code="mutation_uncertain",
                    exit_code=4,
                ) from None
            raise YourlsError("YOURLS API returned malformed JSON", code="malformed_response") from None
        if not isinstance(parsed, dict):
            if mutation:
                raise YourlsError(
                    "The create request returned an unexpected response and may have succeeded; inspect server state before retrying",
                    code="mutation_uncertain",
                    exit_code=4,
                )
            raise YourlsError("YOURLS API returned an unexpected JSON shape", code="malformed_response")
        if _is_auth_error(parsed, http_status):
            raise YourlsError("YOURLS API authentication failed", code="authentication_failed")
        if mutation and (http_status >= 500 or _numeric_status(parsed, http_status) >= 500):
            raise YourlsError(
                "The server failed after receiving the create request; inspect server state before retrying",
                code="mutation_uncertain",
                exit_code=4,
            )
        return ApiResponse(parsed, http_status)


def _extract_keyword(data: dict[str, Any]) -> str | None:
    candidates: list[str] = []
    for container_name in ("url", "link"):
        container = data.get(container_name)
        if isinstance(container, dict) and isinstance(container.get("keyword"), str):
            candidates.append(container["keyword"])
    if isinstance(data.get("keyword"), str):
        candidates.append(data["keyword"])
    short_urls = [data.get("shorturl")]
    link = data.get("link")
    if isinstance(link, dict):
        short_urls.append(link.get("shorturl"))
    candidates.extend(parse_short_reference(value) for value in short_urls if isinstance(value, str) and value)
    unique = set(candidates)
    if len(unique) > 1:
        raise YourlsError("YOURLS returned conflicting keywords", code="record_mismatch", exit_code=6)
    return candidates[0] if candidates else None


def _extract_long_url(data: dict[str, Any]) -> str | None:
    candidates: list[str] = []
    if isinstance(data.get("longurl"), str) and data["longurl"]:
        candidates.append(data["longurl"])
    for container_name in ("url", "link"):
        container = data.get(container_name)
        if isinstance(container, dict) and isinstance(container.get("url"), str) and container["url"]:
            candidates.append(container["url"])
    if len(set(candidates)) > 1:
        raise YourlsError("YOURLS returned conflicting destinations", code="record_mismatch", exit_code=6)
    return candidates[0] if candidates else None


def _extract_short_url(data: dict[str, Any], keyword: str | None = None) -> str | None:
    candidates = [data.get("shorturl")]
    link = data.get("link")
    if isinstance(link, dict):
        candidates.append(link.get("shorturl"))
    validated = [validate_returned_short_url(value) for value in candidates if isinstance(value, str) and value]
    if len({canonical for _, canonical in validated}) > 1:
        raise YourlsError("YOURLS returned conflicting short URLs", code="record_mismatch", exit_code=6)
    if validated:
        returned_keyword, canonical = validated[0]
        if keyword is not None and returned_keyword != keyword:
            raise YourlsError("YOURLS returned a short URL for a different keyword", code="record_mismatch", exit_code=6)
        return canonical
    if keyword:
        return canonical_short_url(keyword)
    return None


def inspect_link(client: ApiClient, short_reference: str) -> dict[str, Any] | None:
    requested_keyword = parse_short_reference(short_reference)
    response = client.request("expand", {"shorturl": requested_keyword})
    if _is_not_found(response.data, response.http_status):
        return None
    long_url = _extract_long_url(response.data)
    if not long_url:
        raise YourlsError("YOURLS expand response did not contain a destination", code="unexpected_response")
    long_url = validate_destination(long_url)
    keyword = _extract_keyword(response.data) or requested_keyword
    keyword = validate_keyword(keyword)
    if keyword != requested_keyword:
        raise YourlsError(
            "YOURLS returned a different keyword than requested",
            code="record_mismatch",
            exit_code=6,
            details={"requested_keyword": requested_keyword, "returned_keyword": keyword},
        )
    short_url = _extract_short_url(response.data, keyword)
    return {"keyword": keyword, "short_url": short_url, "long_url": long_url}


def get_link_stats(client: ApiClient, short_reference: str) -> dict[str, Any] | None:
    expanded = inspect_link(client, short_reference)
    if expanded is None:
        return None
    response = client.request("url-stats", {"shorturl": expanded["keyword"]})
    if _is_not_found(response.data, response.http_status):
        return None
    link = response.data.get("link")
    if not isinstance(link, dict):
        raise YourlsError("YOURLS statistics response did not contain a link record", code="unexpected_response")
    returned_keyword = _extract_keyword(response.data) or expanded["keyword"]
    returned_long_url = _extract_long_url(response.data)
    returned_short_url = _extract_short_url(response.data, returned_keyword)
    if returned_keyword != expanded["keyword"] or returned_long_url != expanded["long_url"]:
        raise YourlsError(
            "YOURLS statistics did not match the expanded record",
            code="record_mismatch",
            exit_code=6,
        )
    clicks: int | str | None = link.get("clicks")
    try:
        clicks = int(clicks) if clicks is not None else None
    except (TypeError, ValueError):
        clicks = str(clicks)
    return {
        "keyword": returned_keyword,
        "short_url": returned_short_url,
        "long_url": returned_long_url,
        "title": link.get("title") if isinstance(link.get("title"), str) else None,
        "created_at": link.get("timestamp") if isinstance(link.get("timestamp"), str) else None,
        "clicks": clicks,
    }


def _response_succeeded(response: ApiResponse) -> bool:
    if "status" in response.data:
        return str(response.data.get("status", "")).lower() == "success"
    if "statusCode" in response.data:
        return _numeric_status(response.data, response.http_status) == 200
    return response.http_status == 200


def create_link(
    client: ApiClient,
    destination: str,
    *,
    keyword: str | None = None,
    title: str | None = None,
) -> dict[str, Any]:
    destination = validate_destination(destination)
    if keyword is not None:
        keyword = validate_keyword(keyword)
        existing = inspect_link(client, keyword)
        if existing is not None:
            if existing["long_url"] == destination:
                return {"status": "already_present", "mutation_performed": False, **existing}
            raise YourlsError(
                "Requested keyword is already mapped to another destination",
                code="keyword_collision",
                exit_code=5,
                details={
                    "keyword": keyword,
                    "existing_short_url": existing["short_url"],
                    "existing_destination": summarize_destination(existing["long_url"]),
                },
            )
    if title is not None and (_contains_control(title) or len(title) > 1000):
        raise YourlsError("Title contains control characters or is too long", code="invalid_title")

    effective_title = title if title is not None and title.strip() else DEFAULT_TITLE

    parameters = {"url": destination, "title": effective_title}
    if keyword is not None:
        parameters["keyword"] = keyword
    response = client.request("shorturl", parameters, mutation=True)

    if not _response_succeeded(response):
        try:
            returned_keyword = _extract_keyword(response.data)
            returned_keyword = validate_keyword(returned_keyword) if returned_keyword else None
            returned_short_url = _extract_short_url(response.data, returned_keyword)
            if returned_keyword and returned_short_url:
                existing = inspect_link(client, returned_keyword)
                if existing is not None and existing["long_url"] == destination:
                    return {"status": "already_present", "mutation_performed": False, **existing}
        except YourlsError:
            pass
        raise YourlsError(
            "YOURLS rejected the create request",
            code="create_rejected",
            details={"status_code": _numeric_status(response.data, response.http_status)},
        )

    try:
        returned_keyword = _extract_keyword(response.data)
        returned_keyword = validate_keyword(returned_keyword) if returned_keyword else None
        returned_short_url = _extract_short_url(response.data, returned_keyword)
    except YourlsError:
        raise YourlsError(
            "The create request returned an unsafe or inconsistent record and may have succeeded; inspect server state before retrying",
            code="mutation_uncertain",
            exit_code=4,
        ) from None
    if not returned_keyword or not returned_short_url:
        raise YourlsError(
            "The create request may have succeeded but returned no usable short URL; inspect server state before retrying",
            code="mutation_uncertain",
            exit_code=4,
        )

    try:
        verified = inspect_link(client, returned_keyword)
    except YourlsError:
        raise YourlsError(
            "The created link could not be verified and has an uncertain outcome; inspect server state before retrying",
            code="mutation_uncertain",
            exit_code=4,
            details={"returned_short_url": returned_short_url},
        ) from None
    if verified is None or verified["long_url"] != destination:
        raise YourlsError(
            "The created link could not be verified; inspect server state before retrying",
            code="mutation_uncertain",
            exit_code=4,
            details={"returned_short_url": returned_short_url},
        )
    if keyword is not None and returned_keyword != keyword:
        raise YourlsError(
            "YOURLS created a sanitized keyword different from the request; review the created record",
            code="server_changed_keyword",
            exit_code=6,
            details={
                "requested_keyword": keyword,
                "created_keyword": returned_keyword,
                **public_link_record(verified),
            },
        )
    return {"status": "created", "mutation_performed": True, **verified}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("credential-status", help="Check credential availability without revealing it")
    subparsers.add_parser("version", help="Read the YOURLS version")

    inspect_parser = subparsers.add_parser("inspect", help="Expand and verify one exact short link")
    inspect_parser.add_argument("short_reference", help="Keyword or full https://soc-n.us short URL")

    stats_parser = subparsers.add_parser("stats", help="Get verified per-link statistics")
    stats_parser.add_argument("short_reference", help="Keyword or full https://soc-n.us short URL")

    create_parser = subparsers.add_parser("create", help="Create or reuse one verified short link")
    create_parser.add_argument(
        "--url-stdin",
        action="store_true",
        required=True,
        help="Read one destination URL line from standard input without echoing it",
    )
    create_parser.add_argument("--keyword", help="Optional requested short keyword")
    create_parser.add_argument("--title", help="Optional title")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "credential-status":
            emit({"status": "ok", **credential_status()})
            return 0

        client = ApiClient()
        if args.command == "version":
            response = client.request("version")
            version = response.data.get("version")
            if not isinstance(version, str):
                raise YourlsError("YOURLS version response was unexpected", code="unexpected_response")
            emit({"status": "success", "operation": "version", "version": version})
            return 0
        if args.command == "inspect":
            record = inspect_link(client, args.short_reference)
            if record is None:
                emit({"status": "not_found", "operation": "inspect", "keyword": parse_short_reference(args.short_reference)})
                return 3
            emit({"status": "success", "operation": "inspect", **public_link_record(record)})
            return 0
        if args.command == "stats":
            stats = get_link_stats(client, args.short_reference)
            if stats is None:
                emit({"status": "not_found", "operation": "stats", "keyword": parse_short_reference(args.short_reference)})
                return 3
            emit({"status": "success", "operation": "stats", **public_link_record(stats)})
            return 0
        if args.command == "create":
            result = create_link(client, read_destination_from_stdin(), keyword=args.keyword, title=args.title)
            emit({"operation": "create", **public_link_record(result)})
            return 0
        raise YourlsError("Unsupported command", code="unsupported_command")
    except YourlsError as exc:
        emit({"status": "error", "error": exc.code, "message": exc.message, **exc.details})
        return exc.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
