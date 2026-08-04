# Use - NVIDIA Nemotron 3 Nano Omni (multimodal)

_What can it do and how do we use it? Capabilities, context window, languages and tool use live
here. Chat template and structured output are recorded as gaps in entry.yaml._

<!-- item: capabilities -->
## Capabilities & modalities

Nano Omni is natively multimodal: it takes **video, audio, image and text** in and returns **text**. It
is a small (31B / ~3B active) hybrid Mamba2-Transformer Mixture-of-Experts built for portable
multimodal reasoning and agentic use.

<!-- item: context-window -->
## Context window & long-context behaviour

Nano Omni supports **256k tokens**. OneHill has not independently measured effective long-context or
cross-modal recall, so treat the maximum as an architectural ceiling rather than a verified working
depth.

<!-- item: languages -->
## Language coverage

English and code are primary, with supported multilingual contexts. Per-language and per-modality depth
is not exhaustively documented.

<!-- item: tool-use -->
## Function / tool calling

Nano Omni is positioned for multimodal agentic use. Expose tools through your serving layer's
function-calling API, and, given the bounded deployment ceiling and the wider multimodal input surface,
allow-list tools and bound their effects with NeMo Guardrails action rails.
