# Use - Meta Llama 4 (multimodal)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Natively multimodal (image + text) mixture-of-experts models with strong general, coding and
multilingual ability and very long context. Scout and Maverick are released; Behemoth is the
larger sibling.

<!-- item: context-window -->
## Context window & long-context behaviour

Meta advertises up to 10M tokens for Scout and 1M for Maverick. OneHill has not measured
effective recall at those lengths, so treat them as declared windows.

<!-- item: chat-template -->
## Prompt format & chat template

Llama 4 uses a chat template with header/turn special tokens and multimodal input formatting.
Apply it through the tokenizer's chat template instead of assembling prompts by hand.

<!-- item: languages -->
## Language coverage

Multilingual coverage is broad, a Llama strength. Per-language depth varies and is not
exhaustively documented.

<!-- item: tool-use -->
## Function / tool calling

Tool calling is documented (built-in and custom), continuing the Llama 3.1+ tradition. Confirm
the schema per serving stack.

<!-- item: structured-output -->
## Structured / JSON-constrained output

Tool calling supports structured responses. Strict JSON or schema-constrained decoding is a
serving-layer feature (vLLM grammars), not a model guarantee.
