# Overview

This project is designed to give a bottom-up understanding of modern AI application building.

The important distinction is that an AI app is not "just a model". A usable system usually has several layers:

1. model
2. prompts
3. context
4. retrieval
5. tools
6. workflow or agent logic
7. evals
8. safety and reliability
9. product interface

## The Core Mental Model

### 1. Model

The model generates text, structured outputs, or tool calls. It is powerful but unreliable if left unconstrained.

### 2. Prompt

The prompt defines the job. Good prompting reduces ambiguity and makes downstream logic simpler.

### 3. Context

The model only sees what is in its context window. If key information is missing, the answer quality drops even if the model is strong.

### 4. Retrieval

Retrieval is how we fetch the right external information and feed it into the model. This is the foundation of RAG.

### 5. Tools

Tools let the model trigger actions or fetch structured data. This is how an AI system moves from "talking" to "doing".

### 6. Workflow vs Agent

A workflow is predefined logic with clear steps. An agent is a loop where the model decides what to do next. Most useful systems should start as workflows and become agentic only where necessary.

### 7. Evals

Without evals, people confuse a few good demos with actual quality. Evals convert intuition into measurement.

### 8. Reliability

Real systems need validation, retries, observability, and safety boundaries. Otherwise they fail in unpredictable ways.

## What We Are Actually Learning

We are not just learning "AI". We are learning how to build disciplined systems around LLMs.

That means learning:

- where models are strong
- where deterministic code should take over
- where retrieval helps
- where agents help
- where they create unnecessary complexity

## The Implementation Principle

Each concept in this repo must appear in two forms:

1. a short explanation in docs
2. a concrete implementation in code

That is the rule for this project. If a concept cannot be demonstrated in the project, it is probably not yet understood deeply enough.
