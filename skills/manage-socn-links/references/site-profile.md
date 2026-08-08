# soc-n.us site profile

## Installation

- Base URL: `https://soc-n.us`
- API URL: `https://soc-n.us/yourls-api.php`
- Admin URL: `https://soc-n.us/admin/`
- Allowed origin: `https://soc-n.us`
- Observed version on 2026-08-04: YOURLS 1.10.2

Treat the observed version as context, not a permanent guarantee. Reinspect the
live page when browser controls differ from this profile.

## Supported core API operations

Send HTTPS POST form data and request JSON output.

| Purpose | Action | Required task parameter |
|---|---|---|
| Create/shorten | `shorturl` | `url`; optional `keyword`, `title` |
| Expand/verify | `expand` | `shorturl` |
| Per-link statistics | `url-stats` | `shorturl` |
| Version | `version` | none |

Stock YOURLS exposes no public edit, delete, or QR action. Use the authenticated
admin UI for edits and deletion. Generate QR files locally.

The `url-stats` response can provide `link.shorturl`, `link.url`, `link.title`,
`link.timestamp`, `link.ip`, and `link.clicks`. Do not expose `link.ip` in
normal results, and replace `link.url` with the safe destination summary below.
Individual visits, referrers, geography, and time-series detail require the
exact record's browser statistics page.

Official references:

- API: https://yourls.org/docs/guide/advanced/api
- Passwordless API: https://yourls.org/docs/guide/advanced/passwordless-api
- Form and nonce security: https://yourls.org/docs/development/form-security

## API authentication

Prefer the account-specific YOURLS API signature because it is usable for API
requests but cannot sign in to the admin UI. The API signature is visible on
the authenticated YOURLS **Tools** page.

Store it as a generic password in macOS Keychain using Keychain Access:

- Service: `codex.yourls.soc-n.us`
- Account: `api-signature`
- Password: the permanent YOURLS API signature

Do not paste the signature into chat or place it in a file. The API client reads
the Keychain item at runtime and derives a time-limited SHA-512 request
signature from the current timestamp. It sends only the timestamp and derived
signature in the HTTPS POST body.

Trusted secret managers may inject `YOURLS_API_SIGNATURE` as a fallback. Never
set it in shell profiles, committed environment files, skill files, or command
arguments.

Changing `YOURLS_COOKIEKEY` invalidates permanent API signatures. Session or
signature expiry requires reauthentication; it never authorizes a retry of an
uncertain mutation.

## Input contract

- Destination URLs must use `http` or `https`, contain a hostname, and contain
  no embedded username or password.
- Preserve destination path, query, and fragment exactly.
- Keywords must be 1–100 characters and must contain no slash, query marker,
  fragment marker, whitespace, or control character.
- A full short URL must be HTTPS on `soc-n.us`, have no user information, port,
  query, or fragment, and contain exactly one path segment.
- YOURLS can sanitize custom keywords. Compare the returned keyword with the
  requested value and stop for review if they differ.
- Do not assume whether duplicate long destinations are enabled. Interpret the
  returned record and verify it instead.
- Always send a nonempty title. Use the literal local default `Short link` when
  the user did not provide one; an omitted title makes stock YOURLS perform a
  server-side request to fetch the destination's page title.

## Safe destination reporting

Preserve exact destination URLs in memory for API submission and equality
checks, but treat every path, query string, and fragment as potentially
secret-bearing. Supply a creation destination only as the single line read by
`create --url-stdin`; never place it in argv, an environment variable, a shell
pipeline command, a here-document, or a temporary file. Normal CLI output must
contain only:

- the scheme and host origin;
- path-segment count;
- whether a query or fragment exists; and
- a SHA-256 fingerprint of the complete exact destination.

Never emit the exact destination in command output, error details, screenshots,
or chat. When action-time review needs the complete value, leave it visible to
the user in the authenticated admin UI and refer to its fingerprint in chat.

## QR contract

- Encode the complete final `https://soc-n.us/<keyword>` value, not the long
  destination or admin URL.
- Prefer a server-verified short URL. For a standalone QR request, allow the
  exact canonical short URL supplied by the user and disclose when server
  existence and destination could not be verified.
- Generate files offline with the bundled Segno 1.6.6 encoder.
- Use error correction Q, a four-module quiet zone, black modules, and a white
  background.
- Default to SVG and PNG. Generate PDF only when requested.
- Never follow the short URL as a QR verification step.
