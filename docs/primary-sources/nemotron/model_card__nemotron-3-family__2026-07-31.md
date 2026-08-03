doc_type: model_card
entity: nemotron
variant/applies-to: Nemotron 3 family - Ultra, Super, Nano, Nano Omni (one file, per-variant blocks)
source_url: https://huggingface.co/nvidia ; per-variant repo URLs below
document_effective_date: Nemotron 3 announced ~2025-12-24
retrieval_date: 2026-07-31
exists: yes
retrieved: true
tag: publisher (NVIDIA self-report on its own HF cards)

## Openness self-description (exact NVIDIA wording, on Super / Nano / Ultra cards - VERBATIM)

"NVIDIA Nemotron(TM) is a family of open models with open weights, training data, and recipes,
delivering leading efficiency and accuracy for building specialized AI agents."
NOTE: Nano Omni does NOT carry this sentence and does not release code/recipes - its openness
posture is weaker.

## Nemotron 3 Super - nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16 (also FP8, NVFP4, Base-BF16)
[Params - VERBATIM] "120B (12B active)"
[Architecture - VERBATIM] "LatentMoE - Mamba-2 + MoE + Attention hybrid with Multi-Token Prediction (MTP)"
[Context - VERBATIM] "Up to 1M tokens"
[Modalities] Text in / text out ("English, Code, and supported multilingual contexts")
[Training tokens - VERBATIM] "approximately 25 trillion tokens" (pre-training)
[Intended use - VERBATIM] "a general purpose reasoning and chat model ... optimized for collaborative agents and high-volume workloads"
[Safety on card - VERBATIM] data-filter note only: "we apply targeted keyword- and regex-based filters and remove all trajectories matching such behavior"
[Licence tag - VERBATIM] nvidia-nemotron-open-model-license: "Use of this model is governed by the NVIDIA Nemotron Open Model License"
[Format/gating] safetensors; weights ungated

## Nemotron 3 Ultra - nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16 (also NVFP4, Base-BF16)
[Params - VERBATIM] "550B Total / 55B Active"
[Architecture - VERBATIM] "Mamba2-Transformer Hybrid Latent Mixture of Experts (LatentMoE) with Multi-Token Prediction (MTP)"
[Context - VERBATIM] "Up to 1M tokens"
[Modalities] Text in / text out
[Training tokens - VERBATIM] "approximately 20T tokens" (pre-training) [NOTE: sources conflict - white paper up to 25T; Ultra blog 10T foundation +212B new; reconcile from full PDF]
[Intended use - VERBATIM] "frontier-scale general purpose reasoning and chat model" for "complex agentic workflows, long-context analysis, and high-stakes analytical workloads"
[Licence tag - VERBATIM - DIFFERENT FROM SUPER/NANO] openmdw-1.1: "Use of this model is governed by the OpenMDW License Agreement, version 1.1"
[Format/gating] safetensors; ungated

## Nemotron 3 Nano - nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 (also FP8, NVFP4)
[Params - VERBATIM] "3.5B active parameters and 30B parameters in total"
[Architecture - VERBATIM] "hybrid Mixture-of-Experts (MoE) architecture, consisting of 23 Mamba-2 and MoE layers, along with 6 Attention layers. Each MoE layer includes 128 experts plus 1 shared expert, with 6 experts activated per token"
[Context - VERBATIM] "Maximum input size: 1M tokens" (note "default context size in the Hugging Face configuration is 256k")
[Modalities - VERBATIM] "Input Type(s): Text" / "Output Type(s): Text"
[Training tokens - VERBATIM] "trained with 25T tokens"
[Safety on card - VERBATIM] "iterative testing and validation at both unit and system levels are essential to mitigate risks ... before deployment" ; "we apply targeted keyword- and regex-based filters"
[Licence tag - VERBATIM] nvidia-nemotron-open-model-license: "Use of this model is governed by the NVIDIA Nemotron Open Model License."
[Format/gating] safetensors; weights ungated - BUT some training data gated: "For all remaining code, math and multilingual data, gating and approval is required"
[Tech report] arXiv 2512.20848 (Nemotron 3 Nano)

## Nemotron 3 Nano Omni (multimodal) - nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
[Params - VERBATIM] "31B" total / ~3B active
[Modalities - VERBATIM] Input "Video, Audio, Image, Text" / Output Text
[Context] 256k
[Training tokens] ~717B
[Licence tag - VERBATIM - THIRD distinct] nvidia-open-model-agreement: "Use of this model is governed by the NVIDIA Open Model Agreement"
[Openness] does NOT carry the "open weights, training data, and recipes" sentence; no released code/recipe - weaker openness posture than the other three.
