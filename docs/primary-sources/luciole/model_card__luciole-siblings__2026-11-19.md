doc_type: model_card
entity: luciole
variant/applies-to: sibling Luciole repos (not the scored release): Luciole-8B-Instruct-1.1, Luciole-1B-Instruct-1.1, Luciole-8B-Base, Luciole-1B-Base, Luciole-8B-KD-Math-Base, Luciole-8B-KD-Math-Thinking-1.1, Luciole-23B-Audio-1.0, and the GGUF and FP8 builds
source_url: https://huggingface.co/OpenLLM-France/<repo>/raw/main/README.md and https://huggingface.co/api/models/OpenLLM-France/<repo>
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Findings

Luciole-8B-Instruct-1.1 and Luciole-1B-Instruct-1.1: the cards match the 23B card line for line apart from the model name, one DPO learning rate (1.0e-6 against 3.0e-7) and the evaluation sentence ("approaches Qwen3 in instruction following"). Same licence (apache-2.0), same base-model link pattern, same post-training dataset, no safety section, no LICENSE file.

Luciole-8B-Base: "a pretrained 8B parameter causal language model with a hybrid Mamba-transformer architecture"; LICENSE.md present; repo ships configuration_nemotron_h.py and modeling_nemotron_h.py. Luciole-1B-Base: LICENSE.md present.

Luciole-8B-KD-Math-Base: "trained through knowledge distillation (KD) following the Minitron approach ... We began by continually pretraining Luciole-23B-Base on a math-heavy mix of around 50 billion tokens to create a teacher ... The teacher was then pruned to a roughly 14 billion parameter model ... A second stage of pruning and distillation was applied, still using the corrected 23B model as the teacher". Apache-2.0, base_model Luciole-23B-Base, no LICENSE file. Teacher and student are both Luciole.

Luciole-8B-KD-Math-Thinking-1.1: same Thinking safety note (DPO safety alignment); no LICENSE file.

Luciole-23B-Audio-1.0: front matter lists "base_model: OpenLLM-France/Luciole-23B-Instruct-1.1" and "nvidia/parakeet-tdt-0.6b-v3", dataset Luciole-Audio-Training-Dataset; card licence section: "released under the Apache License 2.0". The Luciole-Audio-Training-Dataset and Luciole-Audio-Evaluation-Dataset carry licence tag cc-by-nc-sa-4.0 (Hugging Face dataset API). The NOTICE file does not list the Audio models. The Parakeet licence and the audio data terms were not read.

GGUF builds (BF16, Q4_K_M, Q5_K_M, Q8_0, plus a Modelfile) and FP8 builds (compressed-tensors via LLM Compressor, needs Hopper, Ada Lovelace or Blackwell GPUs) exist for the 1B, 8B and 23B Instruct-1.1, the 23B Thinking-1.1 and the 8B KD-Math Thinking-1.1. Cards: "released under the Apache License 2.0", copyright LINAGORA SAS. Uniform with the parent.

## What it establishes

Sizes of one Instruct-1.1 release are uniform on licence and recipe. Differences that would split an entry: the Thinking releases state a safety-alignment note the Instruct card lacks; the Base releases carry a LICENSE.md and no post-training; the 8B family is a hybrid Mamba-transformer needing repository code; Audio-1.0 sits on non-commercial audio data under an Apache label.
