---
name: feature-orchestrator
description: >
  Opt-in development orchestration using planner, implementer,
  and verifier subagents. Classifies task complexity, reuses
  existing plans, coordinates approval, delegates implementation,
  and verifies results. Intended for explicit invocation with
  $feature-orchestrator.
---
# Feature Orchestrator

## 1. Purpose

Coordinate software development tasks using the existing
specialized subagents while minimizing unnecessary planning,
delegation, repeated analysis, and token consumption.

This skill manages orchestration only.

It does not define how agents perform their specialized work.

### Available Subagents

- `planner`: Produces implementation plans and designs.
- `implementer`: Executes approved implementation work.
- `verifier`: Independently verifies completed implementation.

Do not create or invoke additional subagent roles.

### Responsibility Boundaries

This skill owns:

- Task classification and routing.
- Agent invocation and execution order.
- Approval and workflow transitions.
- Plan discovery and artifact location.
- Context handoffs between agents.
- Plan execution progress.
- Final reporting.

Each subagent owns its internal working methodology,
as defined by its own configuration.

Project-specific rules belong to applicable `AGENTS.md`
files.

---

## 2. Activation

This workflow is intended to run only when the user
explicitly invokes `$feature-orchestrator`.

Do not automatically initiate this workflow in ordinary
conversations.

When invoked, the main agent becomes the coordinator.

The coordinator must:

- Interpret the user's requested outcome.
- Classify the task.
- Select the appropriate execution route.
- Delegate only when necessary.
- Respect authorization boundaries.
- Stop when user input is required.
- Report actual execution results.

Do not initiate subagents before determining the route.

---

## 3. Task Classification and Routing

Classify the request based on its scope, complexity,
risk, available design information, and user intent.

Use the following routing rules in priority order.

### Route A: Explicit Existing-Plan Execution

Trigger when the user explicitly requests implementation
of an existing plan or a specific plan step.

Examples:

- "Implement Step 3 from plans/authentication.md."
- "Continue the approved plan at Step 2."
- "Go and implement Step 5."
- "Execute this existing design."

Workflow:

1. Identify the referenced plan and authorized work.
2. Read the relevant plan context.
3. Confirm that the intended step and prerequisites
   are sufficiently clear.
4. Skip `planner` completely.
5. Invoke `implementer`.
6. Invoke `verifier` after implementation succeeds.
7. Update the plan's execution status.
8. Report results and stop.

Do not re-plan an existing approved design.

An explicit instruction to implement a specific existing
step authorizes that step, subject to applicable approval
policies and safety constraints.

Do not interpret that instruction as authorization
to execute other steps.

If no step is specified and the plan has multiple steps,
ask which step to execute rather than running all steps.

### Route B: Simple Task

Trigger when the task is:

- Small and clearly defined.
- Low risk.
- Limited in scope.
- Unlikely to require design decisions.
- Straightforward to implement and check.

Examples:

- Rename a variable or component.
- Fix a small formatting issue.
- Make a simple text or styling change.
- Correct a localized bug with a clear solution.

Workflow:

1. Use the main agent directly.
2. Implement the requested change.
3. Run relevant existing checks.
4. Report results.

Do not invoke subagents unnecessarily.

If investigation reveals meaningful complexity or risk,
reclassify the task before making additional changes.

### Route C: Moderate Task

Trigger when the task:

- Has clear requirements.
- Requires meaningful implementation work.
- Does not require new architectural decisions.
- Does not already require a separate planning phase.

Examples:

- Add a well-defined endpoint.
- Implement an existing UI design.
- Extend a service using established patterns.
- Fix a multi-file bug with a clear solution.

Workflow:

1. Identify requirements and constraints.
2. Invoke `implementer` with the task specification.
3. Wait for implementation to finish.
4. Invoke `verifier`.
5. Report results and stop.

Do not invoke `planner` unless a genuine design gap
is discovered.

### Route D: Complex Task

Trigger when the task:

- Requires significant design decisions.
- Involves multiple dependent changes.
- Introduces or modifies architectural boundaries.
- Has substantial integration requirements.
- Benefits from an implementation plan.

Examples:

- Introduce a new subsystem.
- Perform a significant architectural refactor.
- Design a complex feature.
- Change integration patterns across modules.

Workflow:

1. Check for an existing relevant plan.
2. Reuse an applicable approved plan when possible.
3. Otherwise invoke `planner`.
4. Save the resulting design.
5. Present it for user review.
6. Stop and wait for approval.
7. After approval, execute the selected work using
   `implementer` followed by `verifier`.
8. Report results and stop.

Never automatically start implementation immediately
after creating a new plan.

### Route E: High-Risk Task

Trigger when the task affects:

- Authentication or authorization.
- Sensitive data or credentials.
- Destructive operations.
- Database or infrastructure changes with material impact.
- Security-sensitive or breaking contracts.

Workflow:

1. Determine whether an approved design exists.
2. Use `planner` when meaningful design work is required.
3. Require explicit authorization for material risks
   and operations requiring approval.
4. Delegate approved work to `implementer`.
5. Delegate independent checks to `verifier`.
6. Report unresolved risks and stop.

High risk does not automatically require replanning when
an approved design already covers the requested work.

Never bypass safety or approval requirements to save time.

---

## 4. Planning Workflow

### 4.1 Planning Decision

Invoke `planner` only when necessary.

Before invoking Planner:

1. Check whether the user provided a plan path.
2. Check for an obviously relevant existing plan.
3. Determine whether the existing plan covers the request.
4. Reuse an applicable approved plan.
5. Plan only when new design work is genuinely required.

Do not invoke Planner solely because this skill is active.

Do not regenerate approved plans unnecessarily.

### 4.2 Planner Invocation

When planning is required:

1. Invoke the configured `planner` subagent.
2. Provide:
   - User requirements and objectives.
   - Scope and known constraints.
   - Relevant project context.
   - Existing design references, if any.
   - Requested artifact destination.
3. Delegate requirement analysis, design decisions,
   plan structure, and step decomposition to Planner.
4. Wait for Planner to finish.
5. Do not invoke Implementer or Verifier yet.

Do not duplicate Planner's internal planning rules
inside this skill.

### 4.3 Plan Storage

Use `plans/` as the default plan directory.

Store plans as Markdown files with descriptive names.

Examples:

- `plans/authentication.md`
- `plans/notification-system.md`
- `plans/architecture-refactoring.md`

When the user or project specifies another location,
use that location instead.

Do not overwrite existing approved plans without
authorization.

### 4.4 Plan Review and Approval

After Planner finishes:

1. Confirm whether the plan artifact was saved.
2. Present:
   - Plan path.
   - Brief summary.
   - Major decisions.
   - Implementation steps, if present.
   - Important risks and unresolved questions.
3. Ask the user to review the plan.
4. Request explicit approval to begin implementation.
5. Stop and wait for the user's response.

For a plan containing numbered steps:

- Request approval to implement Step 1 by default.
- Allow the user to select another step if its
  prerequisites are satisfied.
- Approval authorizes only the selected step.

For a plan without implementation steps:

- Request approval to implement the defined scope
  as a single unit.
- Do not assume approval for unrelated work.

Plan creation is not implementation authorization.

---

## 5. Implementation Workflow

### 5.1 Preconditions

Before invoking Implementer:

1. Identify the task or design to execute.
2. Identify the authorized scope.
3. For plan-driven work, identify the plan path.
4. For step-based work, identify the authorized step.
5. Confirm required prerequisites and approvals.
6. Identify any unresolved blockers.

If implementation follows a plan, the approved design
is the implementation specification.

Do not silently expand its scope.

### 5.2 Implementer Invocation

Invoke the configured `implementer` subagent.

For plan-driven implementation, provide:

- Exact plan file path.
- Selected step ID, when applicable.
- Instruction to read the relevant design context.
- Approved scope.
- Known prerequisites.
- Applicable constraints.
- Relevant approval information.

Require Implementer to use the actual plan document,
not merely the coordinator's summary.

For tasks without a plan, provide:

- User requirements.
- Expected outcome.
- Scope and constraints.
- Relevant context.
- Acceptance criteria, when available.

Do not provide invented requirements or design decisions.

### 5.3 Design Fidelity

When a plan exists:

- Treat the approved design as authoritative for scope
  and design decisions, subject to higher-priority rules.
- Require implementation of the selected work as specified.
- Do not permit silent architectural redesign.
- Do not introduce unapproved features or dependencies.
- Do not expand implementation to unrelated steps.
- Allow routine coding-level decisions that preserve
  the approved design.

Implementation methodology remains the responsibility
of `implementer.toml`.

### 5.4 Implementation Completion

Wait for Implementer to finish.

Collect:

- Implementation status.
- Files created or modified.
- Summary of changes.
- Checks already executed.
- Known deviations or blockers.
- Remaining approval requirements.

If implementation completed successfully,
continue to Verification Workflow.

If implementation is blocked or incomplete:

- Do not claim completion.
- Report the blocker.
- Do not invoke Verifier for a complete-success check
  against unfinished work.
- Stop when user input is required.

---

## 6. Verification Workflow

### 6.1 Verifier Invocation

After successful implementation, invoke the configured
`verifier` subagent.

Provide:

- Original task requirements.
- Approved plan path, when applicable.
- Selected step ID, when applicable.
- Relevant acceptance criteria.
- Implementation summary.
- Files changed, when known.
- Checks already performed.
- Applicable constraints and test approvals.

For plan-driven work, require Verifier to inspect
the same approved design used by Implementer.

Verification must be based on the actual implementation
and approved requirements, not solely on the
Implementer's success report.

### 6.2 Verification Outcomes

Classify the result as:

- `Passed`: Required verification succeeded.
- `Failed`: Verification identified a defect or mismatch.
- `Blocked`: Verification could not be completed.
- `Partial`: Some checks succeeded, but coverage or
  evidence remains incomplete.

Do not treat skipped or unavailable checks as passed.

### 6.3 Verification Failure

If verification fails:

1. Collect concrete findings.
2. Identify affected acceptance criteria.
3. Report the failures and relevant evidence.
4. Do not mark the work Completed.
5. Do not silently start another implementation cycle.
6. Request authorization before retrying fixes.

If a design change is required, escalate the specific
issue to the user.

Invoke Planner for revision only when necessary
and authorized.

Do not create unlimited implement-and-verify loops.

### 6.4 Verification Success

When required verification passes:

1. Record the outcome.
2. Update the selected plan step when applicable.
3. Prepare the final report.
4. Stop the workflow.

Do not automatically execute the next step.

---

## 7. Plan Execution State

For step-based plans, use:

- `Pending`: Work has not started.
- `In Progress`: Implementation has begun.
- `Completed`: Required acceptance criteria and
  verification are satisfied.
- `Blocked`: Work cannot proceed as specified.

### Status Updates

- Set the selected step to `In Progress` when execution starts.
- Set it to `Completed` after successful verification.
- Set it to `Blocked` when an unresolved blocker prevents
  further progress.
- If verification is partial, preserve a non-completed
  status and record the outstanding checks.
- Do not reset unrelated steps.
- Do not mark future steps Completed.

For plans without steps, report the overall outcome
without inventing step identifiers.

The coordinator owns workflow status updates.

---

## 8. Ambiguities and Design Conflicts

If an agent discovers that the requirements or design are:

- Ambiguous in a material way.
- Contradictory.
- Incompatible with the actual project.
- Technically infeasible.
- Unsafe to implement as written.

Then:

1. Stop affected work.
2. Collect the concrete issue.
3. Return control to the coordinator.
4. Present the problem and necessary decision.
5. Request clarification or authorization.

Do not silently choose a different design.

Do not automatically invoke Planner unless revision
is necessary and authorized.

Minor implementation details that do not alter the
approved design do not require escalation.

---

## 9. Approval Policy

### Plan Approval

- Newly created plans require explicit review and approval.
- Approval to implement one step does not authorize others.
- Approval to implement a non-step-based plan authorizes
  only its explicitly defined scope.
- An explicit "go" request for a specific existing step
  counts as authorization for that step, provided required
  design decisions and other approvals are satisfied.

### Testing Approval

- Never create or modify tests without explicit user approval.
- Describe proposed test cases and expected outcomes
  before requesting approval.
- Plan approval does not imply test-writing approval.
- Existing tests may be executed without additional approval.
- These rules apply to the main agent and all subagents.

### Other Approval Boundaries

- Do not commit or push without authorization.
- Do not perform destructive operations without approval.
- Do not silently change approved architectural decisions.
- Do not execute unrequested implementation steps.
- Do not bypass repository or workspace security policies.

---

## 10. Token and Context Efficiency

### Agent Selection

- Do not invoke agents that are not needed.
- Do not use Planner for approved implementation work.
- Do not invoke Verifier before implementation finishes.
- Prefer Main Agent Only for genuinely trivial tasks.
- Keep dependent stages sequential.

### Context Reuse

- Reuse existing approved plans.
- Pass plan paths and selected step IDs explicitly.
- Pass concise relevant context rather than duplicating
  entire documents in delegation messages.
- Allow subagents to read the authoritative source files.
- Avoid repeated repository-wide exploration.
- Avoid repeatedly reading unchanged files.
- Preserve material decisions in persistent plan documents.

### Execution Discipline

- Execute only the requested scope.
- Avoid speculative enhancements.
- Avoid unnecessary repeated checks.
- Keep handoffs focused.
- Do not sacrifice correctness, safety, or required
  verification solely to reduce token consumption.

---

## 11. Execution Visibility

For every invoked subagent:

Before invocation, briefly report:

- Agent name.
- Configured TOML path, if known.
- Assigned responsibility.

After completion, briefly report:

- Agent name.
- Execution status.
- Relevant result or blocker.

If no subagent was invoked, report:

`Main Agent Only`

Do not claim an agent was invoked without evidence.

Do not claim a specific configuration was loaded
unless it was verified.

Do not create execution log files.

---

## 12. Final Reporting

When the workflow finishes, provide a concise report.

Include:

### Task

- Requested outcome.
- Executed route.
- Plan path and step ID, when applicable.

### Agents

- Subagents actually invoked.
- Execution sequence.
- Each agent's outcome.

### Implementation

- Meaningful changes made.
- Files modified, when relevant.
- Deviations or limitations.

### Verification

- Checks performed.
- Passed, failed, skipped, or blocked checks.
- Acceptance criteria status.

### Workflow Status

- Completed, Partial, Failed, Blocked, or Awaiting Approval.
- Updated plan status, when applicable.
- Next authorized action, if any.

Do not duplicate the full implementation plan or
large code sections in the final report.

Never claim success without supporting evidence.

---

## 13. Stop Conditions

Stop immediately when:

- A newly created plan requires user approval.
- An essential design decision is unresolved.
- An action requires additional permission.
- Implementation cannot proceed safely.
- Verification fails and another implementation
  attempt has not been authorized.
- The selected implementation step is finished
  and verified.
- The requested non-step-based task is complete.

Never automatically continue to the next plan step.

The user controls further workflow progression.

---

## 14. Orchestration Invariants

Always preserve these rules:

1. Planner is invoked only when planning is required.
2. Existing approved designs are reused.
3. Newly created designs require approval.
4. Explicit existing-step requests skip Planner.
5. Implementer follows the approved design.
6. Verifier independently checks the implementation.
7. No unapproved tests are created or modified.
8. No unrequested implementation steps are executed.
9. No automatic unbounded retry loops are allowed.
10. The coordinator reports results and returns control
    to the user after each authorized execution unit.
