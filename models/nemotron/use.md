# Use - NVIDIA Nemotron 3

_What can it do and how do we use it? Capabilities, context window, languages and tool use live
here. Chat template and structured output are recorded as gaps in entry.yaml._

<!-- item: capabilities -->
## Capabilities & modalities

Nemotron 3 covers reasoning, chat, coding and agentic workloads across four models. Nano, Super and
Ultra are text in / text out; **Nano Omni** is natively multimodal, taking video, audio, image and
text in and returning text. The architecture is a hybrid Mamba-Transformer Latent Mixture-of-Experts
with Multi-Token Prediction, built for efficiency at long context.

<!-- item: context-window -->
## Context window & long-context behaviour

Nano, Super and Ultra support **up to 1M tokens** (Nano defaults to 256k in the Hugging Face
config); Nano Omni supports 256k. OneHill has not independently measured effective long-context
recall, so treat the maximum as the architectural ceiling rather than a verified working depth.

<!-- item: languages -->
## Language coverage

English and code are primary, with supported multilingual contexts. The companion content-safety
classifier covers 12 languages, which indicates the intended multilingual reach, but per-language
model depth is not exhaustively documented.

<!-- item: tool-use -->
## Function / tool calling

The family is positioned for agentic, tool-using workloads, and the training recipe includes
multi-environment reinforcement learning. Expose tools through your serving layer's function-calling
API, and, given the autonomous deployment ceiling, allow-list tools and bound their effects with
NeMo Guardrails action rails.
