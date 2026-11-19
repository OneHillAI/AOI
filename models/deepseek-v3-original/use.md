# Use - DeepSeek-V3 (original, DeepSeek License)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

A text-only model in two variants: Base (a raw completion foundation for further training) and
Chat (the general-instruct assistant). Coding, maths and analysis were strong at release.

<!-- item: context-window -->
## Context window & long-context behaviour

The model card gives a 128K-token context. OneHill has not measured effective long-context
recall, so treat 128K as the declared window, not a verified working depth.

<!-- item: chat-template -->
## Prompt format & chat template

The Chat variant ships a chat template; use `apply_chat_template` instead of assembling prompts
by hand. The Base variant is a completion model with no chat template, so prompt it as raw text.

<!-- item: languages -->
## Language coverage

Strong English and Chinese. Per-language depth varies and is not exhaustively documented, so
evaluate for the target languages.

<!-- item: tool-use -->
## Function / tool calling

The Chat variant supports tool and function calling through the serving stack's schema.
Confirm support and test it per engine.

<!-- item: structured-output -->
## Structured / JSON-constrained output

The model documents no native JSON or schema-constrained output guarantee. Constrained decoding
is available at the serving layer (vLLM/SGLang grammars), as a runtime feature of the server.
