# soofi - primary-source clauses (2026-07-25)

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/Soofi-Project/Soofi-S-Base | 2026-07-25 | yes | true | model exists; license inconsistent ("Other"/TODO vs closed-beta/permissive-pending); LICENSE file 401; no final SPDX
technical_report | https://arxiv.org/abs/2607.09424 | 2026-07-25 | yes | true | real July-2026 paper; OSAID 1.0 claim; per-source data accounting; ~27T tokens
docs | https://github.com/soofi-project/Soofi-Pretraining | 2026-07-25 | yes | true | weights "coming soon"; not yet generally downloadable
```

## license - Soofi-S-30B-A3B (preview)
source_url: huggingface.co/Soofi-Project/Soofi-S-Base | exists: yes | retrieved: true
FINDING: model DOES exist (contrary to handover's "uncertain"). License status INCONSISTENT across fetches ("Other"/TODO vs "closed-beta" + "will be released under a permissive license, without gated access", terms "not yet finalized"). LICENSE file returned HTTP 401; no final SPDX. Hybrid MoE + Mamba-2, 30B total / ~3.5B active; German consortium (SOOFI = Sovereign Open Source Foundation Models); positioned as "a secure, European open-source alternative." Not instruction/safety-tuned. Treat license as pending/unconfirmed.

## technical_report - arXiv 2607.09424
source_url: https://arxiv.org/abs/2607.09424 | exists: yes | retrieved: true
FINDING: arXiv id resolves to a real paper. [Title] "A Sovereign, Open-Source Foundation Model for German and English" (PDF: "Soofi S Pretraining Report v1.0"). [OSAID] "Soofi S satisfies OSAID 1.0: we will release weights, intermediate checkpoints, training and evaluation code, and exact per-source data accounting under permissive licenses." ~27T tokens; Deutsche Telekom German Industrial AI Cloud (Munich). [Data accounting] per-source public identifier + raw/effective token counts; Genios corpus (1.3%) as aggregate stats. NOTE: ~25T (HF) vs ~27T (arXiv) token discrepancy flagged.

## docs - GitHub
source_url: https://github.com/soofi-project/Soofi-Pretraining | exists: yes | retrieved: true
Repo public. Based on Nvidia Nemotron 3 Nano architecture. README: "Open model weights coming soon." Model NOT yet generally downloadable as of 2026-07-25 (HF hosts a preview/internal checkpoint).

## Refresh 2026-11-19
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/Soofi-Project/Soofi-S-Base (rendered page + Hub API, 20 repos) | 2026-11-19 | yes | true | tag license:other / closed-beta; gated:manual on all repos; card says "It is not an open release"; no LICENSE file; raw files 401; see license__soofi-hf-access-gate-and-card__2026-11-19.md
docs | https://github.com/soofi-project/Soofi-Pretraining | 2026-11-19 | yes | true | training code released, no LICENSE (404); README still "Open model weights coming soon"; see docs__soofi-pretraining-and-org-repos__2026-11-19.md
technical_report | https://arxiv.org/abs/2607.09424 | 2026-11-19 | yes | true | v3 (2026-07-22) abstract re-read; release still future tense; see technical_report__soofi-arxiv-v3__2026-11-19.md
marketing | https://www.soofi.info/ | 2026-11-19 | yes | true | "Ein öffentlicher Open-Source-Release ist geplant", no date, no licence, no access form
docs | https://huggingface.co/datasets/Soofi-Project/SOOFI-S-Base-eval-scores | 2026-11-19 | yes | true | cc-by-4.0, ungated eval scores
```

