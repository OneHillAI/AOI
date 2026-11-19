# EuroLLM-22B: Technical Report (arXiv 2602.05879), re-read 2026-11-19

Source: https://arxiv.org/abs/2602.05879 (API record and HTML version). Submitted 2026-02-05.
exists: yes, retrieved: true.

Abstract, final sentence, verbatim: "To support future research, we release our base and
instruction-tuned models, our multilingual web pretraining data and updated EuroBlocks
instruction datasets, as well as our pre-training and evaluation codebases."

Corroboration read this pass:
- Hugging Face dataset `utter-project/EuroWeb-2512` exists (created 2026-02-03, not gated, no
  licence declared in its card metadata). Card: "EuroWeb is a dataset of collecting multilingual
  web data from various sources. It was processed with standard practices and then classified
  with utter-project/EuroFilter-v1."
- Hugging Face dataset `utter-project/EuroBlocks-SFT-2512` exists (created 2026-01-23, 1,094,265
  conversations, not gated, no licence declared in its card metadata).
- The report links two GitHub repos, `github.com/deep-spin/Megatron-LM-pretrain` (a fork of
  NVIDIA Megatron-LM; its root LICENSE is NVIDIA's BSD-style licence) and
  `github.com/deep-spin/eurollm-eval` (no top-level LICENSE or LICENSE.md found).
- The report says parallel data is collected "from various public sources, listed in Table 2".

Consequence for the tracked entry: the statement that the pretraining corpus is "only described"
was true for the 2024 EuroLLM-9B and 1.7B line, but the 2512 generation (22B and 9B-2512) has a
released web corpus and released training and evaluation code. The 22B is a new entity.
