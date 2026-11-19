# Hugging Face malware scan, safetensors metadata, checksums and repository activity for google/gemma-4-31B-it

source_url: https://huggingface.co/api/models/google/gemma-4-31B-it/scan
retrieval_date: 2026-11-19
doc_type: third_party
retrieved: true
note: Platform-generated data (Hugging Face), not publisher prose.


Method: anonymous HF API calls on 2026-11-19.

- https://huggingface.co/api/models/google/gemma-4-31B-it/scan returned `{"scansDone":true,"filesWithIssues":[]}`.
- https://huggingface.co/api/models/google/gemma-4-31B-it?expand[]=safetensors returned `"safetensors":{"parameters":{"BF16":31273088876},"total":31273088876}` and `"gated":false`. Repository head sha 842da3794eaa0b77d5f08bae87a17459d91ff475 (lastModified 2026-07-20T16:42:18Z); the repository file list has only .safetensors weights, no pickle or .bin files (see docs__hf-api-checkpoint-inventory).
- Tree API (https://huggingface.co/api/models/google/gemma-4-31B-it/tree/main) lists an LFS sha256 for each weight shard, for example `model-00001-of-00002.safetensors` size 49784788364 lfs oid eeef8791537bc04f110967c513149e037d2a9ae97d49add7291ebfa62806bbfa and `model-00002-of-00002.safetensors` size 12761549884 lfs oid 018912220f559f7025d60333e0996183cd538aa77ad6f4988a89ce47be681f10.
- Commit history for the repository (API commits/main) shows maintained updates after release, including "fix: chat template - null handling, reasoning preservation, turn-tag balance, input validation" and "Add response_template to tokenizer_config.json" (2026-07-15 and 2026-07-20). Earlier commits in the same history: 2026-04-10 "fix: prefix-preserving tool calls + dialog compliance", 2026-04-28 "fix(chat_template): update SI and tool call handling", 2026-05-18 "fix(chat_template): Emit multimodal placeholders in tool response content-parts", 2026-07-10 "Add Technical Report".
- Open community discussion on the repository (API discussions): for example discussion 156, status open, created 2026-11-18, titled "Chat template: an image-only tool result renders its placeholder after the tool block closes".
- Not found: any cryptographic model signature (no .sig, sigstore bundle or model-signing manifest in any Gemma 4 repository file list) and any SLSA or build-provenance attestation. Absence in the file lists read; Google may sign elsewhere (Kaggle) and that was not checked.
