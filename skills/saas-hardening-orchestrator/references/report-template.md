# Stage report template

Use this structure for every stage report. Keep evidence specific and redact secrets and personal data.

# Stage [number] — [name]

Date: [date]
Commit at checkpoint: [full SHA]
Commit after work: [full SHA or not committed]
Scope: [paths, flows, environments]
Status: [NOT_STARTED | IN_PROGRESS | BLOCKED | PASSED | NOT_VERIFIED]

## Executive summary

[What was inspected, changed, and verified.]

## Findings

For each finding:

### Finding [P0–P3]: [short title]

- Location: [path and line or configuration key]
- Evidence: [observed code, configuration, test, trace, or command result]
- Impact: [who can do what, or which behavior is affected]
- Confidence: [HIGH | MEDIUM | LOW and why]
- Root cause: [underlying condition]
- Remediation: [fix or explicit reason not to change]
- Verification: [test, query, build, or manual evidence]
- Residual risk: [remaining uncertainty or NONE]

## Changes made

| Path | Change | Reason | Verification |
|---|---|---|---|
| [path] | [summary] | [finding or requirement] | [check] |

## Checks and adversarial tests

| Check | Command or scenario | Result | Evidence |
|---|---|---|---|
| [lint/test/etc.] | [command] | [PASS/FAIL/NOT_RUN] | [output reference] |

## Gate decision

Decision: [PASSED | BLOCKED | NOT_VERIFIED]
Required follow-up: [specific next action]
