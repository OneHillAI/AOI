# deepseek-v3-original - primary-source clauses (2026-08-03)

Split from the aggregate `deepseek` primary-sources on the LICENCE axis. This entry is the
original December-2024 DeepSeek-V3, whose *weights* are the custom DeepSeek License Agreement
v1.0 (NOT MIT). Clauses carried verbatim from the aggregate `deepseek/_sources.md` (retrieved
2026-07-25).

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://github.com/deepseek-ai/DeepSeek-V3 (LICENSE-CODE / LICENSE-MODEL) | 2026-07-25 | yes | true | Code=MIT; Weights="DeepSeek License Agreement" v1.0 (NOT MIT), RAIL-style use restrictions
technical_report | https://arxiv.org/abs/2412.19437 | 2026-07-25 | yes | true | V3 report
```

## license DeepSeek-V3 (CODE vs WEIGHTS split) - VERBATIM
source_url: github.com/deepseek-ai/DeepSeek-V3 LICENSE-CODE / LICENSE-MODEL | exists: yes | retrieved: true
[Model card] "This code repository is licensed under the MIT License. The use of DeepSeek-V3 Base/Chat models is subject to the Model License."
[Weights = "DeepSeek License Agreement, Version 1.0" - NOT MIT] Grant: "a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license"; patent license terminates on patent litigation against DeepSeek. Use restrictions (Section 5 & Attachment A) prohibit: use violating "any applicable national or international law"; military applications; harm to minors; generating "verifiably false information and/or content with the purpose of harming others"; unauthorized distribution of PII; defamation/harassment; discrimination; automated decisions affecting legal rights. Output ownership: "DeepSeek claims no rights in the Output You generate." Provided "AS IS."
[Code = MIT] "Copyright (c) 2023 DeepSeek."
IMPORTANT: V3 (original) weights are NOT MIT (differs from R1 and from the later V3-0324/V3.1). Code is MIT but weights are governed by the separate "DeepSeek License Agreement" with the above use restrictions. The later V3-0324/V3.1 generations moved the weights to MIT -> deepseek-v3-mit.

## technical_report V3
source_url: https://arxiv.org/abs/2412.19437 | exists: yes | retrieved: true
[Title] "DeepSeek-V3 Technical Report" - MoE 671B total / 37B active; MLA + DeepSeekMoE; auxiliary-loss-free load balancing; 14.8T tokens; 2.788M H800 GPU-hours.

## hosted-service note (not this entry)
The DeepSeek hosted app/API privacy + PRC-governing-law terms concern the *hosted service*, not the self-hosted open weights this entry scores. Self-hosting the safetensors sidesteps them.
