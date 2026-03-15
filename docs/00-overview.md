# Overview

This project is designed to give a bottom-up understanding of modern AI application building.

The important distinction is that an AI app is not "just a model". A usable system usually has several layers working together.

## How To Read This Repo

This repository should define a term before it starts using that term casually.

That means:

- the overview introduces the main ideas in plain language
- the glossary gives short reference definitions
- later documents assume those basics and go deeper

## Core Terms

### LLM

LLM stands for Large Language Model.

In practice, an LLM is the part of the system that reads text input and produces text output. Depending on how it is configured, it can also produce structured data or decide that a tool should be called.

### Prompt

A prompt is the instruction and input we send to the model.

It usually includes:

- the task
- constraints
- formatting requirements
- any relevant context

### Context Window

The context window is the amount of text the model can "see" in a single request.

If useful information is outside that window, the model cannot use it. This is why context management matters.

### Structured Output

Structured output means asking the model to return data in a machine-readable format such as JSON instead of only free-form prose.

This is important when application code needs predictable outputs.

### Retrieval

Retrieval means finding relevant information from an external source and bringing it into the model's input.

Examples:

- searching a document collection
- finding relevant code files
- looking up records in a database

### RAG

RAG stands for Retrieval-Augmented Generation.

It is a pattern where the system first retrieves relevant information and then asks the model to answer using that information.

In short:

- retrieval finds useful context
- generation uses that context to produce an answer

### Tool

A tool is a function or capability outside the model that the model can ask the system to use.

Examples:

- search a codebase
- call an API
- read a file
- write a record

Tools matter because they let the system do things, not just describe things.

### Workflow

A workflow is a fixed sequence of steps controlled mostly by normal code.

Example:

1. classify the request
2. retrieve context
3. call the model
4. validate the output

### Agent

An agent is a system where the model has more control over deciding the next step.

Instead of following only a fixed flow, it can choose actions iteratively. This is useful in some cases, but it also makes systems harder to reason about and evaluate.

### Eval

An eval is a test or measurement that checks whether the AI system behaves the way we expect.

Without evals, people often confuse a few impressive outputs with actual system quality.

### MCP

MCP stands for Model Context Protocol.

It is a standard way for models and tools or resources to connect through a shared protocol instead of custom one-off integrations.

### Skill

In this repo, a skill is a reusable set of instructions for how an agent should perform a specific kind of task.

This is usually described in a `SKILL.md` file.

## System Layers

Once those terms are clear, the basic layers of an AI app look like this:

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

There is also a third output for major milestones:

3. a short public post draft

If you cannot explain the concept clearly to another person, the understanding is still incomplete.
