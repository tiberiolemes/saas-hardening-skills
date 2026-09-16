# Contributing

[🇧🇷 PT-BR](#pt-br) · [🇺🇸 English](#english)

## PT-BR

Obrigado por ajudar a melhorar o SaaS Hardening Skills. As contribuições devem tornar o framework mais baseado em evidências, mais seguro para executar, mais fácil de retomar e mais útil em diferentes stacks tecnológicas.

### Antes de começar

- Leia o README e o `SKILL.md` relevante.
- Abra uma issue para mudanças significativas na metodologia, ordem das etapas, severidade ou comportamento público.
- Nunca inclua credenciais, dados pessoais, código privado de aplicações ou secrets reais de exploração em issues, pull requests, fixtures ou exemplos.

### Regras de design das Skills

Cada Skill deve:

- viver em `skills/<skill-name>/`;
- conter um `SKILL.md` com frontmatter YAML contendo exatamente o nome em minúsculas separado por hífens e uma descrição que diferencie a Skill;
- manter o entrypoint focado em propósito, roteamento, restrições essenciais e saída;
- colocar procedimentos condicionais, checklists, schemas e exemplos em arquivos focados dentro de `references/`;
- linkar cada referência a partir do entrypoint e explicar quando ela deve ser lida;
- preservar a invocação automática, salvo quando houver motivo documentado para tornar a Skill explícita;
- não prometer segurança, performance, conformidade ou prontidão para produção sem evidências.

Use `agents/openai.yaml` somente para metadados úteis de interface ou uma política real de invocação. Mantenha todos os valores string entre aspas e o prompt padrão curto e explícito sobre `$skill-name`. Para o Claude Code, use o manifesto `.claude-plugin/plugin.json` e subagentes Markdown em `agents/`.

### Validação local

A partir da raiz do repositório, execute:

```bash
python3 scripts/validate_skills.py
```

Se a instalação do Codex incluir o validador do Skill Creator, execute também `quick_validate.py` em cada diretório dentro de `skills/`. Revise links, exemplos, linguagem e escopo manualmente; a validação de sintaxe não prova que o workflow toma boas decisões.

Para validar o plugin Claude Code, execute:

```bash
claude plugin validate .
```

### Documentação e exemplos

Use linguagem portável entre stacks. Prefira “inspecione o limite de autorização do framework” a um comando específico de provedor, salvo quando o provedor for o assunto da referência. Exemplos devem usar placeholders como `example.test`, nunca credenciais reais ou identificadores privados.

### Git e pull requests

Use commits pequenos e lógicos. Prefixos sugeridos:

- `feat:` para uma nova Skill ou capacidade do workflow;
- `fix:` para uma correção de comportamento ou instrução;
- `docs:` para mudanças somente de documentação;
- `test:` para mudanças em validadores ou testes;
- `chore:` para manutenção.

Antes de abrir um pull request:

- inspecione `git diff` e `git status`;
- confirme que somente os caminhos pretendidos estão incluídos;
- faça uma varredura por secrets e dados privados;
- execute os validadores;
- explique mudanças de comportamento, notas de migração e suposições não verificadas.

Não reescreva histórico compartilhado nem faça force push. Não use comandos Git destrutivos nas instruções de contribuição.

### Relatórios de segurança

Não abra uma issue pública para uma vulnerabilidade no framework que possa colocar usuários em risco. Entre em contato privadamente com o responsável pelo repositório, fornecendo evidências de reprodução, arquivos afetados, impacto e uma proposta de cronograma de divulgação. Redija tokens, chaves, dados pessoais e detalhes sensíveis da aplicação.

## English

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
