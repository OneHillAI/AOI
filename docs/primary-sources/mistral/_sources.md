# mistral - primary-source clauses (2026-07-25)

## _sources.md
```
docs | https://docs.mistral.ai/getting-started/models/weights | yes | true | per-model license (Apache-2.0 / MRL / MNPL)
license | https://mistral.ai/licenses/MRL-0.1.md | yes | true | research/non-commercial only
license | https://mistral.ai/licenses/MNPL-0.1.md | yes | true | non-production only
dpa | https://legal.mistral.ai/terms/data-processing-addendum | yes | true | SCCs Module 4; sub-processors on Trust Center; 30-day retention
model_card | https://huggingface.co/mistralai | yes | true | per-variant HF tags: Mistral-Small-4-119B-2603 = apache-2.0; Pixtral-Large-Instruct-2411 = mrl - corroborates docs__weights
```

## docs__weights
[Apache-2.0] "Mistral 7B, Mixtral 8x7B/8x22B, Codestral Mamba, Mathstral, Mistral Nemo, Pixtral 12B, Mistral Small, Magistral Small and Devstral Small are under Apache 2 License." [MNPL] "Codestral is under Mistral AI Non-Production (MNPL) License." [MRL] "Ministral 8B, Mistral Large, and Pixtral Large are under Mistral Research License."

## dpa
[Sec 8 Transfers] SCCs Module 4 (Processor-to-Controller), governing law France. [Sec 7 Subprocessing] list on Trust Center; 10-day objection. [Sec 10] data "will no longer be accessible upon the expiry of a thirty (30) days period following the termination."

## license MRL-0.1 (Ministral 8B, Mistral Large, Pixtral Large)
[Research only] "solely for (a) personal, scientific or academic research, and (b) for non-profit and non-commercial purposes"; excludes revenue activity + SaaS distribution. France/Paris jurisdiction.

## license MNPL-0.1 (Codestral etc.)
[Non-Production only] "You shall only use the Mistral Models and Derivatives for testing, research, Personal, or evaluation purposes in Non-Production Environments." No commercial supply "including...SaaS, cloud instances." Outputs unowned by Mistral. France/Paris.

## Re-verification 2026-11-19 (index additions)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
model_card | https://huggingface.co/mistralai/<repo>/raw/main/README.md (+ HF API) | 2026-11-19 | yes | true | Large-3 675B, Ministral-3 3B/8B/14B, Small-4 119B = apache-2.0 from RAW card front matter and card License section (closes the 2026-09-21 summariser item); Codestral-22B-v0.1 still mnpl; file: model_card__hf-licence-tags-and-cards__2026-11-19.md
docs | https://docs.mistral.ai/models/overview | 2026-11-19 | yes | true | per-model licence labels and hosted-API retirement table; file: docs__models-overview__2026-11-19.md
docs | https://docs.mistral.ai/getting-started/models/weights | 2026-11-19 | no | false | HTTP 404 "Page not found" (page removed or moved); the 2026-07-25 verbatim extract stays as a dated record
license | https://mistral.ai/licenses/MRL-0.1.md ; https://mistral.ai/licenses/MNPL-0.1.md | 2026-11-19 | yes | true | texts unchanged; file: license__mrl-mnpl-reread__2026-11-19.md
privacy_policy | https://legal.mistral.ai/terms/privacy-policy | 2026-11-19 | yes | true | effective 2026-09-03; file: privacy_policy__retention-training-transfers__2026-11-19.md
docs | https://help.mistral.ai/en/articles/347617 ; 347629 ; 347612 ; 347628 | 2026-11-19 | yes | true | training, location, ZDR; file: docs__help-centre-training-zdr-residency__2026-11-19.md
dpa | https://legal.mistral.ai/terms/data-processing-addendum | 2026-11-19 | yes | true | effective 2026-07-27; file: dpa__effective-2026-07-27__2026-11-19.md
terms | https://legal.mistral.ai/terms/commercial-terms-of-service | 2026-11-19 | yes | true | effective 2026-09-25, clause 4.2 training; file: terms__commercial-tos-training-clause__2026-11-19.md
license | https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B ; Timestral-* ; Devstral-2-123B ; Mistral-Medium-3.5-128B (raw LICENSE) | 2026-11-19 | yes | true | NEW ENTITIES, not scored in this entry; file: license__new-entities-large4-timestral__2026-11-19.md
third_party | https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai | 2026-11-19 | yes | true | Mistral AI listed among 22 signatories (page last updated 7 October 2026), read through WebFetch summary
security | https://trust.mistral.ai/ (Trust Center sub-processor list) | 2026-11-19 | unknown | false | single-page application, not read; DPA points to it
```
