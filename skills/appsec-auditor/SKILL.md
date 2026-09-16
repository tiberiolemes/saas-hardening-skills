---
name: appsec-auditor
description: Audit web application security across authentication, authorization, input handling, sessions, secrets, dependencies, abuse controls, and common web threats.
---

# AppSec auditor

Review the application's reachable security boundaries and produce an evidence-based Stage 01 report. Understand the architecture before proposing fixes and keep the review stack-agnostic.

## Correction mode

Do not stop at the report. After classifying findings, implement safe, proportionate, well-understood fixes within the user's authorization, then run focused regression and adversarial tests. Mark a finding `RESOLVED` only when the verification evidence is recorded; document unsafe, ambiguous, or unauthorized changes as `ACCEPTED`, `BLOCKED`, or `NOT_VERIFIED`.

## Workflow

1. Identify trust boundaries, assets, actors, authentication/session lifecycle, authorization decisions, and sensitive data.
2. Trace server-side enforcement for object and function access; test negative paths, not only happy paths.
3. Review input/output boundaries for injection, XSS, CSRF, SSRF, path traversal, unsafe uploads, open redirects, CORS, headers, webhooks, and error disclosure.
4. Inspect secrets handling, logs, configuration, dependency risk, and supply-chain exposure without printing sensitive values.
5. Classify findings P0–P3 with location, evidence, impact, confidence, root cause, remediation, and verification.
6. Implement only authorized, proportionate fixes; run focused regression and adversarial tests.
7. Write docs/audit/01-appsec.md and provide a gate recommendation.

Read [references/authentication-authorization.md](references/authentication-authorization.md), [references/web-threats.md](references/web-threats.md), and [references/secrets-dependencies.md](references/secrets-dependencies.md) only when those surfaces apply.
