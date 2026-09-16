# Web threat review

Inspect the actual boundary for each threat and record evidence only when the data flow is reachable.

## Input, output, and requests

- Validate input server-side with allowlists and type/size limits.
- Use parameterized queries and safe command/process APIs.
- Encode output for its context and review HTML, template, markdown, URL, and DOM sinks.
- Check CSRF protection for state-changing browser requests.
- Review SSRF controls for user-influenced URLs, redirects, metadata access, and internal network reachability.
- Check path traversal, archive extraction, file upload type/size/storage/execution, and download authorization.
- Review mass assignment, over-posting, unsafe deserialization, and excess response fields.

## Browser and API controls

- Verify CORS origins, credentials, methods, headers, and preflight behavior.
- Inspect CSP, frame restrictions, content type, referrer, transport, and permissions headers where relevant.
- Review rate limits, abuse controls, pagination caps, body limits, idempotency, and expensive endpoints.
- Validate webhook signatures, timestamp/replay protection, event authorization, and retry behavior.
- Ensure errors do not disclose stack traces, secrets, internal paths, or sensitive existence information.

For each issue, demonstrate the source, sink, boundary, impact, and safe verification path. Do not include exploit payloads that contain real credentials or destructive commands.
