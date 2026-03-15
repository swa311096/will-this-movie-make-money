# Roadmap

This is the execution roadmap for the repository.

## Phase 0: Orientation

Goal:
Lock the curriculum, architecture, and project scope.

Deliverables:

- overview docs
- learning modules
- project blueprint
- implementation roadmap

## Phase 1: Minimal LLM App

Goal:
Build the smallest possible useful assistant with structured output.

Deliverables:

- API wrapper
- prompt layer
- schema-validated response objects
- small CLI or local web interface

Learning focus:

- LLM fundamentals
- prompt design
- structured outputs

## Phase 2: Retrieval Layer

Goal:
Add local document ingestion and retrieval.

Deliverables:

- document loader
- chunker
- embedding pipeline
- retrieval endpoint
- cited answers

Learning focus:

- embeddings
- RAG
- grounding

## Phase 3: Tool Use

Goal:
Let the system perform bounded actions through explicit tools.

Deliverables:

- tool registry
- tool schema definitions
- execution loop
- validation and error handling

Learning focus:

- function calling
- deterministic wrappers
- safety boundaries

## Phase 4: Agent Workflow

Goal:
Introduce a controlled planning and execution loop.

Deliverables:

- task planner
- step executor
- state object
- loop guardrails

Learning focus:

- workflow vs agent
- state
- stop conditions

## Phase 5: MCP Integration

Goal:
Connect the system to MCP-style tools or resources.

Deliverables:

- MCP integration notes
- at least one MCP-backed capability
- comparison against direct tool integration

Learning focus:

- MCP model
- client/server boundaries

## Phase 6: Skills and Instructions

Goal:
Make the system explicitly configurable through repo instructions and skills.

Deliverables:

- project-level instructions
- one or more example skills
- examples showing behavior change

Learning focus:

- AGENTS.md
- SKILL.md
- reusable workflows

## Phase 7: Evals

Goal:
Measure the system instead of relying on intuition.

Deliverables:

- baseline eval dataset
- prompt/output assertions
- retrieval checks
- agent success criteria

Learning focus:

- eval design
- regression testing

## Phase 8: Reliability and Showcase

Goal:
Make the project demoable and defensible.

Deliverables:

- logging and traces
- failure handling
- polished demo flow
- concise architecture write-up

Learning focus:

- reliability
- observability
- communication

## Implementation Rule

Each phase should produce:

1. code
2. a short explanation
3. an eval or verification step
4. a short public post draft

That prevents the project from turning into a pile of disconnected experiments.
