# Use - Qwen (Qwen3 family)

_What can it do and how do we use it? Capabilities, context window, chat template, languages
and tool use live here._

<!-- item: capabilities -->
## Capabilities & modalities

Qwen3 is a **strong general text model with class-leading open coding and agentic**
performance. The family is text-focused and spans an unusually wide ladder - from a 0.5B
dense model up to a 480B coder - so you can match capability to budget without leaving the
family or changing integration.

<!-- item: context-window -->
## Context window & long-context behaviour

Mainstream Qwen3 checkpoints support **up to 128k** context. Exact per-variant limits
differ, so confirm the window on each model card rather than assuming 128k everywhere.

<!-- item: chat-template -->
## Prompt format & chat template

Qwen3 ships a **chat template in its tokenizer config**, including a **thinking / non-thinking
mode**. Use **`apply_chat_template`** rather than hand-rolling roles, and decide up front
whether you want thinking-mode output - its format is the main thing to normalise when
comparing Qwen against another model.

<!-- item: languages -->
## Language coverage

Qwen is **broadly multilingual** with particularly strong **Chinese and English**.
Per-language depth varies across the long tail and is not exhaustively documented, so
validate any non-English, non-Chinese target language for your workload.

<!-- item: tool-use -->
## Function / tool calling

Qwen3 - especially **Qwen3-Coder** - is explicitly positioned for **agentic tool use and
function calling**. Exact schema support is per-checkpoint, so confirm the tool-calling
format on the specific model card before relying on it in an agent loop.
