# deepseek-r1-distill-qwen - primary-source clauses (2026-08-03)

Split from the aggregate `deepseek` primary-sources on the LICENCE axis. These are the
R1-Distill checkpoints on Apache-2.0 Qwen2.5 bases. Licence-boundary note carried from the
aggregate `deepseek/_sources.md` (retrieved 2026-07-25).

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B | 2026-08-03 | yes | true | Distils inherit the Qwen2.5 base licence = Apache-2.0
technical_report | https://arxiv.org/abs/2501.12948 | 2026-07-25 | yes | true | R1 report (distillation section)
```

## license R1-Distill-Qwen (inherits Apache-2.0)
source_url: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B | exists: yes | retrieved: true
[R1 README / distil cards] The distilled variants carry the licence of their base model. The Qwen distils (1.5B/7B/14B/32B) are "derived from ... Qwen-2.5 series, which are originally licensed under Apache 2.0 License." Apache-2.0: OSI-approved, permissive, explicit patent grant, no field-of-use restriction.
NOTE (per-checkpoint boundary): the Llama-base distils (Llama-8B = Llama 3.1, Llama-70B = Llama 3.3) carry the Llama Community Licence, NOT Apache-2.0 -> deepseek-r1-distill-llama. The full R1 weights are MIT -> deepseek-r1.

## technical_report R1 (distillation)
source_url: https://arxiv.org/abs/2501.12948 | exists: yes | retrieved: true
[Title] "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" - R1's reasoning distilled into smaller dense models (Qwen and Llama bases); the distils are strong-for-size reasoning models.

## EU note
The distils are small (1.5B-32B), well below the systemic-risk threshold. Apache-2.0 is FOSS, so the Article 53 open-source exemption applies to the transparency duties; no DeepSeek copyright policy / training-content summary is published (obligations that survive the exemption).
