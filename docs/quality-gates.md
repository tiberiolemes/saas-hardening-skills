# Quality gates

Gates are decision points, not summaries. A stage is PASSED only when required evidence exists and the remaining risk is understood and accepted according to the project's policy.

## Status values

| Status | Meaning |
|---|---|
| NOT_STARTED | No work has begun for the stage. |
| IN_PROGRESS | Discovery, fixes, or verification are underway. |
| BLOCKED | A required fix, test, decision, permission, or external dependency prevents safe progress. |
| PASSED | Required controls were verified and no disqualifying finding remains. |
| NOT_VERIFIED | The repository or environment did not provide enough evidence to make a pass claim. |

## Stage criteria

| Stage | Minimum gate evidence |
|---:|---|
| 00 | Architecture, stack, critical flows, data/tenant model, auth model, attack surface, and baseline check results are documented. |
| 01 | Authentication and authorization paths, input/output boundaries, secrets, dependencies, and relevant negative paths are reviewed; required P0/P1 issues are resolved or explicitly blocked. |
| 02 | Resource ownership matrix, server-side enforcement, privileged paths, database/storage isolation, and cross-tenant negative tests are evidenced. |
| 03 | Constraints, migrations, critical queries, transaction/concurrency behavior, integrity checks, and non-destructive migration safety are reviewed. |
| 04 | Dead-code removals are proven safe, complexity risks are addressed proportionately, changed behavior is covered by meaningful tests, and the diff is focused. |
| 05 | Before/after measurements or a clear measurement limitation exist; optimizations preserve correctness, isolation, and cache invalidation behavior. |
| 06 | Critical journeys, loading/error/empty states, keyboard/focus behavior, semantic structure, contrast, responsive behavior, and regression evidence are reviewed. |
| 07 | Production configuration, secrets handling, observability, release/rollback, backups/restore, health checks, shutdown, and operational ownership are documented. |

## Shared disqualifiers

Do not mark a gate PASSED when:

- a required P0 remains unresolved;
- a required P1 remains unmitigated or lacks an explicit accepted-risk decision;
- a critical test or build is failing and its impact is unknown;
- a security or data correction has no negative-path or adversarial evidence;
- the report or status file is stale relative to the code;
- secrets or unrelated user changes are present in the proposed commit;
- a claim depends on an unavailable production or provider state and is not marked NOT_VERIFIED.

When a gate fails, record the blocker, owner/decision needed, evidence, and the exact condition for resumption.
