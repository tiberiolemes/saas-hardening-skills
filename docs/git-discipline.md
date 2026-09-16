# Git discipline

The framework treats Git as an evidence and recovery system. It does not authorize destructive operations or an automatic push.

## Preflight

Before inspecting or changing code, capture:

~~~bash
git status --short --branch
git remote -v
git branch --show-current
git log -5 --oneline
~~~

Record the current commit in the stage checkpoint. If the working tree is dirty, identify which files predate the audit. Preserve them, avoid overwriting them, and do not include them in stage commits.

## Branches and commits

Use a dedicated branch only when safe and authorized. Do not switch branches if doing so could hide or overwrite existing work. Prefer one logical commit per completed stage or coherent fix group. Commit messages should state the stage or purpose, for example:

~~~text
fix(security): close object authorization gap
docs(audit): record Stage 01 gate evidence
~~~

Before committing, review git diff, git diff --cached, the path list, and a secret scan. A passing gate does not imply permission to push.

## Prohibited by default

Never use git reset --hard, git clean -fd, force push, broad checkout/discard operations, or commands that overwrite unrelated work. Do not make destructive database changes as a convenience for the audit.

## Resumption and rollback

A checkpoint records the commit SHA, stage, status, findings, tests, and blockers. On resume, compare the current SHA and working tree with that checkpoint. If they differ, revalidate affected conclusions. Recovery should use reviewable commits or a user-approved approach; do not erase evidence to obtain a clean tree.
