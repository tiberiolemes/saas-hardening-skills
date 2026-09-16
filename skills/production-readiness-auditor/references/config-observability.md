# Configuration and observability checklist

## Configuration

- Separate development, staging, and production settings.
- Keep secrets in the approved secret manager or runtime injection path.
- Check debug mode, verbose errors, source maps, CORS, cookies, HTTPS, security headers, origins, storage, and administrative flags.
- Review least-privilege deploy and runtime identities.
- Confirm logs and artifacts do not contain tokens, passwords, private keys, or unnecessary personal data.
- Identify configuration drift and a safe way to detect it.

## Observability

- structured logs with timestamps, levels, service, route, outcome, and correlation/request IDs;
- metrics for availability, latency, errors, saturation, queue depth, database health, and critical business operations;
- liveness/readiness health checks that do not leak sensitive details;
- alerts with thresholds, ownership, escalation, and runbook links;
- audit trails for privileged, security-sensitive, billing, and data-export actions.

Evidence must distinguish configured controls from observed production behavior. Provider-side facts that cannot be inspected are NOT_VERIFIED.
