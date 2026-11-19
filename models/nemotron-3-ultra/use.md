# Use - NVIDIA Nemotron 3 Ultra (550B)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Ultra covers frontier-scale reasoning, chat, complex agentic workflows and long-context analysis. It is
text in / text out. The architecture is a Mamba2-Transformer hybrid Latent Mixture-of-Experts with
Multi-Token Prediction, built for efficiency at very long context and large scale.

<!-- item: context-window -->
## Context window & long-context behaviour

Ultra supports **up to 1M tokens**. OneHill has not independently measured effective long-context
recall, and the released recipe notes the 1M-context data is not open, so treat the maximum as an
architectural ceiling. Working depth is unverified.

<!-- item: languages -->
## Language coverage

English and code are primary, with supported multilingual contexts. Per-language model depth is not
exhaustively documented.

<!-- item: tool-use -->
## Function / tool calling

Ultra is positioned for complex agentic workflows. Expose tools through your serving layer's
function-calling API, and, given the autonomous deployment ceiling, allow-list tools and bound their
effects with NeMo Guardrails action rails.
