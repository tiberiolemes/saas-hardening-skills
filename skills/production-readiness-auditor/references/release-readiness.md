# Release readiness checklist

Review the complete release path:

- reproducible install and build from a clean checkout;
- lint, typecheck, tests, dependency audit, schema validation, and production build;
- migration ordering, backward compatibility, lock/latency risk, and rollback or forward-fix plan;
- feature flags, staged rollout, health checks, smoke tests, and release ownership;
- deploy permissions, artifact provenance, immutable versioning, and secret injection;
- error budget, rate limits, capacity assumptions, and cost guardrails;
- post-release verification, monitoring window, and stop condition.

Do not mark a release safe because the local build is green if required staging or production evidence is missing. Record exactly which environment was verified.
