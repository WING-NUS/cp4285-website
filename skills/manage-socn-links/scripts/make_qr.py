#!/usr/bin/env python3
"""Generate deterministic local QR files for one verified soc-n.us short URL."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import uuid
import urllib.parse
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "_vendor"))

try:
    import segno
except ImportError as exc:  # pragma: no cover - installation integrity failure
    raise SystemExit("Bundled Segno QR encoder is missing") from exc


BASE_URL = "https://soc-n.us"


class QrError(Exception):
    pass


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))


def validate_short_url(value: str) -> tuple[str, str]:
    if not value or value != value.strip() or any(ord(char) < 32 or ord(char) == 127 for char in value):
        raise QrError("Short URL contains whitespace or control characters")
    parsed = urllib.parse.urlsplit(value)
    if parsed.scheme.lower() != "https" or (parsed.hostname or "").lower() != "soc-n.us":
        raise QrError("Short URL must use the https://soc-n.us origin")
    if parsed.username is not None or parsed.password is not None or parsed.query or parsed.fragment:
        raise QrError("Short URL must not contain credentials, a query, or a fragment")
    try:
        if parsed.port is not None:
            raise QrError("Short URL must not specify a port")
    except ValueError as exc:
        raise QrError("Short URL contains an invalid port") from exc
    path = parsed.path.removeprefix("/")
    if not path or "/" in path or parsed.path.endswith("/"):
        raise QrError("Short URL must contain exactly one keyword path segment")
    keyword = urllib.parse.unquote(path)
    if (
        not keyword
        or len(keyword) > 100
        or any(char.isspace() for char in keyword)
        or any(ord(char) < 32 or ord(char) == 127 for char in keyword)
        or any(char in keyword for char in "/?#")
    ):
        raise QrError("Short URL contains an invalid keyword")
    canonical = f"{BASE_URL}/{urllib.parse.quote(keyword, safe='-._~')}"
    if value != canonical:
        raise QrError("Short URL must be in canonical encoded form")
    return keyword, canonical


def sanitize_stem(value: str) -> str:
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return (stem[:60] or "short-link")


def _file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_file(path: Path, extension: str) -> None:
    content = path.read_bytes()
    if len(content) < 100:
        raise QrError(f"Generated {extension.upper()} file is unexpectedly small")
    if extension == "png" and not content.startswith(b"\x89PNG\r\n\x1a\n"):
        raise QrError("Generated PNG has an invalid signature")
    if extension == "svg" and b"<svg" not in content[:500]:
        raise QrError("Generated SVG has an invalid header")
    if extension == "pdf" and not content.startswith(b"%PDF"):
        raise QrError("Generated PDF has an invalid header")


def _save_atomic(qr: Any, final_path: Path, extension: str) -> None:
    temporary = final_path.with_name(f".{final_path.stem}.{uuid.uuid4().hex}.tmp.{extension}")
    try:
        if extension == "png":
            qr.save(temporary, scale=10, border=4, dark="#000000", light="#ffffff")
        else:
            qr.save(temporary, scale=8, border=4, dark="#000000", light="#ffffff")
        _validate_file(temporary, extension)
        try:
            os.link(temporary, final_path)
        except FileExistsError:
            if not final_path.is_symlink() and final_path.is_file() and _file_digest(final_path) == _file_digest(temporary):
                return
            raise QrError(f"Output file already exists with different contents: {final_path}")
    finally:
        if temporary.exists():
            temporary.unlink()


def generate_qr_files(short_url: str, output_dir: Path, output_format: str, basename: str | None = None) -> dict[str, Any]:
    keyword, canonical = validate_short_url(short_url)
    output_dir = output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    payload_digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    base = sanitize_stem(basename if basename is not None else keyword)
    stem = f"{base}-{payload_digest[:10]}"

    formats = {
        "svg": ["svg"],
        "png": ["png"],
        "pdf": ["pdf"],
        "both": ["svg", "png"],
        "all": ["svg", "png", "pdf"],
    }[output_format]
    qr = segno.make_qr(canonical, error="q", boost_error=False)
    files: list[dict[str, Any]] = []
    for extension in formats:
        final_path = output_dir / f"{stem}.{extension}"
        _save_atomic(qr, final_path, extension)
        files.append(
            {
                "format": extension,
                "path": str(final_path),
                "bytes": final_path.stat().st_size,
                "sha256": _file_digest(final_path),
            }
        )
    return {
        "status": "success",
        "operation": "generate_qr",
        "short_url": canonical,
        "keyword": keyword,
        "payload_sha256": payload_digest,
        "error_correction": "Q",
        "files": files,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--short-url", required=True, help="Verified https://soc-n.us short URL")
    parser.add_argument("--output-dir", required=True, type=Path, help="Directory for generated files")
    parser.add_argument("--format", choices=("svg", "png", "pdf", "both", "all"), default="both")
    parser.add_argument("--basename", help="Optional safe filename stem; a payload digest is always appended")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        emit(generate_qr_files(args.short_url, args.output_dir, args.format, args.basename))
        return 0
    except (QrError, OSError, KeyError) as exc:
        emit({"status": "error", "error": "qr_generation_failed", "message": str(exc)})
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
