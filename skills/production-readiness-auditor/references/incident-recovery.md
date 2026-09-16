# Incident and recovery checklist

## Resilience

Review timeouts, bounded retries, backoff, circuit behavior, graceful shutdown, queue draining, idempotency, rate limits, overload handling, and isolation of external dependencies. Confirm failures do not create duplicate billing, lost writes, privilege bypass, or misleading success messages.

## Backup and recovery

Document:

- protected data and backup frequency;
- encryption and access control;
- retention and deletion behavior;
- recovery point and recovery time objectives;
- restore procedure, owner, dependencies, and validation;
- last restore drill and evidence;
- rollback, failover, and communications.

A backup configuration is not restore evidence. Do not test recovery destructively against production. If no drill or owner exists, record the gap as a finding or NOT_VERIFIED and state the next safe action.

## Incident readiness

Check severity definitions, escalation, contact ownership, evidence preservation, credential rotation, customer communication, post-incident review, and runbooks for common failure modes. Keep real incident secrets and personal data out of the repository.
