# Baseline discovery checklist

Use this checklist during Stage 00. Record actual paths and command results; do not fill gaps with assumptions.

## Repository and runtime

- Identify languages, frameworks, package managers, runtime versions, entrypoints, build targets, and generated artifacts.
- Locate environment templates, configuration loaders, deployment manifests, containers, infrastructure code, CI/CD, scheduled jobs, and feature flags.
- Identify test suites, fixtures, local services, staging assumptions, and known gaps.
- Record dependency audit results and versions that affect security or compatibility.

## Architecture and flows

- Trace browser or client to API, service, persistence, queue, storage, and external provider.
- Locate business rules, validation, authorization, persistence, integration, and asynchronous boundaries.
- Map login, registration, recovery, onboarding, CRUD, administration, billing, export, upload, webhook, and integration flows as applicable.
- Mark flows that cross trust boundaries or handle sensitive data.

## Identity and tenancy

- Identify principal creation, session storage, token/cookie handling, logout, expiry, role changes, and impersonation/support access.
- Identify tenants, memberships, roles, resource ownership, tenant keys, database policies, storage paths, caches, queues, and analytics.
- List what is verified, inferred, and unknown.

## Attack and operations surface

- List public, authenticated, administrative, internal, worker, webhook, upload, storage, and health endpoints.
- Identify secrets, personal data, payment data, audit records, and operational controls.
- Map observability, error handling, rate limits, backups, restore procedures, release and rollback.

## Baseline checks

Run applicable checks without hiding failures:

- lint;
- typecheck;
- unit and integration tests;
- end-to-end or smoke tests;
- production build;
- dependency audit;
- schema or migration validation.

The report must include command, environment, date, result, and meaningful failure context. Use NOT_VERIFIED when a check could not run.
