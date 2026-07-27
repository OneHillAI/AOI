# Use - Ai2 OLMo (OLMo 2 / OLMo 3)

_What can it do and how do we use it well? Capabilities, context window, chat template,
languages; tool-use and structured output are current gaps._

<!-- item: capabilities -->
## Capabilities & modalities

OLMo is a **text-only** language model for general English generation and assistant tasks -
question answering, summarisation, drafting, and light reasoning. Behaviourally it is a solid
general assistant with a normal hallucination profile for its size and no standout
pathologies. Per aggregated leaderboards and Ai2's technical reports (`ev-perf`,
`ev-tech-report`) it is **competitive within its size class but not frontier-leading**: a
same-size commercial instruct model will usually edge it on raw capability. Choose OLMo when
transparency, reproducibility, and auditability matter more than topping a benchmark.

<!-- item: context-window -->
## Context window & long-context behaviour

Context length varies by generation and variant, so confirm the exact number on the specific
model card:

- **OLMo 2** - roughly **4k-8k** tokens.
- **OLMo 3** - longer, as documented in its technical report (`ev-tech-report`).

This item is marked *partial*: per-variant limits differ, so treat the published maximums as the
architectural ceiling rather than a verified quality guarantee at full length.

<!-- item: chat-template -->
## Prompt format & chat template

The **Instruct** variants ship a chat template in their tokenizer configuration. Use it
rather than hand-rolling role markers, which keeps you correct across OLMo 2 and OLMo 3:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Summarize the following..."},
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

Base checkpoints have **no** chat template - they are plain text-completion models and should
not be prompted as chat assistants.

<!-- item: languages -->
## Language coverage

OLMo is **primarily English**: the Dolma training corpus is English-dominant, so English is
the only well-supported target. Other-language output may occur but is incidental and
unverified - do not rely on OLMo for multilingual production without your own per-language
evaluation. Marked *partial* to reflect that non-English coverage is neither a design goal
nor independently benchmarked here.

<!-- tool-use is a `gap` item - OLMo Instruct is not documented as trained for structured
     function/tool calling and ships no official tool-calling schema. See gap_reason. -->

<!-- structured-output is a `gap` item - no native JSON/schema-constrained output is
     documented; constrained decoding is a serving-layer feature. See gap_reason. -->
