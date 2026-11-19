# Ai2 OLMo 3 family - model cards, licence tags and released components, read 2026-11-19

- **doc_type:** model_card
- **source_url:** https://huggingface.co/allenai/Olmo-3-1025-7B ; https://huggingface.co/allenai/Olmo-3-1125-32B ; https://huggingface.co/allenai/Olmo-3-7B-Instruct ; https://huggingface.co/allenai/Olmo-3.1-32B-Think ; https://huggingface.co/allenai/Olmo-Hybrid-7B
- **retrieval_date:** 2026-11-19
- **exists:** yes
- **retrieved:** true

## Governing text (verbatim, raw README of each card)

Olmo-3-1025-7B and Olmo-3-1125-32B (base):

> - **License:** The code and model are released under Apache 2.0.
> ## License
> This model is licensed under Apache 2.0. It is intended for research and educational use in accordance with [Ai2's Responsible Use Guidelines](https://allenai.org/responsible-use).

Olmo-3-7B-Instruct, Olmo-3.1-32B-Think and Olmo-Hybrid-7B:

> - **License:** This model is licensed under Apache 2.0. It is intended for research and educational use in accordance with Ai2's [Responsible Use Guidelines](https://allenai.org/responsible-use).

The OLMo 2 base cards (OLMo-2-1124-7B, OLMo-2-0325-32B, OLMo-2-0425-1B) read "The code and model are released under
Apache 2.0." with no Responsible Use reference. The OLMo-2-1124-13B-Instruct card says "OLMo 2 is licensed under
the Apache 2.0 license. For more information, please see our Responsible Use Guidelines". The Responsible Use
reference is therefore present on the tracked OLMo 2 Instruct line as well as on every OLMo 3 card read.

## Hugging Face API (same day)

| repo | gated | licence tag | created | last modified |
| --- | --- | --- | --- | --- |
| allenai/Olmo-3-1025-7B | False | apache-2.0 | 2025-09-12 | 2026-04-21 |
| allenai/Olmo-3-1125-32B | False | apache-2.0 | 2025-11-04 | 2025-12-03 |
| allenai/Olmo-3-7B-Instruct | False | apache-2.0 | 2025-11-19 | 2026-06-25 |
| allenai/Olmo-3-7B-Think, Olmo-3-32B-Think | False | apache-2.0 | 2025-11 | 2026-06-25 |
| allenai/Olmo-3.1-32B-Think | False | apache-2.0 | 2025-12-10 | 2026-10-13 |
| allenai/Olmo-3.1-32B-Instruct | False | apache-2.0 | 2025-12-10 | 2026-01-05 |
| allenai/Olmo-Hybrid-7B | False | apache-2.0 | 2026-01-28 | 2026-05-26 |

Context length from config.json: OLMo 2 (1B, 7B, 13B, 32B) 4096; OLMo 3 (7B, 32B, Think) 65536. The OLMo 3 card
table gives 5.93T tokens (7B) and 5.50T tokens (32B), layers 32 and 64.

## Components released (as read)

| component | what is released | licence as read |
| --- | --- | --- |
| weights | Base, SFT, DPO and final RLVR stages for Think (7B, 32B) and Instruct (7B; 3.1 adds 32B), RL-Zero (Code, Math, IF, General, Mix) | Apache-2.0 (HF tag and card) |
| intermediate checkpoints | HF revisions: Olmo-3-1025-7B 1,487 branches (stage1/stage2/stage3), Olmo-3-1125-32B 719, Olmo-3-7B-Think 56 RL steps, Olmo-3.1-32B-Think 47 | same repo licence |
| pre-training data | Dolma 3 (about 9.3T-token pool, ~6T mix, Dolmino 100B, Longmino 50B) | ODC-By v1.0 |
| post-training data | Dolci SFT, DPO and RL suites | mostly ODC-By; Dolci-Instruct-SFT-Tool-Use-SA is cc-by-sa-4.0 |
| training code | OLMo-core (github.com/allenai/OLMo-core), open-instruct | Apache-2.0 (raw LICENSE read) |
| evaluation | OLMES and OLMo-Eval, OlmoBaseEval | Apache-2.0 (raw LICENSE read) |
| data tooling | dolma, datamap-rs, duplodocus, decon, olmo-cookbook | Apache-2.0 (raw LICENSE read) |
| logs | W&B report links on the 7B and 32B cards; the card lines for pretraining and annealing W&B logs are commented out; the Hybrid card says logs are "coming soon" | not stated |

The Olmo 3 technical report (arXiv 2512.13961, abstract read) says the release "includes the entire model flow,
i.e., the full lifecycle of the family of models, including every stage, checkpoint, data point, and dependency
used to build it."

## Marketing against binding text

The Ai2 Olmo 3 blog (allenai.org/blog/olmo3) says Ai2 is "making every training and fine-tuning dataset available
for download without any license restrictions". The dataset cards read ODC-By v1.0 (attribution required), one
Dolci subset is CC-BY-SA-4.0 (share-alike), and the cards add "intended for research and educational use in
accordance with Ai2's Responsible Use Guidelines". The Dolci-Think-SFT card says new reasoning traces were
generated with DeepSeek R1 and R1-0528 and that some prompts were filtered by "blocked requests" at the Azure API.
"Without any license restrictions" is therefore marketing wording, not the binding text.
