# Use - Ai2 OLMo (OLMo 2 / OLMo 3)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

OLMo is a text-only language model for general English generation and assistant tasks: question answering, summarisation, drafting and light reasoning. It is a solid general assistant with a normal hallucination profile for its size.

Per aggregated leaderboards and Ai2's technical reports (`ev-perf`, `ev-tech-report`) it is competitive within its size class but not frontier-leading, and a same-size commercial instruct model will usually edge it on raw capability. Choose OLMo when transparency, reproducibility and auditability matter more than topping a benchmark.

<!-- item: context-window -->
## Context window & long-context behaviour

Context length varies by generation, per each model's `config.json`. OLMo 2 has 4,096 tokens on the 1B, 7B, 13B and 32B checkpoints. OLMo 3 has 65,536 tokens on the 7B and 32B base and Think checkpoints (`ev-hf-olmo3`), and the technical report documents the long-context stage (`ev-tech-report`).

These are architectural ceilings and quality at full length is unverified, so the item is marked partial.

<!-- item: chat-template -->
## Prompt format & chat template

The Instruct variants ship a chat template in their tokenizer configuration. Use it instead of hand-rolling role markers, which keeps prompts correct across OLMo 2 and OLMo 3:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Summarize the following..."},
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

Base checkpoints have no chat template. They are plain text-completion models and should not be prompted as chat assistants.

<!-- item: languages -->
## Language coverage

OLMo is primarily English: the Dolma training corpus is English-dominant, so English is the only well-supported target. Other-language output may occur but is incidental and unverified, so multilingual production needs per-language evaluation. The item is marked partial because non-English coverage is neither a design goal nor benchmarked.

<!-- tool-use is a `gap` item - OLMo Instruct is not documented as trained for structured
     function/tool calling and ships no official tool-calling schema. See gap_reason. -->

<!-- structured-output is a `gap` item - no native JSON/schema-constrained output is
     documented; constrained decoding is a serving-layer feature. See gap_reason. -->
