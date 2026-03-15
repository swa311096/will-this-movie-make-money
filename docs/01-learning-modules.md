# Learning Modules

This is the exact module sequence for the project.

The ordering matters. Each module depends on earlier ones.

If a keyword feels unfamiliar, check `docs/00-overview.md` first and `docs/glossary.md` for the short definition.

## Module 1: AI Systems Map

Learn the moving parts of an AI app:

- model
- prompt
- context
- retrieval
- tools
- agent logic
- evals
- reliability

Outcome:
You can describe the architecture of an AI app without collapsing everything into "the model".

## Module 2: LLM Fundamentals

Learn:

- tokens
- context windows
- sampling and temperature
- latency and cost
- hallucinations
- instruction hierarchy

Outcome:
You know what an LLM can and cannot be trusted to do.

## Module 3: Prompting and Structured Output

Learn:

- task framing
- role and constraint design
- few-shot prompting
- schema-driven outputs
- extraction and classification patterns

Outcome:
You can make the model produce reliable machine-readable outputs.

## Module 4: Embeddings and Semantic Search

Learn:

- embeddings
- vector similarity
- keyword search vs semantic retrieval
- chunking fundamentals

Outcome:
You understand how a system can find relevant information instead of relying only on the prompt.

## Module 5: RAG (Retrieval-Augmented Generation)

Learn:

- chunking strategies
- indexing
- retrieval
- reranking
- citations
- grounding
- common failure modes

Outcome:
You can explain when RAG is useful and implement a basic retrieval-backed assistant.

## Module 6: Tool Calling

Learn:

- tool schemas
- function calling loops
- validation
- execution boundaries
- deterministic code around model output

Outcome:
You can make the model trigger real actions safely.

## Module 7: Agent Workflows

Learn:

- workflow vs agent
- planner/executor patterns
- iterative loops
- stop conditions
- state management

Outcome:
You can build agentic behavior intentionally instead of using loops blindly.

## Module 8: MCP (Model Context Protocol)

Learn:

- what MCP solves
- MCP server and client roles
- tools vs resources
- integration patterns

Outcome:
You understand how standardized model-tool integration works.

## Module 9: Skills, AGENTS, and SKILL.md

Learn:

- repo-level instructions
- reusable task playbooks
- skill boundaries
- context discipline

Outcome:
You can explain how an agent is customized for a project or workflow.

## Module 10: Evals

Learn:

- golden datasets
- assertion-based evals
- judge-model evals
- retrieval evals
- agent task evals
- regression testing

Outcome:
You can measure whether the system is improving or regressing.

## Module 11: Reliability and Guardrails

Learn:

- output validation
- retries
- fallbacks
- prompt injection awareness
- tool safety
- user boundary enforcement

Outcome:
You can make the system less brittle and less dangerous.

## Module 12: Memory and State

Learn:

- short-term context
- persistent memory
- session state
- what should and should not be remembered

Outcome:
You can design continuity without creating confusion or unnecessary storage.

## Module 13: Model Selection and Adaptation

Learn:

- choosing models for task quality, latency, and cost
- prompt engineering vs RAG vs fine-tuning
- high-level transformer and RLHF/RLAIF concepts

Outcome:
You can justify architectural choices instead of copying patterns.

## Module 14: Observability and Cost

Learn:

- logs
- traces
- token accounting
- failure inspection
- cost monitoring

Outcome:
You can run the system with visibility into performance and spend.

## Module 15: AI Prototyping Workflow

Learn:

- start simple
- set baselines
- iterate with evals
- avoid premature agent complexity

Outcome:
You can build quickly without losing rigor.

## Module 16: Deployment Patterns

Learn:

- local prototype
- service layer
- app integration
- background jobs
- config and secrets

Outcome:
You can move from experiment to a usable demo or product foundation.

## What We Will Cover First

The first implementation pass will prioritize:

1. Module 1
2. Module 2
3. Module 3
4. Module 5
5. Module 6
6. Module 7
7. Module 8
8. Module 9
9. Module 10

The rest will be layered in as the system matures.
