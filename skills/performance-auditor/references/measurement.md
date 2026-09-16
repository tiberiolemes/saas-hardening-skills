# Measurement procedure

A credible comparison records:

- exact route or user journey;
- application version and commit;
- environment, device, browser, network, data volume, and feature flags;
- warm/cold cache and authentication state;
- sample size, aggregation, and percentile;
- baseline and after values with units;
- correctness, error rate, authorization, tenant, and regression checks;
- known limitations and what remains NOT_VERIFIED.

Prefer p50 and p95 for latency, error rate, throughput, and resource cost when available. For browser work, record Core Web Vitals and the test conditions. If production telemetry is unavailable, say so and use a reproducible local or staging proxy without presenting it as production evidence.
