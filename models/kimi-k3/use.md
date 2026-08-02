# Use - Kimi K3 (Moonshot AI)

_What can it do and how do we use it? Capabilities, context window, and tool use live here.
Chat template, language coverage, and structured output are recorded as gaps in entry.yaml._

<!-- item: capabilities -->
## Capabilities & modalities

Kimi K3 is **natively multimodal** (text, image, video) and frontier-competitive: standout
coding, agentic and reasoning capability with a 1M-token context. On public benchmarks it leads
other open models on coding and agentic tasks and places 1st on the Frontend Code Arena, while
sitting behind only Claude Fable 5 and GPT-5.6 Sol overall.

<!-- item: context-window -->
## Context window & long-context behaviour

The model card reports a **1M-token** (1048576) context window, reached through a cooldown
curriculum that grows the window from 256K to 1M. OneHill has not independently measured effective
long-context recall, so treat the 1M maximum as the architectural ceiling rather than a verified
working depth.

<!-- item: tool-use -->
## Function / tool calling

Agentic tool use is a core design goal. The technical report frames long-horizon interaction over
many tool calls as central to K3, and the model leads agentic benchmarks (BrowseComp,
OSWorld-Verified, agentic search). Expose tools through your serving layer's function-calling API,
and, given the documented offensive-cyber capability, allow-list tools and bound their effects.
