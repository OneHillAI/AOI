# Use - DeepSeek-V3 (MIT)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

A text-only general instruct model with strong coding, maths and analysis. V3-0324 is the general assistant refresh. V3.1 adds a hybrid reasoning mode that can emit an explicit reasoning segment before its answer.

<!-- item: context-window -->
## Context window & long-context behaviour

The model card declares a 128K-token context. Effective long-context recall is not measured, so 128K is the declared window and not a verified working depth.

<!-- item: chat-template -->
## Prompt format & chat template

The model ships a chat template; use `apply_chat_template` instead of hand-assembling prompts. V3.1's hybrid reasoning mode has its own convention, and the client decides whether to expose or strip the reasoning segment.

<!-- item: languages -->
## Language coverage

English and Chinese are strong. Per-language depth varies and is not exhaustively documented, so test the target languages.

<!-- item: tool-use -->
## Function / tool calling

The instruct line supports tool and function calling through the serving stack's schema. Test support per engine, because parity across V3-0324 and V3.1 is not documented.

<!-- item: structured-output -->
## Structured / JSON-constrained output

The model documents no native JSON or schema-constrained output guarantee. Constrained decoding is available at the serving layer (vLLM and SGLang grammars), but it is a runtime feature of the server and not a property of the model.
