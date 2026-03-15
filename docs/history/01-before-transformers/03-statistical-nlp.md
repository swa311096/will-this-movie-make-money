# 03: Statistical NLP

Statistical NLP was a major shift in mindset.

Instead of writing every rule by hand, researchers used large amounts of text data to estimate how language behaves.

## The New Idea

The system does not need an explicit rule for every case.

Instead, it can learn probabilities such as:

- how often words appear together
- how likely one word is to follow another
- which patterns correlate with a label

## Why This Was Better

This approach handled variation better than strict rules.

A model could learn from examples instead of depending only on manual pattern design.

## Simple Example: N-Grams

An n-gram model looks at short sequences of words.

If it sees:

- "New York" very often
- "machine learning" very often

it learns that those sequences are meaningful and likely.

That already gives better behavior than a hand-written system that never saw those patterns.

## What Statistical NLP Could Do Well

- language modeling over short contexts
- tagging and labeling tasks
- text classification
- machine translation components

## What It Could Not Do Well

These models were often good at local regularities, but weak at deeper meaning.

They struggled with:

- long-range dependencies
- flexible context use
- richer semantic representation

## Why This Still Mattered

Statistical NLP proved that language systems improve when they learn from data rather than relying only on handcrafted rules.

That was a foundational change.

## What Came Next

The next question became:

how can we represent word meaning more effectively than just counts and short-range probabilities?

That leads to embeddings.
