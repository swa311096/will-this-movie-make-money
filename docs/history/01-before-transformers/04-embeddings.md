# 04: Embeddings

Embeddings changed how words were represented.

Before embeddings, many systems treated words more like discrete symbols or counts.

Embeddings moved the field toward learned numeric representations of meaning.

## The Core Idea

Represent each word as a vector.

A vector is just a list of numbers, but the important part is this:

words used in similar contexts end up with similar vectors.

## Why This Was Useful

Now the model could capture rough semantic relationships.

For example:

- "cat" and "dog" can end up closer together
- "doctor" and "hospital" can end up related
- "Paris" and "France" can show meaningful structure

## Simple Intuition

Think of embeddings as placing words on a semantic map.

Words with similar usage patterns end up near one another on that map.

## What This Improved

Embeddings helped models move beyond simple word counts.

They made it easier to generalize between related words and contexts.

## The Big Limitation

Classic embeddings usually assign one vector per word.

That means:

- `bank` in "river bank"
- `bank` in "bank account"

may get the same representation even though the meanings differ.

## Why This Matters

Embeddings were a huge step forward, but they still did not fully solve context-sensitive meaning.

That pushed the field toward models that process full sequences more effectively.
