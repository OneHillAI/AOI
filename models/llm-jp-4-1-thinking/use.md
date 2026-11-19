# Use - LLM-jp-4.1 thinking (8B, 32B-A3B, 33B)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

A text-only reasoning ("thinking") model series for Japanese and English chat, mathematics,
science question answering, code, instruction following, translation between Japanese and
English, and, new in 4.1, tool calling (`ev-card-41`, `ev-blog`). Reasoning effort is set to
`low`, `medium` or `high` in the chat template. The 4.1 post-training targeted STEM gains and
shorter answers (`ev-blog`).

Sizes: 8B dense, 32B-A3B mixture of experts (3.8B active, 128 experts, 8 per token) and 33B
dense. The vision-language model is a separate release and is not covered here.

Strength: Japanese-language tasks, where the 32B-A3B matched Qwen3-8B and gpt-oss-20b in the
technical report. Weaker: English averages, GPQA Diamond and AIME against those peers
(`ev-techreport`, `ev-blog`).

<!-- item: context-window -->
## Context window & long-context behaviour

The configuration sets `max_position_embeddings` to 65,536 for all three sizes (`ev-hub-api`).
The technical report describes extending context from 4K to 64K in mid-training through a 16K
stage (`ev-techreport`). The publisher's blog reports that on BFCL's multi-turn long-context
category the 33B model beats the 8B and 32B-A3B models by the widest margin, and that this is
also the category where LLM-jp-4.1 trails Qwen3.5 most (`ev-blog`). No needle-in-a-haystack or
long-context reasoning benchmark is published; test your own long inputs.

<!-- item: chat-template -->
## Prompt format & chat template

The chat template is a modified version of the OpenAI Harmony response format, with analysis
(reasoning), commentary (tool calls) and final channels. The 4.1 changes: parallel tool calls
end all but the last call with `<|end|>`, and reasoning is handled differently across turns from
standard Harmony (`ev-blog`, `ev-card-41`).

Rules from the publisher (`ev-cookbook`, `ev-card-41`):

- load the tokenizer bundled with the model; the `openai-harmony` library's tokenizer has different
  token IDs;
- use `apply_chat_template` with `add_generation_prompt=True` and pass `reasoning_effort`;
- parse token IDs, not decoded text, when message boundaries matter, because user text resembling
  special tokens such as `<|...|>` is ambiguous;
- the 4.0 GGUF templates lack the declaration that selects the 4.1 parser, so use 4.1 GGUF files.

<!-- item: languages -->
## Language coverage

The model cards tag English and Japanese. Pre-training also uses Chinese and Korean web data
(Chinese and Korean FineWeb-2 portions and Wikipedia) and code, with the tokenizer trained on
English and code 0.68, Japanese 0.18, Chinese 0.09 and Korean 0.05 (`ev-techreport`,
`ev-corpus-v4`). Post-training data is Japanese and English plus a small Korean maths subset
(`ev-sft-dpo`). Chinese and Korean output quality and safety are not evaluated by the
publisher, so treat them as unverified.

Japanese-specific work: Japanese Wikipedia, e-Gov legal texts, patents, Diet minutes, KAKEN
abstracts, Aozora Bunko books and National Diet Library web archive are in the pre-training
corpus (`ev-corpus-v4`); the post-training set includes a Japanese maths dataset aligned with the
Ministry of Education curriculum (to be released) and the Japanese safety set AnswerCarefully
(gated) (`ev-techreport`, `ev-sft-dpo`).

<!-- item: tool-use -->
## Function / tool calling

New in 4.1 and described by the publisher as the first LLM-jp series with tool calling
(`ev-blog`). The training mix added a Nemotron agentic subset (21,048 samples) and a Japanese
translation of it (11,174 samples), prioritising multi-step and parallel calls and excluding
incorrect calls from the loss (`ev-blog`, `ev-sft-dpo`).

Evaluated by the publisher on BFCL (categories up to v3) and tau2-bench at medium reasoning effort;
single-turn BFCL is equal to or slightly below Qwen3, tau2-bench is above Qwen3 and far below
Qwen3.5, and multi-turn long-context is the weakest category (`ev-blog`, `ev-card-41`). The
cookbook ships function-calling examples for Transformers and vLLM (`ev-cookbook`). The tool
calls are parsed by publisher plugins; test the parser on your serving stack before use.
