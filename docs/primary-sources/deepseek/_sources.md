# deepseek - primary-source clauses (2026-07-25)

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/deepseek-ai/DeepSeek-R1 (+/raw/main/LICENSE) | 2026-07-25 | yes | true | MIT for R1 code+weights; distills carry base-model licenses
license | https://github.com/deepseek-ai/DeepSeek-V3 (LICENSE-CODE / LICENSE-MODEL) | 2026-07-25 | yes | true | Code=MIT; Weights="DeepSeek License Agreement" v1.0 (NOT MIT). HF root /raw/main/LICENSE 404s
technical_report | https://arxiv.org/abs/2501.12948 | 2026-07-25 | yes | true | R1 report
technical_report | https://arxiv.org/abs/2412.19437 | 2026-07-25 | yes | true | V3 report
privacy_policy | https://chat.deepseek.com/downloads/DeepSeek%20Privacy%20Policy.html | 2026-07-25 | yes | true | China data storage; deepseek.com/privacy-policy 404'd, used downloads mirror
terms | https://chat.deepseek.com/downloads/DeepSeek%20Terms%20of%20Use.html | 2026-07-25 | yes | true | PRC governing law; venue discrepancy flagged
```

## license DeepSeek-R1
source_url: https://huggingface.co/deepseek-ai/DeepSeek-R1 | exists: yes | retrieved: true
[Model card] "This code repository and the model weights are licensed under the MIT License. DeepSeek-R1 series support commercial use, allow for any modifications and derivative works, including...distillation for training other LLMs." [LICENSE] "Copyright (c) 2023 DeepSeek"; standard MIT + AS IS.
NOTE (per-checkpoint): main R1 weights are MIT; distilled variants carry base license (Qwen distills = Apache-2.0; Llama-8B = Llama 3.1; Llama-70B = Llama 3.3) - verify each distill card.

## license DeepSeek-V3 (CODE vs WEIGHTS split)
source_url: github.com/deepseek-ai/DeepSeek-V3 LICENSE-CODE / LICENSE-MODEL | exists: yes | retrieved: true
[Model card] "This code repository is licensed under the MIT License. The use of DeepSeek-V3 Base/Chat models is subject to the Model License."
[Weights = "DeepSeek License Agreement, Version 1.0" - NOT MIT] Grant: "a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license"; patent license terminates on patent litigation against DeepSeek. Use restrictions (Section 5 & Attachment A) prohibit: use violating "any applicable national or international law"; military applications; harm to minors; generating "verifiably false information and/or content with the purpose of harming others"; unauthorized distribution of PII; defamation/harassment; discrimination; automated decisions affecting legal rights. Output ownership: "DeepSeek claims no rights in the Output You generate." Provided "AS IS."
[Code = MIT] "Copyright (c) 2023 DeepSeek."
IMPORTANT: V3 weights are NOT MIT (differs from R1) - code is MIT but weights are governed by the separate "DeepSeek License Agreement" with the above use restrictions.

## technical_report R1
source_url: https://arxiv.org/abs/2501.12948 | exists: yes | retrieved: true
[Title] "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" - reasoning incentivized via pure RL, no human-labeled reasoning trajectories; distilled into smaller models.

## technical_report V3
source_url: https://arxiv.org/abs/2412.19437 | exists: yes | retrieved: true
[Title] "DeepSeek-V3 Technical Report" - MoE 671B total / 37B active; MLA + DeepSeekMoE; auxiliary-loss-free load balancing; 14.8T tokens; 2.788M H800 GPU-hours.

## privacy_policy (hosted service)
source_url: https://chat.deepseek.com/downloads/DeepSeek%20Privacy%20Policy.html | exists: yes | retrieved: true
[Retention] "as long as necessary to provide our Services..." [China storage - VERBATIM] "We store the information we collect in secure servers located in the People's Republic of China." [AI training] not addressed in retrieved text.

## terms (hosted service)
source_url: https://chat.deepseek.com/downloads/DeepSeek%20Terms%20of%20Use.html | exists: yes | retrieved: true
[9.1 Governing Law] "governed by the laws of the People's Republic of China in the mainland." Negotiation then PRC-court litigation; no arbitration. (Hangzhou/Haidian venue discrepancy flagged.)
