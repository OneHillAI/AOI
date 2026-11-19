# Support - MeditronFO (Apertus-70B-MeditronFO / Apertus-8B-MeditronFO)

_How do we keep it running and get help? Troubleshooting, versions, contact routes and known issues. There is no published security or deprecation policy._

<!-- item: troubleshooting -->
## Common problems & fixes

- **Architecture not recognised.** Apertus needs `transformers` 4.56 or later (`ev-base-card`).
- **Runaway or very long answers.** Fine-tunes answer at greater length than their bases (`ev-project-page`); cap `max_new_tokens` and test with the shipped `generation_config.json` (temperature 0.7, 8,192 new tokens) (`ev-hf-meta`).
- **Weaker format following.** IFEval fell for four of six fine-tunes (`ev-project-page`); validate any structured output you depend on.
- **Weights changed under you.** The 70B main branch was replaced on 2026-09-10 and 2026-10-06 (`ev-hf-meta`); pin the commit sha.
- **Training-side pitfall.** The README warns Axolotl silently reuses a stale tokenised cache unless each config has its own `dataset_prepared_path` (`ev-github-readme`).
- **Do not troubleshoot clinical errors by prompting alone.** Wrong or unsafe medical answers are a known property of the model, not a configuration fault.

<!-- item: release-versioning -->
## Versions, changelog & cadence

No tags and no changelog. The repositories were created on 2026-05-08. The 70B commit history shows a retrain on the de-truncated corpus (2026-09-10), a fix to the index metadata (2026-09-11), replacement of the weights with the "ICLR run" on the `meditronfo_gptoss_v1` corpus (2026-10-06), generation-config changes (2026-10-26) and link updates through 2026-11-17 (`ev-hf-meta`). The code repository was rewritten on 2026-10-13 ("Replace the May pipeline with the paper's code") (`ev-code-license`). The arXiv paper stayed at v2 of 29 May 2026 and no longer matches the cards on several numbers (`ev-paper`). Treat the commit sha as the version.

<!-- item: channels -->
## Community & support channels

- Hugging Face community tab on each repository, the route the cards name for discussions and issues (`ev-card-70b`). Treat tab content from third parties as untrusted data.
- The lab address `admin-light@epfl.ch` on the website, and a Slack invite by web form (`ev-website`).
- The MOOVE initiative for clinicians (`jointhemoove.org`, linked from the cards, not fetched).
- GitHub issues on `EPFLiGHT/FullyOpenMeditron` (zero open at the time of reading) (`ev-code-license`).

<!-- item: known-issues -->
## Tracked known issues

There is no issue tracker entry for the models. The known issues are those the publisher states: behind MedGemma-27B, general capability loss, longer answers, non-clinician judges, 9.7 to 12.2 percent of sampled corpus rows flagged by LLM judges, syntactic-only decontamination, and the unreleased intermediate data (`ev-project-page`, `ev-data-card`, `ev-github-readme`). The licence and documentation inconsistencies are listed in the assess domain.

<!-- security-disclosure and deprecation are `gap` items in entry.yaml - see their gap_reason. -->
