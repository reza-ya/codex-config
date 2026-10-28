# Repository Instructions

## 1. Instruction Hierarchy

- The root `AGENTS.md` defines the repository-wide rules and takes precedence over nested `AGENTS.md` files when instructions conflict.
- Nested `AGENTS.md` files may introduce directory-specific rules, provided they do not contradict the root instructions.
- Apply both root and directory-specific instructions whenever they are compatible.
- If a conflict is detected, follow the root instructions and briefly report the conflict.

## 2. General Guidelines

- Keep changes focused on the requested task.
- Do not refactor unrelated code.
- Never expose secrets, credentials, or sensitive information.
- Follow existing project architecture, conventions, and coding standards.
- Ask for clarification when requirements are ambiguous or important decisions are missing.
- Use consistent indentation and line breaks.
- Do not activate the `feature-orchestrator` skill or its
  multi-agent workflow unless the user explicitly invokes
  `$feature-orchestrator`.

## 3. Avoid Overengineering

- Prefer simple, clean, and maintainable solutions.
- Implement only what is required by the current task.
- Avoid unnecessary abstractions, design patterns, architectural layers, and dependencies.
- Do not introduce complexity for hypothetical future requirements.
- Reuse existing solutions and conventions whenever practical.
- Choose the simplest solution that satisfies the requirements without compromising correctness, security, or maintainability.

## 4. Test Approval Policy

- Before creating or modifying any test, explain what you intend to test and why.
- Present the proposed test cases and their expected outcomes.
- Wait for explicit user approval before writing or modifying tests.
- Never assume that approval for feature implementation includes approval to write tests.
- Existing tests may be executed without additional approval.
- If new or updated tests are necessary but approval has not been granted, report the proposed tests and wait for approval.
- This policy applies to the main agent and all subagents.
- Approval for implementing a feature does not imply approval to create tests.

## 5. Development Workflow

- Implement changes incrementally, following the approved plan when one exists.
- Explain important architectural decisions and their trade-offs.
- Avoid unnecessary planning or repeated analysis when an approved plan already exists.
- Do not expand the scope of an approved implementation step without permission.
- Run relevant existing builds, tests, and checks before completing a task.
- Never claim that verification succeeded unless the relevant checks were actually executed.
- Report failed, skipped, or unavailable checks honestly.
- Summarize implemented changes and any remaining issues concisely.

## 6. Code Quality

- Use descriptive names for variables, methods, and classes.
- Prefer small functions with a single responsibility.
- Use early returns to reduce unnecessary nesting.
- Handle errors explicitly and consistently.
- Avoid duplicated logic where practical.
- Optimize for readability and maintainability over cleverness.
- Keep implementations consistent with existing patterns unless there is a justified reason to change them.

## 7. Agent Execution Visibility

- During task execution, briefly announce in the chat whenever a subagent starts or finishes.
- Include the subagent's name, configured TOML path (if known), and execution status.
- If no subagent is used, indicate `Main Agent Only`.
- Never report unverified agent activity or claim that a specific configuration was loaded without evidence.
- Keep status updates concise.
- Do not create execution log files unless explicitly requested.

## 8. Token Efficiency

- Inspect only files relevant to the current task and its necessary dependencies.
- Avoid repeatedly reading files when their relevant contents are already available.
- Reuse existing implementation plans instead of generating new ones unnecessarily.
- Avoid spawning unnecessary subagents.
- Keep tool calls and reports focused without sacrificing correctness.
- Do not sacrifice required verification, security, or code quality solely to reduce token usage.
