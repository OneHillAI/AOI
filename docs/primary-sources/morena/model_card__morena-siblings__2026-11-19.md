doc_type: model_card
entity: morena
variant/applies-to: sibling repos in the MORENA family: morena-0.5b-mini, morena-0.2b-nano, morena-1.5b-instruct-gguf (cards read); morena-0.5b-mini-instruct (API card data only)
source_url: https://huggingface.co/vamboai/morena-0.5b-mini ; https://huggingface.co/vamboai/morena-0.2b-nano ; https://huggingface.co/vamboai/morena-1.5b-instruct-gguf ; https://huggingface.co/api/models/vamboai/morena-0.5b-mini-instruct
retrieval_date: 2026-11-19
exists: yes
retrieved: true (cards read; the mini-instruct README was not read, only its API metadata)

## Governing statements (verbatim)

[Licence on every sibling read] "license: apache-2.0" in the front matter of morena-0.5b-mini, morena-0.2b-nano, morena-1.5b-instruct-gguf and (API cardData) morena-0.5b-mini-instruct. Each card ends: "Apache 2.0. Commercial use is permitted, including fine-tuning and redistributing derivatives, under the terms of the licence. The training corpus is not released with these weights." No sibling diverges on licence.

[mini] tags include "from-scratch, distilled, pruned"; "A 503M-parameter model cut from MORENA 1.5B base in one pruning pass (28 layers to 16, channels ...". "Not a chat model." "It has not been safety-tested or put in front of a person." base_model: vamboai/morena-1.5b-base.

[nano] "built not as an assistant but as a cheap trunk for ASR rescoring, on-device keyboards and text normalisation in twelve African languages. Not a chat model, has no instruct version, not safety-tested."

[GGUF] "GGUF conversion of `vamboai/morena-1.5b-instruct`, verified for logit equivalence against the safetensors weights. **Read that model card first**; everything in it, including the release status and the safety notes, applies unchanged." Files Q4_K_M 0.92 GB, Q8_0 1.58 GB, f16 2.97 GB. llama.cpp prompt example: `llama-completion -m morena-1.5b-instruct-f16.gguf -p "<reserved_0>\nNdeipi guta guru reZimbabwe?\n<reserved_1>\n" -e -n 64 --temp 0`.
