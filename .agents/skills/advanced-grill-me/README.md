# Advanced Grill Me (Codex skill)

An original, extended implementation inspired by the *approach* of Matt Pocock's grill-me/grilling. This package does not copy their skill text. It is intended as a self-contained skill and does **not** depend on `grilling` being installed.

## Install in your repository
Copy this **entire** `advanced-grill-me/` directory into:

`<repository>/.agents/skills/advanced-grill-me/`

Use the skill in a **new Codex thread**, for example:

`Use $advanced-grill-me to stress-test a proposed order management feature. Read AGENTS.md and relevant backend code, ask architecture decisions in rounds, and don't write feature code.`

Global install option (if supported by your Codex version): `~/.agents/skills/advanced-grill-me/`. Repository-local path is recommended for this exercise. For Windows the repository path works unchanged; `~` is usually your Windows home directory.

## Files
- `SKILL.md`: main agent instructions and behavioral contract.
- `references/`: deep design rules only loaded when needed.
- `assets/`: state, decision, and final-plan templates.
- `scripts/validate_state.py`: Python standard-library, **read-only**, optional state validation.
- `evals/cases.md`: manual behavioral test matrix.
- `agents/openai.yaml`: optional UI metadata.

## Resuming a session
Ask: `Use $advanced-grill-me in resume mode for plans/grill-sessions/<session-id>. Reconcile current code and outstanding decisions. Do not implement.`

Persistence only occurs when Codex has the required file permissions and writes the state; Markdown instructions alone do not guarantee a durable checkpoint or exact agent orchestration.

## Safety and limitations
The skill does not change permissions, choose a model, guarantee activation, or create subagents. Its state validator checks structure/basic invariants, not whether architecture decisions are technically correct. File output and script execution depend on Codex tooling and permissions. Review all code before running it.
