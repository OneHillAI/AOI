# Use - DeepSeek-R1-Distill (Llama base)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Text reasoning models (maths, coding, analysis) distilled from R1 onto Llama bases (8B, 70B).
They emit explicit reasoning traces (think tags) and are strong for their size, the 70B
especially.

<!-- item: context-window -->
## Context window & long-context behaviour

The cards declare a 128K-token context. Effective long-context recall has not been measured,
so treat 128K as the declared window.

<!-- item: chat-template -->
## Prompt format & chat template

The models follow the R1 reasoning / think-tag convention. Use `apply_chat_template` and
handle the reasoning segment at the client, either exposing or stripping it.

<!-- item: languages -->
## Language coverage

English is strongest (Llama base plus R1 distillation). Per-language depth varies with model
size.

<!-- item: tool-use -->
## Function / tool calling

These are reasoning distils, and native structured tool-calling is not documented as a primary
behaviour. Confirm per serving stack and size, and test.

<!-- item: structured-output -->
## Structured / JSON-constrained output

No model-documented native JSON or schema-constrained output guarantee exists. Constrained
decoding is available at the serving layer (vLLM and SGLang grammars) as a runtime feature of
the server.
