doc_type: model_card
entity: nemotron-3
variant/applies-to: Nemotron 3 Super (120B/12B) and Nano (30B/3.5B)
source_url: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16 ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 ; https://arxiv.org/abs/2512.20856
document_effective_date: ~2025-12
retrieval_date: 2026-08-03
exists: yes
retrieved: true
tag: publisher

## Nemotron 3 Super - nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16
[Params - VERBATIM] "120B (12B active)"
[Architecture - VERBATIM] "LatentMoE - Mamba-2 + MoE + Attention hybrid with Multi-Token Prediction (MTP)"
[Context - VERBATIM] "Up to 1M tokens"
[Training tokens - VERBATIM] "approximately 25 trillion tokens" (pre-training)
[Intended use - VERBATIM] "a general purpose reasoning and chat model ... optimized for collaborative agents and high-volume workloads"
[Licence tag - VERBATIM] nvidia-nemotron-open-model-license: "Use of this model is governed by the NVIDIA Nemotron Open Model License"
[Format/gating] safetensors; weights ungated; BF16 / FP8 / NVFP4 variants

## Nemotron 3 Nano - nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
[Params - VERBATIM] "3.5B active parameters and 30B parameters in total"
[Architecture - VERBATIM] "23 Mamba-2 and MoE layers, along with 6 Attention layers. Each MoE layer includes 128 experts plus 1 shared expert, with 6 experts activated per token"
[Context - VERBATIM] "Maximum input size: 1M tokens" (note: "default context size in the Hugging Face configuration is 256k")
[Training tokens - VERBATIM] "trained with 25T tokens"
[Modalities - VERBATIM] "Input Type(s): Text" / "Output Type(s): Text"
[Licence tag - VERBATIM] nvidia-nemotron-open-model-license
[Format/gating] safetensors; weights ungated; some training data gated ("For all remaining code, math and multilingual data, gating and approval is required")
[Tech report] Nemotron 3 Nano arXiv 2512.20848

## White paper (arXiv 2512.20856)
[Abstract - VERBATIM] "We introduce the Nemotron 3 family of models - Nano, Super, and Ultra ... a Mixture-of-Experts hybrid Mamba-Transformer architecture ... context lengths of up to 1M tokens. Super and Ultra models are trained with NVFP4 and incorporate LatentMoE ..."
[Training COMPUTE / FLOPs] NOT stated (tokens only).
