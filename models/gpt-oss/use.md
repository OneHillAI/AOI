# Use - OpenAI gpt-oss (gpt-oss-120b / gpt-oss-20b)

_What can it do and how do we use it well? Capabilities, context window, chat template,
languages, tool use, and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

gpt-oss is a family of **text-only reasoning** models. Both variants expose **configurable
reasoning effort** (low / medium / high) so you can trade latency for depth, and both are
built for **agentic** work: native function calling, web browsing, and Python execution,
plus structured outputs. Per aggregated leaderboards and OpenAI's model card
(`ev-openai-intro`, `ev-model-card`), **gpt-oss-120b lands near OpenAI o4-mini** and
**gpt-oss-20b near o3-mini** on core reasoning benchmarks, strong for open weights. Choose gpt-oss when you want a capable
reasoning/agentic model you can run locally under a permissive license.

<!-- item: context-window -->
## Context window & long-context behaviour

Both gpt-oss-120b and gpt-oss-20b **natively support up to a 128K-token context window**
(`ev-model-card`). Size the KV cache for the context length you actually use, and - as with
any long-context model - validate effective recall at the top of the window for your own
workload rather than assuming uniform quality across the full 128K.

<!-- item: chat-template -->
## Prompt format & chat template

gpt-oss is trained **exclusively for OpenAI's harmony response format** - this is the single
most important usage detail. Harmony defines a role hierarchy (**system > developer > user >
assistant > tool**, where a developer message outranks a user message on conflict) and gives
the assistant **separate channels for reasoning, tool calls, and the final answer**. Render
it with the official library rather than hand-rolling strings:

```python
# openai/harmony renderer
from openai_harmony import load_harmony_encoding, HarmonyEncodingName
enc = load_harmony_encoding(HarmonyEncodingName.HARMONY_GPT_OSS)
# build system/developer/user messages, then render to tokens for the model
```

If you prompt gpt-oss with a plain chat template, it will underperform or emit malformed
channels - treat harmony as mandatory. Remember that the **reasoning channel is unfiltered**
and must not be shown to end users.

<!-- item: languages -->
## Language coverage

gpt-oss is **primarily English-oriented** per the model card. Other-language output may occur
but is incidental and not a documented supported target, so this item is marked *partial*: do
not rely on gpt-oss for multilingual production without your own per-language evaluation.

<!-- item: tool-use -->
## Function / tool calling

Tool use is a **native, documented capability** rather than prompt scaffolding. The models are
trained for **function calling, web browsing, and Python code execution**, all expressed
through the harmony format's **tool channel** (`ev-openai-intro`, `ev-harmony`). This makes
gpt-oss a genuine agentic backbone - but because tool calls flow through harmony, you must
render and parse them with the harmony renderer, and you must treat tool/retrieved content as
untrusted input to the model.

<!-- item: structured-output -->
## Structured / JSON-constrained output

**Structured Outputs are a documented native capability** (`ev-openai-intro`, `ev-harmony`),
carried in the harmony format alongside tool calls and reasoning - a notable step up from
open families that leave JSON conformance entirely to the serving layer. You can additionally
enforce schemas at the runtime (grammar/guided decoding in vLLM or llama.cpp) for hard
guarantees, but unlike many peers gpt-oss does not depend on that fallback to produce
structured responses.
