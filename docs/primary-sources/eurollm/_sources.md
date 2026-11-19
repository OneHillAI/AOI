# eurollm - primary-source clauses (2026-07-25)

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/utter-project/EuroLLM-9B-Instruct | 2026-07-25 | yes | true | apache-2.0 (9B, 1.7B, 22B-2512)
technical_report | https://arxiv.org/abs/2506.04079 | 2026-07-25 | yes | true | EuroLLM-9B Technical Report
model_card | https://huggingface.co/utter-project/EuroLLM-9B-Instruct | 2026-07-25 | yes | true | -
model_card | https://huggingface.co/utter-project/EuroLLM-1.7B-Instruct | 2026-07-25 | yes | true | -
docs | https://huggingface.co/utter-project/EuroLLM-22B-Instruct-2512 | 2026-07-25 | yes | true | openness PARTIAL: weights + SFT dataset (EuroBlocks-SFT-2512) released; full pretraining corpus not released as one dataset
```

## license - Apache-2.0
source_url: huggingface.co/utter-project/EuroLLM-9B-Instruct ; EuroLLM-1.7B-Instruct | exists: yes | retrieved: true
9B, 1.7B, and 22B-Instruct-2512 all Apache-2.0. Not preference-aligned (may hallucinate/produce harmful content).

## technical_report
source_url: https://arxiv.org/abs/2506.04079 | exists: yes | retrieved: true
[Title] "EuroLLM-9B: Technical Report" - trained from scratch, all 24 EU official languages + 11 more; "Open release: Public availability of models, filters, and datasets."

## model_card 9B / 1.7B
source_url: huggingface.co/utter-project/EuroLLM-9B-Instruct ; -1.7B-Instruct | exists: yes | retrieved: true
9B: 4T tokens; EuroBlocks instruct data; comparable to Gemma-2-9B (EU) / Mistral-7B (English). 1.7B: 1.7B params, 4,096 ctx, 35 languages; comparable to Gemma-7B on MT benchmarks.

## docs - openness (22B-Instruct-2512)
source_url: huggingface.co/utter-project/EuroLLM-22B-Instruct-2512 | exists: yes | retrieved: true
[Released dataset - CONFIRMED] links "EuroBlocks-SFT-2512" (utter-project/EuroBlocks-SFT-2512). [Pretraining corpus - NOT fully released] ~4T tokens described (web, parallel, Wikipedia, Arxiv, books, math, code, Apollo) but not released as one dataset. POSITION: partial openness - stronger than weights-only, weaker than fully-open (cf. OLMo/Soofi).

## Refresh 2026-11-19
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/api/models/utter-project/EuroLLM-9B-Instruct (+ rendered page, 1.7B raw card) | 2026-11-19 | yes | true | apache-2.0 unchanged; no LICENSE file in repos; 9B repos gated:auto (contact sharing), 1.7B ungated; see license__eurollm-hf-licence-and-gating__2026-11-19.md
model_card | https://huggingface.co/utter-project/EuroLLM-22B-2512 | 2026-11-19 | yes | true | NEW sibling, apache-2.0, ungated, 32k context; see model_card__eurollm-22b-2512__2026-11-19.md
technical_report | https://arxiv.org/abs/2602.05879 | 2026-11-19 | yes | true | EuroLLM-22B report; releases web pretraining data and pretraining and eval code; see technical_report__eurollm-22b__2026-11-19.md
technical_report | https://arxiv.org/abs/2506.04079 | 2026-11-19 | yes | true | 9B report abstract re-read (API); release of models, EuroFilter, synthetic post-training set
docs | https://huggingface.co/utter-project/EuroLLM-22B-2512/blob/main/EuroLLM_Public_Summary.pdf | 2026-11-19 | yes | false | PDF fetched (234 KB) but text not extractable with available tools; not read
marketing | https://eurollm.io/ | 2026-11-19 | yes | true | lists 22B flagship (32K), 9B, 1.7B; no licence statement, no dates, no news after Sept 2026
```
