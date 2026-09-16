---
name: tenant-isolation-auditor
description: Verify SaaS tenant and resource isolation, server-side authorization, privileged paths, database policies, storage boundaries, and cross-tenant negative paths.
---

# Tenant isolation auditor

Treat tenant isolation as an end-to-end property. A tenant identifier, UUID, hidden UI control, or frontend check is not authorization.

## Workflow

1. Map tenants, users, memberships, roles, resources, ownership edges, privileged actors, and background workers.
2. Build a resource ownership matrix for reads, creates, updates, deletes, exports, searches, files, jobs, and administrative actions.
3. Trace how the server derives principal, tenant, resource owner, and role; reject client-provided authority.
4. Inspect database row-level policies, service-role paths, storage rules, caches, queues, analytics, and logs for boundary leaks.
5. Run or add negative-path tests for same-tenant, cross-tenant, unauthenticated, downgraded-role, and privileged-support scenarios.
6. Classify and fix findings only with authorization, then rerun authorized and adversarial paths.
7. Write docs/audit/02-tenant-isolation.md and gate evidence.

Read [references/ownership-authorization.md](references/ownership-authorization.md), [references/rls-and-storage.md](references/rls-and-storage.md), and [references/adversarial-tests.md](references/adversarial-tests.md).
