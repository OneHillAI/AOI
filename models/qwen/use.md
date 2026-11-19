# Use - Qwen (Qwen3 family)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Qwen3 is a strong general text model with class-leading open coding and agentic performance. The family is text-focused and spans sizes from a 0.6B dense model to a 480B coder, so capability can be matched to budget without changing integration.

<!-- item: context-window -->
## Context window & long-context behaviour

Qwen3 dense and MoE checkpoints support 32,768 tokens natively and 131,072 with YaRN scaling (per the Qwen3-235B-A22B card). Qwen3-Coder-480B-A35B-Instruct supports 262,144 natively.

Limits differ per variant, so confirm the window on each model card and do not assume 128k everywhere.

<!-- item: chat-template -->
## Prompt format & chat template

Qwen3 ships a chat template in its tokenizer config, including a thinking / non-thinking mode. Use `apply_chat_template` instead of hand-rolling roles.

Decide up front whether thinking-mode output is wanted, because its format is the main thing to normalise when comparing Qwen with another model.

<!-- item: languages -->
## Language coverage

Qwen is broadly multilingual, with particularly strong Chinese and English. Per-language depth varies across the long tail and is not exhaustively documented, so validate any other target language for the workload.

<!-- item: tool-use -->
## Function / tool calling

Qwen3, especially Qwen3-Coder, is positioned for agentic tool use and function calling. Exact schema support is per checkpoint, so confirm the tool-calling format on the specific model card before relying on it in an agent loop.
