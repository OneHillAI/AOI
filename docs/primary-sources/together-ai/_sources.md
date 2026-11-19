# together-ai - primary-source clauses

Re-read 2026-11-19 by a code session; together.ai, docs.together.ai, status.together.ai, support.together.ai and the
DPA PDF were fetched directly (HTTP 200) with a browser user agent. The trust centre is a Vanta single-page app and
could not be read. The human-supervised baseline in [`browser-verified/`](browser-verified/) (2026-09-20) is kept; the
2026-11-19 extracts in this folder supersede it where they differ (notably default retention, passthrough models,
residency, status page and the catalogue). Earlier rows from the 2026-07-25 search-extraction pass are superseded.

## _sources.md
```
doc_type       | source_url                                                          | retrieval_date | exists | retrieved | notes
terms          | https://www.together.ai/terms-of-service                            | 2026-11-19     | yes    | yes       | "Updated May 19, 2026", unchanged. Sec 9 still reads "The parties will have no confidentiality obligations to each other unless otherwise agreed in writing" (disclaimed). Sec 1 disclaims uptime; Sec 4 bars sending financial, medical or sensitive personal data. See terms__terms-of-service__2026-11-19.md
privacy_policy | https://www.together.ai/privacy                                     | 2026-11-19     | yes    | yes       | "Updated December 17, 2025", unchanged. ZDR is opt-in (Sec 2.6); training opt-in only; playground history stored by default (Sec 2.7). See privacy_policy__privacy-policy__2026-11-19.md
dpa            | https://cdn.prod.website-files.com/5ce11396d0cadb55a02cabf7/696024ff5649fb30b125686c_Together%20DPA%20(Website).pdf | 2026-11-19 | yes | yes | No effective date on the PDF. Annex III names 9 sub-processors incl. OpenAI OpCo LLC (Generative AI). Annex 1 scope is account and employee data. The earlier "default routing through North America data centres" statement is NOT in this PDF. See dpa__data-processing-addendum__2026-11-19.md
docs           | https://docs.together.ai/docs/privacy-and-security ; /docs/zero-data-retention | 2026-11-19 | yes | yes   | NEW: prompt storage ON by default and "may use them for product improvements"; passthrough models ON by default (data goes to the upstream provider's policy); ZDR is an org-admin toggle that also disables passthrough; private HackerOne programme. See docs__privacy-zdr-geo-ratelimits__2026-11-19.md
docs           | https://docs.together.ai/docs/serverless/geo-specific-inference     | 2026-11-19     | yes    | yes       | NEW: US-only endpoint us-api.together.ai at 1.25x for 8 models; api.together.ai gives no region guarantee; guarantee covers processing only, not storage or logs; no EU serverless endpoint
docs           | https://docs.together.ai/docs/serverless/rate-limits                | 2026-11-19     | yes    | yes       | Serverless is best-effort; SLA only via provisioned throughput (sales); Enterprise and Scale now legacy contracts
docs           | https://support.together.ai/articles/8079447813-eu-data-centres-and-dedicated-model-deployment | 2026-11-19 | yes | yes | EU dedicated endpoints only on Scale and Enterprise plans; article "Last updated 1 year ago", so the tier names may be stale
docs           | https://docs.together.ai/docs/serverless-models                     | 2026-11-19     | yes    | yes       | 24 serverless chat models with API strings, context and quantisation; no embeddings, rerank or moderation. See marketing__pricing-and-catalogue__2026-11-19.md
marketing      | https://www.together.ai/pricing                                     | 2026-11-19     | yes    | yes       | Serverless per-token, dedicated GPU hourly, GPU clusters, fine-tuning, PTU. See marketing__pricing-and-catalogue__2026-11-19.md
sla            | https://status.together.ai/                                         | 2026-11-19     | yes    | yes       | Better Stack status page with per-model 90-day uptime (99.28% to 100%); feed shows two maintenance notices in 2026 and no incident posts since January 2025; no SLA statement. See sla__status-page__2026-11-19.md
sla            | (provisioned throughput / dedicated SLA)                            | -              | yes    | no        | "defined service level agreement" via sales; SLA text not public
security       | https://www.together.ai/blog/soc-2-compliance                       | 2026-11-19     | yes    | yes       | Published 2025-07-08; SOC 2 Type 2 completed, auditor unnamed, report not published; HIPAA/BAA stated. Vendor announcement
security       | https://www.together.ai/blog/iso-27001-2022-certification           | 2026-11-19     | yes    | yes       | NEW: published 2026-06-10; ISO 27001:2022 from A-LIGN (ANAB-accredited); certificate itself not read. See security__soc2-iso-trust__2026-11-19.md
security       | https://trust.together.ai/                                          | 2026-11-19     | yes    | no        | Vanta SPA shell (7.9 KB), no readable content; certificates, SOC 2 report and any sub-processor list not read; not re-scored on
subprocessors  | https://www.together.ai/subprocessors ; /security ; /sla ; /legal/dpa | 2026-11-19   | no     | no        | All return 404. The DPA Annex III (9 names) remains the only readable sub-processor source
security       | (SOC 2 Type II report itself)                                       | -              | yes    | no        | Obtainable only via the trust centre or sales; not obtained
```
