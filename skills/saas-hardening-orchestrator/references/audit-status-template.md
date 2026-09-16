# SaaS hardening status

Copy this template into docs/audit/AUDIT-STATUS.md in the application repository and replace every bracketed value with evidence. Do not mark unknown values as passed.

Current stage: [00–07 or COMPLETE]
Program status: [NOT_STARTED | IN_PROGRESS | BLOCKED | COMPLETE]
Last successful gate: [stage or NONE]
Current commit: [full SHA]
Current branch: [branch]
Last checkpoint: [timestamp or date]
Current blockers: [NONE or documented blockers]
Next action: [specific action]

## Stages

| Stage | Status | P0 | P1 | Gate | Report | Commit |
|---|---|---:|---:|---|---|---|
| 00 Baseline | NOT_STARTED | 0 | 0 | NOT_VERIFIED | 00-baseline.md | — |
| 01 AppSec | NOT_STARTED | 0 | 0 | NOT_VERIFIED | 01-appsec.md | — |
| 02 Tenant isolation | NOT_STARTED | 0 | 0 | NOT_VERIFIED | 02-tenant-isolation.md | — |
| 03 Database | NOT_STARTED | 0 | 0 | NOT_VERIFIED | 03-database.md | — |
| 04 Code health | NOT_STARTED | 0 | 0 | NOT_VERIFIED | 04-code-health.md | — |
| 05 Performance | NOT_STARTED | 0 | 0 | NOT_VERIFIED | 05-performance.md | — |
| 06 UX/accessibility | NOT_STARTED | 0 | 0 | NOT_VERIFIED | 06-ux-accessibility.md | — |
| 07 Production | NOT_STARTED | 0 | 0 | NOT_VERIFIED | 07-production-readiness.md | — |

## Checkpoints

| Date | Stage | Commit | Working tree | Checks | Notes |
|---|---|---|---|---|---|
| [date] | [stage] | [full SHA] | [clean or listed pre-existing paths] | [commands and results] | [decision] |

## Blockers and decisions

| Stage | Blocker | Evidence | Owner/decision needed | Resume when |
|---|---|---|---|---|
| [stage] | [blocker or NONE] | [path, test, or command] | [person or decision] | [specific condition] |
