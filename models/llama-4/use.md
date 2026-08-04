# Use - Meta Llama 4 (multimodal)

_What can it do? Capabilities, context window, chat template, languages, tool use, and
structured output live here._

<!-- item: capabilities -->
## Capabilities & modalities

Natively multimodal (image + text) mixture-of-experts models with strong general, coding, and
multilingual ability and very long context. Scout and Maverick are released; Behemoth is the
larger sibling.

<!-- item: context-window -->
## Context window & long-context behaviour

Scout advertises up to 10M tokens, Maverick up to 1M, per Meta. OneHill has not independently
measured effective recall at those lengths, so treat them as declared windows.

<!-- item: chat-template -->
## Prompt format & chat template

A Llama-4 chat template with header/turn special tokens and multimodal input formatting. Apply
via the tokenizer's chat template rather than hand-assembling prompts.

<!-- item: languages -->
## Language coverage

Broad multilingual coverage (a Llama strength); per-language depth varies and is not
exhaustively documented.

<!-- item: tool-use -->
## Function / tool calling

Documented tool-calling (built-in and custom), continuing the Llama 3.1+ tradition. Confirm the
schema per serving stack.

<!-- item: structured-output -->
## Structured / JSON-constrained output

Tool-calling supports structured responses; strict JSON / schema-constrained decoding is a
serving-layer feature (vLLM grammars), not a model guarantee.
