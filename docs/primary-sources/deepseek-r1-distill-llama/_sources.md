# deepseek-r1-distill-llama - primary-source clauses (2026-08-03)

Split from the aggregate `deepseek` primary-sources on the LICENCE axis. These are the
R1-Distill checkpoints on Meta Llama bases (8B on Llama 3.1, 70B on Llama 3.3), carrying the
Llama Community Licence. Licence-boundary note carried from the aggregate `deepseek/_sources.md`
(retrieved 2026-07-25).

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B | 2026-08-03 | yes | true | Distils inherit the Llama base licence: 8B=Llama 3.1, 70B=Llama 3.3 Community Licence
technical_report | https://arxiv.org/abs/2501.12948 | 2026-07-25 | yes | true | R1 report (distillation section)
```

## license R1-Distill-Llama (inherits Llama Community Licence)
source_url: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B | exists: yes | retrieved: true
[R1 README / distil cards] The distilled variants carry the licence of their base model. The Llama distils are: Llama-8B on Llama 3.1, Llama-70B on Llama 3.3 - both the Llama Community Licence (non-OSI). Key terms: Acceptable Use Policy (RAIL-style field-of-use restrictions); the "700 million monthly active users" clause (a separate Meta licence required if the products exceed that threshold); "Built with Llama" attribution and the requirement that derivative model names include "Llama"; the licence + AUP must accompany redistribution.
NOTE (per-checkpoint boundary): the Qwen-base distils (1.5B/7B/14B/32B) carry Apache-2.0, NOT the Llama licence -> deepseek-r1-distill-qwen. The full R1 weights are MIT -> deepseek-r1.

## technical_report R1 (distillation)
source_url: https://arxiv.org/abs/2501.12948 | exists: yes | retrieved: true
[Title] "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" - R1's reasoning distilled into smaller dense models (Qwen and Llama bases); the distils are strong-for-size reasoning models.

## EU note
The distils are small (8B-70B), below the systemic-risk threshold. The Llama Community Licence is NOT FOSS, so the Article 53 open-source exemption does not apply on the licence axis; no DeepSeek copyright policy / training-content summary is published, and Meta's AUP + 700M-MAU clause bind downstream.
