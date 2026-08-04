# Use - DeepSeek-V3 (MIT)

_What can it do? Capabilities, context window, chat template, languages, tool use, and
structured output live here._

<!-- item: capabilities -->
## Capabilities & modalities

A text-only general-**instruct** model with strong coding, maths, and analysis. V3-0324 is
the general assistant refresh; V3.1 adds a hybrid reasoning mode that can emit an explicit
reasoning segment before its answer.

<!-- item: context-window -->
## Context window & long-context behaviour

128K-token context per the model card. OneHill has not independently measured effective
long-context recall, so treat the headline figure as the declared window rather than a
verified working depth.

<!-- item: chat-template -->
## Prompt format & chat template

Ships a chat template - use `apply_chat_template` rather than hand-assembling prompts.
V3.1's hybrid reasoning mode has its own convention; decide at the client whether to expose
or strip the reasoning segment.

<!-- item: languages -->
## Language coverage

Strong English and Chinese. Per-language depth varies and is not exhaustively documented;
evaluate for your target languages.

<!-- item: tool-use -->
## Function / tool calling

The instruct line supports tool / function calling through the serving stack's schema.
Confirm support and test it per engine rather than assuming parity across V3-0324 and V3.1.

<!-- item: structured-output -->
## Structured / JSON-constrained output

No model-documented native JSON/schema-constrained output guarantee. Constrained decoding is
available at the serving layer (vLLM/SGLang grammars), but that is a runtime feature of the
server, not a property of the model.
