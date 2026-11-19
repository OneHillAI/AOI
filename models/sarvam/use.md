# Use - Sarvam-30B, Sarvam-105B and Sarvam-105B-1711

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Text-only reasoning models for chat, mathematics, code, tool calling and agentic tasks. The 105B targets agentic and reasoning work. The 30B targets low-latency conversation and voice-agent tool calls. The 1711 build adds post-training for tool calling, instruction following, agentic tasks and Indian languages (`ev-card-105b`, `ev-card-30b`, `ev-card-1711`).

All scores are the publisher's own. Artificial Analysis ranks both March builds below its listed peers (`ev-aa`).

<!-- item: context-window -->
## Context window & long-context behaviour

The 105B card states 128K tokens through YaRN scaling. The 30B card states 65,536 tokens as its evaluation length, and its config allows 131,072. The 1711 examples use 131,072, and the config allows 163,840 (`ev-card-105b`, `ev-card-30b`, `ev-card-1711`, `ev-hub`).

No long-context retrieval benchmark is published. Test your own long inputs.

<!-- item: chat-template -->
## Prompt format & chat template

Each repo bundles `chat_template.jinja`. Call `apply_chat_template` with `enable_thinking=True` or `False`. The 1711 cards recommend temperature 1.0 with thinking and 0.6 without, and thinking is on by default (`ev-card-105b`, `ev-card-1711`).

<!-- item: languages -->
## Language coverage

The cards tag 22 language codes plus English. The tags include Tibetan (bo) and omit Bodo (brx), so they are not the 22 scheduled languages exactly (`ev-card-105b`).

The blog says pre-training emphasised the 10 most-spoken Indian languages and the tokenizer covers all 22 scheduled languages (`ev-blog`). Sarvam's API documentation lists 10 Indian languages plus English for the 105B and the 30B (`ev-api-docs`). The 10 are Hindi, Bengali, Tamil, Telugu, Gujarati, Kannada, Malayalam, Marathi, Punjabi and Odia.

The only 22-language evidence is a pairwise LLM-judge comparison over the public indivibe prompts, with average win rates reported and per-language results shown as charts (`ev-blog`, `ev-indivibe`). The 1711 Indic Suite is internal and has no language list. Treat the other 12 languages as unverified.

<!-- item: tool-use -->
## Function / tool calling

The blog describes native tool calling. The 1711 build is further post-trained for it and the cards use vLLM's `glm45` tool parser. Publisher scores: tau2-Bench 85.5 and BFCL v4 62.4 for 1711, tau2-Bench 68.3 for the 105B and 45.7 for the 30B (`ev-blog`, `ev-card-1711`, `ev-card-105b`, `ev-card-30b`).

Test the parser on your own serving stack and sandbox tool execution.

<!-- item: structured-output -->
## Structured / JSON-constrained output

The hosted API documentation lists JSON and json_schema outputs. No card or cookbook documents a constrained-output mode for the downloadable weights. That is a gap.
