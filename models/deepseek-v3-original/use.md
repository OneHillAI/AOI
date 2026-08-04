# Use - DeepSeek-V3 (original, DeepSeek License)

_What can it do? Capabilities, context window, chat template, languages, tool use, and
structured output live here._

<!-- item: capabilities -->
## Capabilities & modalities

A text-only model in two variants: **Base** (a raw completion foundation for further
training) and **Chat** (the general-instruct assistant), with strong coding, maths, and
analysis at release.

<!-- item: context-window -->
## Context window & long-context behaviour

128K-token context per the model card. OneHill has not independently measured effective
long-context recall, so treat the headline figure as the declared window rather than a
verified working depth.

<!-- item: chat-template -->
## Prompt format & chat template

The **Chat** variant ships a chat template - use `apply_chat_template` rather than
hand-assembling prompts. The **Base** variant is a completion model with no chat template;
prompt it as raw text.

<!-- item: languages -->
## Language coverage

Strong English and Chinese. Per-language depth varies and is not exhaustively documented;
evaluate for your target languages.

<!-- item: tool-use -->
## Function / tool calling

The Chat variant supports tool / function calling through the serving stack's schema. Confirm
support and test it per engine.

<!-- item: structured-output -->
## Structured / JSON-constrained output

No model-documented native JSON/schema-constrained output guarantee. Constrained decoding is
available at the serving layer (vLLM/SGLang grammars), but that is a runtime feature of the
server, not a property of the model.
