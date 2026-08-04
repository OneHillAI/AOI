# deepseek-v3-mit - primary-source clauses (2026-08-03)

Split from the aggregate `deepseek` primary-sources. This entry is the MIT-licensed V3 line
(V3-0324, V3.1). The licence-boundary clauses below are carried from the aggregate
`deepseek/_sources.md` (retrieved 2026-07-25); the split isolates the MIT V3 generations from
the original December-2024 V3 weights (custom DeepSeek License Agreement -> deepseek-v3-original).

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/deepseek-ai/DeepSeek-V3-0324 | 2026-08-03 | yes | true | V3-0324/V3.1 weights = MIT (a change from the original V3 weights)
license | https://github.com/deepseek-ai/DeepSeek-V3 (LICENSE-CODE / LICENSE-MODEL) | 2026-07-25 | yes | true | ORIGINAL V3: Code=MIT; Weights="DeepSeek License Agreement" v1.0 (NOT MIT) -> deepseek-v3-original
technical_report | https://arxiv.org/abs/2412.19437 | 2026-07-25 | yes | true | V3 report
```

## license DeepSeek-V3-0324 / V3.1 (MIT)
source_url: https://huggingface.co/deepseek-ai/DeepSeek-V3-0324 | exists: yes | retrieved: true
[Model card] The V3-0324 refresh and the later V3.1 generation license both the code repository AND the model weights under the MIT License. This is the material change from the original December-2024 DeepSeek-V3, whose weights are the custom "DeepSeek License Agreement, Version 1.0" (see below / deepseek-v3-original). MIT: commercial use, any modification, no field-of-use restriction; AS IS.

## license boundary - ORIGINAL DeepSeek-V3 (NOT this entry)
source_url: github.com/deepseek-ai/DeepSeek-V3 LICENSE-CODE / LICENSE-MODEL | exists: yes | retrieved: true
[Original V3 model card] "This code repository is licensed under the MIT License. The use of DeepSeek-V3 Base/Chat models is subject to the Model License." [Weights = "DeepSeek License Agreement, Version 1.0" - NOT MIT], with RAIL-style use restrictions. Recorded here only to mark the boundary: the original V3 weights are the `deepseek-v3-original` entry, not this one.

## technical_report V3
source_url: https://arxiv.org/abs/2412.19437 | exists: yes | retrieved: true
[Title] "DeepSeek-V3 Technical Report" - MoE 671B total / 37B active; MLA + DeepSeekMoE; auxiliary-loss-free load balancing; 14.8T tokens; 2.788M H800 GPU-hours.

## hosted-service note (not this entry)
The DeepSeek hosted app/API privacy + PRC-governing-law terms concern the *hosted service*, not the self-hosted open weights this entry scores. Self-hosting the safetensors sidesteps them.
