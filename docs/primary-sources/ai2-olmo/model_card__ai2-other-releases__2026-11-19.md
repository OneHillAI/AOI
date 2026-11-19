# Ai2 Hugging Face org: releases after the 2026-07-25 grounding, listed 2026-11-19

- **doc_type:** model_card
- **source_url:** https://huggingface.co/api/models?author=allenai&sort=createdAt&direction=-1 ; https://huggingface.co/allenai
- **retrieval_date:** 2026-11-19
- **exists:** yes
- **retrieved:** true

The HF API listing (createdAt order, 100 newest repos) and a second listing by lastModified were read, then the
licence tag and, for the families below, the card licence line. None is gated (`gated: False` for all).
These are reported, not folded into the tracked entry.

| family or repo | created | licence as read | note |
| --- | --- | --- | --- |
| Olmo-3-1025-7B, Olmo-3-1125-32B, Think, Instruct, RL-Zero | 2025-09 to 2025-12 | Apache-2.0 | already named in the tracked entry; see model_card__olmo-3-family |
| Olmo-3.1-32B-Think, -Instruct, 7B RL-Zero Math and Code | 2025-12-10 | Apache-2.0 | same generation, longer RL |
| Olmo-Hybrid-7B and Instruct/Think SFT and DPO | 2026-01-28 to 2026-03-05 | Apache-2.0 | 7B hybrid RNN-transformer, 5.50T tokens, checkpoints released, logs "coming soon" |
| OlmoEarth v1, v1_1, v1_2, v1_3-Base, FT-LFMC-Base | 2025-10-23 to 2026-10-23 | OlmoEarth Artifact License (hub tag other) | use restrictions, see license__olmoearth-artifact-license |
| EMO index repo and Emo_1b14b_1T and StdMoE baselines | 2026-04-29 to 2026-05-08 | index repo tag other (no weights), checkpoints Apache-2.0 | 1B active / 14B total MoE, trust_remote_code |
| Bolmo-1B, Bolmo-7B, Bwen-8B, Llama-3-Blama-8B | 2025-12 to 2026-08-26 | Apache-2.0; Blama is llama3 | byte-level and adapted models; Blama inherits the Llama 3 licence |
| BAR-7B, BAR-2x7B family | 2026-04-19 | Apache-2.0 | mixture-of-experts-from-experts research models |
| SERA-8B, SERA-32B | 2026-01-27 | Apache-2.0 | coding agents; card allows commercial use "in accordance with" Responsible Use Guidelines |
| tmax-2b to tmax-27b, qwen35-9b-* | 2026-06-17 to 2026-06-21 | Apache-2.0 | fine-tunes of third-party bases |
| AstaBrief_8B, AstaBrief_8B_SFT | 2026-02-09, 2026-09-10 | Apache-2.0 | based on Qwen 3-8B |
| HiRO-ACEv2 | 2026-10-12 | Apache-2.0 | climate emulator |
| Molmo2-4B-tb, maniflow-tb | 2026-11-05 | Apache-2.0 | newest repos at the read date |
| ACE2, SamudrACE, MolmoAct2, MolmoMotion | 2026-05 to 2026-09 | Apache-2.0 or untagged | science and robotics |

Nothing named Olmo 4 or Olmo 3.5 exists in the allenai model listing at the read date. Two tokenizer repos
(`olmo-3.2-tokenizer-think-release`, 2025-11-03; `olmo-3-tokenizer-instruct-release`, 2026-02-19) and the dataset
`allenai/dolma3.5_pool` (2026-03-25, odc-by) exist, which suggests unreleased work, but no model uses them yet.
