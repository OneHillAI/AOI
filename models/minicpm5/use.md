# Use - MiniCPM5-1B

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Text in, text out (`ev-aa`, `ev-card`). One checkpoint serves a fast assistant mode and a deliberate reasoning mode, switched by `enable_thinking`. The publisher highlights code, maths, instruction following and tool use. Its figures (Thinking mode, unverified): MATH-500 91.60, LCB-v6 33.52, AIME-2026 40.42, IFEval 80.41, MMLU-Pro 48.85, tau2-Bench Telecom 79.53 (`ev-bench`). Non-thinking performance is not published. Treat these as claims until reproduced.

<!-- item: context-window -->
## Context window & long-context behaviour

131,072 tokens in config.json and the GGUF metadata, with rope_theta 5,000,000 and no rope scaling (`ev-repo-files`). The card says "native long-context support" but publishes no long-context result for the 1B (the series radar chart with a long-context axis belongs to the 2B card). For a 1B model, test retrieval and instruction following at the real context lengths. Cap the context on small devices, because the KV cache grows to about 3.2 GB at the full window.

<!-- item: chat-template -->
## Prompt format & chat template

The tokenizer ships `chat_template.jinja`, a ChatML-style template (`<|im_start|>role ... <|im_end|>`). Use `apply_chat_template` with `enable_thinking=True` (the template appends `<think>`) or `enable_thinking=False` (it appends an empty think block). Tool definitions are injected in `<tools></tools>` and calls use `<function name="..."><param name="...">...</param></function>`, with tool results wrapped in `<tool_response>` (`ev-repo-files`). Sampling per mode is on the card: 0.9 or 0.7 temperature, top_p 0.95. The generation config defaults to temperature 0.9. EOS ids are 1 and 130073.

<!-- item: languages -->
## Language coverage

English and Chinese. The card metadata lists `en` and `zh`, a Chinese README is provided, and the training datasets are English and Chinese (`ev-card`, `ev-datasets`). No other language is documented or evaluated by the publisher, and the benchmark table has no multilingual row. Community fine-tunes for other languages exist on the Hub but are not evidence of base-model capability. Any third language is unverified and needs testing.

<!-- item: tool-use -->
## Function / tool calling

Native. The model emits XML-style function calls; SGLang's `minicpm5` parser converts them to OpenAI-style `tool_calls`, and the repository includes `tool_parsers/minicpm5xml_tool_parser.py` (`ev-card`, `ev-github`). On the publisher table BFCLv4 is 25.15, level with Qwen3-0.6B (25.43) and Qwen3.5-0.8B (25.53) and above LFM2.5-1.2B (10.60), while tau2-Bench Telecom is 79.53 (`ev-bench`). The card's claim of a tool-use lead rests mainly on the second result. Validate every call before executing it.

<!-- structured-output is a `gap` item in entry.yaml - see its gap_reason. -->
