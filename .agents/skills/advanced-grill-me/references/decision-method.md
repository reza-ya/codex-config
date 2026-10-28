# Decision graph and prioritization

Each decision D has `id`, `prerequisites`, `options`, `recommendation`, `evidence`, `status`, `risk`, `owner`. Distinguish constraints (externally fixed), choices (user must own), hypotheses (need verification), and facts (supported by repository evidence). Never promote a recommendation to approved without permission.

## Frontier algorithm
1. List unresolved decisions.
2. Exclude any with unsettled prerequisites.
3. Rank ready decisions by impact × uncertainty × irreversibility (1–5 each). Break ties by dependency-unblocking count.
4. Choose 1–4 independent items per round. Ask recommendations and trade-offs; await answers.
5. Recompute graph after response; add emerging dependent decisions. Detect cycles; reformulate them into a single joint decision.

## Conflict and stopping rules
- When the user contradicts a previous decision, point out the exact conflict, propose options, and re-open dependent nodes.
- For an unknown that can be resolved from code, inspect read-only before asking.
- A deferred blocker means not-ready; a deferred low-risk detail can appear in rollout follow-ups.
- End only with explicit confirmation, evidence, testable acceptance criteria and no hidden blockers.
