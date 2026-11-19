doc_type: docs
entity: luciole
variant/applies-to: Hugging Face organisation OpenLLM-France and the scored repo OpenLLM-France/Luciole-23B-Instruct-1.1
source_url: https://huggingface.co/api/models?author=OpenLLM-France ; https://huggingface.co/api/datasets?author=OpenLLM-France ; https://huggingface.co/api/organizations/OpenLLM-France/overview ; https://huggingface.co/api/models/OpenLLM-France/Luciole-23B-Instruct-1.1 (+ ?blobs=true, ?securityStatus=true, /tree/main, /commits/main, /discussions, /refs)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Organisation

Org overview: fullname "OpenLLM France", name OpenLLM-France, "isVerified": false, plan "team", numUsers 20, numModels 38, numDatasets 19, numSpaces 2, numFollowers 426. The organisation is NOT verified on Hugging Face.

## The 38 model repos (created, last modified, licence tag, gated)

All 38 carry licence tag apache-2.0 or cc-by-nc-sa-4.0 (Claire only) and none is gated.

Older, not Luciole: Claire-7B-0.1, Claire-7B-Apache-0.1, Claire-Mistral-7B-0.1, Claire-7B-EN-0.1, Claire-7B-FR-Instruct-0.1 (2023-11 to 2024-09; the Claire models other than Claire-7B-Apache are cc-by-nc-sa-4.0); Lucie-7B (2024-10-10), Lucie-7B-Instruct-human-data (2025-01-07), Lucie-7B-Instruct-v1.1 (2025-02-13), Lucie-7B-Instruct-v1.1-gguf (2025-02-14), all apache-2.0.

Luciole (all apache-2.0 by tag, not gated):
- 2026-02-17: Luciole-23B-Base, Luciole-8B-Base, Luciole-1B-Base
- 2026-05-22: seven luciole-ablation-1B-* (data-mix ablations: en1.0, en0.99-fr0.01, en0.95-fr0.05, en0.66-fr0.33, en0.5-fr0.5, en0.33-fr0.66, fr1.0)
- 2026-07-07: Luciole-1B/8B/23B-Instruct-1.1
- 2026-07-08: Luciole-1B/8B/23B-Instruct-1.1-GGUF and -FP8
- 2026-09-09: Luciole-23B-Thinking-1.1 (+ GGUF); FP8 on 2026-11-05
- 2026-09-18: Luciole-1B/8B/23B-Audio-1.0
- 2026-09-28: Luciole-8B-KD-Math-Thinking-1.1 (GGUF 2026-10-15, FP8 2026-11-05)
- 2026-10-13: Luciole-8B-KD-Math-Base
Many repos show last modified 2026-11-12 (README and tokenizer-class edits). There is no Luciole-8B-Thinking or Luciole-1B-Thinking repo in the org (the GitHub finetune/model_cards folder lists 1B-Thinking-1.1 and 8B-Thinking-1.1 cards, but no such HF repos exist in the listing).

Downloads shown at the time of the listing: 23B-Instruct-1.1 1,158; 8B-Instruct-1.1 3,063; 1B-Instruct-1.1 1,313; 23B-Base 667; 23B-Thinking-1.1 346.

## Scored repo: OpenLLM-France/Luciole-23B-Instruct-1.1

- sha 770af27b30611fc513d41cae28cb45e3ad9a79b3; created 2026-07-07T15:01:01Z; last modified 2026-11-12T11:09:10Z; gated false; 21 likes.
- Tags: safetensors, nemotron, openllm-france, text-generation, conversational, fr, en, dataset:OpenLLM-France/Luciole-PostTraining-Dataset-1.1, base_model:OpenLLM-France/Luciole-23B-Base, base_model:finetune:OpenLLM-France/Luciole-23B-Base, license:apache-2.0.
- Files: ten model-0000N-of-00010.safetensors shards (4.8 to 5.0 GB each, 23,216,467,968 BF16 parameters in total), model.safetensors.index.json, config.json (architectures NemotronForCausalLM, model_type nemotron, 40 layers, hidden 6144, max_position_embeddings 131072, rope_theta 2000000, vocab 128000, transformers 4.57.1), generation_config.json (temperature 0.7, top_p 0.9), chat_template.jinja, tokenizer.json, tokenizer_config.json, special_tokens_map.json, benchmark_eval.png, luciole_logo.png, README.md, .gitattributes. No pickle (.bin) file, no custom Python code, no LICENSE file.
- LFS sha256 oids are listed by the tree API for every shard (for example shard 1 d55d64a9ad007583...). The publisher publishes no separate checksum file.
- Security scan: scansDone true, filesWithIssues empty.
- Commit history (main): 2026-07-09 "Initial release of Luciole-23B-Instruct-1.1"; 2026-07-21 and 2026-07-22 README and benchmark figure; 2026-08-28 and 2026-10-06 README; 2026-11-04 "Add tool calling usage"; 2026-11-10 "Add License section to model card"; 2026-11-12 "Use PreTrainedTokenizerFast as tokenizer_class for transformers 5 compatibility".
- Discussions: one open discussion ("Additional parser config for vLLM"). inferenceProviderMapping: none.
- Refs API for Luciole-23B-Base: one branch (main) and no tags, although the card says intermediate checkpoints use "dedicated revision tags".

## Differences in sibling Instruct repos

Luciole-8B-Instruct-1.1: architecture NemotronHForCausalLM (hybrid Mamba-transformer), 8,075,686,912 parameters, ships configuration_nemotron_h.py and modeling_nemotron_h.py (82 KB of repository Python code). Luciole-1B-Instruct-1.1: NemotronForCausalLM, 1,319,309,312 parameters, single model.safetensors, plus bfcl_live.png and bfcl_non_live.png.

## Quantised builds of the scored release (HF API tree sizes)

Luciole-23B-Instruct-1.1-GGUF: BF16 46.44 GB, Q8_0 24.67 GB, Q5_K_M 16.69 GB, Q4_K_M 14.47 GB, plus a Modelfile (num_ctx 32000, temperature 0.2, ChatML-style template with tool calls). The Modelfile comment mentions "Luciole-1B-Instruct-1.2", a name that matches no repo. Hugging Face parses the GGUF as architecture nemotron, context length 131072.
Luciole-23B-Instruct-1.1-FP8: six safetensors shards, 24.8 GB in total (compressed-tensors, LLM Compressor recipe.yaml).
Luciole-8B-Instruct-1.1-GGUF: BF16 16.16 GB, Q8_0 8.59 GB, Q5_K_M 5.77 GB, Q4_K_M 4.96 GB. Luciole-1B-Instruct-1.1-GGUF: BF16 3.17 GB, Q8_0 1.68 GB, Q5_K_M 1.15 GB, Q4_K_M 1.02 GB.
The 23B bf16 safetensors shards total 46.4 GB (23,216,467,968 parameters at 2 bytes).
