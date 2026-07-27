# Use - Mistral AI (open-weight family)

_What can it do and how do we use it well? Capabilities, context window, chat template,
languages, tool-use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Mistral's open-weight models are strong **generalist, coding and multilingual text** models, with
**Pixtral** adding native vision (image) input. Behaviourally they are solid general assistants
with a normal hallucination profile for their size. Per aggregated leaderboards (`ev-leaderboard`,
`ev-small3`) they are **competitive-to-strong within each size class** - Mistral 7B and Mixtral
were class-leading at release, and Mistral Small 3.x is competitive for a 24B while adding tool use
and structured output. Choose Mistral when you want a strong, EU-domiciled open model with clean
Apache licensing on the flagship checkpoints.

<!-- item: context-window -->
## Context window & long-context behaviour

Context length varies by model, so confirm the number on the specific model card:

- **Mistral Nemo (12B)** and **Mistral Small 3.x (24B)** - **128K** tokens.
- **Mixtral 8x7B / 8x22B** - roughly **32k-64k**.
- **Mistral 7B** - **8k-32k** depending on version.

Treat the published maximum as the architectural ceiling, and validate quality at your target length.

<!-- item: chat-template -->
## Prompt format & chat template

Use the model's **chat template** rather than hand-rolling role markers. Mistral's `mistral-common`
library is the ground truth for tokenization and templating, newer models use the **Tekken**
tokenizer (tiktoken-based, larger vocabulary), and the Hugging Face chat template is kept to match
`mistral-common` output:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Summarize the following..."},
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

Base checkpoints have **no** chat template - they are plain text-completion models and should not
be prompted as chat assistants. Getting the template or special tokens wrong is the most common
cause of garbled or over-verbose output.

<!-- item: languages -->
## Language coverage

Mistral is **genuinely multilingual**, with particular strength in **European languages**
(English, French, German, Italian, Spanish and more) - a natural fit for its EU market. The scope
is broad enough that even the companion Moderation API spans **11 languages** (`ev-moderation`).
Still, validate per-language quality for production, especially for lower-resource languages, since
per-model coverage varies.

<!-- item: tool-use -->
## Function / tool calling

The instruct models support **native function/tool calling**, and it is a documented capability of
the flagship releases. Mistral Small 3.2 specifically **improved tool-use accuracy** over 3.1
(`ev-small3`). Use the model's tool-call schema via the chat template / `mistral-common` rather
than improvising a prompt format, and validate the emitted call structure - some releases note
residual variability in tool-use reliability.

<!-- item: structured-output -->
## Structured / JSON-constrained output

The instruct models support **JSON / structured output**, and Mistral Small 3.2 improved
structured-output quality over 3.1 (`ev-small3`). This item is marked *partial* because *hard*
schema-constrained decoding - a guarantee that output conforms to a grammar/JSON schema - is
delivered at the **serving layer** (guided decoding/grammars in vLLM, TGI, llama.cpp) rather than
as a model-level guarantee. Treat the
model's structured output as strong-but-best-effort unless you add constrained decoding.
