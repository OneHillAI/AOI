# deepseek-r1-distill-qwen - primary-source clauses (2026-08-03)

Split from the aggregate `deepseek` primary-sources on the LICENCE axis. These are the
R1-Distill checkpoints on Qwen2.5 bases, released under DeepSeek's MIT licence. The Qwen2.5 bases are
Apache-2.0 per their cards. Licence-boundary note carried from the aggregate `deepseek/_sources.md`
(retrieved 2026-07-25).

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B | 2026-08-03 | yes | true | DeepSeek's MIT licence applies to the distils; the Qwen2.5 bases are Apache-2.0
technical_report | https://arxiv.org/abs/2501.12948 | 2026-07-25 | yes | true | R1 report (distillation section)
```

## license R1-Distill-Qwen (MIT, over Apache-2.0 bases)
source_url: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B | exists: yes | retrieved: true
[R1 README / distil cards] The Qwen distils (1.5B/7B/14B/32B) are "derived from ... Qwen-2.5 series, which are originally licensed under Apache 2.0 License." The repositories carry DeepSeek's MIT licence (LICENSE file and card metadata `license: mit`). MIT is OSI-approved and permissive with no field-of-use restriction, and has no express patent grant.
NOTE (per-checkpoint boundary): the Llama-base distils (Llama-8B = Llama 3.1, Llama-70B = Llama 3.3) carry the Llama Community Licence -> deepseek-r1-distill-llama. The full R1 weights are MIT -> deepseek-r1.

## technical_report R1 (distillation)
source_url: https://arxiv.org/abs/2501.12948 | exists: yes | retrieved: true
[Title] "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" - R1's reasoning distilled into smaller dense models (Qwen and Llama bases); the distils are strong-for-size reasoning models.

## EU note
The distils are small (1.5B-32B), well below the systemic-risk threshold. The MIT licence is free and open-source, so the Article 53 open-source exemption applies to the transparency duties; no DeepSeek copyright policy / training-content summary is published (obligations that survive the exemption).

## Refresh 2026-11-19
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B/raw/main/LICENSE + README.md | 2026-11-19 | yes | true | MIT on the DeepSeek repos; base-licence statement in card section 7 unchanged
license | https://huggingface.co/Qwen/Qwen2.5-32B/raw/main/LICENSE (+ 14B, Math-1.5B, Math-7B) | 2026-11-19 | yes | true | base licence terms re-read; see license__base-licences__2026-11-19.md
```
