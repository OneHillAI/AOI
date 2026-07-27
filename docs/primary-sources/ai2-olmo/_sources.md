# ai2-olmo - primary-source clauses (2026-07-25)

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
model_card | https://huggingface.co/allenai/OLMo-2-1124-7B | 2026-07-25 | yes | true | Apache 2.0; OLMo 2 family
model_card | https://huggingface.co/models?search=allenai%20olmo-3 | 2026-07-25 | yes | true | search listing only; per-card details unverified
license | https://github.com/allenai/OLMo/blob/main/LICENSE | 2026-07-25 | yes | true | Apache 2.0
license | https://huggingface.co/datasets/allenai/dolma | 2026-07-25 | yes | true | ODC-BY; no ImpACT terms found in this fetch
technical_report | https://arxiv.org/abs/2501.00656 | 2026-07-25 | yes | true | "2 OLMo 2 Furious"
technical_report | https://arxiv.org/abs/2512.13961 | 2026-07-25 | yes | true | "Olmo 3"; abstract verbatim (recovered after allenai.org 429)
docs | https://github.com/allenai/OLMo | 2026-07-25 | yes | true | repo marked out-of-date/no longer active
```

## license Apache-2.0 (code + weights)
source_url: https://github.com/allenai/OLMo/blob/main/LICENSE | exists: yes | retrieved: true
[LICENSE header] "Apache License, Version 2.0, January 2004". Corroborated by OLMo-2-1124-7B card ("The code and model are released under Apache 2.0").

## license Dolma data (dataset)
source_url: https://huggingface.co/datasets/allenai/dolma | exists: yes | retrieved: true
[License] ODC-BY (Open Data Commons Attribution). [Source compliance] "you are also bound any license agreements and terms of use of the original data sources." [History] "transitioned to ODC-BY as of April 15, 2024."
NOTE: no ImpACT/medium-risk language found in this fetch.

## model_card OLMo 2 (1B/7B/13B/32B + instruct)
source_url: https://huggingface.co/allenai/OLMo-2-1124-7B | exists: yes | retrieved: true
[License] "The code and model are released under Apache 2.0." [Training data] Stage 1 OLMo-Mix-1124 (~3.9T); Stage 2 Dolmino-Mix-1124 (843B); cutoff Dec 2023.

## model_card OLMo 3 (7B/32B; Base/Think/Instruct/RL-Zero; +3.1)
source_url: https://huggingface.co/models?search=allenai%20olmo-3 | exists: yes | retrieved: true
[Repo slugs] Olmo-3-1025-7B, -7B-Instruct(-SFT/-DPO), -7B-Think(-SFT/-DPO), -7B-RL-Zero-{General,IF,Math,Code}, -1125-32B, -32B-Think(-SFT/-DPO), Olmo-3.1-32B-Think, -3.1-32B-Instruct-{SFT,DPO}. NOTE: from a search listing; per-card details unverified.

## technical_report OLMo 2
source_url: https://arxiv.org/abs/2501.00656 | exists: yes | retrieved: true
[Title] "2 OLMo 2 Furious" [Abstract] "...OLMo 2...dense autoregressive language models at 7B, 13B and 32B scales with fully released artifacts -- model weights, full training data, training code and recipes, training logs and thousands of intermediate checkpoints...Dolmino Mix 1124...OLMo 2-Instruct...RLVR...at the Pareto frontier..."

## technical_report OLMo 3
source_url: https://arxiv.org/abs/2512.13961 | exists: yes | retrieved: true
[Title] "Olmo 3" [Abstract, verbatim] "We introduce Olmo 3, a family of state-of-the-art, fully-open language models at the 7B and 32B parameter scales...This release includes the entire model flow...every stage, checkpoint, data point, and dependency...Our flagship model, Olmo 3 Think 32B, is the strongest fully-open thinking model released to-date."
[Blog] "Dolma 3" (~9.3T tokens) + "Dolci" post-training; "all the components of the Olmo 3 flow openly available-data, code, model weights, and checkpoints." NOTE: arXiv id recovered via search after allenai.org 429.

## docs GitHub README
source_url: https://github.com/allenai/OLMo | exists: yes | retrieved: true
[Status] "This repository is out of date...no longer active." [Released] weights OLMo-2 1B/7B/13B/32B + instruct; both-stage checkpoints; training data + code + W&B logs. [License] Apache-2.0.
