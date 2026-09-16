# Maintainability review

Look for changes that reduce real maintenance risk:

- functions or components with mixed responsibilities;
- repeated security, validation, persistence, or error-handling logic;
- excessive coupling and hidden global state;
- unclear names, magic values, unsafe null handling, weak types, and swallowed errors;
- complexity that prevents testing or obscures authorization and business rules;
- abstractions that add indirection without reducing duplication or risk.

Prefer a small refactor with a clear invariant and regression test. Preserve public contracts and product behavior. Do not rewrite a module for style or replace a framework without objective evidence.
