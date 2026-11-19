# Use - Tucano 2 (Qwen-derived 0.5B, 1.5B and 3.7B; Base, Instruct and Think)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Text only. The post-training data covers 12 task types: code, function calling, general instructions, maths, maths with chain of thought, reasoning, retrieval-augmented answers, rewriting, structured output, summarisation, system prompts and translation (`ev-gv2-post`). The 3.7B Instruct leads its 3 to 4B class on Knowledge and Reasoning (56.22) and trails Qwen3-4B on instruction following and coding (`ev-paper`). The Think models write chain-of-thought in Portuguese inside think tags and have no coding training. All figures are the publisher's own.

<!-- item: context-window -->
## Context window & long-context behaviour

The context is 4,096 tokens in `config.json` and `tokenizer_config.json`. Qwen3-4B-Base supports 32,768, and the Tucano continual pretraining and post-training stop at 4,096 (`ev-card-instruct`, `ev-qwen3-licence`). RULER-PT at 4,096 tokens is 0.686 for the 3.7B Instruct and 0.707 for the 3.7B Think, against 0.979 for Qwen3-4B. The paper attributes the gap to missing long-context data and lists context extension as future work (`ev-paper`). Chunk documents and retrieve.

<!-- item: chat-template -->
## Prompt format & chat template

The format is ChatML. Turns open with `<|im_start|>` and the role, and close with `<|im_end|>`. A tools block lists function signatures in `<tools></tools>` in Portuguese and asks for a JSON call inside `<tool_call></tool_call>` (`ev-configs`). The Think template wraps reasoning in `<think>` and `</think>`. The tokenizer is a 49,152-token Portuguese vocabulary with `<|im_end|>` as the end-of-sequence token. Use the repo's `apply_chat_template`. The Base models have no chat format.

<!-- item: languages -->
## Language coverage

Portuguese only. The cards say other languages may cause misinterpretation, and the continual pretraining data is purely Portuguese (`ev-card-instruct`, `ev-paper`). Qwen3 covers 119 languages, and the Tucano tokenizer swap and Portuguese training reduce that coverage in ways the publisher does not measure. The Instruct card shows an English translation task.

<!-- item: tool-use -->
## Function / tool calling

The Instruct SFT mix includes about 17.5 million tokens of function-call data, and the card shows a correct `create_todo` call in `<tool_call>` format (`ev-configs`, `ev-card-instruct`). No tool-calling benchmark is reported, so test your own schemas.

<!-- item: structured-output -->
## Structured / JSON-constrained output

The Instruct SFT mix includes about 35 million tokens of structured-output data, and the card shows a JSON extraction with the requested keys (`ev-configs`, `ev-card-instruct`). No benchmark or schema-guarantee is reported. Use constrained decoding in your serving layer if you need valid JSON every time.
