doc_type: openness
entity: nemotron-3-ultra
variant/applies-to: Nemotron 3 Ultra - openness, safety, provenance, deployment, EU AI Act
source_url: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16 ; https://github.com/NVIDIA-NeMo/Nemotron ; https://arxiv.org/abs/2512.20856 ; https://huggingface.co/nvidia/Nemotron-3-Content-Safety ; https://huggingface.co/nvidia ; https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai
document_effective_date: ~2025-12
retrieval_date: 2026-08-03
exists: yes
retrieved: true
tag: publisher / third_party (EU list)

## Model card (VERBATIM)
[Params] "550B Total / 55B Active".
[Architecture] "Mamba2-Transformer Hybrid Latent Mixture of Experts (LatentMoE) with Multi-Token Prediction (MTP)".
[Context] "Up to 1M tokens".
[Training tokens] "approximately 20T tokens".
[Openness self-description] "open models with open weights, training data, and recipes".
[Licence tag] openmdw-1.1: "Use of this model is governed by the OpenMDW License Agreement, version 1.1".
[Format/gating] safetensors; ungated; BF16 / NVFP4 variants.

## Openness tier (open_weights_recipe, with representative-recipe caveats)
Ultra recipe at github.com/NVIDIA-NeMo/Nemotron docs/nemotron/ultra3 (Pretrain -> SFT -> MOPD ->
Quant), described as "a representative single pass". Caveats VERBATIM: "the intermediate checkpoints
it depends on have not been open-sourced" and the "1M-context LC phase is not included because its
data ... is not open-source". So: open_weights_recipe, short of fully_open because the intermediate
checkpoints and the 1M-context data are not open.

## Safety (the honest gap)
White Paper Section 3 "Evaluation, Safety and Release" is only a contributor list - no methodology,
red-team or benchmarks. Safety appears only as post-training data curation (Nemotron Content Safety
v2 + Gretel refusal data + keyword/regex filtering). NO dedicated model-level safety evaluation for
Ultra. The family-level companion guard classifier (Nemotron-3-Content-Safety), NeMo Guardrails
(Apache-2.0) and garak (Apache-2.0) are downloadable and attributable. Safety dimension = 3 (held
below 4 by the missing model-level evaluation; above 2 by the downloadable companion guard stack).

## Provenance
HF org "nvidia" VERIFIED; Ultra weights ungated safetensors with BF16 / NVFP4 quant variants;
checksums / signing / attestation not verified this pass (checklist about 4/8).

## Deployment (data control)
NIM self-hosted ("data never leaves your secure enclave"); NVIDIA is not an AOI inference-provider
entry. Self-hosting plus the OpenMDW "without restriction" grant supports data_control strong.

## EU AI Act
GPAI. NVIDIA NOT on the GPAI Code of Practice signatory list; no training-content summary or
copyright policy located. Training compute is NOT disclosed (only "approximately 20 trillion
tokens"), so whether Ultra 550B crosses the 1e25-FLOP systemic-risk threshold is UNDETERMINABLE;
over_1e25_threshold is recorded null. Do NOT assert a FLOP number.
