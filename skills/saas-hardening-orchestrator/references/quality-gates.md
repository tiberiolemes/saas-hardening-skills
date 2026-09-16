# Orchestrator gate procedure

Before a gate decision, collect the current stage report, status file, changed paths, test output, adversarial evidence, and current Git state.

## Decision

1. Confirm the stage is the current stage in AUDIT-STATUS.md.
2. Confirm the report describes scope, evidence, findings, fixes, tests, limitations, and residual risk.
3. Confirm every required P0 and P1 is resolved, explicitly accepted by the authorized owner, or recorded as BLOCKED. An unreviewed P0/P1 is not a pass.
4. Confirm all stage-specific evidence in the repository's quality-gate table.
5. Confirm the diff is focused, no secret or unrelated user file is included, and business behavior is understood.
6. Confirm negative-path tests exist when the change affects security, authorization, tenancy, data, APIs, or resilience.
7. Mark PASSED only when all required conditions are evidenced. Otherwise mark BLOCKED or NOT_VERIFIED and state why.

Never infer a pass from a green lint run, a successful build, or the absence of a search result.
