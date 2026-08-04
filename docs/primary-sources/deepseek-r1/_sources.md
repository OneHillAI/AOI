# deepseek-r1 - primary-source clauses (2026-08-03)

Split from the aggregate `deepseek` primary-sources. This entry is the pure-MIT reasoning
line (R1, R1-0528). The R1 licence clauses below are carried verbatim from the aggregate
`deepseek/_sources.md` (retrieved 2026-07-25); the split adds nothing new to the R1 reading,
it isolates it.

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/deepseek-ai/DeepSeek-R1 (+/raw/main/LICENSE) | 2026-07-25 | yes | true | MIT for R1 code+weights; commercial + distillation permitted
technical_report | https://arxiv.org/abs/2501.12948 | 2026-07-25 | yes | true | R1 report (pure-RL reasoning)
```

## license DeepSeek-R1
source_url: https://huggingface.co/deepseek-ai/DeepSeek-R1 | exists: yes | retrieved: true
[Model card] "This code repository and the model weights are licensed under the MIT License. DeepSeek-R1 series support commercial use, allow for any modifications and derivative works, including...distillation for training other LLMs." [LICENSE] "Copyright (c) 2023 DeepSeek"; standard MIT + AS IS.
NOTE (per-checkpoint boundary): the main R1 weights are MIT. The **distilled** variants are separate entries and carry their base licence (Qwen distils = Apache-2.0 -> `deepseek-r1-distill-qwen`; Llama-8B = Llama 3.1, Llama-70B = Llama 3.3 -> `deepseek-r1-distill-llama`). DeepSeek-V3 original weights are the custom DeepSeek License Agreement, not MIT -> `deepseek-v3-original`; V3-0324/V3.1 moved to MIT -> `deepseek-v3-mit`.

## technical_report R1
source_url: https://arxiv.org/abs/2501.12948 | exists: yes | retrieved: true
[Title] "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" - reasoning incentivized via pure RL, no human-labeled reasoning trajectories; distilled into smaller models.

## hosted-service note (not this entry)
The DeepSeek hosted app/API privacy + PRC-governing-law terms (China data storage) documented in the aggregate `deepseek/_sources.md` concern the *hosted service*, not the self-hosted open weights this entry scores. Self-hosting the safetensors sidesteps them.
