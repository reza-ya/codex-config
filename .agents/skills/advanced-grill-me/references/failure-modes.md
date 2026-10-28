# Failure-mode prompts

Use risk-based scenario walkthroughs. For each: trigger, observed behavior, expected behavior, mitigation, proof/test, owner.

- Two requests concurrently modify the same entity; stale write or duplicate execution.
- Network timeout after server commits, followed by a client retry.
- Actor attempts cross-tenant read/write or privilege escalation.
- Migration runs with mixed old/new app versions.
- External dependency returns partial response or rate-limits requests.
- User cancels during a long-running operation; cleanup and state consistency.
- Monitoring shows success while output is wrong; how is correctness measured?
- Rollback must restore behavior without losing writes.

Do not invent failures as confirmed bugs. Mark as scenarios to test.
