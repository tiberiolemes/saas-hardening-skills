---
name: saas-hardening-orchestrator
description: Coordinate an evidence-based SaaS hardening program across stages 00–07, controlling audit artifacts, quality gates, checkpoints, commits, and safe resumption.
---

# SaaS hardening orchestrator

Use this Skill as the entry point when the user wants a complete review or a controlled continuation of the SaaS hardening program. It coordinates the specialist auditors; it does not replace their domain checks.

## Operating contract

1. Inspect the application repository before changing anything: working tree, branch, recent history, remote, stack, and existing audit artifacts.
2. Preserve existing user work. Do not discard, overwrite, or silently include unrelated changes.
3. Run stages strictly in order: 00 baseline, 01 AppSec, 02 tenant isolation, 03 database integrity, 04 code health, 05 performance, 06 UX/accessibility, and 07 production readiness.
4. At each stage execute CHECKPOINT → AUDIT → PLAN → FIX → TEST → ADVERSARIAL TEST → VERIFY → REPORT → GATE → COMMIT.
5. Do not advance after a BLOCKED gate. Record the blocker, evidence, decision needed, and resumption condition.
6. Make changes only within the user's authorization. Never push automatically; commit only when the task and repository policy permit it.
7. Never expose secrets, personal data, exploit credentials, or sensitive production values in reports, tests, or commits.

## Shared control files

Maintain docs/audit/AUDIT-STATUS.md as the program source of truth and update it with every meaningful stage transition. Produce one stage report per stage under docs/audit/. Use the templates in references/audit-status-template.md and references/report-template.md.

## Routing

- Read references/stage-map.md to select the specialist and required report for the current stage.
- Read references/quality-gates.md before judging a gate.
- Read references/git-discipline.md before any repository mutation or commit.
- On resume, read references/resumption.md and the current status/report before repeating work.
- Read only the references relevant to the current decision; do not load the entire reference set by default.

## Completion

Finish only when Stage 07 has a documented gate decision and the status file reflects all eight stages. If evidence is missing, use NOT_VERIFIED rather than inferring success. Report unresolved findings, residual risk, skipped checks, and exact next actions.
