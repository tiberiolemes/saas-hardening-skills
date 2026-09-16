# Cross-tenant adversarial tests

Use test fixtures for at least two tenants, two users per tenant, one revoked membership, one lower-privilege role, and one privileged support path where applicable.

For each resource and operation, exercise:

| Scenario | Expected property |
|---|---|
| Tenant A reads Tenant B detail by identifier | Denied without revealing protected data |
| Tenant A lists/searches with Tenant B filters | No cross-tenant rows or aggregates |
| Tenant A updates or deletes Tenant B resource | Denied and no mutation |
| Tenant A exports or downloads Tenant B data | Denied and no issued URL/job |
| User with revoked membership repeats an old request | Denied after revocation |
| Lower role invokes admin operation | Denied |
| Tampered tenant, owner, role, or price input | Server ignores or rejects authority changes |
| Background job receives wrong tenant context | Job fails closed or remains scoped |

Also test pagination, batch IDs, nested resources, soft-deleted records, duplicate identifiers, cache hits, retry paths, and signed URLs. Record actual response semantics and evidence; do not use destructive payloads against live data.
