# Use - Mistral AI (open-weight family)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Mistral's open-weight models are strong generalist, coding and multilingual text models, and
Pixtral adds native image input. They are solid general assistants with a normal hallucination
profile for their size. Per aggregated leaderboards (`ev-leaderboard`, `ev-small3`) they are
competitive to strong within each size class. Mistral 7B and Mixtral were class-leading at
release, and Mistral Small 3.x is competitive for a 24B while adding tool use and structured
output. Mistral suits a deployer who wants a strong, EU-domiciled open model with Apache
licensing on the flagship checkpoints.

<!-- item: context-window -->
## Context window & long-context behaviour

Context length varies by model, so confirm the number on the model card. Mistral Nemo (12B)
and Mistral Small 3.x (24B) offer 128K tokens, Mixtral 8x7B and 8x22B roughly 32k-64k, and
Mistral 7B 8k-32k depending on version. The published maximum is the architectural ceiling, so
validate quality at the target length.

<!-- item: chat-template -->
## Prompt format & chat template

Use the model's chat template instead of hand-rolling role markers. `mistral-common` is the
ground truth for tokenization and templating, newer models use the Tekken tokenizer
(tiktoken-based, larger vocabulary), and the Hugging Face chat template matches
`mistral-common` output.

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Summarize the following..."},
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

Base checkpoints have no chat template. They are plain text-completion models and should not
be prompted as chat assistants. A wrong template or wrong special tokens is the most common
cause of garbled or over-verbose output.

<!-- item: languages -->
## Language coverage

Mistral is multilingual, with particular strength in European languages (English, French,
German, Italian, Spanish and more), a natural fit for its EU market. Even the companion
Moderation API spans 11 languages (`ev-moderation`). Validate per-language quality for
production, especially for lower-resource languages, because per-model coverage varies.

<!-- item: tool-use -->
## Function / tool calling

The instruct models support native function and tool calling, a documented capability of the
flagship releases. Mistral Small 3.2 improved tool-use accuracy over 3.1 (`ev-small3`). Use
the model's tool-call schema via the chat template or `mistral-common` instead of improvising
a prompt format, and validate the emitted call structure, since some releases note residual
variability in tool-use reliability.

<!-- item: structured-output -->
## Structured / JSON-constrained output

The instruct models support JSON and structured output, and Mistral Small 3.2 improved
structured-output quality over 3.1 (`ev-small3`). The item is marked partial because hard
schema-constrained decoding, a guarantee that output conforms to a grammar or JSON schema, is
delivered at the serving layer (guided decoding or grammars in vLLM, TGI, llama.cpp) and not
as a model-level guarantee. Without constrained decoding, structured output from the model is
strong but best-effort.
