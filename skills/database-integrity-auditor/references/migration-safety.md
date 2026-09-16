# Migration safety procedure

Prefer expand–migrate–contract:

1. Add backward-compatible schema or code support.
2. Deploy code that can read both old and new shapes.
3. Backfill in bounded, resumable batches with monitoring and idempotency.
4. Verify counts, constraints, performance, and application behavior.
5. Switch reads/writes only after verification.
6. Remove old structures in a separately reviewed cleanup step.

Before an operational migration, document:

- data volume and lock duration;
- indexes and constraint build strategy;
- backup freshness and restore evidence;
- deploy ordering and compatibility window;
- rollback or forward-fix plan;
- validation queries and alert thresholds;
- owner, maintenance window, and stop condition.

Do not drop columns, tables, constraints, indexes, or data during an audit without explicit authorization, a verified recovery path, and evidence that all consumers have migrated.
