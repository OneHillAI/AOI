doc_type: docs
entity: minicpm5
variant/applies-to: openbmb/MiniCPM5-1B and its sibling repos (file lists, formats, hashes, config)
source_url: https://huggingface.co/api/models/openbmb/MiniCPM5-1B/tree/main?recursive=1 ; .../raw/main/config.json ; .../raw/main/generation_config.json ; same /tree/main endpoints for -SFT, -Base, -GGUF, -MLX
retrieval_date: 2026-11-19
exists: yes
retrieved: true
note: Weights were NOT downloaded. Only the repository listing (sizes and LFS sha256 object ids) and small config files were read.

## openbmb/MiniCPM5-1B file list (verbatim from the tree API)
README-cn.md 22108 B; README.md 23436 B; chat_template.jinja 9062 B; config.json 726 B; generation_config.json 213 B; model-00000-of-00001.safetensors 2161290912 B, LFS sha256 7ab8fd86563125929be78aeec8cb3969c7ed2ead3be1ab9d3ec0a9fa69c8660d; model.safetensors.index.json 18004 B; special_tokens_map.json 551 B; tokenizer.json 9894271 B; tokenizer_config.json 94416 B; .gitattributes 1519 B.
There is no LICENSE file, no .bin or .pt pickle file, and no SECURITY or model-signature file in this repository. Format: one safetensors shard. HF safetensors metadata: {'BF16': 1080632832}, total 1080632832.
Gating: "gated": false, "private": false (API). Downloads 226,265, likes 1,180 on 2026-11-19. Author org: openbmb.

## Sibling repos (tree API, 2026-11-19)
MiniCPM5-1B-SFT: safetensors 2161290944 B sha256 3d55612299c140fb1f16180df61ccf8166f48fb4ba7b499435aac6a4055f1675; also tokenizer.model (SentencePiece) 1181204 B.
MiniCPM5-1B-Base: safetensors 2161290944 B sha256 bcf629379a6f5f5e18e9ec637a0e054de7f14e311a66b3d9b0932d06ec487f0e.
MiniCPM5-1B-GGUF: MiniCPM5-1B-F16.gguf 2166551936 B (sha256 68c40b08...); MiniCPM5-1B-Q8_0.gguf 1153529216 B (sha256 0dc76385...); MiniCPM5-1B-Q4_K_M.gguf 688065920 B (sha256 81b64d05...). GGUF metadata: architecture llama, context_length 131072. Library tag llama.cpp.
MiniCPM5-1B-MLX: model.safetensors 608026621 B sha256 a23e0c5c79944a0b2cc92cb9ab79376b4dce41e2312383727e21ee43fe19cb4f; tensor types U32 1080557568 + BF16 75264 (4-bit quantised).

## config.json (verbatim, key fields)
"architectures": ["LlamaForCausalLM"], "model_type": "llama", "hidden_size": 1536, "intermediate_size": 4608, "num_hidden_layers": 24, "num_attention_heads": 16, "num_key_value_heads": 2, "head_dim": 128, "max_position_embeddings": 131072, "rope_theta": 5000000, "rope_scaling": null, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "vocab_size": 130560, "transformers_version": "5.6.2", "eos_token_id": [1, 130073].
generation_config.json: "do_sample": true, "temperature": 0.9, "top_p": 0.95.

## Chat template (chat_template.jinja, 9062 B, read via the API's chat_template field)
ChatML-style: "<|im_start|>system ... <|im_end|>", tool definitions injected inside <tools></tools> with an XML tool-call format ("<function name=...><param name=...>...</param></function>"), tool results wrapped in <tool_response>, and "enable_thinking" appends "<think>\n\n</think>\n\n" when false and "<think>\n" when true.

## Unreviewed derivatives (search result, 2026-11-19, third-party repos on the Hub)
Community repos exist for MiniCPM5-1B including quantisations (mlx-community, mradermacher, PrunaAI, cyankiwi, turboderp exl3, taobao-mnn MNN, Tdamre litert-lm), and repos named "MiniCPM5-1B-Uncensored" (sahilchachra, tinyopsec). These are not from the publisher and were not inspected.

## Publisher identity and scan status on the Hub (API, 2026-11-19)
Organisation API (https://huggingface.co/api/organizations/openbmb/overview): fullname "OpenBMB", "isVerified": false, numFollowers 6213, numModels 199, details "Large Language Models". The openbmb org does NOT carry the Hub's verified badge. Identity is cross-confirmed by the GitHub repository OpenBMB/MiniCPM (which links these exact Hub repos) and by Artificial Analysis ("created by OpenBMB"), not by a Hub verification.
Model API for MiniCPM5-1B: "securityRepoStatus": {"scansDone": true, "filesWithIssues": []} (the Hub's own file scan found no flagged files). This is the Hub platform scan, not a publisher attestation and not a signature. No cryptographic signature, SLSA or sigstore attestation file exists in the repo.
