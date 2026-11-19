# berget - primary-source clauses

Berget's own documents are readable by curl (HTTP 200, server-rendered). Verbatim governing text
for the documents used by the entry is stored in the `__2026-11-19.md` files in this folder. The
earlier scaffold (which marked the DPA, docs and pricing as not retrieved) is superseded by the
table below.

## _sources.md (2026-11-19 re-verification, rubric 1.2)
```
doc_type       | source_url                                      | retrieval_date | exists | retrieved | notes
terms          | https://berget.ai/en/terms                      | 2026-11-19     | yes    | yes       | Page stamp 2026-10-16. Sec 7 content never stored; Sec 17.1 customer retains IP; Sec 18 mutual confidentiality incl. Customer Data (Sec 18.5 cease use and destroy on termination); Sec 19.1 aggregated anonymised data right; Sec 6.7 TOMs and ISO 27001 "actively working toward". See terms__tos-2026-10-16__2026-11-19.md
dpa            | https://berget.ai/en/dpa                        | 2026-11-19     | yes    | yes       | Last updated 2026-10-22. NEW: Appendix 2 express no-training sentence and no persisted disk even during inference; Sec 10.1 DC choice excludes serverless inference, all DCs in the EEA; four sub-processors (Toriv AB dropped). See dpa__dpa-2026-10-22__2026-11-19.md
sla            | https://berget.ai/en/sla                        | 2026-11-19     | yes    | yes       | Last updated 2026-10-23. NEW: serverless best effort with no compensation; 99.5% with credits only for Dedicated Inference HA. See sla__sla-2026-10-23__2026-11-19.md
sla            | https://status.berget.ai/ (and /en/status)       | 2026-11-19     | yes    | no        | JavaScript shell only (title "Berget AI Status"). Incident history and uptime unreadable; not scored on.
privacy_policy | https://berget.ai/en/privacy                    | 2026-11-19     | yes    | yes       | Website privacy policy dated 2025-03-10; contains no Sweden-only or zero-retention statement (the stored ev-privacy claim was wrong). See privacy_policy__website-policy__2026-11-19.md
security       | https://berget.ai/en/security                   | 2026-11-19     | yes    | yes       | Responsible disclosure page only; no TOMs, no attestations. See security__responsible-disclosure-page__2026-11-19.md
security       | (SOC 2 / ISO 27001 / pen-test attestation)       | 2026-11-19     | no     | no        | None found on any Berget page; ISO 27001 is "actively working toward" (ToS 6.7). Recorded exists: no.
docs           | https://docs.berget.ai/ (+ llms.txt, .md pages)  | 2026-11-19     | yes    | yes       | Now readable. Model lifecycle policy (2 to 3 weeks notice for Active models) and retired-model list. See docs__model-catalogue-and-lifecycle__2026-11-19.md
docs           | https://api.berget.ai/v1/models                 | 2026-11-19     | yes    | yes       | 15 catalogue entries with prices, licences, lifecycle status.
marketing      | https://berget.ai/en/pricing                    | 2026-11-19     | yes    | yes       | Plans; no pure pay-as-you-go; per-model table JS-rendered (rates taken from the API listing). See marketing__pricing-landing-dedicated__2026-11-19.md
marketing      | https://berget.ai/en                            | 2026-11-19     | yes    | yes       | Landing claims (Swedish jurisdiction, zero data retention, no US entity involvement).
marketing      | https://berget.ai/en/dedicated-inference        | 2026-11-19     | yes    | yes       | Dedicated Inference now offered (sales-led), SLA-backed; AMD MI300X named.
marketing      | https://berget.ai/en/blog/berget-code-launch    | 2026-11-19     | yes    | yes       | 2026-05-13 launch post: "stays within Sweden's borders", no training on code.
third_party    | https://mastra.ai/models/providers/berget       | 2026-11-19     | yes    | yes       | Mastra lists 6 Berget models via the router; OpenAI-compatible.
third_party    | https://tech.eu/2026/02/02/swedish-startup-berget-ai-lands-2-1m-as-demand-grows-for-sovereign-ai-in-europe/ | 2026-11-19 | yes | yes | Link live (HTTP 200); content not re-quoted.
acceptable_use | https://berget.ai/en/acceptable-use             | 2026-11-19     | yes    | yes       | Last updated 2026-04-14. EU AI Act customer-responsibility clauses; no data-use clause read.
```
