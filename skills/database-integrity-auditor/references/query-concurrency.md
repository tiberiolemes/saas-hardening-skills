# Query and concurrency review

Trace critical read/write paths with realistic data volume.

## Queries

- detect N+1 queries, redundant round trips, unbounded lists, unsafe sorting, and missing pagination;
- inspect filters and joins for tenant and ownership scope;
- check selected columns for unnecessary sensitive or large payloads;
- inspect indexes and query plans when available;
- confirm query timeouts, cancellation, and connection-pool behavior;
- distinguish a measured slow query from a hypothesis.

## Transactions and races

- group invariants that must commit atomically;
- inspect read-modify-write paths, uniqueness races, retries, and idempotency keys;
- check job deduplication and exactly-once assumptions;
- define behavior for partial external side effects;
- test concurrent create, update, delete, payment, webhook, and retry paths where relevant.

Record isolation level, locking behavior, evidence, and limitations. Never claim race resistance without a reproducible test or documented database guarantee.
