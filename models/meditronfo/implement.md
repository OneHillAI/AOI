# Implement - MeditronFO (Apertus-70B-MeditronFO / Apertus-8B-MeditronFO)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

The checkpoints are standard safetensors on Hugging Face under `EPFLiGHT`. The Apertus architecture needs `transformers` 4.56 or later (`ev-base-card`). Pin the commit, because the weights on main were replaced twice in autumn 2026 (`ev-hf-meta`).

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "EPFLiGHT/Apertus-70B-MeditronFO"   # or Apertus-8B-MeditronFO
rev = "d13151ac9ff56b966dd5257d5064876685a750e3"  # 70B revision; do not float on main
tok = AutoTokenizer.from_pretrained(model_id, revision=rev)
model = AutoModelForCausalLM.from_pretrained(
    model_id, revision=rev, torch_dtype=torch.bfloat16, device_map="auto")
```

The card's own example uses sampling with temperature 0.7 and `max_new_tokens=8192`, and the repo's `generation_config.json` sets the same defaults (`ev-card-70b`, `ev-hf-meta`). Verify the per-shard sha256 against the Hugging Face file record after download. The code repository (`ev-github-readme`) is a separate Apache-2.0 project for reproducing the paper and is not an inference package.

<!-- item: hardware -->
## Hardware & VRAM requirements

The publisher gives training compute only (70B: 16 nodes of 4 GH200 for 3 h 06 min, 199 GPU-hours) and no serving guidance (`ev-card-70b`). Sizes come from the file listing (`ev-hf-meta`):

| Checkpoint | Parameters | BF16 weight size | Practical minimum (OneHill estimate, untested) |
|---|---:|---:|---|
| Apertus-70B-MeditronFO | 70.6B in 30 shards | about 141 GB | two to four 80 GB GPUs for BF16 plus KV cache, or a quantised build |
| Apertus-8B-MeditronFO | 8.05B in 4 shards | about 16 GB | one 24 GB GPU with short contexts |

KV-cache memory grows with context. The fine-tuning used 8,192-token sequences, so plan around that length.

<!-- item: serving -->
## Serving stacks

The MeditronFO cards document only `transformers`. The Apertus base card lists `transformers`, vLLM, SGLang and MLX as supported (`ev-base-card`). That is a statement about the base architecture and not a test of these fine-tunes. Community GGUF conversions (llama.cpp) and an 8B MLX conversion exist (`ev-quants`). OneHill has not run any of them.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling: T1 (internal assistant), conditional, and only for non-clinical use. Clinical decision use is outside any ceiling because the publisher prohibits it (`ev-project-page`). T2 and above are not recommended: no guard model, no independent safety evaluation and low-agreement safety judging mean the playbook's model layer is missing.

Controls required to reach T1 on non-patient work:

1. Pin the commit and verify shard hashes (supply-chain layer).
2. Keep a qualified person reading every output, and feed no output into any patient pathway.
3. Run a clinical safety evaluation and a red-team for the use case. The publisher says its judge is unsuitable as a deployment-readiness signal for safety criteria (`ev-paper`) and recommends independent safety evaluation (`ev-data-card`).
4. Add input and output guardrails and a separate guard or classifier model; none ships with the release.
5. Constrain answer length, because answers run longer than the base model's (`ev-project-page`).
6. Resolve the licence chain with counsel before any commercial use (see the licence item in assess), and consider the Apertus acceptable-use and personal-data output-filter advice (`ev-base-card`).
7. If the product could influence a clinical decision, treat medical-device and AI Act high-risk assessment as a precondition to development.

<!-- item: quantization -->
## Available quantizations

There is no official quantisation. Community GGUF and i1-GGUF conversions of both sizes (mradermacher), an MLX conversion of the 8B (loleg) and Q4 and Q5 GGUF of the 8B (BrazosDeDios) are listed (`ev-quants`). None is opened, and quantisation can change clinical answer quality in ways nobody has measured for this model. Prefer the canonical safetensors for anything under evaluation.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Fine-tuning is the strongest part of the release. The GitHub repository publishes the Axolotl training configs for every reported model, the data-generation, resampling and decontamination scripts, and the evaluation harness fork. The recipe is published: 70B, 1 epoch, learning rate 1e-5, cosine decay, 10 percent warmup, effective batch 64 packed sequences of 8,192 tokens, AdamW, seed 42, DeepSpeed ZeRO-3, bf16 (`ev-github-readme`, `ev-card-70b`).

The corpus loads with `datasets.load_dataset("EPFLiGHT/fully-open-meditron")` and each row carries its source dataset, gold label and teacher (`ev-data-card`). The README warns that Axolotl silently reuses a stale tokenised cache unless each config has its own `dataset_prepared_path`. The paper reports an optional 10 percent Tulu 3 replay that recovers most of the general-capability loss (`ev-paper`). The intermediate data and per-item evaluation outputs are not yet released, so a full reproduction from a fresh clone is not possible (`ev-github-readme`).

<!-- item: integration -->
## API / OpenAI-compatible integration

No MeditronFO-specific API documentation exists. A serving stack that supports the Apertus architecture (the base card names vLLM and SGLang) can expose an OpenAI-compatible endpoint, but OneHill has not tested that for these checkpoints (`ev-base-card`). The chat template is bundled in the repository (`ev-hf-meta`).
