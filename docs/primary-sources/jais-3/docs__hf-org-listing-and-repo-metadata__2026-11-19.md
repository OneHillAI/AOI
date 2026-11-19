# docs / Hugging Face organisation listing and repo metadata for Jais-3

source_url: https://huggingface.co/api/models?author=inception42 ; https://huggingface.co/api/organizations/inception42/overview ; https://huggingface.co/api/models/inception42/<repo>?blobs=true&securityStatus=true ; https://huggingface.co/api/models/inception42/<repo>/refs ; https://huggingface.co/api/models?author=IFM
retrieval_date: 2026-11-19
doc_type: docs
exists: yes
retrieved: true
tag: publisher (hub metadata)

## Organisation
inception42 overview (API): "fullname":"Inception42","details":"Generative AI, Arabic NLP","isVerified":true,"plan":"team","numModels":46.
IFM overview (API): "fullname":"Institute of Foundation Models","isVerified":false,"plan":"enterprise","numModels":126. The IFM organisation hosts the official quantised builds (FP8, GGUF, MLX) of Jais-3 and the K2-Horizon base models.

## inception42 Jais-3 repositories (all returned by the author listing)
| repo | created | last modified | gated | HF licence tag | in-repo LICENSE or NOTICE file | pickle or .bin files | scansDone / filesWithIssues |
|---|---|---|---|---|---|---|---|
| inception42/Jais-3-0.9B | 2026-09-29 | 2026-11-12 | False | apache-2.0 (card front matter and tag license:apache-2.0) | none (raw LICENSE, LICENSE.md and NOTICE each returned HTTP 404; file list has no LICENSE) | none | scan reported done by hub; see 7B detail below |
| inception42/Jais-3-3.7B | 2026-09-29 | 2026-11-12 | False | apache-2.0 (card front matter and tag license:apache-2.0) | none (raw LICENSE, LICENSE.md and NOTICE each returned HTTP 404; file list has no LICENSE) | none | scan reported done by hub; see 7B detail below |
| inception42/Jais-3-7B | 2026-09-29 | 2026-11-12 | False | apache-2.0 (card front matter and tag license:apache-2.0) | none (raw LICENSE, LICENSE.md and NOTICE each returned HTTP 404; file list has no LICENSE) | none | scan reported done by hub; see 7B detail below |
| inception42/Jais-3-32B | 2026-09-29 | 2026-11-12 | False | apache-2.0 (card front matter and tag license:apache-2.0) | none (raw LICENSE, LICENSE.md and NOTICE each returned HTTP 404; file list has no LICENSE) | none | scan reported done by hub; see 7B detail below |
| inception42/Jais-3-MoVA-36B-A4B | 2026-09-29 | 2026-11-12 | False | apache-2.0 (card front matter and tag license:apache-2.0) | none (raw LICENSE, LICENSE.md and NOTICE each returned HTTP 404; file list has no LICENSE) | none | scan reported done by hub; see 7B detail below |
| inception42/Jais-3-375B-A23B | 2026-09-29 | 2026-11-12 | False | apache-2.0 (card front matter and tag license:apache-2.0) | none (raw LICENSE, LICENSE.md and NOTICE each returned HTTP 404; file list has no LICENSE) | none | scan reported done by hub; see 7B detail below |

Safetensors parameter counts from the API (BF16 unless stated): 0.9B repo 1,078,285,824; 3.7B repo 5,058,255,360; 7B repo 8,999,178,240; 32B repo 34,779,304,960; MoVA-36B-A4B repo 37,444,792,020 (BF16 37,444,784,640, F32 7,380); 375B-A23B repo 379,167,159,168 (BF16 379,167,148,032, F32 11,136). The card names (0.9B, 3.7B, 7B, 32B, 36B, 375B) are size classes; counts include embeddings.

config.json max_position_embeddings: 0.9B 131072; 3.7B, 7B, 32B, MoVA-36B-A4B and 375B-A23B 524288. Architecture class K2HorizonForCausalLM (model_type k2_horizon); num_experts 192 in the 375B repo, 100 in the MoVA repo, 0 in the dense repos. Each repo contains configuration_k2_horizon.py and modeling_k2_horizon.py (custom code; the card examples use trust_remote_code=True).

## Detail for inception42/Jais-3-7B (securityStatus=true, blobs=true)
securityRepoStatus: {"scansDone": true, "filesWithIssues": []}. Four safetensors shards with LFS sha256 values published in the API (for example model-00000-of-00004.safetensors 5,314,184,744 bytes, sha256 prefix 0adda0c43ca49c64). Files: .gitattributes, README.md, assets/jais-3-7b-benchmarks.png, chat_template.jinja, config.json, configuration_k2_horizon.py, generation_config.json, four safetensors shards, model.safetensors.index.json, modeling_k2_horizon.py, tokenizer.json, tokenizer_config.json.

## Stage branches (API /refs, same four on every Jais-3 weights repo)
branches: main, CPT, Cooldown, FTPO, SFT. No tags. (The technical report lists RLVR as a released stage checkpoint; no RLVR branch exists, so main is presumed to be the final RLVR checkpoint. This is OneHill inference, not stated.)

## Adapters in the same organisation
inception42/Jais-3-{0.9B,3.7B,7B,32B}-Uno: PEFT LoRA adapters (tags peft, lora, uno, diffusion-language-model), no licence tag and no licence statement in the card body (card front matter has base_model inception42/Jais-3-32B, base_model_relation adapter). The adapters are outside this entry.

## Official quantised builds (IFM organisation, API listing, each tagged license:apache-2.0)
FP8: IFM/Jais-3-{3.7B,7B,32B,MoVA-36B-A4B,375B-A23B}-FP8 (2026-09-29 to 2026-09-30; no 0.9B FP8).
MLX: IFM/Jais-3-{0.9B,3.7B,7B,32B}-MLX-{4bit,8bit,bf16} and IFM/Jais-3-MoVA-36B-A4B-MLX-{4bit,8bit,bf16} (2026-10-01 to 2026-10-02).
GGUF: IFM/Jais-3-{0.9B,3.7B,7B,32B,MoVA-36B-A4B}-GGUF (2026-10-12 to 2026-10-13). IFM/Jais-3-32B-GGUF holds BF16, Q4_K_M, Q5_0, Q5_K_M, Q6_K and Q8_0 files; its card front matter says license apache-2.0, base_model inception42/Jais-3-32B. No GGUF listed for 375B-A23B.
Related: IFM/Jais-ASR (speech, created 2026-10-06, Apache-2.0 tag).

## inception42 listing: full list of Jais-3 and earlier Jais repositories (names, created, licence tags where present)
- inception42/Jais-3-MoVA-36B-A4B created 2026-09-29 gated=False ['license:apache-2.0']
- inception42/jais-13b created 2023-08-17 gated=auto ['license:apache-2.0']
- inception42/jais-13b-chat created 2023-08-23 gated=auto ['license:apache-2.0']
- inception42/jais-30b-v1 created 2023-10-27 gated=auto ['license:apache-2.0']
- inception42/jais-30b-chat-v1 created 2023-11-06 gated=auto ['license:apache-2.0']
- inception42/jais-30b-v3 created 2024-02-14 gated=auto ['license:apache-2.0']
- inception42/jais-30b-chat-v3 created 2024-02-14 gated=auto []
- inception42/jais-6p7b-chat created 2024-05-09 gated=False []
- inception42/jais-adapted-70b-chat created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-adapted-70b created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-family-590m-chat created 2024-08-02 gated=False ['license:apache-2.0']
- inception42/jais-family-590m created 2024-08-02 gated=False ['license:apache-2.0']
- inception42/jais-adapted-7b created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-family-1p3b-chat created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-adapted-7b-chat created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-family-1p3b created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-adapted-13b created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-adapted-13b-chat created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-family-2p7b-chat created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-family-2p7b created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-family-6p7b-chat created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-family-6p7b created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-family-13b-chat created 2024-08-02 gated=False ['license:apache-2.0']
- inception42/jais-family-13b created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-family-30b-8k-chat created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-family-30b-8k created 2024-08-02 gated=False ['license:apache-2.0']
- inception42/jais-family-30b-16k-chat created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-family-30b-16k created 2024-08-02 gated=auto ['license:apache-2.0']
- inception42/jais-family-256m-chat created 2024-08-26 gated=False ['license:apache-2.0']
- inception42/jais-family-256m created 2024-08-26 gated=False ['license:apache-2.0']
- inception42/JaisFamilySupplmentary created 2024-09-06 gated=False ['license:apache-2.0']
- inception42/Llama-3.1-Sherkala-8B-Chat created 2025-02-07 gated=auto ['license:cc-by-nc-sa-4.0']
- inception42/jais-adapted-70b-chat-4bit-bnb created 2025-02-21 gated=False ['license:apache-2.0']
- inception42/Jais-2-70B-Chat created 2025-12-09 gated=auto ['license:apache-2.0']
- inception42/Jais-2-8B-Chat created 2025-12-09 gated=auto ['license:apache-2.0']
- inception42/Jais-2-8B-Chat-GGUF created 2026-02-05 gated=auto ['license:apache-2.0']
- inception42/Jais-2-70B-Chat-GGUF created 2026-02-09 gated=auto ['license:apache-2.0']
- inception42/Jais-3-0.9B created 2026-09-29 gated=False ['license:apache-2.0']
- inception42/Jais-3-3.7B created 2026-09-29 gated=False ['license:apache-2.0']
- inception42/Jais-3-7B created 2026-09-29 gated=False ['license:apache-2.0']
- inception42/Jais-3-32B created 2026-09-29 gated=False ['license:apache-2.0']
- inception42/Jais-3-375B-A23B created 2026-09-29 gated=False ['license:apache-2.0']
- inception42/Jais-3-0.9B-Uno created 2026-09-29 gated=False []
- inception42/Jais-3-3.7B-Uno created 2026-09-29 gated=False []
- inception42/Jais-3-7B-Uno created 2026-09-29 gated=False []
- inception42/Jais-3-32B-Uno created 2026-09-29 gated=False []
