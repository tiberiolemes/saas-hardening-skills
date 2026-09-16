# Schema and integrity checklist

For each important entity, record its identifier, tenant key, ownership path, lifecycle, and constraints.

Review:

- foreign keys and delete/update actions;
- unique constraints that include the correct tenant scope;
- check constraints, enum boundaries, numeric precision, and valid state transitions;
- nullability and defaults;
- timestamps, timezone, clock source, and audit fields;
- soft-delete semantics and uniqueness with deleted rows;
- tenant keys on direct and join tables;
- sensitive data classification, retention, and masking;
- indexes that support authorization predicates and critical access paths;
- views, triggers, functions, and materialized data that can become stale or bypass controls.

Use the database to enforce invariants that must hold regardless of client or application bugs. Do not weaken constraints to make a failing test pass.
