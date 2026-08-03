# Use - Kimi K2 (Moonshot AI)

_What can it do and how do we use it well? Capabilities, context window, chat template,
languages, and native tool use; structured output is a current gap._

<!-- item: capabilities -->
## Capabilities & modalities

Kimi K2 is a **text-focused**, frontier-adjacent general model whose standout strengths are
**agentic tool use, coding, and reasoning**. Per Moonshot's technical report and independent
evaluation (`ev-perf`, `ev-tech-report`) it is **among the strongest open-weight models** on
agentic and coding benchmarks - it is designed as an "open agentic intelligence" rather than a
plain chat model. Choose Kimi K2 when you need frontier-adjacent open-weight capability for
coding/agentic workloads and can provide the serving infrastructure; account for China-aligned
censorship on sensitive topics.

<!-- item: context-window -->
## Context window & long-context behaviour

Kimi K2 exposes a **128K-token context window** per the model card. This item is marked *partial*:
treat the
128K maximum as the architectural ceiling rather than a verified quality guarantee at full length,
and budget KV-cache memory accordingly on your serving cluster.

<!-- item: chat-template -->
## Prompt format & chat template

**Kimi-K2-Instruct** ships a chat template in its tokenizer configuration. Use it rather than
hand-rolling role markers:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Summarize the following..."},
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

**Kimi-K2-Base** has **no** chat template - it is a plain text-completion checkpoint and should
not be prompted as a chat assistant.

<!-- item: languages -->
## Language coverage

Kimi K2 is **multilingual** with particularly strong **English and Chinese**. Per-language depth
varies and is not exhaustively documented, so this item is *partial*: validate quality on your
target languages before relying on it in production, and remember that China-aligned content
filtering can affect coverage of sensitive topics regardless of language.

<!-- item: tool-use -->
## Function / tool calling

**Native tool-calling and agentic behaviour are a core design goal** of Kimi K2 - the model is
trained and benchmarked specifically for agentic tasks, and this is its headline differentiator.
Tool calling is exposed through the **OpenAI/Anthropic-compatible function-calling API** on vLLM
/ SGLang, so existing tool routers and agent frameworks work with little adaptation. Treat all
tool/retrieved content as untrusted and add prompt-injection defences (see Implement).

<!-- structured-output is a `gap` item - no native JSON/schema-constrained output is documented;
     constrained decoding is a serving-layer feature (e.g. vLLM/SGLang grammars). See gap_reason. -->
