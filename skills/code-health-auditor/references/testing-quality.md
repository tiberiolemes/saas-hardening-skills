# Test quality checklist

Prioritize tests that protect user-visible and security-relevant behavior:

- authentication, authorization, tenant isolation, and privilege changes;
- create, edit, delete, export, upload, billing, admin, webhook, and recovery flows as applicable;
- validation failures, permission denials, timeouts, retries, empty states, and partial failures;
- migration and data invariants affected by a change.

A useful test states the setup, trusted principal, expected behavior, and denial or failure property. Avoid tests that only increase line coverage or assert implementation details likely to change. Run the narrowest test first, then the full relevant suite and build.
