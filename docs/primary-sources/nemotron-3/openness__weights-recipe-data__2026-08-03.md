doc_type: openness
entity: nemotron-3
variant/applies-to: Nemotron 3 Super + Nano - weights, recipe and training-data release
source_url: https://github.com/NVIDIA-NeMo/Nemotron ; https://huggingface.co/datasets/nvidia/Nemotron-SFT-Safety-v1 ; https://huggingface.co/datasets/nvidia/Nemotron-CC-v2.1
document_effective_date: ~2025-12
retrieval_date: 2026-08-03
exists: yes
retrieved: true
tag: publisher

## Openness self-description (Super + Nano cards - VERBATIM)
"NVIDIA Nemotron(TM) is a family of open models with open weights, training data, and recipes,
delivering leading efficiency and accuracy for building specialized AI agents."

## Runnable recipes (VERBATIM caveat)
Recipes for super3 and nano3 (Pretrain -> SFT -> RL) live at github.com/NVIDIA-NeMo/Nemotron.
Decisive reproducibility caveat, VERBATIM: "These recipes train exclusively on the open-sourced
subset of training data. Results will differ from the tech report benchmarks, which used additional
proprietary data."

## Training data (partial release)
Post-training data (Nemotron-Post-Training-v3, e.g. Nemotron-SFT-Safety-v1) is CC-BY-4.0 (+ Apache
2.0 + MIT) and confirmed as the post-training data used for Nano/Super/Ultra v3. Some code, math and
multilingual data are gated ("gating and approval is required"). The pretraining web corpus
(Nemotron-CC-v2.1, 2.5T tokens) sits under a custom "NVIDIA Data Access Agreement for Model
Training", not CC-BY. Cards report far larger training totals (~25T tokens) than the released
subset, so the FULL corpus is NOT reproducible.

## Conclusion
open_weights_recipe (tier 4): ungated safetensors weights, runnable recipes, a white paper and
CC-BY post-training data, but the pretraining corpus is only partially released, so the model is not
reproducible. Short of fully_open.
