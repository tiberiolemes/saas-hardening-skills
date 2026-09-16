# Frontend performance checklist

For critical journeys, inspect:

- initial HTML, JavaScript and CSS transfer, bundle composition, code splitting, lazy loading, and unused dependencies;
- render frequency, state subscriptions, layout work, long tasks, hydration, and loading waterfalls;
- image dimensions, formats, compression, responsive sources, fonts, third-party scripts, and cache headers;
- preconnect, preload, prefetch, and resource priority choices;
- LCP, INP, CLS, TTFB, and interaction latency in a representative environment;
- loading, error, empty, and offline behavior while assets or data are slow.

Do not optimize by hiding content, weakening accessibility, removing validation, or weakening security controls. Record the measurement environment and tradeoffs.
