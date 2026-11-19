# meditronfo - primary-source index (2026-11-19)

Scope of this entry: the Apertus-based MeditronFO checkpoints, EPFLiGHT/Apertus-70B-MeditronFO and EPFLiGHT/Apertus-8B-MeditronFO. Sibling checkpoints (OLMo-2, EuroLLM, Gemma-3 and the older Meditron3 line) are follow-ups, see the entry.

```
doc_type | source_url | retrieval_date | exists | retrieved | notes
model_card | https://huggingface.co/EPFLiGHT/Apertus-70B-MeditronFO | 2026-11-19 | yes | true | full card; front matter license: apache-2.0; no LICENSE file in the repo (raw/main/LICENSE is HTTP 404); file model_card__apertus-70b-meditronfo__2026-11-19.md
model_card | https://huggingface.co/EPFLiGHT/Apertus-8B-MeditronFO | 2026-11-19 | yes | true | extracts: front matter, benchmark table, training, limitations; file model_card__apertus-8b-meditronfo__2026-11-19.md
docs | https://huggingface.co/api/models/EPFLiGHT/Apertus-70B-MeditronFO | 2026-11-19 | yes | true | HF API: files, safetensors, gated=False, commits, config.json, organisation isVerified=false; file docs__hf-repo-metadata__2026-11-19.md
license | https://raw.githubusercontent.com/EPFLiGHT/FullyOpenMeditron/main/LICENSE | 2026-11-19 | yes | true | Apache-2.0 for the CODE repository only; not a licence for the weights; file license__github-fullyopenmeditron-LICENSE__2026-11-19.md
docs | https://meditron.light-laboratory.org/meditronfo | 2026-11-19 | yes | true | project page: not medical devices, not tested in clinical practice, availability and licence statement; file docs__project-page-meditronfo__2026-11-19.md
docs | https://github.com/EPFLiGHT/FullyOpenMeditron | 2026-11-19 | yes | true | README: what is and is not released; known gaps; file docs__github-readme-fullyopenmeditron__2026-11-19.md
docs | https://huggingface.co/datasets/EPFLiGHT/fully-open-meditron | 2026-11-19 | yes | true | dataset card: Apache-2.0 tag, 533,888 rows, per-source licence table with unverified rows, limitations; file docs__dataset-card-fully-open-meditron__2026-11-19.md
technical_report | https://arxiv.org/abs/2605.16215 | 2026-11-19 | yes | true | v2 of 29 May 2026, HTML read; says corpus is under a research-use licence; numbers differ from current cards; file technical_report__arxiv-2605-16215v2__2026-11-19.md
model_card | https://huggingface.co/swiss-ai/Apertus-70B-Instruct-2509 | 2026-11-19 | yes | true | base model: Apache-2.0 tag, Acceptable Use Policy gate prompt with indemnity (gate off per API), Legal Aspects incl. no PII output filter yet; 8B card identical bar name; file model_card__base-apertus-instruct-2509__2026-11-19.md
model_card | https://huggingface.co/openai/gpt-oss-120b | 2026-11-19 | yes | true | teacher model that wrote all training answers; Apache-2.0 plus USAGE_POLICY; file model_card__teacher-gpt-oss-120b__2026-11-19.md
marketing | https://ai.epfl.ch/?p=18464 | 2026-11-19 | yes | true | EPFL AI Center news item, 17 June 2026; marketing register; file marketing__epfl-ai-center-press-release__2026-11-19.md
marketing | https://meditron.light-laboratory.org/ | 2026-11-19 | yes | true | website main page; chat disclaimer "research model, not a doctor"; contact address; file marketing__meditron-website__2026-11-19.md
docs | https://huggingface.co/api/models?author=EPFLiGHT | 2026-11-19 | yes | true | sibling checkpoints and their licence tags; base licence tags; EuroLLM base cards unreadable; file docs__sibling-checkpoints-and-base-licences__2026-11-19.md
third_party | https://huggingface.co/api/models?search=MeditronFO | 2026-11-19 | yes | true | community GGUF and MLX conversions exist (listing only, conversions not opened); file third_party__community-quantisations__2026-11-19.md
technical_report | https://arxiv.org/abs/2509.14233 | 2026-11-19 | yes | false | Apertus technical report (base model); linked from the base card, not fetched; nothing scored on it
docs | https://huggingface.co/swiss-ai/Apertus-70B-2509/blob/main/Apertus_EU_Public_Summary.pdf | 2026-11-19 | yes | false | EU AI Act public summary of the base model, linked from the base card; PDF not fetched; nothing scored on it
docs | https://huggingface.co/swiss-ai/Apertus-70B-2509/blob/main/Apertus_EU_Code_of_Practice.pdf | 2026-11-19 | yes | false | Apertus Code of Practice document, linked from the base card; PDF not fetched; nothing scored on it
model_card | https://huggingface.co/utter-project/EuroLLM-22B-Instruct | 2026-11-19 | unknown | false | base named on EPFLiGHT/EuroLLM-22B-MeditronFO; API and raw files return HTTP 401; follow-up scope only
model_card | https://huggingface.co/utter-project/EuroLLM-9B-Instruct | 2026-11-19 | yes | false | gated=auto, card and raw files HTTP 401; licence tag apache-2.0 from API only; follow-up scope only
security | https://github.com/EPFLiGHT/FullyOpenMeditron/blob/main/SECURITY.md | 2026-11-19 | no | false | raw SECURITY.md is HTTP 404; no vulnerability-disclosure policy found in the code repository or on the model cards
terms | none found | 2026-11-19 | no | false | no separate terms of use, acceptable-use policy or medical-use licence addendum found for the weights; the only use statements are in the cards, project page and dataset card
docs | https://jointhemoove.org/ | 2026-11-19 | yes | false | MOOVE clinician evaluation platform, linked from the cards; not fetched; MOOVE vignettes are stated to be non-public
```
