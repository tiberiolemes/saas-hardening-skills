---
name: code-health-auditor
description: Improve an existing SaaS codebase by proving dead code, reducing unnecessary complexity, preserving behavior, and strengthening meaningful tests.
---

# Code health auditor

Make the codebase easier to understand and change without turning style preferences into findings. Remove code only when references and runtime behavior have been checked.

## Workflow

1. Inventory modules, exports, routes, feature flags, dependencies, generated code, configuration, and test coverage.
2. Verify suspected dead code across direct, indirect, dynamic, configuration, plugin, and deployment references.
3. Review responsibilities, coupling, duplication, complexity, typing, null handling, error paths, and maintainability hotspots.
4. Plan small changes with explicit behavior and compatibility risks; do not mix cleanup with unrelated feature changes.
5. Add or improve tests for changed critical behavior, then run lint, typecheck, tests, and build as applicable.
6. Inspect the diff for accidental behavior changes and document removals and residual uncertainty.
7. Write docs/audit/04-code-health.md and gate evidence.

Read [references/dead-code.md](references/dead-code.md), [references/maintainability.md](references/maintainability.md), and [references/testing-quality.md](references/testing-quality.md).
