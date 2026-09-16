---
name: production-readiness-auditor
description: Review SaaS production configuration, observability, release safety, resilience, backups, recovery, health checks, and operational ownership.
---

# Production readiness auditor

Assess whether the application can be operated safely in its actual deployment context. Do not claim readiness when provider or production evidence is unavailable.

## Workflow

1. Inventory environments, configuration, secrets, build and deploy paths, permissions, dependencies, source maps, debug behavior, and security headers.
2. Review structured logs, redaction, correlation IDs, metrics, health checks, alerts, audit trails, and ownership of critical signals.
3. Review releases, migrations, compatibility, rollback, feature flags, graceful shutdown, retries, rate limits, and failure isolation.
4. Verify backup coverage, restore evidence, RTO/RPO assumptions, incident procedures, and access to runbooks.
5. Run safe checks and drills where authorized; never mutate production or destroy data for evidence.
6. Classify findings, document limitations, write docs/audit/07-production-readiness.md, and make a gate recommendation.

Read [references/config-observability.md](references/config-observability.md), [references/release-readiness.md](references/release-readiness.md), and [references/incident-recovery.md](references/incident-recovery.md).
