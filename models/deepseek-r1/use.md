# Use - DeepSeek-R1

_What can it do? Capabilities, context window, chat template, languages, tool use, and
structured output live here._

<!-- item: capabilities -->
## Capabilities & modalities

A text-only **reasoning** model with strong maths, coding, and analysis. R1 emits explicit
reasoning traces (think tags) before its final answer, which is the behaviour that
distinguishes it from the DeepSeek-V3 general-instruct line.

<!-- item: context-window -->
## Context window & long-context behaviour

128K-token context per the model card. OneHill has not independently measured effective
long-context recall, so treat the headline figure as the declared window rather than a
verified working depth.

<!-- item: chat-template -->
## Prompt format & chat template

Ships a chat template with a reasoning / think-tag convention. Use `apply_chat_template`
rather than hand-assembling prompts, and handle the reasoning segment at the client - decide
whether to expose or strip it before showing users.

<!-- item: languages -->
## Language coverage

Strong English and Chinese. Per-language depth varies and is not exhaustively documented;
evaluate for your target languages.

<!-- item: tool-use -->
## Function / tool calling

R1 is a reasoning model; native structured tool-calling is not its primary documented
behaviour and was not grounded this session. If you need tool use, confirm support per
serving stack and test it - do not assume parity with the V3 instruct line.

<!-- item: structured-output -->
## Structured / JSON-constrained output

No model-documented native JSON/schema-constrained output guarantee. Constrained decoding is
available at the serving layer (vLLM/SGLang grammars), but that is a runtime feature of the
server, not a property of the model.
