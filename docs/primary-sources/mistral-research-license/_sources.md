# mistral-research-license - primary-source clauses (2026-08-03)

Split from the aggregate `mistral` primary-sources on the LICENCE axis. This entry is the
non-commercial Mistral line: MRL (research-only) and MNPL (non-production). Clauses carried
verbatim from the aggregate `mistral/_sources.md` (retrieved 2026-07-25).

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
docs | https://docs.mistral.ai/getting-started/models/weights | 2026-07-25 | yes | true | per-model license (Apache-2.0 / MRL / MNPL)
license | https://mistral.ai/licenses/MRL-0.1.md | 2026-07-25 | yes | true | research/non-commercial only
license | https://mistral.ai/licenses/MNPL-0.1.md | 2026-07-25 | yes | true | non-production only
model_card | https://huggingface.co/mistralai | 2026-07-25 | yes | true | per-variant HF tags: Pixtral-Large-Instruct-2411 = mrl
```

## per-model licence assignment (Mistral weights doc) - VERBATIM
source_url: docs.mistral.ai/getting-started/models/weights | exists: yes | retrieved: true
[Apache-2.0] "Mistral 7B, Mixtral 8x7B/8x22B, Codestral Mamba, Mathstral, Mistral Nemo, Pixtral 12B, Mistral Small, Magistral Small and Devstral Small are under Apache 2 License." -> these are the `mistral` entry.
[MNPL] "Codestral is under Mistral AI Non-Production (MNPL) License." -> this entry.
[MRL] "Ministral 8B, Mistral Large, and Pixtral Large are under Mistral Research License." -> this entry.

## license MRL-0.1 (Ministral 8B, Mistral Large, Pixtral Large) - VERBATIM
source_url: mistral.ai/licenses/MRL-0.1.md | exists: yes | retrieved: true
[Research only] use "solely for (a) personal, scientific or academic research, and (b) for non-profit and non-commercial purposes"; excludes revenue activity + SaaS distribution. France/Paris jurisdiction. Commercial use requires a separately negotiated licence.

## license MNPL-0.1 (Codestral) - VERBATIM
source_url: mistral.ai/licenses/MNPL-0.1.md | exists: yes | retrieved: true
[Non-Production only] "You shall only use the Mistral Models and Derivatives for testing, research, Personal, or evaluation purposes in Non-Production Environments." No commercial supply "including...SaaS, cloud instances." Outputs unowned by Mistral. France/Paris. Commercial/production use requires a separately negotiated licence.

## boundary
The Apache-2.0 flagship models (Mistral 7B, Mixtral, Nemo, Mistral Small, Codestral Mamba, Mathstral, Devstral Small, Pixtral 12B) are the `mistral` entry - NOT this one. Verify the per-model tier against Mistral's weights doc.
