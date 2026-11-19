# Use - Kimi K2 (Moonshot AI)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Kimi K2 is a text-focused, frontier-adjacent general model with strong agentic tool use, coding
and reasoning. Per Moonshot's technical report and independent evaluation (`ev-perf`,
`ev-tech-report`) it is among the strongest open-weight models on agentic and coding benchmarks.
It is designed as an "open agentic intelligence". Choose it for frontier-adjacent open-weight
coding and agentic workloads when the serving infrastructure is available, and allow for
China-aligned censorship on sensitive topics.

<!-- item: context-window -->
## Context window & long-context behaviour

Kimi K2 has a 128K-token context window per the model card. Coverage is partial: treat 128K as
the architectural ceiling, not a verified quality guarantee at full length, and budget KV-cache
memory on the serving cluster.

<!-- item: chat-template -->
## Prompt format & chat template

Kimi-K2-Instruct ships a chat template in its tokenizer configuration. Use it instead of
hand-rolling role markers:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Summarize the following..."},
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

Kimi-K2-Base has no chat template. It is a plain text-completion checkpoint and should not be
prompted as a chat assistant.

<!-- item: languages -->
## Language coverage

Kimi K2 is multilingual with particularly strong English and Chinese. Per-language depth varies
and is not exhaustively documented, so coverage is partial. Validate quality on the target
languages before production use. China-aligned content filtering can affect coverage of sensitive
topics in any language.

<!-- item: tool-use -->
## Function / tool calling

Native tool calling and agentic behaviour are a core design goal of Kimi K2. The model is trained
and benchmarked for agentic tasks, and this is its headline differentiator. Tool calling is
exposed through the OpenAI/Anthropic-compatible function-calling API on vLLM and SGLang, so
existing tool routers and agent frameworks work with little adaptation. Treat all tool and
retrieved content as untrusted and add prompt-injection defences (see Implement).

<!-- structured-output is a `gap` item - no native JSON/schema-constrained output is documented;
     constrained decoding is a serving-layer feature (e.g. vLLM/SGLang grammars). See gap_reason. -->
