# Use - NVIDIA Nemotron 3 Nano Omni (multimodal)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Nano Omni is natively multimodal: it takes video, audio, image and text in and returns text. It
is a small (31B / ~3B active) hybrid Mamba2-Transformer Mixture-of-Experts built for portable
multimodal reasoning and agentic use.

<!-- item: context-window -->
## Context window & long-context behaviour

Nano Omni supports 256k tokens. OneHill has not measured effective long-context or cross-modal
recall, so treat the maximum as an architectural ceiling, not a verified working depth.

<!-- item: languages -->
## Language coverage

English and code are primary, with supported multilingual contexts. Per-language and
per-modality depth is not exhaustively documented.

<!-- item: tool-use -->
## Function / tool calling

Nano Omni is positioned for multimodal agentic use. Expose tools through the serving layer's
function-calling API. Given the bounded deployment ceiling and the wider multimodal input
surface, allow-list tools and bound their effects with NeMo Guardrails action rails.
