# Authenticated browser workflows

Use these workflows only after reading and following the installed Browser
skill. Honor an explicitly selected browser. Otherwise prefer a browser profile
that already has the required `soc-n.us` session.

Never inspect cookies, local storage, browser profiles, password stores, or
session stores. If signed out, show the selected browser and ask the user to
sign in there. Resume only after verifying the visible account and the exact
`https://soc-n.us` origin.

Use current DOM evidence to locate controls. Prefer stable attributes and
accessible labels. YOURLS row IDs and nonces are dynamic; never copy them into
this skill or guess them. Do not call internal admin AJAX endpoints directly.

## Browser creation fallback

Use only when the user requested creation and the API credential is unavailable.

1. Open `https://soc-n.us/admin/` and authenticate through the visible browser.
2. Identify the standard add-link form from the live DOM.
3. Fill the exact destination and optional keyword supplied by the user. Fill
   the title with the user's value or the literal `Short link`; never leave it
   empty because stock YOURLS may fetch the destination to discover a title.
4. Re-read the values and submit once.
5. Verify the resulting row contains the returned short URL and destination.
6. If the response is ambiguous, search once for the exact destination and
   require one unambiguous result before reporting success. Do not resubmit.

## Edit

1. Require the current keyword or full short URL.
2. Run API `inspect` and `stats` to capture the current destination fingerprint,
   title, and click count. Obtain the complete destination only from one exact
   admin row in the visible browser.
3. If changing the keyword, inspect the proposed keyword. Stop on a collision
   unless it already identifies the same record.
4. Open the admin page and use its search UI to locate the exact current
   keyword. Require exactly one matching row and verify its destination.
5. Activate that row's Edit control. Build locators from a fresh DOM snapshot;
   do not rely on the row's position.
6. Preserve the current title unless the user requested a title change.
7. Re-read the record immediately before mutation. If it changed since the
   initial lookup, stop for user direction.
8. Keep the exact current and proposed destinations visible in the admin UI.
   In chat, show their origins and SHA-256 fingerprints with the keyword, short
   URL, and title. Warn about the effect on existing links and QR codes. Obtain
   action-time confirmation.
9. Fill only the requested fields, verify their values, and activate Save once.
10. Verify the saved destination through API `inspect`. When the keyword
    changed, require the old keyword to be `not_found` and the new keyword to
    match the expected destination.
11. If save completion is ambiguous, inspect both old and new keywords before
    considering any further action. Never save blindly a second time.

## Per-link detailed statistics

Use the API for title, creation timestamp, and aggregate clicks. If the user
requests referrers, geography, individual visits, or time-series detail:

1. Resolve the exact keyword with API `inspect` and `stats`.
2. Locate exactly one matching admin row.
3. Open that row's Statistics control.
4. Verify the page identifies the same keyword and destination.
5. Read only the requested statistics. Do not change filters or settings beyond
   what the request needs.

Never visit the public short URL to gather statistics.

## Delete

Deletion is destructive and always requires fresh confirmation.

1. Require an exact keyword or full short URL. Refuse deletion based only on a
   long destination, partial text, a list position, or a broad cleanup request.
2. Run API `stats`; require the record to exist and capture its complete short
   URL, destination origin and fingerprint, title, and click count.
3. Open the admin page, locate exactly one row with the same keyword, and verify
   the same destination.
4. Re-run API `stats` immediately before confirmation. Stop if the keyword,
   destination, or title changed.
5. Keep the exact destination visible in the authenticated admin UI. Present
   the short URL, title, destination origin and SHA-256 fingerprint in chat;
   warn that the short URL and its QR codes will stop working. Obtain explicit
   action-time confirmation for this one record.
6. After confirmation, run a fresh API lookup and freshly locate the admin row.
   Reverify the keyword, complete destination fingerprint, and title against
   the confirmed record. If anything changed, stop and request a new
   confirmation. Build a fresh locator for that verified row.
7. Activate the freshly verified row's Delete control once. Accept the site's
   deletion confirmation dialog once.
8. Run a fresh API `stats` or `inspect` lookup. Report success only when it
   returns `not_found`.
9. If the keyword remains, the response is malformed, or the keyword now maps
   to another destination, stop and report the unresolved state. Never click
   Delete again automatically.

Do not batch deletions. Confirm and verify each record separately unless a
future reviewed atomic compare-and-delete API explicitly supports safe batch
semantics.
