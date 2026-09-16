# Execution contract

The framework runs in correction mode after discovery. An audit report is an intermediate artifact, not the end of the work.

For each finding in stages 01–07:

1. Classify severity, confidence, evidence, impact, root cause, and remediation.
2. Decide whether the correction is safe, proportionate, technically understood, and within the user's authorization.
3. Implement authorized corrections in small, reviewable groups. Do not bundle unrelated cleanup or speculative redesign.
4. Run focused tests after each group, then run broader regression and relevant adversarial or negative-path tests.
5. Inspect the final diff and record the exact verification evidence before changing the finding to `RESOLVED`.

Do not stop after identifying or reporting a finding when a safe, authorized correction can be made. A finding that cannot be safely changed must remain documented with one of these states:

- `ACCEPTED` — an authorized owner explicitly accepts the residual risk;
- `BLOCKED` — a decision, dependency, environment, or authorization is required;
- `NOT_VERIFIED` — the available evidence is insufficient to reach a conclusion.

Never make destructive production changes, alter ambiguous business rules, rotate or print credentials, weaken controls to make tests pass, or change public contracts without explicit authorization. Record the reason and the resumption condition.

Stage 00 is the exception: it is read-only discovery and baseline construction. It must not modify application code or begin broad remediation. Its job is to establish the map, identify unknowns, and prepare the evidence needed by stages 01–07.
