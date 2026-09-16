# Failure and feedback review

Exercise slow, failed, and interrupted paths:

- API timeout, network loss, server error, malformed response, and rate limit;
- expired session or permission change during an open form;
- duplicate click, retry, refresh, back navigation, and concurrent edit;
- empty data, partial data, deleted resource, and unavailable integration;
- upload or export progress, cancellation, retry, and completion.

The interface should communicate what happened, preserve safe user input where possible, avoid claiming success before confirmation, and offer a recoverable next action. Verify that error messages reveal no sensitive implementation detail or protected resource existence.
