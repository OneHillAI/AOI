# fireworks-ai - primary-source clauses

**CORRECTED 2026-09-21** after an independent Cowork browser verification pass - see
[`browser-verified/`](browser-verified/) for the full capture and
[`RESEARCH-RETURN__fireworks-ai__2026-09-20.md`](browser-verified/RESEARCH-RETURN__fireworks-ai__2026-09-20.md)
for the field-by-field findings. The prior version of this file (2026-09-20) claimed the Terms of
Service and DPA had been downloaded and parsed as PDFs; an independent real browser session could
not reproduce that - both pages are page-level noindexed and return ROBOTS_DISALLOWED. That claim
is not necessarily false (a non-robots-respecting fetch could reach content a browser cannot), but
it is not independently verified, and `inference-providers/fireworks-ai/entry.yaml` has been
corrected accordingly (confidentiality: functional_only -> unknown; subprocessors_disclosed:
true -> false; trains_on_inputs: never -> opt_in_only).

## _sources.md
```
doc_type       | url                                                                           | exists | retrieved | notes
terms          | https://fireworks.ai/terms-of-service                                        | yes    | NO        | UNCONFIRMED. Page-level noindexed, ROBOTS_DISALLOWED to a real browser (both with/without trailing slash). A prior claim of having downloaded/parsed this as a PDF is not independently verified. ZDR clause, confidentiality direction NOT established from this pass.
privacy        | https://fireworks.ai/privacy-policy                                          | yes    | yes       | Independently browser-read. Verbatim no-training-without-opt-in + no-log-for-open-models statements. Substitute grounding for the training claim (see trains_on_inputs).
docs           | https://docs.fireworks.ai/guides/security_compliance/data_handling           | yes    | yes       | Independently browser-read, verbatim. Response API default-on storage, 30-day auto-delete, store=false opt-out, DELETE by response_id.
dpa            | https://fireworks.ai/dpa                                                     | yes    | NO        | UNCONFIRMED. Noindexed, not in sitemap, ROBOTS_DISALLOWED; also JS-gated via Trust Center. Sub-processor Schedule (incl. the Anthropic claim) NOT established from this pass.
security       | https://docs.fireworks.ai/guides/security_compliance/data_security           | yes    | yes       | Independently browser-read, verbatim. TLS1.2+/AES-256, logical isolation, least-privilege, pen testing, CMEK.
security       | https://docs.fireworks.ai/faq/enterprise/compliance/certifications           | yes    | yes       | "SOC 2 Type II" + "HIPAA Certified"; no ISO, no dates, no auditor.
marketing      | https://fireworks.ai/blog/fireworks-ai-achieves-soc-2-type-ii-and-hipaa-compliance | yes | yes  | Published 2023-10-27; auditor unnamed; no audit period.
marketing      | https://fireworks.ai/blog/fireworks-triple-iso-certification-enterprise-trust | yes    | yes       | Published 2025-11-19; ISO 27001/27701/42001; auditor unnamed; no dates.
security       | https://trust.fireworks.ai/ (+ /subprocessors)                               | yes    | no        | Fully JS-gated SafeBase; only title/meta render. No dated SOC2 report, no ISO certs, no sub-processor list visible.
docs           | https://docs.fireworks.ai/serverless/pricing                                 | yes    | yes       | Per-token rates, batch 50% discount, US-only-serverless 1.5x premium.
docs           | https://docs.fireworks.ai/guides/ondemand-deployments                        | yes    | yes       | Self-serve dedicated GPU deployments (GPU-second billing); region-pinning gated to sales quota.
marketing      | https://fireworks.ai/blog/virtual-cloud                                      | yes    | yes       | BYOC/Virtual Cloud, GA 2025-06-16, enterprise-negotiated.
sla            | https://status.fireworks.ai/                                                 | yes    | yes       | Per-endpoint 90-day uptime ~99.67-100% (28 components); no SLA/credit clause found in standard Terms.
docs           | https://fireworks.ai/models                                                  | yes    | yes       | Live model catalogue.
docs           | https://docs.fireworks.ai/tools-sdks/openai-compatibility                    | yes    | YES (upgraded) | Independently browser-confirmed: base URL api.fireworks.ai/inference/v1, Chat Completions + Completions. CORRECTION: a prior claim of a Responses API with MCP support was NOT found on this page and has been removed.
```

## Re-read 2026-11-19 (freshness refresh)
The Terms and DPA ARE readable: both page URLs answer with an HTTP 308 redirect to a text-extractable PDF on cdn.sanity.io (robots.txt currently allows all). The 2026-09-20 browser pass saw a noindex/ROBOTS_DISALLOWED result and recorded them as unreachable; that was a limit of that route, not an absence of text. Clause extracts are in the dated files named below. The sub-processor list still cannot be read (Vanta JS-only trust centre).
```
doc_type       | source_url                                                          | retrieval_date | exists | retrieved | notes
terms          | https://fireworks.ai/terms-of-service                               | 2026-11-19     | yes    | YES       | Last Updated July 10, 2026. Sec 3.6 ZDR + no training CONFIRMED; Sec 8 confidentiality is one-directional (Fireworks' information only); 3.2 customer owns Content; 16.1 Delaware. Extract: terms__2026-11-19.md
dpa            | https://fireworks.ai/dpa                                            | 2026-11-19     | yes    | YES       | v3.4 exhibit version. Processor role, 4.5 retention (Response API and prompt caching named), 6 sub-processors by reference to trust.fireworks.ai/subprocessors (30 days notice), 10.1 48h breach notice, 11.2 30-day return, SCC Module Two + UK Addendum. NO Schedule 4, no Anthropic. Extract: dpa__2026-11-19.md
privacy_policy | https://fireworks.ai/privacy-policy                                 | 2026-11-19     | yes    | YES       | No-training "without your explicit opt-in" wording unchanged; Terms are stronger. Extract: privacy_policy__2026-11-19.md
docs           | https://docs.fireworks.ai/guides/security_compliance/data_handling  | 2026-11-19     | yes    | YES       | Adds Batch API exclusion, prompt-cache minutes, metadata logging, enterprise ZDR policy. Extract: docs__data-handling-security__2026-11-19.md
security       | https://docs.fireworks.ai/guides/security_compliance/data_security  | 2026-11-19     | yes    | YES       | Unchanged: TLS 1.2+, AES-256, logical isolation, pen testing; no bug bounty.
security       | https://docs.fireworks.ai/faq/enterprise/compliance/certifications  | 2026-11-19     | yes    | YES       | SOC 2 Type II, ISO 27001/27701/42001, HIPAA; no dates or auditors.
subprocessors  | https://trust.fireworks.ai/subprocessors                            | 2026-11-19     | yes    | NO        | Vanta single-page app; HTTP 200 but only an empty shell renders without JavaScript. List contents (and whether Anthropic is named) UNKNOWN.
security       | https://trust.fireworks.ai/                                         | 2026-11-19     | yes    | NO        | Same Vanta shell; no certificates or reports readable.
docs           | https://docs.fireworks.ai/serverless/pricing                        | 2026-11-19     | yes    | YES       | Kimi K3 3.00/0.30/15.00; US column 1.5x; Priority tier added. Extract: docs__pricing-regions-status__2026-11-19.md
docs           | https://fireworks.ai/pricing                                        | 2026-11-19     | yes    | YES       | Batch 50% off; spot 30% off; GPU per-hour rates; Reserved Throughput "99.9% uptime terms" (not public).
docs           | https://fireworks.ai/models                                         | 2026-11-19     | yes    | YES       | Kimi K3.1 Pro, MiniMax M3.1 Flash, Muse Spark Open, Ember-1, Rune, Ultramarine 1 Flash and others now listed.
docs           | https://docs.fireworks.ai/guides/ondemand-deployments               | 2026-11-19     | yes    | YES       | GLOBAL default; US/CANADA/EUROPE/APAC need quota granted by Fireworks.
docs           | https://fireworks.ai/product/sovereign                              | 2026-11-19     | yes    | YES       | Fireworks Sovereign, enterprise, priced by contract, runs in customer cluster.
sla            | https://status.fireworks.ai/                                        | 2026-11-19     | yes    | YES (status) / n/a (SLA) | 23 components; lowest 99.50%; no incidents; no SLA.
docs           | https://docs.fireworks.ai/tools-sdks/openai-compatibility           | 2026-11-19     | yes    | YES       | Completions + Chat Completions only documented.
docs           | https://docs.fireworks.ai/guides/regions                            | 2026-11-19     | no     | NO        | HTTP 404.
```
