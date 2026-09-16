# Database, storage, and cache isolation

Review every layer that can read or retain tenant data.

## Database

- Confirm tenant/resource policies exist for reads, inserts, updates, and deletes.
- Verify policies use the authenticated principal and trusted membership, not request parameters.
- Check policy behavior for missing, stale, or downgraded membership.
- Review joins, views, functions, triggers, reporting queries, and bulk jobs for implicit bypass.
- Identify service-role or owner connections and constrain them to explicit trusted workflows with audit logging.
- Test policy enforcement through the same path used by the application.

## Storage and asynchronous paths

- Derive object paths from trusted tenant/resource context.
- Authorize upload, download, rename, delete, signed URL creation, and metadata access.
- Review queues, exports, caches, search indexes, analytics, logs, notifications, and webhooks for tenant context.
- Prevent shared cache keys and background jobs from crossing tenant boundaries.
- Verify support or impersonation tools have explicit scope, expiry, audit trail, and least privilege.

Document provider controls as NOT_VERIFIED when they cannot be inspected or tested.
