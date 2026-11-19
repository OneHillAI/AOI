# Use - DeepSeek-R1-Distill (Qwen base)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Text reasoning models (maths, coding, analysis) distilled from R1 into dense 1.5B-32B
weights. They emit explicit reasoning traces (think tags). They are strong for their size,
most of all the 14B and 32B.

<!-- item: context-window -->
## Context window & long-context behaviour

The cards declare a 128K-token context, from the Qwen2.5 bases. OneHill has not measured
effective long-context recall, so treat 128K as the declared window.

<!-- item: chat-template -->
## Prompt format & chat template

The models ship a chat template with the R1 reasoning (think-tag) convention. Use
`apply_chat_template` and decide in the client whether to expose or strip the reasoning segment.

<!-- item: languages -->
## Language coverage

English and Chinese are strongest (Qwen2.5 base plus R1 distillation). Depth in other
languages varies with model size.

<!-- item: tool-use -->
## Function / tool calling

These are reasoning distils. Native tool calling is not their primary documented behaviour and
is unverified. Confirm per serving stack and size, and test.

<!-- item: structured-output -->
## Structured / JSON-constrained output

No native JSON or schema-constrained output guarantee is documented. Constrained decoding is a
serving-layer feature, available through vLLM and SGLang grammars.
