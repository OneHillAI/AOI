# Use - EuroLLM (EuroLLM-9B / EuroLLM-1.7B)

_What can it do and how do we use it well? Capabilities, context window, chat template, and -
the headline strength - languages; tool-use and structured output are current gaps._

<!-- item: capabilities -->
## Capabilities & modalities

EuroLLM is a **text-only** multilingual language model for European-language generation,
assistant tasks and **machine translation**. Per aggregated benchmarks and the technical
report (`ev-tech-report`, `ev-moonlight`) it is **the strongest for its size on multilingual
EU-language tasks** - on par with Gemma-2-9B on multilingual benchmarks, ahead on WMT24++
translation, and matching Mistral-7B on English - while remaining, at 9B, below frontier on
raw single-language reasoning. Choose EuroLLM when you need broad, even EU-language coverage
from a European, Apache-2.0 model more than you need class-topping English reasoning.

<!-- item: context-window -->
## Context window & long-context behaviour

Both EuroLLM-9B and EuroLLM-1.7B use a **4,096-token** context window. This is **short by
current standards**, so design around it:

- Chunk long inputs and use retrieval rather than stuffing large documents into the prompt.
- Budget the 4k across system prompt, few-shot examples, input and output.

Treat 4k as the architectural ceiling.

<!-- item: chat-template -->
## Prompt format & chat template

The **Instruct** variants ship a chat template in their tokenizer configuration (with BOS
token id 1 and EOS token id 4). Use it rather than hand-rolling role markers:

```python
messages = [
    {"role": "system", "content": "You are a helpful multilingual assistant."},
    {"role": "user", "content": "Traduis en portugais : ..."},
]
inputs = tok.apply_chat_template(messages, tokenize=True,
                                 add_generation_prompt=True, return_tensors="pt")
```

Base checkpoints have **no** chat template - they are plain text-completion models and should
not be prompted as chat assistants.

<!-- item: languages -->
## Language coverage

This is EuroLLM's **defining strength**. It is trained **from scratch** for multilingual EU
coverage: **all 24 official EU languages** - Bulgarian, Croatian, Czech, Danish, Dutch,
English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian,
Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish - plus
roughly **11 additional strategic languages**: Arabic, Catalan, Chinese, Galician, Hindi,
Japanese, Korean, Norwegian, Russian, Turkish and Ukrainian.

Unlike English-centric open models where non-English behaviour is incidental, EU-language
coverage is EuroLLM's **design target**, and translation quality (WMT24++) is a documented
strength. The practical caveat: with 35 languages sharing a 9B (or 1.7B) budget, quality is
**uneven** - the smaller and lower-resource languages trail the majors - so evaluate each
target language for your task rather than assuming uniform quality.

<!-- tool-use is a `gap` item - EuroLLM-9B-Instruct is not documented as trained for structured
     function/tool calling and ships no official tool-calling schema. See gap_reason. -->

<!-- structured-output is a `gap` item - no native JSON/schema-constrained output is
     documented; constrained decoding is a serving-layer feature. See gap_reason. -->
