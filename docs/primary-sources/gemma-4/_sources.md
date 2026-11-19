# gemma-4 - primary-source clauses (2026-11-19)

Entity: Gemma 4 release (Google DeepMind). Retrieval by OneHill agent on 2026-11-19 with curl, the Hugging Face public API, macOS PDFKit (PDF text) and WebFetch. No model weights or large files were downloaded.

```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://ai.google.dev/gemma/docs/gemma_4_license (redirects to https://gemma.ai/resources/apache-2/) | 2026-11-19 | yes | true | Apache License 2.0 full text, identical to the Apache text in google-deepmind/gemma LICENSE; file license__gemma-4-apache-2.0
license | https://huggingface.co/google/gemma-4-31B-it (README front matter, 10 core repos + drafter + QAT sample) | 2026-11-19 | yes | true | license: apache-2.0 and license_link on every repo read; no LICENSE or NOTICE file in any repo; file docs__hf-api-checkpoint-inventory
terms | https://ai.google.dev/gemma/terms (redirects to https://gemma.ai/resources/terms/) | 2026-11-19 | yes | true | Gemma Terms of Use, last modified April 1, 2026; scoped to Gemma 1 to 3n and siblings, states "For Gemma 4 terms, see the Gemma 4 license"; file terms__gemma-terms-of-use-gemma-1-to-3
terms | https://ai.google.dev/gemma/prohibited_use_policy (redirects to https://gemma.ai/resources/prohibited-use/) | 2026-11-19 | yes | true | Prohibited Use Policy, last modified Feb 21, 2024; incorporated only via Gemma Terms 3.2; no Gemma 4 document references it
model_card | https://huggingface.co/google/gemma-4-31B-it/raw/main/README.md | 2026-11-19 | yes | true | 31B-it card; 31B base, 12B, 12B-it, 26B A4B, E2B, E4B cards share the text; file model_card__gemma-4-31B-it
model_card | https://gemma.ai/models/gemma-4/model-card/ | 2026-11-19 | yes | true | Google docs model card, same content as the HF card, header "License : Apache 2.0"; covered in docs__gemma-4-overview-memory-qat
docs | https://gemma.ai/models/gemma-4/ (from https://ai.google.dev/gemma/docs/core) | 2026-11-19 | yes | true | Overview: sizes, memory table, QAT checkpoint routing, MTP drafters
technical_report | https://arxiv.org/abs/2607.02770 (HTML https://arxiv.org/html/2607.02770) | 2026-11-19 | yes | true | Gemma 4 Technical Report v2 (24 Jul 2026), HTML read
technical_report | https://arxiv.org/pdf/2607.02770 | 2026-11-19 | yes | false | PDF of the same report; not separately read, HTML used
docs | https://storage.googleapis.com/transparencyreport/report-downloads/pdf-report-nn_2026-7-31_2026-7-31_en_v1.pdf | 2026-11-19 | yes | true | EU AI Act Art 53(1)(d) Public Summary of Training Content, Gemma 4 family, v1, 31 July 2026; text plus page images
docs | https://huggingface.co/api/models?author=google&search=gemma-4 | 2026-11-19 | yes | true | 38 Gemma 4 repos, all apache-2.0 and gated=false; org verified; Gemma 3 contrast (gated manual, license gemma, raw README 401)
third_party | https://huggingface.co/api/models/google/gemma-4-31B-it/scan | 2026-11-19 | yes | true | scansDone true, filesWithIssues empty; safetensors metadata; LFS sha256 per shard; commit history; no signature files found
marketing | https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/ | 2026-11-19 | yes | true | Launch blog Apr 02, 2026; marketing, cannot justify a rating; says four sizes (12B added later)
third_party | https://the-decoder.com/googles-gemma-4-is-now-available-with-apache-2-0-licensing-for-the-first-time/ | 2026-11-19 | yes | true | Independent press on the licence change and launch-time Artificial Analysis GPQA figures
third_party | https://artificialanalysis.ai/models/gemma-4-31b | 2026-11-19 | yes | true | Artificial Analysis Intelligence Index v5.0.1: 4, "#14 / 15", lower end of comparable open-weights models; reads less favourably than launch coverage
third_party | https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai | 2026-11-19 | yes | true | European Commission GPAI Code of Practice page lists Google as a signatory (page last update 7 October 2026)
third_party | https://ollama.com/library/gemma4 | 2026-11-19 | yes | true | Ollama library: e2b, e4b, 12b, 26b, 31b tags, vision, tools, thinking, audio; 29.5M downloads
security | https://github.com/google/.github/blob/master/SECURITY.md ; https://github.com/google-deepmind/gemma | 2026-11-19 | yes | true | Google-wide GitHub security policy (g.co/vulnz); not Gemma-specific; no Gemma-specific SECURITY.md (404); gemma library README and Apache LICENSE
third_party | https://aial.ie/research/gpai-training-transparency/evals/gemma-4/ | 2026-11-19 | yes | false | ADAPT Centre AI Accountability Lab evaluation of the Gemma 4 training summary, linked from a secondary blog; connection refused (ECONNREFUSED) from the fetch tool and curl returned no response; not read, nothing scored on it
docs | https://huggingface.co/google/gemma-3-4b-it/raw/main/README.md | 2026-11-19 | yes | false | Gemma 3 README returned HTTP 401 (gated, manual approval); only the public API metadata was read (see docs__hf-api-checkpoint-inventory)
docs | https://ai.google.dev/gemma/terms-archive (previous versions of the Gemma Terms) | 2026-11-19 | yes | false | Linked from the Terms page; the archived Gemma Terms versions (including the February 2024 and the Gemma 3 era text) were not read; only the current Terms text was
docs | https://ai.google.dev/responsible (redirects to https://ai.google/safety/) | 2026-11-19 | yes | false | Responsible Generative AI Toolkit, linked from the model card; page fetched (HTTP 200) but not read, nothing scored on it
docs | https://deepmind.google/ Frontier Safety Framework and Google AI responsibility update PDF | 2026-11-19 | yes | false | Referenced by the technical report and model card; not fetched
docs | Kaggle model page for Gemma 4 | 2026-11-19 | yes | false | Named by the model card and blog as a distribution channel; not fetched, so any signing or licence presentation on Kaggle is unverified
docs | Model-signing or SLSA provenance attestation for Gemma 4 weights | 2026-11-19 | unknown | false | None found in any repository file list or Google page read
```
