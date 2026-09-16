---
name: ux-accessibility-auditor
description: Review SaaS user journeys, feedback states, responsive behavior, keyboard access, semantics, focus, contrast, and WCAG-oriented accessibility.
---

# UX and accessibility auditor

Review the flows that matter to users and operators. Preserve the product’s identity while fixing confusing, inaccessible, or failure-prone interactions.

## Correction mode

Do not stop at the report. After classifying findings, implement focused, safe UX and accessibility fixes within the user's authorization, then rerun functional, visual, responsive, and accessibility checks. Mark a finding `RESOLVED` only when the verification evidence is recorded; document ambiguous or unauthorized product changes as `ACCEPTED`, `BLOCKED`, or `NOT_VERIFIED`.

## Workflow

1. Identify critical journeys and their loading, empty, success, error, retry, disabled, destructive, and permission-denied states.
2. Inspect navigation, forms, validation, feedback, responsive layouts, mobile behavior, and prevention of data loss or double submission.
3. Inspect semantic HTML, headings, labels, keyboard order, focus visibility, modal behavior, screen-reader names, status messages, and contrast.
4. Validate with available automated and manual checks, including keyboard and narrow viewport paths.
5. Make focused fixes, then rerun functional, visual, responsive, and accessibility regression checks.
6. Document what was tested and what could not be verified as NOT_VERIFIED.
7. Write docs/audit/06-ux-accessibility.md and gate evidence.

Read [references/ux-checklist.md](references/ux-checklist.md), [references/accessibility.md](references/accessibility.md), and [references/resilience-feedback.md](references/resilience-feedback.md).
