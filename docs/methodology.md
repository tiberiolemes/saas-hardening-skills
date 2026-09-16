# Methodology

SaaS Hardening Skills uses a staged, evidence-first program. It is designed for an existing application where correctness, tenant boundaries, production behavior, and traceability matter as much as finding issues.

## Stage map

| Stage | Name | Required output |
|---:|---|---|
| 00 | Baseline | docs/audit/00-baseline.md |
| 01 | AppSec | docs/audit/01-appsec.md |
| 02 | Tenant isolation | docs/audit/02-tenant-isolation.md |
| 03 | Database integrity | docs/audit/03-database.md |
| 04 | Code health | docs/audit/04-code-health.md |
| 05 | Performance | docs/audit/05-performance.md |
| 06 | UX and accessibility | docs/audit/06-ux-accessibility.md |
| 07 | Production readiness | docs/audit/07-production-readiness.md |

The source of truth for the whole program is docs/audit/AUDIT-STATUS.md.

## Operating loop

Every stage uses the following loop:

1. **CHECKPOINT** — record the current commit, branch, working-tree condition, earlier reports, and applicable checks.
2. **AUDIT** — inspect the relevant surface before making changes; distinguish evidence from hypotheses.
3. **PLAN** — group findings by root cause, severity, dependencies, and risk. Prioritize P0 then P1, P2, P3.
4. **FIX** — make small, related changes only when authorized. Preserve business rules and public contracts unless the evidence requires a change.
5. **TEST** — run the narrowest relevant checks first, then the broader regression suite.
6. **ADVERSARIAL TEST** — try negative paths for security, authorization, tenant, data, API, and resilience changes.
7. **VERIFY** — inspect the final diff, changed behavior, compatibility, and newly introduced risk.
8. **REPORT** — write findings, evidence, fixes, test results, residual risk, and limitations to the stage report.
9. **GATE** — apply the shared and stage-specific criteria. Use NOT_VERIFIED when evidence is absent.
10. **COMMIT** — create a logical stage commit only when permitted by the task and repository policy; never include unrelated user work.

## Findings

- P0: active path to severe unauthorized access, credential exposure, destructive data loss, or a comparable critical impact.
- P1: high-impact authorization, tenant isolation, privilege escalation, integrity, or availability risk.
- P2: meaningful injection, abuse, resilience, maintainability, performance, or accessibility issue with bounded impact.
- P3: hardening, observability, documentation, cleanup, or preventive improvement.

Every finding should state location, evidence, impact, confidence, root cause, remediation, verification, and residual risk. Never copy secrets into reports or tests.

## Resumption

On every resume, read the status file first, then re-check the current commit, branch, working tree, outstanding blockers, and the latest stage report. If the code changed since the last checkpoint, invalidate conclusions that depend on the changed surface and repeat the relevant checks.

## Non-negotiable constraints

Do not assume a UUID is authorization, a hidden button is a security control, a frontend check is sufficient, or a client-provided tenant, role, price, or ownership value is trustworthy. Do not relax authentication, authorization, RLS, CORS, or validation to make tests pass. Do not claim a gate passed without evidence.
