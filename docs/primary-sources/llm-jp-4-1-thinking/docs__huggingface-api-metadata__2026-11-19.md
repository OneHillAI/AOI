# docs / huggingface-api-metadata

source_url: https://huggingface.co/api/models/llm-jp/llm-jp-4.1-33b-thinking ; https://huggingface.co/api/organizations/llm-jp/overview
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE (OneHill): Hugging Face JSON API read on 2026-11-19 (https://huggingface.co/api/models/llm-jp/<name>?blobs=true, and ?securityStatus=true). Metadata only. No weights downloaded.

## Per-repository metadata
```
llm-jp-4.1-33b-thinking: gated=False private=False createdAt=2026-09-16T06:14:16.000Z lastModified=2026-09-28T07:27:30.000Z downloads=8264 sha=de581ee4353568c480d47129948d1be99f02f4ff tags=['transformers', 'safetensors', 'llama', 'text-generation', 'conversational', 'en', 'ja', 'license:apache-2.0', 'text-generation-inference', 'region:us'] safetensors_params=33219548160 n_safetensors_shards=14 has_LICENSE_file=False has_pickle_bin=False
llm-jp-4.1-8b-thinking: gated=False private=False createdAt=2026-09-15T23:33:30.000Z lastModified=2026-09-28T07:26:13.000Z downloads=100382 sha=7c19bc90e49b717381e4f474ee95964c05217a28 tags=['transformers', 'safetensors', 'llama', 'text-generation', 'conversational', 'en', 'ja', 'license:apache-2.0', 'text-generation-inference', 'region:us'] safetensors_params=8590200832 n_safetensors_shards=4 has_LICENSE_file=False has_pickle_bin=False
llm-jp-4.1-32b-a3b-thinking: gated=False private=False createdAt=2026-09-16T05:12:15.000Z lastModified=2026-09-28T07:27:08.000Z downloads=4198 sha=cda260706786758045e5e96bf4d738bbc01155b5 tags=['transformers', 'safetensors', 'qwen3_moe', 'text-generation', 'conversational', 'en', 'ja', 'license:apache-2.0', 'region:us'] safetensors_params=32139028992 n_safetensors_shards=13 has_LICENSE_file=False has_pickle_bin=False
llm-jp-4.1-33b-thinking-gguf: gated=False private=False createdAt=2026-09-24T10:17:08.000Z lastModified=2026-10-20T04:18:44.000Z downloads=5586 sha=f91445c4ac24e9b75357681017f955e7e14bbca2 tags=['transformers', 'gguf', 'text-generation', 'en', 'ja', 'license:apache-2.0', 'region:us', 'conversational'] safetensors_params=None n_safetensors_shards=0 has_LICENSE_file=False has_pickle_bin=False
```

## Security scan (llm-jp-4.1-33b-thinking, securityStatus=true)
```
securityRepoStatus: {'scansDone': True, 'filesWithIssues': []}
```
Per-file LFS sha256 values are present in the API listing for every safetensors shard (for example model-00001-of-00014.safetensors sha256 begins 8309caa249697cae). No repository files are pickle or .bin. The repository carries two Python files that execute on load with trust_remote_code=True: llmjp4_tokenizer.py (3,876 bytes) and llmjp4_harmony.py (4,177 bytes).

## Organisation
https://huggingface.co/api/organizations/llm-jp/overview: fullname "LLM-jp", name "llm-jp", isVerified: false, plan: team, numUsers: 51, numModels: 275, numDatasets: 64, numFollowers: 738. The Hugging Face verified-organisation badge is NOT set. NII's own release page (https://llm-jp.nii.ac.jp/en/release-en/) links to https://huggingface.co/llm-jp as the place where the models are published ("Open on Hugging Face").

## config.json of llm-jp-4.1-33b-thinking
```
{
  "architectures": [
    "LlamaForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 1,
  "eos_token_id": [2, 13],
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 5120,
  "initializer_range": 0.02,
  "intermediate_size": 27648,
  "max_position_embeddings": 65536,
  "mlp_bias": false,
  "model_type": "llama",
  "num_attention_heads": 40,
  "num_hidden_layers": 64,
  "num_key_value_heads": 8,
  "pretraining_tp": 1,
  "rms_norm_eps": 1e-06,
  "rope_scaling": null,
  "rope_theta": 500000,
  "tie_word_embeddings": false,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.51.0",
  "use_cache": true,
  "vocab_size": 196608
}
```
Context: max_position_embeddings 65536; vocab_size 196608; architecture LlamaForCausalLM (dense). The 32B-A3B uses Qwen3MoeForCausalLM, 128 experts, 8 per token, max_position_embeddings 65536.

## Collection
https://huggingface.co/api/collections/llm-jp/llm-jp-41-models (title "LLM-jp-4.1 Models") lists six items: llm-jp/llm-jp-4.1-33b-thinking, llm-jp/llm-jp-4.1-33b-thinking-gguf, llm-jp/llm-jp-4.1-32b-a3b-thinking, llm-jp/llm-jp-4.1-32b-a3b-thinking-gguf, llm-jp/llm-jp-4.1-8b-thinking, llm-jp/llm-jp-4.1-8b-thinking-gguf. The 4.1 series has no new base model; the 4.0 base models (llm-jp-4-8b-base, llm-jp-4-32b-a3b-base, llm-jp-4-33b-base, created 2026-03-15 to 2026-08-14) are the pre-trained models behind it (blog: 4.1 "improves the post-training of the LLM-jp-4 series").
