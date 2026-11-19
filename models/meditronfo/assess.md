# Assess - MeditronFO (Apertus-70B-MeditronFO / Apertus-8B-MeditronFO)

_Should we adopt this? Openness, licence, provenance, EU AI Act, safety, evaluation, and the AOI score live here. Read the first section before anything else: this is a specialist medical model and the decision is about what it may be used for._

<!-- item: intended-use -->
## Intended & out-of-scope use

**Decision: adopt it for research, evaluation, auditing and as a base for your own medical specialisation. Do not adopt it for clinical use.** The publisher says so in its own words: "MeditronFO models are not medical devices and have not been tested in clinical practice. Don't use them to make decisions about a patient." (project page, `ev-project-page`). The model cards say the models are "intended to be used for Medicine related tasks evaluation" and should be "assistive tools rather than definitive sources of information" (`ev-card-70b`). The dataset card says models trained on the corpus "should not be deployed without independent safety evaluation" (`ev-data-card`). The website chat describes it as "a research model, not a doctor" (`ev-website`).

| Use | Status | Basis |
|---|---|---|
| Research on medical LLMs, benchmarking, auditing the open pipeline | Cleared by the publisher's stated intent | cards, dataset card |
| Specialisation base for your own medical fine-tune | Cleared in practice (open weights, corpus and training code); licence chain needs the checks under the licence item | `ev-github-readme` |
| Internal, non-patient drafting or education with a clinician reading every output | Possible at Deployment Ceiling T1 with your own safety evaluation; not covered by any publisher evaluation | OneHill ceiling |
| Any output that informs a decision about a patient | Not cleared: the publisher prohibits it in plain words | `ev-project-page` |
| Use as, or inside, a medical device or clinical decision support product | Not cleared: no device status, no clinical testing, no regulatory file; the publisher announces clinical trials as future work | `ev-project-page`, `ev-press` |
| Autonomous or patient-facing deployment | Out of scope | `ev-project-page` |

Who makes it: the LiGHT laboratory at EPFL (Switzerland), with Swiss AI Initiative funding and CSCS compute (`ev-card-70b`). This entry covers the two Apertus-based checkpoints, Apertus-70B-MeditronFO (the flagship) and Apertus-8B-MeditronFO. Both are supervised fine-tunes of the Apertus-Instruct models for English medical question answering and open-ended clinical reasoning.

<!-- item: limitations -->
## Known limitations, bias & failure modes

All figures below are publisher statements; no independent evaluation exists.

- **Behind the closest open competitor.** On the five-benchmark medical average Apertus-70B-MeditronFO scores 54.56 against 63.75 for MedGemma-27B, a smaller model (`ev-project-page`).
- **General capability falls.** The general-purpose average falls for four of the six fine-tunes, mostly through IFEval (down 17.6 to 31.4 points) (`ev-project-page`).
- **Longer answers.** Part of the HealthBench gain is length: after length adjustment the 70B scores 40.3 against 35.7 for its base (`ev-project-page`).
- **Judges are not clinicians.** Agreement on safety is low, kappa 0.311 between judge and clinicians against 0.306 between clinicians, and the paper calls the judge unsuitable as a deployment-readiness signal for harmlessness and fairness (`ev-project-page`, `ev-paper`).
- **Corpus quality.** Two LLM judges flag 9.7 to 12.2 percent of sampled rows of the final corpus; about 63 percent of questions and all answers come from one teacher, gpt-oss-120b; decontamination is syntactic, not semantic; clinician review covered prompts and sample outputs, not individual items (`ev-project-page`, `ev-data-card`).
- **English only, and geographically skewed.** The corpus is English and draws mostly on North American, European and Indian exam material, partly offset by AfriMed-QA (`ev-data-card`).
- **Multiple-choice answers distilled from a teacher.** Answers were kept only if they reached the gold label in 8 samples; open-ended answers and vignettes had no such filter (`ev-data-card`).
- **Hallucination.** The card says generated content may be factually inaccurate, inconsistent or biased (`ev-card-70b`).

<!-- item: openness -->
## Openness tier & components

Tier `open_weights_recipe`. The project page claims the first fully open medical models, and the base is genuinely fully open (Apertus: open weights, data and training details per its card, `ev-base-card`). For this release:

| Component | State | Evidence |
|---|---|---|
| Weights | open (BF16 safetensors, ungated) | `ev-hf-meta` |
| Training data | partial: 533,888-row corpus released with source fields; intermediate pipeline outputs, MOOVE vignettes and some upstream inputs not released | `ev-data-card`, `ev-github-readme` |
| Training code | open: Axolotl configs, data generation, resampling, decontamination | `ev-github-readme`, `ev-code-license` |
| Evaluation | partial: harness, HealthBench and AutoMOOVE code public; the MOOVE evaluation vignettes are not public | `ev-github-readme` |
| Documentation | open: cards, dataset card, paper, project page | |
| Licence | partial: declared Apache-2.0, no LICENSE file with the weights | `ev-hf-meta` |

**Marketing against the repository.** The project page says the 534k examples were "released with the code and outputs of every step", and the EPFL press item says "every stage of development publicly available" (`ev-project-page`, `ev-press`). The GitHub README says "The intermediate files and per-item evaluation outputs (tens of GB) are not released yet" and that the MOOVE vignettes "are not public", and lists in its known gaps that section 1 "cannot be rerun from a fresh clone yet" (`ev-github-readme`). This entry follows the README. It also holds the tier at open_weights_recipe rather than fully_open for that reason.

<!-- item: license -->
## License terms & permitted use

**Verdict: Apache-2.0 is declared, commercial use is permitted on that declaration, and four loose ends mean you should get legal review before relying on it.**

What was read:

- Both weight repositories declare `license: apache-2.0` in the card metadata and link the Apache 2.0 text on apache.org from the card header (`ev-card-70b`, `ev-card-8b`). Neither repository contains a LICENSE or NOTICE file (raw LICENSE is HTTP 404) and no copyright holder is named beyond "Authors: LiGHT" (`ev-hf-meta`). The Apache-2.0 LICENSE in the GitHub repository covers the code, not the weights (`ev-code-license`).
- **Corpus licence stated two ways.** The arXiv paper (v2, 29 May 2026) says "We release the corpus under a research-use license" and that assets are "restricted to research purposes"; the dataset card (last modified 17 Nov 2026) and project page say Apache-2.0 (`ev-paper`, `ev-data-card`, `ev-project-page`). The weights were retrained after the paper (September and October 2026), so the cards may be newer, but no document says the licence was changed on purpose.
- **Source dataset terms.** The dataset card lists LiveQA-Med as "Open / research use" and AfriMed-QA as CC BY-SA 4.0 (the paper says CC BY 4.0), both marked "Verify the upstream terms before redistribution". The paper lists the guidelines corpus as "Per-source (mixed); research use" and the MOOVE training split as "Research use" (`ev-data-card`, `ev-paper`).
- **Inherited base terms.** The Apertus base card carries an Acceptable Use Policy with an indemnity clause in its gate prompt and advises applying a personal-data output filter every six months; Hugging Face reports the gate off today. The MeditronFO cards do not mention it, and no document says whether it binds a fine-tune (`ev-base-card`).
- **Teacher outputs.** Every training answer was written by gpt-oss-120b, which is Apache-2.0 with a one-sentence usage policy requiring compliance with law (`ev-teacher`). This is not a restriction on the outputs as read.
- **No medical-use grant or restriction in the licence.** The research and not-for-patients statements are use statements on the cards and project page, not licence terms; the Apache-2.0 declaration itself carries no field-of-use limit.

**Follow-up entries needed (diverging base or licence).** `OLMo-2-32B-MeditronFO` (base OLMo-2-0325-32B-SFT, Apache-2.0 per its card), `EuroLLM-22B-MeditronFO` (base `EuroLLM-22B-Instruct` is not readable, HTTP 401) and `EuroLLM-9B-MeditronFO` (base is auto-gated), each declared Apache-2.0; `Gemma-3-27B-MeditronFO` (Gemma Terms of Use, a different licence, and the card still carries the `fully-open` tag); the older `Meditron3` line (Llama 3.1, Gemma, Apache-2.0 and MIT tags by base); and `Gemma-3-27B-MeditronFO-Amharic` (no licence tag) (`ev-siblings`).

<!-- item: provenance -->
## Supply-chain & provenance

- **Source:** `EPFLiGHT/Apertus-70B-MeditronFO` and `EPFLiGHT/Apertus-8B-MeditronFO` on Hugging Face. The organisation is named "Laboratory for Intelligent Global Health & Humanitarian Response Technologies" but is **not a verified organisation** (`isVerified` false, team plan, two members) (`ev-hf-meta`). The identity is corroborated by the EPFL AI Center press item, which names the LiGHT laboratory as the releasing group, and by the project page on an EPFL-linked site (`ev-press`, `ev-project-page`).
- **Format and integrity:** safetensors only (30 shards for 70B, 4 for 8B), every shard has an LFS sha256, no pickle or `.bin` file (`ev-hf-meta`). No signature, attestation or scan result was found. Checklist score about 3 of 8.
- **Mutable weights.** The 70B main branch was retrained on the de-truncated corpus on 2026-09-10 and replaced with the "ICLR run" on 2026-10-06; there are no tags. Pin the commit sha (70B `d13151ac9ff56b966dd5257d5064876685a750e3`, 8B `c0f8a017b6abaed4335e68a5f6c5e0096c17115f`, as read on 2026-11-19) and re-verify the shard hashes (`ev-hf-meta`).
- **Lineage is well documented:** base `swiss-ai/Apertus-*-Instruct-2509`, 533,888-row corpus with `teacher_model`, `source_dataset` and `source_id` fields, answers by gpt-oss-120b (`ev-card-70b`, `ev-data-card`, `ev-teacher`).
- **Community conversions** (GGUF, MLX) exist and are not canonical; none were opened (`ev-quants`).

<!-- item: eu-ai-act -->
## EU AI Act posture and medical-use caveats

- **GPAI status:** a general-purpose language model fine-tuned for a domain. The Apertus-70B base is estimated at about 6.4e24 FLOPs by the 6ND rule (70.6B parameters, 15T tokens), under the 1e25 systemic-risk line; the fine-tune used 199 GPU-hours and adds little. This is a OneHill estimate from card figures, not a publisher statement (`ev-card-70b`, `ev-base-card`).
- **Open-source exemption:** not established. The declared licence would normally qualify, but the missing LICENSE file and the corpus-licence disagreement mean OneHill does not treat it as settled. Whether fine-tuning makes EPFL or you a provider depends on the modification-compute rule, which was not read here.
- **Provider documentation:** the base publisher links an EU AI Act public summary and a Code of Practice document on the Apertus card (`ev-apertus-eu-docs`, documented but unverified: the PDFs were not fetched). MeditronFO publishes no provider package of its own; the open corpus with source fields and the paper help a deployer build a training-content summary.
- **Medical purpose is the live regulatory question, and it is yours.** The publisher states the models are not medical devices and untested in clinical practice (`ev-project-page`). If you build a product that informs clinical decisions, you need to assess medical-device software and AI Act high-risk obligations for that product before development. This entry did not read those instruments and does not assess them. Nothing in the release is a regulatory clearance of any kind.

<!-- item: evaluation -->
## Benchmarks & evaluation

All results are the publisher's, run with an LLM grader (Gemma-4-31B for HealthBench) and greedy decoding for multiple choice. No independent re-run was found.

| Benchmark | Apertus-70B-Instruct | Apertus-70B-MeditronFO | MedGemma-27B (project page) |
|---|---:|---:|---:|
| MedMCQA | 52.8 | 60.2 | |
| MedQA | 61.9 | 71.1 | |
| PubMedQA | 74.7 | 74.9 | |
| MedXpertQA | 13.0 | 17.3 | |
| HealthBench (5,000 conversations) | 39.4 | 49.3 | 54.8 |
| Five-benchmark average | 48.35 | 54.56 | 63.75 |

The 8B scores 48.26 against 42.39 for its base (`ev-card-8b`). On AutoMOOVE (516 clinician-written vignettes, three LLM judges) the 70B is preferred over its base in 89.7 percent of comparisons and over MedGemma-27B in 35.8 percent, losing to it under all three judges (`ev-project-page`). The arXiv paper v2 reports different numbers for the same model (47.2 to 53.8) and a different corpus description (eight source datasets and 46,469 guidelines against five or seven datasets and 14,192 guidelines on the cards), so treat the paper as older than the released weights (`ev-paper`).

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. -->
