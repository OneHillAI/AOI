# docs / hf-repo-metadata

source_url: https://huggingface.co/api/models/EPFLiGHT/Apertus-70B-MeditronFO?blobs=true
retrieval_date: 2026-11-19
retrieved_by: curl, text read in full or in the extracts marked below
note: Hugging Face API output for the two Apertus-based MeditronFO repositories, plus config files, commit list and organisation record.

Verbatim extracts follow. Nothing below is paraphrased unless it is under a heading that says OneHill note.

## Apertus-70B-MeditronFO
- createdAt: 2026-05-08T11:49:31.000Z
- lastModified: 2026-11-17T13:48:57.000Z
- gated: False
- sha: d13151ac9ff56b966dd5257d5064876685a750e3
- tags: ['transformers', 'safetensors', 'apertus', 'text-generation', 'medical', 'clinical', 'healthcare', 'meditron', 'fully-open', 'medical-llm', 'conversational', 'en', 'dataset:EPFLiGHT/fully-open-meditron', 'arxiv:2605.16215', 'base_model:swiss-ai/Apertus-70B-Instruct-2509', 'base_model:finetune:swiss-ai/Apertus-70B-Instruct-2509', 'license:apache-2.0', 'endpoints_compatible', 'region:us']
- safetensors: {'parameters': {'BF16': 70599864480}, 'total': 70599864480}
- files: [('.gitattributes', 1634), ('README.md', 7684), ('assets/healthbench_size.png', 120617), ('chat_template.jinja', 14601), ('config.json', 897), ('generation_config.json', 197), ('model-00001-of-00030.safetensors', 4865428944), ('model-00002-of-00030.safetensors', 4429289408), ('model-00003-of-00030.safetensors', 4999714024), ('model-00004-of-00030.safetensors', 4966160096), ('model-00005-of-00030.safetensors', 4429256040), ('model-00006-of-00030.safetensors', 4429289448), ('model-00007-of-00030.safetensors', 4999714064), ('model-00008-of-00030.safetensors', 4966160128), ('model-00009-of-00030.safetensors', 4429256040), ('model-00010-of-00030.safetensors', 4429289448), ('model-00011-of-00030.safetensors', 4999714064), ('model-00012-of-00030.safetensors', 4966160128), ('model-00013-of-00030.safetensors', 4429256040), ('model-00014-of-00030.safetensors', 4429289448), ('model-00015-of-00030.safetensors', 4999714064), ('model-00016-of-00030.safetensors', 4966160128), ('model-00017-of-00030.safetensors', 4429256040), ('model-00018-of-00030.safetensors', 4429289448), ('model-00019-of-00030.safetensors', 4999714064), ('model-00020-of-00030.safetensors', 4966160128), ('model-00021-of-00030.safetensors', 4429256040), ('model-00022-of-00030.safetensors', 4429289448), ('model-00023-of-00030.safetensors', 4999714064), ('model-00024-of-00030.safetensors', 4966160128), ('model-00025-of-00030.safetensors', 4429256040), ('model-00026-of-00030.safetensors', 4429289448), ('model-00027-of-00030.safetensors', 4999714064), ('model-00028-of-00030.safetensors', 4966160128), ('model-00029-of-00030.safetensors', 4429256040), ('model-00030-of-00030.safetensors', 4563487752), ('model.safetensors.index.json', 90962), ('special_tokens_map.json', 565), ('tokenizer.json', 17078474), ('tokenizer_config.json', 177334)]
- LICENSE file at /raw/main/LICENSE: HTTP 404 (no LICENSE file in either model repository)

## Apertus-8B-MeditronFO
- createdAt: 2026-05-08T11:57:22.000Z
- lastModified: 2026-11-17T13:48:59.000Z
- gated: False
- sha: c0f8a017b6abaed4335e68a5f6c5e0096c17115f
- tags: ['transformers', 'safetensors', 'apertus', 'text-generation', 'medical', 'clinical', 'healthcare', 'meditron', 'fully-open', 'medical-llm', 'conversational', 'en', 'dataset:EPFLiGHT/fully-open-meditron', 'arxiv:2605.16215', 'base_model:swiss-ai/Apertus-8B-Instruct-2509', 'base_model:finetune:swiss-ai/Apertus-8B-Instruct-2509', 'license:apache-2.0', 'endpoints_compatible', 'region:us']
- safetensors: {'parameters': {'BF16': 8053338176}, 'total': 8053338176}
- files: [('.gitattributes', 1634), ('README.md', 7073), ('assets/healthbench_size.png', 120617), ('chat_template.jinja', 14601), ('config.json', 897), ('generation_config.json', 197), ('model-00001-of-00004.safetensors', 4999776656), ('model-00002-of-00004.safetensors', 4882374192), ('model-00003-of-00004.safetensors', 4974647808), ('model-00004-of-00004.safetensors', 1249928160), ('model.safetensors.index.json', 36480), ('special_tokens_map.json', 565), ('tokenizer.json', 17078474), ('tokenizer_config.json', 177334)]
- LICENSE file at /raw/main/LICENSE: HTTP 404 (no LICENSE file in either model repository)

## config.json (70B), max_position_embeddings and architecture
```
{
  "architectures": [
    "ApertusForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 1,
  "dtype": "bfloat16",
  "eos_token_id": 68,
  "hidden_act": "xielu",
  "hidden_dropout": 0.0,
  "hidden_size": 8192,
  "initializer_range": 0.02,
  "intermediate_size": 43008,
  "max_position_embeddings": 65536,
  "mlp_bias": false,
  "model_type": "apertus",
  "num_attention_heads": 64,
  "num_hidden_layers": 80,
  "num_key_value_heads": 8,
  "pad_token_id": 3,
  "post_norm": false,
  "qk_norm": true,
  "rms_norm_eps": 1e-05,
  "rope_scaling": {
    "factor": 8.0,
    "high_freq_factor": 4.0,
    "low_freq_factor": 1.0,
    "original_max_position_embeddings": 8192,
    "rope_type": "llama3",
    "type": "llama3"
  },
  "rope_theta": 12000000,
  "tie_word_embeddings": false,
  "transformers_version": "4.57.1",
  "use_cache": false,
  "vocab_size": 131072
}

```
## config.json (8B) max_position_embeddings
```
  "architectures": [
    "ApertusForCausalLM"
  "max_position_embeddings": 65536,
    "original_max_position_embeddings": 8192,
```
## generation_config.json (70B)
```
{
  "bos_token_id": 1,
  "do_sample": true,
  "eos_token_id": [
    2,
    68,
    72
  ],
  "pad_token_id": 3,
  "transformers_version": "4.57.1",
  "temperature": 0.7,
  "max_new_tokens": 8192
}

```
## Commit history of EPFLiGHT/Apertus-70B-MeditronFO main (HF API /commits/main, newest first, first 8)
- 2026-11-17T13:48:57.000Z Links: the Meditron site moved to meditron.light-laboratory.org (d13151ac)
- 2026-10-31T18:44:21.000Z README: link the Meditron website (d8e617cb)
- 2026-10-26T15:30:06.000Z README: usage example with the recommended sampling (temperature 0.7, max_new_tokens 8192) (a3b0a519)
- 2026-10-26T15:25:29.000Z generation_config: default temperature 0.7, max_new_tokens 8192 (57a8dae4)
- 2026-10-06T21:32:03.000Z Model card: ICLR results, training recipe and figure (b6213fa7)
- 2026-10-06T21:31:50.000Z Update weights to the ICLR run (meditronfo_gptoss_v1 corpus) (c65210bc)
- 2026-09-11T06:51:32.000Z Fix total_parameters in index metadata (was 1.34M, should be ~70B) (c1c0f119)
- 2026-09-10T19:47:51.000Z Retrained on the de-truncated corpus: fixes mid-answer truncation (6810a6d0)
- 2026-06-26T14:40:54.000Z Update model.safetensors.index.json (9d4a3413)
- 2026-06-26T14:31:21.000Z Update README.md (7b0daa49)
- 2026-06-26T08:43:45.000Z Update README.md (82f25fae)
- 2026-06-25T15:12:13.000Z Update README.md (81b6daeb)
- 2026-06-24T13:17:41.000Z Update README.md (96eed2dd)
- 2026-06-24T12:16:46.000Z Update README.md (079a9a66)
- 2026-05-28T11:57:00.000Z Add files using upload-large-folder tool (a424ad01)
- 2026-05-18T14:46:45.000Z Update model card with paper link and citation (352a4a26)
- 2026-05-18T14:44:10.000Z Update model card with paper link and citation (f4b8e564)
- 2026-05-18T14:20:54.000Z Fix total_parameters in index metadata (was 1.34M, should be ~70B) (9876f074)
- 2026-05-08T12:50:14.000Z Add model card (bce2b71a)
- 2026-05-08T12:46:38.000Z Add model card (2ea6940a)
- 2026-05-08T11:57:08.000Z Add files using upload-large-folder tool (eb8ca443)
- 2026-05-08T11:49:31.000Z initial commit (098641d6)

## Hugging Face organisation EPFLiGHT (HF API /api/organizations/EPFLiGHT/overview)
```
{"_id":"69f9ce161dd7d4b2840a55f3","fullname":"Laboratory for Intelligent Global Health & Humanitarian Response Technologies","name":"EPFLiGHT","isVerified":false,"isFollowing":false,"plan":"team","numUsers":2,"numModels":14,"numSpaces":1,"numDatasets":2,"numKernels":0,"numBuckets":0,"numPapers":1,"numFollowers":39}
```
OneHill note: `isVerified` is false, so the publishing organisation is not a verified organisation on Hugging Face. The organisation full name matches the EPFL LiGHT laboratory named on the card and on epfl.ch pages.


## File tree with LFS sha256 (HF API /api/models/<repo>/tree/main), first 3 weight shards of each repo plus all small files

### Apertus-70B-MeditronFO
- assets | size 0 | lfs sha256 -
- .gitattributes | size 1634 | lfs sha256 -
- README.md | size 7684 | lfs sha256 -
- chat_template.jinja | size 14601 | lfs sha256 -
- config.json | size 897 | lfs sha256 -
- generation_config.json | size 197 | lfs sha256 -
- model-00001-of-00030.safetensors | size 4865428944 | lfs sha256 29d3cefffb083625de57797a0245e563dbcade304c0bb4308365d9c83735219e
- model-00002-of-00030.safetensors | size 4429289408 | lfs sha256 aa0db83efdc889cb7dd83591d122cace7c6d96ee0dbd34424d24631dd1ad5f8a
- model-00003-of-00030.safetensors | size 4999714024 | lfs sha256 dcd1dcb4a57d6c4f433157f3a5ddeab2a85fde3e391fbe5fd2a93091711e45aa
- model.safetensors.index.json | size 90962 | lfs sha256 -
- special_tokens_map.json | size 565 | lfs sha256 -
- tokenizer.json | size 17078474 | lfs sha256 010095abf1dc6f52d4867584e7b3f0d4eece854593ae310220ec7782dd1b0a66
- tokenizer_config.json | size 177334 | lfs sha256 -
- (total safetensors shards: 30; every shard carries an LFS sha256 oid in the tree record; no other weight format, no .bin or .pt file)

### Apertus-8B-MeditronFO
- assets | size 0 | lfs sha256 -
- .gitattributes | size 1634 | lfs sha256 -
- README.md | size 7073 | lfs sha256 -
- chat_template.jinja | size 14601 | lfs sha256 -
- config.json | size 897 | lfs sha256 -
- generation_config.json | size 197 | lfs sha256 -
- model-00001-of-00004.safetensors | size 4999776656 | lfs sha256 7a28fe3d250f6291266c020472fd6f8a4837a56b587eb24b44cc0969b6cae1f2
- model-00002-of-00004.safetensors | size 4882374192 | lfs sha256 72dc53e22f3ca97fe7da6c6dbf51f836eb7bd569f9427b713e164e5fd9ab4436
- model-00003-of-00004.safetensors | size 4974647808 | lfs sha256 bfe3e6336485a1aa19cc6f361f2b49b93ae229ccd21fb63242672daeee815c66
- model.safetensors.index.json | size 36480 | lfs sha256 -
- special_tokens_map.json | size 565 | lfs sha256 -
- tokenizer.json | size 17078474 | lfs sha256 010095abf1dc6f52d4867584e7b3f0d4eece854593ae310220ec7782dd1b0a66
- tokenizer_config.json | size 177334 | lfs sha256 -
- (total safetensors shards: 4; every shard carries an LFS sha256 oid in the tree record; no other weight format, no .bin or .pt file)
