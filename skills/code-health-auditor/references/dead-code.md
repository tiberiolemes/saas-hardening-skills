# Dead-code evidence procedure

A search result is a lead, not proof. Before removal, inspect:

- direct imports, exports, and call sites;
- dynamic imports, reflection, route registries, dependency injection, plugin hooks, and event names;
- configuration, feature flags, migrations, scheduled jobs, templates, generated output, and deployment references;
- public packages, scripts, CLI entrypoints, and external consumers;
- tests and snapshots that encode intended behavior.

Classify each candidate as proven unused, likely unused, or not verified. Remove only the first category unless the user explicitly authorizes a broader cleanup. After removal, run focused tests, lint, typecheck, build, and the relevant application smoke path. Record deleted paths, evidence, and residual uncertainty in the Stage 04 report.
