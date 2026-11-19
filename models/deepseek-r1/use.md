# Use - DeepSeek-R1

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

R1 is a text-only reasoning model with strong maths, coding and analysis. It emits explicit reasoning traces (think tags) before its final answer, which distinguishes it from the DeepSeek-V3 general-instruct line.

<!-- item: context-window -->
## Context window & long-context behaviour

The model card declares a 128K-token context. Effective long-context recall is unmeasured, so treat 128K as the declared window and working depth as unverified.

<!-- item: chat-template -->
## Prompt format & chat template

R1 ships a chat template with a reasoning / think-tag convention. Use `apply_chat_template` instead of hand-assembling prompts. Handle the reasoning segment at the client and decide whether to expose or strip it before showing users.

<!-- item: languages -->
## Language coverage

Strong English and Chinese. Per-language depth varies and is not exhaustively documented, so evaluate for the target languages.

<!-- item: tool-use -->
## Function / tool calling

Native tool calling is not documented as a primary behaviour of R1 and is unverified. Confirm support per serving stack and test it before relying on it. Do not assume parity with the V3 instruct line.

<!-- item: structured-output -->
## Structured / JSON-constrained output

The model documents no native JSON or schema-constrained output guarantee. Constrained decoding is available at the serving layer (vLLM and SGLang grammars) as a runtime feature of the server.
