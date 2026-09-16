# Secrets and dependency review

## Secrets

Search configuration, source, history, logs, test fixtures, build artifacts, CI output, and documentation for credential-like values. Distinguish names and placeholders from actual values. If a secret is found:

1. Do not copy it into a report or test.
2. Record only its location, type, exposure scope, and redacted fingerprint if needed.
3. Recommend rotation and exposure assessment according to the owner’s process.
4. Review logs, caches, artifacts, forks, and deployment systems for propagation.
5. Ensure examples use clearly fake values and the ignore rules cover local secrets.

Check that production secrets are injected through the approved secret store and are absent from client bundles, source maps, images, and public error responses.

## Dependencies and supply chain

Review lockfiles, direct and transitive dependencies, advisories, abandoned packages, install scripts, provenance, permissions, and update policy. Separate a known vulnerable reachable dependency from an unused or unreachable package. Upgrade in small groups and run compatibility checks; do not apply broad major upgrades merely to silence a report.

Redact tokens, private URLs, and personal data from all evidence.
