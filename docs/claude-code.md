# Claude Code

This repository is also distributed as a Claude Code plugin. The `SKILL.md` files and their `references/` directories are shared with the Codex distribution; the Claude-specific layer is limited to `.claude-plugin/plugin.json` and the Markdown subagents under `agents/`.

## Install from the repository

Clone the public repository, then start Claude Code with the cloned folder as a plugin:

```bash
git clone https://github.com/tiberiolemes/saas-hardening-skills.git
claude --plugin-dir /path/to/saas-hardening-skills
```

For a project-scoped installation, copy the complete cloned plugin folder to `.claude/skills/saas-hardening-skills/` in the application repository and start Claude Code from that application root. Claude Code will ask you to trust repository-provided components before loading them.

```text
your-saas/
└── .claude/
    └── skills/
        └── saas-hardening-skills/
            ├── .claude-plugin/
            ├── agents/
            └── skills/
```

## Invoke

When loaded as a plugin, use the namespaced Skill:

```text
/saas-hardening-skills:saas-hardening-orchestrator
```

For a scoped stage, invoke the Skill directly:

```text
/saas-hardening-skills:appsec-auditor
```

Claude subagents are available with the `@` mention interface, for example:

```text
@saas-hardening-skills:appsec-auditor-agent review and safely remediate the current Stage 01 findings.
```

The orchestrator remains the source of truth for order, gates, status, checkpoints, and resumption. Use specialist subagents for isolated stage work when the parent session chooses to delegate. Subagents cannot replace the orchestrator's gate decision.

## Compatibility boundary

| Shared component | Claude Code behavior |
|---|---|
| `skills/*/SKILL.md` | Loaded as plugin Skills and invoked with `/plugin:skill`. |
| `skills/*/references/` | Supporting files available to the corresponding Skill. |
| `skills/*/agents/openai.yaml` | Codex UI metadata; ignored by Claude Code. |
| `agents/*.md` | Claude Code subagent definitions, with Claude-specific YAML frontmatter. |
| `$skill-name` examples | Codex syntax; use `/plugin:skill` in Claude Code. |

## Updating

Pull a newer revision of the clone and restart Claude Code, or run `/reload-plugins` after plugin component changes. Changes to agent definitions and plugin metadata require reload or a new session.

## Safety

Claude Code may ask for permission before edits and shell commands. Review proposed changes, preserve existing work, do not expose secrets, and never authorize destructive production actions merely to make a gate pass.
