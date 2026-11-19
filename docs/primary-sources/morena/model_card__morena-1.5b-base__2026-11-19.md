doc_type: model_card
entity: morena
variant/applies-to: vamboai/morena-1.5b-base (base checkpoint, exists beside the instruct one)
source_url: https://huggingface.co/vamboai/morena-1.5b-base (raw: https://huggingface.co/vamboai/morena-1.5b-base/raw/main/README.md)
repo_sha_read: 52276f457fb74a545ffc47dd5c6f928c892a10b7 (created 2026-09-15, last modified 2026-10-14)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Governing clauses (verbatim extracts, README.md read in full)

[Front matter] "license: apache-2.0" ; "tags: [african-languages, from-scratch, base-model, isheanesu-misi, vambo-ai]" ; "inference: false". Datasets list is the pretraining set only (no vamboai/fikira, no vamboai/morena-sft-corpus). Repo files (API tree): .gitattributes, README.md, SHA256SUMS, config.json, load_example.py, model.safetensors, modeling_morena.py, poster.png, tokenizer.json, tokenizer_config.json. No LICENSE file. Not gated. 1,484,900,352 BF16 parameters.

[From scratch - PUBLISHER CLAIM] "The pretrained and mid-trained base model of the MORENA family: a 1.5B-parameter decoder trained from scratch on 251.7B tokens for twelve Latin-script African languages plus English, French and code, then annealed for 63B tokens on higher-quality and task data. **This is not a chat model.** It is the recommended starting point for fine-tuning, continued pretraining and domain adaptation in these languages."

[Safety] "No safety evaluation applies to this checkpoint; it has not been instruction-tuned."

[Benchmarks] "ARC-easy / ARC-challenge (English, zero-shot cloze, 250 items each) 0.676 / 0.412" ; "MMLU 0.284 ... close to the 0.25 floor, factual knowledge was traded away deliberately" ; African bits per byte "1.408, lowest of 26 models measured".

[Compute] "12,661 A100 GPU-hours (about 20% useful utilisation across the whole run, 28 to 33% in steady state during pretraining)".

[Licence section] "Apache 2.0. Commercial use is permitted, including fine-tuning and redistributing derivatives, under the terms of the licence. The training corpus is not released with these weights."

[Probe] https://huggingface.co/vamboai/morena-1.5b-base/raw/main/LICENSE returned HTTP 404 ("Entry not found") on 2026-11-19.
