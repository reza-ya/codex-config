# Targeted design prompts (use selectively)

## Scope and value
Who is the user? What measurable outcome? What is expressly excluded? What would invalidate the need?
## Contracts
What inputs, outputs, permissions, errors, UX states, pagination, API versioning, client compatibility?
## Domain and data
Which entities own invariants? Concurrent writes? Transaction boundaries? Data retention? Uniqueness? Schema migration?
## .NET / ASP.NET Core
Endpoints vs controllers? DI lifetimes? CancellationToken? Authorization policy? EF Core tracking/migrations? Background jobs? Outbox? Structured logs? Integration tests? Modular Monolith boundaries?
## Next.js / React
Server vs client components? Auth/session boundaries? Caching/revalidation? Error/loading states? Accessibility? Optimistic updates? Hydration? API contract types?
## Security
Trust boundaries? Role/tenant isolation? PII? Secret handling? Rate limiting? CSRF/XSS? Audit trail?
## Reliability
Idempotent retries? Timeouts? Partial failure? Queue delivery semantics? Rollback? Backup/recovery?
## Operability
Telemetry, alerts, auditability, release flags, performance budgets, cost ceilings?
## Verification
Unit/integration/e2e boundaries? Reproduction steps? Explicit testable acceptance criteria? Unhappy paths?
