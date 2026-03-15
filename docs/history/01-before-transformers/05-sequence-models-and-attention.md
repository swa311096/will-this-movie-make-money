# 05: Sequence Models and Attention

Once researchers had better word representations, the next challenge was handling language across time.

Words do not appear independently. Meaning depends on sequence.

## Why Sequence Matters

These two sentences use the same words but mean different things:

- "Dog bites man."
- "Man bites dog."

A good language system must care about order.

## Sequence Models

This is where models like RNNs, LSTMs, and GRUs became important.

They process text as a sequence and try to carry forward useful information from earlier tokens.

## What They Improved

Compared with simpler earlier methods, sequence models improved:

- translation
- text generation
- speech recognition
- sequence labeling tasks

## Simple Example

In this sentence:

"The film started well, but by the end it felt empty."

the meaning near the end depends on what came before.

A sequence model tries to carry that earlier information forward as it processes the sentence.

## The Main Limitation

Sequence models often struggled with long-range dependencies.

As the sequence grew longer, important earlier information could fade or become hard to use.

They were also harder to parallelize efficiently during training.

## Attention

Attention was a major breakthrough because it let the model look back more directly at relevant parts of the input.

Instead of depending only on one running compressed state, the model could ask:

"Which earlier tokens matter most right now?"

## Simple Example

In translation, when generating a word in the output sentence, attention can help the model focus on the most relevant source word or phrase.

## Why Attention Was So Important

Attention did not just improve old sequence models.

It pointed toward a new architecture that would become the transformer.

That is where the next part begins.
