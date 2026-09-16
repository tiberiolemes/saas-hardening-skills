# Backend performance checklist

Start with a representative request, data shape, environment, and measurement window.

Inspect:

- database query count, duration, plans, indexes, N+1 behavior, pagination, and payload size;
- serialization, validation, loops, memory, CPU, blocking work, and connection pools;
- external calls, timeouts, retries, parallelism, rate limits, and circuit behavior;
- queues, batch size, job duration, backpressure, duplicate work, and failure handling;
- cache keys, scope, freshness, invalidation, stampede control, and tenant isolation;
- compression and response fields for sensitive or unnecessarily large data.

Prefer a measured, localized change. Validate correctness, authorization, tenant scope, consistency, and error behavior after optimization.
