---
name: performance-auditor
description: Measure and improve SaaS backend and frontend performance with evidence while preserving correctness, tenant isolation, and operability.
---

# Performance auditor

Measure before optimizing. Separate observed bottlenecks from hypotheses and do not invent before/after gains.

## Workflow

1. Establish the workload, environment, user journey, data shape, and baseline metrics.
2. Trace backend latency, database work, serialization, external calls, queues, cache behavior, payload size, and concurrency.
3. Trace frontend loading, bundles, rendering, network waterfalls, images, fonts, scripts, and Core Web Vitals.
4. Choose the smallest safe optimization with an invalidation, consistency, and rollback story.
5. Run comparable before/after measurements, relevant correctness and isolation tests, and regression checks.
6. Record limits such as unavailable production traffic or missing instrumentation as NOT_VERIFIED.
7. Write docs/audit/05-performance.md and gate evidence.

Read [references/backend-performance.md](references/backend-performance.md), [references/frontend-performance.md](references/frontend-performance.md), and [references/measurement.md](references/measurement.md).
