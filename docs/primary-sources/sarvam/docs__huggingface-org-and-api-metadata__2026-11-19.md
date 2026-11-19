# docs / Hugging Face organisation listing and per-repo API metadata

source_url: https://huggingface.co/api/models?author=sarvamai ; https://huggingface.co/api/models/sarvamai/<repo>?blobs=true&securityStatus=true
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

## Organisation sarvamai
isVerified: false (https://huggingface.co/api/organizations/sarvamai/overview), numModels 17, numDatasets 17.

## All 17 model repositories in the organisation (API listing, 2026-11-19)
```
sarvamai/prism | created 2026-11-02 | ['license:apache-2.0'] | text-classification
sarvamai/sarvam-105b-1711-bf16 | created 2026-11-15 | ['license:apache-2.0'] | text-generation
sarvamai/sarvam-105b | created 2026-03-03 | ['license:apache-2.0'] | text-generation
sarvamai/sarvam-105b-1711 | created 2026-11-15 | ['license:apache-2.0'] | text-generation
sarvamai/OpenHathi-7B-Hi-v0.1-Base | created 2023-12-13 | ['license:llama2'] | text-generation
sarvamai/sarvam-30b | created 2026-03-03 | ['license:apache-2.0'] | text-generation
sarvamai/shuka-1 | created 2024-08-08 | ['license:llama3'] | audio-text-to-text
sarvamai/sarvam-1-v0.5 | created 2024-08-13 | ['license:other'] | text-generation
sarvamai/sarvam-1 | created 2024-10-23 | [] | text-generation
sarvamai/sarvam-m | created 2025-05-20 | ['license:apache-2.0'] | text-generation
sarvamai/sarvam-m-q8-gguf | created 2025-05-24 | ['license:apache-2.0'] | None
sarvamai/sarvam-m-gguf | created 2025-05-24 | ['license:apache-2.0'] | None
sarvamai/sarvam-translate | created 2025-06-07 | ['license:gpl-3.0'] | translation
sarvamai/sarvam-105b-gguf | created 2026-03-20 | ['license:apache-2.0'] | text-generation
sarvamai/sarvam-30b-gguf | created 2026-03-23 | ['license:apache-2.0'] | text-generation
sarvamai/sarvam-105b-fp8 | created 2026-03-25 | ['license:apache-2.0'] | text-generation
sarvamai/sarvam-30b-fp8 | created 2026-03-26 | ['license:apache-2.0'] | text-generation
```
NOTE: all 17 are ungated. Only the eight repos below belong to this entry. The others are separate releases: sarvam-translate (gpl-3.0 tag), prism (LoRA decision model on Sarvam-105B), sarvam-m and its GGUFs (Apache-2.0 tag), sarvam-1 and sarvam-1-v0.5 (license other or none), shuka-1 (llama3), OpenHathi-7B (llama2).

## Repos in this entry

| repo | created | modified | gated | size on disk | tensor dtype and count | hub scan |
|---|---|---|---|---|---|---|
| sarvam-30b | 2026-03-03 | 2026-11-12 | False | 128.6 GB | {'F32': 32152650368} | scansDone=True filesWithIssues=[] |
| sarvam-105b | 2026-03-03 | 2026-09-21 | False | 424.2 GB | {'F32': 106031767424} | scansDone=True filesWithIssues=[] |
| sarvam-105b-1711 | 2026-11-15 | 2026-11-18 | False | 70.2 GB | {'F32': 3968, 'BF16': 2164019200, 'F8_E4M3': 4009754624, 'U8': 49928994816} | scansDone=True filesWithIssues=[] |
| sarvam-105b-1711-bf16 | 2026-11-15 | 2026-11-18 | False | 218.3 GB | {'F32': 3968, 'BF16': 106031763456} | scansDone=True filesWithIssues=[] |
| sarvam-105b-fp8 | 2026-03-25 | 2026-03-31 | False | 112.6 GB | {'F32': 2164023168, 'F8_E4M3': 103867744256} | scansDone=True filesWithIssues=[] |
| sarvam-30b-fp8 | 2026-03-26 | 2026-03-31 | False | 38.7 GB | {'F32': 2157085312, 'F8_E4M3': 29995565056} | scansDone=True filesWithIssues=[] |
| sarvam-105b-gguf | 2026-03-20 | 2026-03-23 | False | 64.2 GB | GGUF Q4_K_M | scansDone=False filesWithIssues=[] |
| sarvam-30b-gguf | 2026-03-23 | 2026-03-23 | False | 19.6 GB | GGUF Q4_K_M | scansDone=False filesWithIssues=[] |

NOTE: sarvam-30b and sarvam-105b store weights as float32 (config dtype float32), about 128.6 GB and 424.2 GB. The 1711 BF16 repo is bfloat16 (218.3 GB) and the 1711 NVFP4 repo is a mixed NVFP4/MXFP8 compressed-tensors build (70.2 GB). All safetensors files carry LFS sha256 values and no pickle files exist. The GGUF repos report scansDone=False. Each main repo ships custom Python (configuration_sarvam_moe.py, modeling_sarvam_moe.py); sarvam-30b and sarvam-105b also ship hotpatch_vllm.py and sarvam.py, which patch a vLLM install.

## Base-model metadata
- sarvam-105b-1711-bf16: base_model sarvamai/sarvam-105b, base_model_relation finetune.
- sarvam-105b-1711: base_model sarvamai/sarvam-105b-1711-bf16, quantized.
- sarvam-30b, sarvam-105b: no base_model field.
- No base (pre-trained only) checkpoint repo exists in the organisation.

## Commit history (API commits/main)
- sarvam-105b: created 2026-03-03; 2026-09-21 'Fix MoE routing and training gradients (#13)'.
- sarvam-30b: created 2026-03-03; 2026-11-12 'Fix HF/vLLM parity and Transformers 5 loading, RoPE, and serialization (#16)'.
- sarvam-105b-1711 and -bf16: 2026-11-17 'Initial release'; 2026-11-18 'vLLM hosting: block rejection sampling for DSpark'.

## config.json
sarvam-30b: SarvamMoEForCausalLM, 19 layers, 128 experts, 6 per token, max_position_embeddings 131072, vocab 262144. sarvam-105b: SarvamMLAForCausalLM, 32 layers, 128 experts, 8 per token, max_position_embeddings 131072. sarvam-105b-1711: max_position_embeddings 163840 (cards use 131072 in examples).
