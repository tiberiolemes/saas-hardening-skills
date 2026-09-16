# Examples

## Full run

~~~text
Use $saas-hardening-orchestrator to run the complete 00–07 program on this SaaS repository. Start with a read-only baseline, preserve existing changes, classify findings P0–P3, update docs/audit/AUDIT-STATUS.md at every stage, stop on a blocked gate, run relevant positive and negative-path tests, and never expose secrets.
~~~

## Scoped tenant review

~~~text
Use $tenant-isolation-auditor to review the invoice, export, and support-admin flows. Build the resource ownership matrix first. Trace server-side authorization and database/storage scoping, then add or run cross-tenant negative tests. Report evidence before proposing changes.
~~~

## Baseline only

~~~text
Use $saas-baseline to map this application without large refactors. Identify the stack, architecture, auth, roles, tenants, data model, critical flows, integrations, deployment, tests, and current lint/typecheck/test/build results. Write docs/audit/00-baseline.md and list unknowns as NOT_VERIFIED.
~~~

## Gate review

~~~text
Use $saas-hardening-orchestrator to review the Stage 05 gate. Compare the performance report with the current diff and measured evidence. Reject claims without before/after data, check cache invalidation and tenant correctness, and update AUDIT-STATUS.md only if the documented criteria are satisfied.
~~~

## Report shape

~~~markdown
## Finding P1: object authorization is missing on export lookup

- Location: server/exports/... (use the actual path and line when available)
- Evidence: the handler loads an export by identifier without deriving ownership from the authenticated principal.
- Impact: an authenticated user may retrieve another tenant's export.
- Confidence: HIGH — reproduced with a negative-path test.
- Remediation: enforce server-side ownership/tenant scope before loading the resource.
- Verification: negative test returns the project's intended denial response; authorized path remains green.
- Residual risk: background export worker still needs review.
~~~
