doc_type: openness
entity: nemotron-3-nano-omni
variant/applies-to: Nemotron 3 Nano Omni - openness, safety, provenance, deployment, EU AI Act
source_url: https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 ; https://github.com/NVIDIA-NeMo/Nemotron ; https://huggingface.co/nvidia/Nemotron-3-Content-Safety ; https://huggingface.co/nvidia ; https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai
document_effective_date: ~2026
retrieval_date: 2026-08-03
exists: yes
retrieved: true
tag: publisher / third_party (EU list)

## Model card (VERBATIM)
[Params] "31B" total / ~3B active.
[Architecture] Mamba2-Transformer hybrid MoE.
[Modalities - VERBATIM] Input "Video, Audio, Image, Text" / Output "Text".
[Context] 256k.
[Training tokens] ~717B.
[Licence tag] nvidia-open-model-agreement: "Use of this model is governed by the NVIDIA Open Model Agreement".
[Repo id] nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 (NO "NVIDIA-" prefix, unlike Super/Nano/Ultra).

## Openness tier (open_weights - BORDERLINE, weaker than the others)
The Nano Omni card does NOT carry the "open models with open weights, training data, and recipes"
self-description the Super/Nano/Ultra cards carry. It links only nvidia/Nemotron-Image-Training-v3
(not the full open collections) and a TensorRT-LLM DEPLOY cookbook (deployment, not training). On
card signals alone this is open_weights, not open_weights_recipe. A genuine training recipe DOES
exist in the NeMo repo (docs/nemotron/omni3, SFT -> RL), caveat VERBATIM: "The 20 RL datasets / 25
environments / ~2.3M rollouts referenced in the release blog compose the full upstream alignment
corpus; this recipe surfaces the public/open-source subset." CONCLUSION: classify open_weights
(card signals are weaker), with a note that a recipe exists in the NeMo repo. Do NOT force
open_weights_recipe on card signals alone.

## Safety (the honest gap)
No dedicated model-level safety evaluation for Nano Omni; safety is post-training data curation only.
The family-level Nemotron-3-Content-Safety classifier is multimodal (text + images) and so is partly
attributable; NeMo Guardrails and garak are Apache-2.0 and downloadable. Safety dimension = 3 (held
below 4 by the missing model-level evaluation; above 2 by the downloadable, partly-attributable
companion guard stack).

## Provenance
HF org "nvidia" VERIFIED; Nano Omni weights ungated safetensors (BF16). Checksums / signing not
verified (checklist about 4/8).

## Deployment (data control)
NIM self-hosted plus a TensorRT-LLM deploy cookbook; "data never leaves your secure enclave".
Self-hosting plus the irrevocable Open Model Agreement grant supports data_control strong.

## EU AI Act
GPAI. NVIDIA NOT on the GPAI Code of Practice signatory list; no training-content summary or
copyright policy located. Training compute undisclosed (tokens only).
