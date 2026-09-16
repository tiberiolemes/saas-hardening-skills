# Stage map

Use this routing table to select one specialist at a time. Read the specialist entrypoint before the stage audit and load only the references relevant to the current application.

| Stage | Specialist | Report | Primary questions |
|---:|---|---|---|
| 00 | saas-baseline | docs/audit/00-baseline.md | What exists, how does it work, and what is not known? |
| 01 | appsec-auditor | docs/audit/01-appsec.md | Can untrusted actors cross authentication, authorization, input, or secret boundaries? |
| 02 | tenant-isolation-auditor | docs/audit/02-tenant-isolation.md | Can a principal read or mutate another tenant's resource through any path? |
| 03 | database-integrity-auditor | docs/audit/03-database.md | Can schema, writes, migrations, or concurrency create invalid or lost data? |
| 04 | code-health-auditor | docs/audit/04-code-health.md | Which complexity and dead-code claims are proven, and what tests protect changes? |
| 05 | performance-auditor | docs/audit/05-performance.md | What is measured slow, and does an optimization preserve correctness and isolation? |
| 06 | ux-accessibility-auditor | docs/audit/06-ux-accessibility.md | Can users complete critical journeys across failure, mobile, and assistive paths? |
| 07 | production-readiness-auditor | docs/audit/07-production-readiness.md | Can the system be released, observed, recovered, and operated safely? |

The orchestrator must not silently reorder stages. A narrowly scoped user request may invoke one specialist without claiming the full program passed.
