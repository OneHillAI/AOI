# Use - OpenAI gpt-oss (gpt-oss-120b / gpt-oss-20b)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

gpt-oss is a family of text-only reasoning models. Both variants expose configurable
reasoning effort (low / medium / high), which trades latency for depth, and both are built for
agentic work: native function calling, web browsing and Python execution, plus structured
outputs.

Per aggregated leaderboards and OpenAI's model card (`ev-openai-intro`, `ev-model-card`),
gpt-oss-120b lands near OpenAI o4-mini and gpt-oss-20b near o3-mini on core reasoning
benchmarks, strong for open weights. gpt-oss suits a deployer who wants a capable reasoning
and agentic model that runs locally under a permissive licence.

<!-- item: context-window -->
## Context window & long-context behaviour

Both gpt-oss-120b and gpt-oss-20b natively support up to a 128K-token context window
(`ev-model-card`). Size the KV cache for the context length actually used. As with any
long-context model, validate effective recall at the top of the window on the target workload
instead of assuming uniform quality across the full 128K.

<!-- item: chat-template -->
## Prompt format & chat template

gpt-oss is trained exclusively for OpenAI's harmony response format, the most important usage
detail. Harmony defines a role hierarchy (system > developer > user > assistant > tool, where a
developer message outranks a user message on conflict) and gives the assistant separate
channels for reasoning, tool calls and the final answer. Render it with the official library
instead of hand-rolling strings.

```python
# openai/harmony renderer.
from openai_harmony import load_harmony_encoding, HarmonyEncodingName
enc = load_harmony_encoding(HarmonyEncodingName.HARMONY_GPT_OSS)
# Build system/developer/user messages, then render to tokens for the model.
```

Prompting gpt-oss with a plain chat template makes it underperform or emit malformed channels,
so harmony is mandatory. The reasoning channel is unfiltered and must not be shown to end
users.

<!-- item: languages -->
## Language coverage

gpt-oss is primarily English-oriented per the model card. Other-language output may occur but
is incidental and not a documented supported target, so this item is marked partial. Do not
rely on gpt-oss for multilingual production without a per-language evaluation.

<!-- item: tool-use -->
## Function / tool calling

Tool use is a native, documented capability, not prompt scaffolding. The models are trained for
function calling, web browsing and Python code execution, all expressed through the harmony
format's tool channel (`ev-openai-intro`, `ev-harmony`). This makes gpt-oss a capable agentic
backbone.

Tool calls flow through harmony, so they must be rendered and parsed with the harmony
renderer. Tool and retrieved content must be treated as untrusted input to the model.

<!-- item: structured-output -->
## Structured / JSON-constrained output

Structured Outputs are a documented native capability (`ev-openai-intro`, `ev-harmony`),
carried in the harmony format alongside tool calls and reasoning. Many open families leave
JSON conformance entirely to the serving layer, and gpt-oss does not depend on that fallback to
produce structured responses. Schemas can additionally be enforced at the runtime (grammar or
guided decoding in vLLM or llama.cpp) for hard guarantees.
