# Authentication and authorization review

## Authentication

Trace the complete lifecycle:

- registration, email verification, password reset, password change, session renewal, logout, account recovery, and account deletion;
- password storage, credential policy, brute-force controls, MFA where applicable, and user enumeration behavior;
- cookie flags, token audience/issuer/expiry, rotation, revocation, CSRF model, and session fixation defenses;
- sensitive actions that require recent authentication or step-up verification.

Do not report a library name as proof of a correct configuration. Verify the actual path and failure behavior.

## Authorization

For every sensitive route and operation:

1. Identify the authenticated principal and the server-side source of identity.
2. Identify the required permission, role, tenant, ownership, and state transition.
3. Verify enforcement occurs on the server or trusted data layer.
4. Test missing identity, wrong role, wrong tenant, wrong owner, stale membership, and tampered identifiers.
5. Check list, search, export, download, batch, background, webhook, and admin paths in addition to detail routes.

Treat deny-by-default and least privilege as design goals, not assumptions. Record the intended status and response semantics for denied access without exposing whether protected data exists.
