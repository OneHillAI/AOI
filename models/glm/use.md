# Use - GLM (Zhipu AI / Z.ai)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

GLM is a text-focused family with a clear tilt toward coding, tool use and agentic workloads.
Per aggregated third-party evaluation and Zhipu's technical reports (`ev-perf-coding`,
`ev-glm46`), GLM-4.6 is among the stronger open models for real-world coding and agentic tasks
and is competitive on general capability. The size ladder runs from a 9B dense model to the
355B/32B MoE, so capability can be traded against serving cost. GLM suits cases where coding
and agentic performance under a permissive MIT license matters, with its China-aligned
behaviour accounted for (see Assess).

<!-- item: context-window -->
## Context window & long-context behaviour

Context length varies by variant, so confirm the number on the model card. GLM-4.6 offers 200K
tokens, the family's longest. GLM-4.5 and GLM-4.5-Air offer up to 128K, per checkpoint.
GLM-4-32B-0414 and GLM-4-9B-0414 offer 32K native, up to 128K extended.

Coverage is partial: per-variant limits differ and effective long-context recall at full
length is not independently benchmarked. Treat the published maximums as the architectural
ceiling, not a verified quality guarantee at full length.

<!-- item: chat-template -->
## Prompt format & chat template

GLM ships a chat template (with a thinking / agentic mode) in its tokenizer configuration. Use
it instead of hand-rolling role markers.

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Refactor this function..."},
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

Applying the template keeps prompts correct across the GLM-4.5/4.6 and 0414 checkpoints and
handles the thinking/agentic output format. Hand-rolled prompts commonly cause garbled or
over-verbose output.

<!-- item: languages -->
## Language coverage

GLM is strong in Chinese and English, with broader multilingual coverage beyond those two.
Per-language depth varies and is not exhaustively documented, so this item is partial.
Validate any non-Chinese/English target with a per-language evaluation before production use.

<!-- item: tool-use -->
## Function / tool calling

GLM-4.6 is explicitly positioned for agentic tool use and function calling, including
MCP-style workflows (`ev-perf-coding`), which is one of the family's strengths. Exact
tool-calling schema support is per checkpoint, so confirm the format on the model card and
test the tool schema before production. The item is partial because schema details vary
across variants.

<!-- structured-output is a `gap` item - no model-documented native JSON/schema-constrained
     output is guaranteed; constrained decoding is a serving-layer feature (vLLM/SGLang
     grammars). See gap_reason. -->
