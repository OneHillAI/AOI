# Assess - Gemma 4 (E2B, E4B, 12B, 26B A4B, 31B)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Use the instruction-tuned (`-it`) checkpoints for general assistants, coding, reasoning, agentic tool use, document and image understanding, and on-device work (`ev-card-31b`).

Audio input is available on E2B, E4B and 12B only. The base checkpoints are for research and fine-tuning and not for customer-facing use. The model card lists content creation, chatbots, summarisation, image data extraction, audio processing, NLP research and language learning as the uses the developers considered.

No Prohibited Use Policy binds these weights (see the license item), so Google sets no use limits beyond the Apache-2.0 text. The out-of-scope decision therefore falls to the deployer: write an acceptable-use policy and enforce it at the application layer. Treat high-stakes automated decisions as out of scope until the model is evaluated on the deployer's own data, because the safety evidence is publisher-only.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The model card says the training data shapes the model's capabilities, with a January 2025 cutoff (`ev-card-31b`, `ev-eu-summary`). It also says the models are not knowledge bases and can state incorrect or outdated facts.

Independent capability evidence is mixed. The launch-time GPQA result was strong, but the Artificial Analysis Intelligence Index v5.0.1 rates the 31B at the lower end of comparable open-weights models (`ev-decoder`, `ev-aa`). Test on your own tasks.

The small models are far weaker. On the publisher's own table the E2B scores 43.4 percent on GPQA Diamond against 84.3 percent for the 31B, and 19.1 percent against 66.4 percent on 8-needle 128K retrieval.

Thinking-mode behaviour differs by size. With thinking off, every size except E2B and E4B still emits an empty thought block (`ev-card-31b`).

<!-- item: openness -->
## Openness tier & components

Gemma 4 is `open_weights`. The weights for all five sizes, base and instruction-tuned, are downloadable under Apache-2.0. The documentation is open: a model card, a technical report (`ev-tech-report`) and a docs site.

The tier is not `open_weights_recipe` because the data and the pipeline are not released:

- Training data is closed. The model card and report describe web documents, code, mathematics, images and audio with a January 2025 cutoff. The EU training-content summary gives size bands (text above 10 trillion tokens) and names no dataset or domain (`ev-eu-summary`).
- Training code is partial. The google-deepmind/gemma library supports inference and fine-tuning (`ev-gemma-lib`), but the pre-training pipeline is not there.
- Evaluation is partial. Benchmark tables and per-repository evaluation result files are published, but no full evaluation harness has been identified.

<!-- item: license -->
## License terms & permitted use

Gemma 4 is Apache-2.0 on every checkpoint: commercial use is allowed, and there is no gate and no use policy. The licence page that every Gemma 4 model card links is the full Apache License 2.0 text. Its sections 1 to 9 are identical, whitespace aside, to the Apache text in Google's own `google-deepmind/gemma` code repository (`ev-license`).

All 38 Gemma 4 repositories in the verified `google` organisation (10 core checkpoints, 10 drafters, 18 quantised releases) carry the Apache-2.0 tag and are ungated, and every README states `license: apache-2.0` (`ev-hf-inventory`). The technical report says the models are released under Apache 2.0 (`ev-tech-report`), and independent press confirms the licence (`ev-decoder`). No repository carries a LICENSE or NOTICE file; the licence lives in the README front matter and the linked page.

The old terms do not apply to Gemma 4. Google's Gemma Terms of Use (last modified April 1, 2026) list Gemma 1, 1.1, 2, 3, 3n and a set of siblings in an appendix, do not list Gemma 4, and say 'For Gemma 4 terms, see the Gemma 4 license' (`ev-terms-old`). The Gemma Prohibited Use Policy is bound into a contract only by section 3.2 of those terms, and no Gemma 4 document refers to it (`ev-pup`). The policy page itself does not name the models it covers and is still live, so a cautious lawyer may note a residual ambiguity. No clause makes it bind Gemma 4.

Apache-2.0 still imposes conditions. Redistributing the weights or a derivative requires giving recipients a copy of the licence, marking changed files and keeping copyright and attribution notices (section 4). Modifications may carry the redistributor's own terms. The licence grants no trademark licence (section 6), and the patent licence ends for a user who sues alleging the Work infringes a patent (section 3). It says nothing about model outputs.

The launch blog's 'complete control over your data, infrastructure, and models' is marketing, and the grant is the Apache text (`ev-blog`). One leftover sentence on the overview page says Gemma models 'permit responsible commercial use'. That wording is from the Gemma Terms era, is not a clause and does not narrow Apache-2.0 (`ev-docs-overview`).

Licences differ by checkpoint. Other Google 'gemma' releases still diverge: `translategemma` is tagged `gemma` (Gemma Terms), `medgemma-1.5` is tagged `other`, and `embeddinggemma-2` is Apache-2.0 (`ev-hf-inventory`). Gemma 3 is gated for manual approval and tagged `gemma`. None of these releases is covered here.

A model built on a Gemma 3 checkpoint stays under the Gemma Terms of Use. Those terms define a Model Derivative to include modifications, works based on Gemma and any model trained by distillation or on Gemma outputs (section 1.1(e)). They require the use restrictions and the terms to travel with it (section 3.1), incorporate the Prohibited Use Policy, and let Google restrict usage remotely (section 3.2) (`ev-terms-old`).

A Gemma 3 derivative labelled Apache-2.0, MIT, GPL or CC BY on its own card is therefore inconsistent with the Gemma Terms that apply to it. Only a publisher that also carries the Gemma Terms and the policy resolves that; the label alone does not remove them. Several Gemma 3 derivatives carry such labels (Fanar-2, Sarvam-translate, AfriqueLLM, PLLuM 4B) and should be assessed as Gemma Terms derivatives. That reading rests on the Terms text and is not a legal opinion.

A model built on a Gemma 4 checkpoint is under Apache-2.0 section 4: the publisher must ship the licence text, mark changes and keep notices, and may license its own modifications on different terms. Nothing in the Apache text restricts using Gemma 4 outputs to train other models. Moving a derivative's base from Gemma 3 to Gemma 4 changes its licence reading, but it does not retroactively relicense an existing Gemma 3 derivative.

<!-- item: provenance -->
## Supply-chain & provenance

The weights come from the verified `google` organisation on Hugging Face as safetensors, with an LFS sha256 for each shard and a Hugging Face scan that reports no flagged files (`ev-hf-inventory`, `ev-hf-scan`). Google documents official quantised and drafter checkpoints by use case in the same organisation (`ev-docs-overview`), so a trusted route to quantised weights exists in place of community quants.

The checkpoint trust checklist scores 6 of 8. The missing controls are a cryptographic weight signature (none in any file list) and a build attestation. Kaggle, which Google also lists as a source, is unchecked.

Training-data provenance is a separate point. Google's EU training-content summary says the training data included user interactions with Google products, naming Gemini Apps chats (`ev-eu-summary`). It also lists commercially licensed and private third-party datasets (none named), crawled web data, and synthetic data generated by the Gemini 3 family.

The model card describes the pre-training data as web documents, code, mathematics and images and does not mention user data. Record both documents in the AI-BOM.

<!-- item: eu-ai-act -->
## EU AI Act posture

Gemma 4 is a general-purpose AI model. Google Ireland Limited published an Article 53(1)(d) Public Summary of Training Content for the Gemma 4 family (v1, 31 July 2026) and answers 'Yes' to being a Code of Practice signatory (`ev-eu-summary`). The European Commission's page lists Google as a signatory (`ev-ec-cop`). The summary names no dataset and no domain, so it supports 'a public summary exists' and not reproducibility.

The compute figure is not disclosed. The summary bands text at more than 10 trillion tokens. At that lower bound the 31B is about 1.8e24 FLOPs, below the 1e25 systemic-risk presumption, but 1e25 would need about 54 trillion tokens and no document states the true count. No designation has been identified.

The Article 53(2) open-source exemption needs a free and open-source licence and no monetisation. Apache-2.0 satisfies the licence condition. Google sells hosted access, so whether the exemption applies to Google is a legal question that stays open. A fine-tuner who places a derivative on the EU market under its own name may become its provider. No Google copyright-policy document or Annex XI style form has been identified.

<!-- item: evaluation -->
## Benchmarks & evaluation

Publisher figures for the instruction-tuned models (`ev-card-31b`), in the order MMLU Pro, AIME 2026 without tools, LiveCodeBench v6, GPQA Diamond and Tau2:

- 31B: 85.2, 89.2, 80.0, 84.3 and 76.9.
- 26B A4B: 82.6, 88.3, 77.1, 82.3 and 68.2.
- 12B Unified: 77.2, 77.5, 72.0, 78.8 and 69.0.
- E4B: 69.4, 42.5, 52.0, 58.6 and 42.2.
- E2B: 60.0, 37.5, 44.0, 43.4 and 24.5.
- Gemma 3 27B without thinking: 67.6, 20.8, 29.1, 42.4 and 16.2.

Independent evidence conflicts. At launch the trade press relayed an Artificial Analysis GPQA Diamond score of 85.7 percent for the 31B in reasoning mode, second among open models under 40B (`ev-decoder`). The Artificial Analysis Intelligence Index v5.0.1 page shows the 31B at 4, ranked 14 of 15 among comparable open-weights models and described as lower end (`ev-aa`). The index weights agentic and expert tasks, so the two results measure different things.

The technical report also names a human-preference leaderboard where the 31B was the leading dense open model on June 19, 2026 (`ev-tech-report`). That is publisher-reported.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. The only safety evidence
     is the publisher's qualitative statement (model card section Ethics and Safety;
     technical report section 5): five policy areas, 'minimal policy violations', no numbers. -->
