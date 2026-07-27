# Use - GLM (Zhipu AI / Z.ai)

_What can it do and how do we use it well? Capabilities, context window, chat template,
languages, and tool use. Structured/JSON-constrained output is a current gap._

<!-- item: capabilities -->
## Capabilities & modalities

GLM is a **text-focused** family with a clear tilt toward **coding, tool use, and agentic**
workloads. Per aggregated third-party evaluation and Zhipu's technical reports
(`ev-perf-coding`, `ev-glm46`), **GLM-4.6** is among the stronger open models for real-world
coding and agentic tasks, and competitive on general capability. The family spans a wide size
ladder - from a **9B dense** model to the **355B/32B MoE** - so you can trade capability for
serving cost. Choose GLM when coding/agentic performance under a permissive MIT license
matters, and account for its China-aligned behaviour (see Assess).

<!-- item: context-window -->
## Context window & long-context behaviour

Context length varies by variant, so confirm the exact number on the specific model card:

- **GLM-4.6** - **200K** tokens (the family's longest).
- **GLM-4.5 / GLM-4.5-Air** - up to **128K** (per checkpoint).
- **GLM-4-32B-0414 / GLM-4-9B-0414** - **32K** native, up to **128K** extended.

Marked *partial*: per-variant limits differ and effective long-context recall at full length is
not independently benchmarked, so treat the published maximums as the
architectural ceiling rather than a verified quality guarantee at full length.

<!-- item: chat-template -->
## Prompt format & chat template

GLM ships a **chat template** (with a thinking / agentic mode) in its tokenizer configuration.
Use it rather than hand-rolling role markers:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Refactor this function..."},
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

Applying the template keeps you correct across the GLM-4.5/4.6 and 0414 checkpoints and
handles the thinking/agentic output format; hand-rolled prompts commonly cause garbled or
over-verbose output.

<!-- item: languages -->
## Language coverage

GLM is **bilingual-strong in Chinese and English**, with broader multilingual coverage beyond
those two. Per-language depth varies and is not exhaustively documented, so this item is
*partial*: validate any non-Chinese/English target with your own per-language evaluation
before relying on it in production.

<!-- item: tool-use -->
## Function / tool calling

GLM-4.6 is explicitly positioned for **agentic tool use and function calling**, including
MCP-style workflows (`ev-perf-coding`) - this is one of the family's strengths. Exact
tool-calling schema support is **per-checkpoint**, so confirm the format on the specific
model card and test your tool schema before production. Marked *partial* because schema
details vary across variants.

<!-- structured-output is a `gap` item - no model-documented native JSON/schema-constrained
     output is guaranteed; constrained decoding is a serving-layer feature (vLLM/SGLang
     grammars). See gap_reason. -->
