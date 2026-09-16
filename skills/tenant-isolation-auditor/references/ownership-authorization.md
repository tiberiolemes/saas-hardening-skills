# Ownership and authorization matrix

Create a matrix before reviewing individual handlers.

| Resource | Read | Create | Update | Delete | Export/download | Derived from |
|---|---|---|---|---|---|---|
| [resource] | [principal, tenant, role] | [trusted inputs] | [owner/state] | [owner/role] | [owner/tenant] | [server source] |

For each resource:

- identify the tenant and ownership relationship;
- identify the principal, membership, role, and state needed for each operation;
- trace server-side derivation of those values;
- check list, search, batch, export, download, async, and admin paths;
- check object lookup before authorization as well as authorization after lookup;
- check create-time ownership and mass assignment;
- check authorization again for updates, deletes, and state transitions;
- check response fields, counts, filters, sort keys, and error behavior for leakage.

Client-provided tenant_id, organization_id, role, owner_id, price, or permission fields must be treated as untrusted input. A random or opaque identifier is not an access control.
