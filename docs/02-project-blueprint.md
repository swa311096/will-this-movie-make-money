# Project Blueprint

## Project Choice

We will build an AI research and execution copilot.

This project is a strong learning vehicle because it naturally supports:

- question answering
- structured extraction
- retrieval from documents
- tool use
- controlled agent loops
- MCP integrations
- skills and project instructions
- evaluation suites

## Why This Project Is Better Than a Random Chatbot

A plain chatbot teaches very little. It mostly teaches prompting.

This project is better because it forces the full stack of AI application concerns:

- when the model should answer directly
- when the system should retrieve context
- when the system should call tools
- when workflow logic should stay deterministic
- when agentic behavior is actually justified

## Product Vision

The user can give the system:

- a question
- a task
- a set of local documents
- a repository

The system should then:

- understand the request
- retrieve relevant context
- produce structured plans or outputs
- call tools when appropriate
- optionally run an agent loop for multi-step work
- explain its reasoning clearly enough to inspect

## What This Project Will Demonstrate

### Stage 1

A plain LLM-powered assistant with structured outputs.

This covers:

- prompts
- schemas
- deterministic wrappers

### Stage 2

A retrieval-backed assistant over project documents.

This covers:

- embeddings
- chunking
- search
- grounding

### Stage 3

A tool-using assistant.

This covers:

- tool calling
- validation
- action boundaries

### Stage 4

A controlled agent workflow.

This covers:

- planning loops
- step execution
- state
- stop conditions

### Stage 5

MCP integration.

This covers:

- standard protocol-based tools
- resource discovery
- integration design

### Stage 6

Skills and custom instructions.

This covers:

- AGENTS.md
- SKILL.md
- reusable task playbooks

### Stage 7

Evaluation and regression tracking.

This covers:

- task datasets
- retrieval evals
- agent outcome checks
- pass/fail expectations

## What We Will Avoid

We will avoid:

- building a vague general assistant
- adding agent loops before deterministic workflows
- treating RAG as mandatory for every feature
- treating evals as an afterthought
- optimizing UI before the system behavior is clear

## Showcase Value

If built well, this project will let you demonstrate:

- conceptual understanding
- architecture judgment
- implementation skill
- evaluation discipline

That is stronger than a flashy but shallow demo.
