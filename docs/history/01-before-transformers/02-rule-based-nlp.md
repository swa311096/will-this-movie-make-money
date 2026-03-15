# 02: Rule-Based NLP

The earliest natural language systems often relied on explicit rules written by humans.

The basic idea was simple:

if we know enough language rules, we can make the machine follow them.

## What A Rule-Based System Looks Like

A developer writes logic such as:

- if the sentence contains these words, classify it as positive
- if the pattern matches this template, extract this entity
- if this grammar rule applies, assign this structure

## Why This Approach Made Sense

At the beginning, this was a reasonable idea.

Humans understand language using patterns, so it was natural to try to write those patterns down.

## Simple Example

Imagine a sentiment system with rules like:

- if the text contains "good", mark it as positive
- if the text contains "bad", mark it as negative

This works for:

- "The movie was good."
- "The movie was bad."

But it starts failing quickly on:

- "The movie was not bad."
- "The movie looked good, but it was boring."
- "Good luck finishing that disaster."

## The Core Problem

Language has too many edge cases.

Every time you add more rules, you usually uncover more exceptions.

This creates three problems:

1. the system becomes hard to maintain
2. rules conflict with one another
3. performance breaks outside the cases you anticipated

## Why This Matters

Rule-based systems taught an important lesson:

language understanding does not scale well if the system depends on humans manually encoding every pattern.

## What Came Next

This limitation pushed the field toward statistical methods.

Instead of telling the system exactly how language works, researchers started asking:

can the machine learn patterns from data instead?
