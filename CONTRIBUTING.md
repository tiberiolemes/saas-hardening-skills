# Contributing

Thank you for helping improve SaaS Hardening Skills. Contributions should make the framework more evidence-driven, safer to run, easier to resume, and more useful across technology stacks.

## Before you start

- Read the README and the relevant Skill entrypoint.
- Open an issue for a significant change to methodology, stage order, severity, or public behavior.
- Never include credentials, personal data, private application code, or real exploit secrets in an issue, pull request, fixture, or example.

## Skill design rules

Each Skill must:

- live under skills/<skill-name>/;
- contain a SKILL.md with YAML frontmatter containing exactly the lowercase hyphenated name and a discriminating description;
- keep the entrypoint focused on purpose, routing, essential constraints, and output;
- place conditional procedures, checklists, schemas, and examples in focused references/ files;
- link every reference from the entrypoint and explain when it should be read;
- preserve automatic invocation unless there is a documented reason to make the Skill explicit-only;
- avoid promising security, performance, compliance, or production readiness without evidence.

Use agents/openai.yaml only for useful UI metadata or a real invocation policy. Keep all string values quoted and keep its default prompt short and explicit about $skill-name.

## Local validation

From the repository root, run:

~~~bash
python3 scripts/validate_skills.py
~~~

If your Codex installation includes the system Skill Creator validator, run quick_validate.py against every directory under skills/ as well. Review links, examples, wording, and scope manually; syntax validation cannot prove that the workflow makes good decisions.

## Documentation and examples

Use language that is portable across stacks. Prefer “inspect the framework’s authorization boundary” over a provider-specific command unless the provider is the subject of a reference. Examples must use placeholders such as example.test, never real credentials or private identifiers.

## Git and pull requests

Use small, logical commits. Suggested prefixes are:

- feat: for a new Skill or workflow capability;
- fix: for a correction to behavior or instructions;
- docs: for documentation-only changes;
- test: for validator or test changes;
- chore: for maintenance.

Before opening a pull request:

- inspect git diff and git status;
- confirm only intended paths are included;
- scan for secrets and private data;
- run the validator;
- explain behavior changes, migration notes, and any unverified assumptions.

Do not rewrite shared history or force-push branches. Do not use destructive Git commands in contribution instructions.

## Security reports

Do not open a public issue for a vulnerability in the framework that could put users at risk. Contact the repository owner privately with reproduction evidence, affected files, impact, and a proposed disclosure timeline. Redact tokens, keys, personal data, and sensitive application details.
