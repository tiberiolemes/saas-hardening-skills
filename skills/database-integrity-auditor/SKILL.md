---
name: database-integrity-auditor
description: Review SaaS database schema, constraints, migrations, queries, transactions, concurrency, indexes, and data-integrity risks.
---

# Database integrity auditor

Review the database as a correctness, security, and operational boundary. Preserve data and avoid destructive migrations during an audit.

## Correction mode

Do not stop at the report. After classifying findings, implement safe, proportionate, well-understood integrity fixes within the user's authorization, then run integrity, regression, and concurrency checks. Mark a finding `RESOLVED` only when the verification evidence is recorded; document unsafe, ambiguous, destructive, or unauthorized changes as `ACCEPTED`, `BLOCKED`, or `NOT_VERIFIED`.

## Workflow

1. Inventory schema, migrations, foreign keys, unique/check constraints, nullability, tenant keys, timestamps, soft deletes, and ownership relationships.
2. Trace critical writes and reads for validation, transactions, idempotency, authorization scope, error handling, and partial failure.
3. Inspect indexes, query plans where available, pagination, N+1 patterns, redundant round trips, locking, race conditions, and isolation levels.
4. Assess migration safety using an expand–migrate–contract approach and document backup, rollback, and compatibility requirements.
5. Classify findings P0–P3, fix only authorized issues, and run integrity, regression, and concurrency checks.
6. Write docs/audit/03-database.md with evidence, commands, residual risk, and gate recommendation.

Read [references/schema-integrity.md](references/schema-integrity.md), [references/query-concurrency.md](references/query-concurrency.md), and [references/migration-safety.md](references/migration-safety.md).
