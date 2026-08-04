# Use - DeepSeek-R1-Distill (Llama base)

_What can it do? Capabilities, context window, chat template, languages, tool use, and
structured output live here._

<!-- item: capabilities -->
## Capabilities & modalities

Text reasoning models (maths, coding, analysis) distilled from R1 onto Llama bases (8B, 70B).
They emit explicit reasoning traces (think tags) and are strong for their size - the 70B
notably.

<!-- item: context-window -->
## Context window & long-context behaviour

128K-token context per the cards. OneHill has not independently measured effective
long-context recall, so treat it as the declared window.

<!-- item: chat-template -->
## Prompt format & chat template

Ship a chat template with the R1 reasoning / think-tag convention. Use `apply_chat_template`
and handle the reasoning segment at the client - decide whether to expose or strip it.

<!-- item: languages -->
## Language coverage

English is strongest (Llama base plus R1 distillation); per-language depth varies with model
size.

<!-- item: tool-use -->
## Function / tool calling

These are reasoning distils; native structured tool-calling is not the primary documented
behaviour and was not grounded this session. Confirm per serving stack and size, and test.

<!-- item: structured-output -->
## Structured / JSON-constrained output

No model-documented native JSON/schema-constrained output guarantee. Constrained decoding is
available at the serving layer (vLLM/SGLang grammars), a runtime feature of the server.
