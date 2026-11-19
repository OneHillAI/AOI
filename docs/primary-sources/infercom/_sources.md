# infercom - primary-source clauses

Re-read 2026-11-19 by a code session. infercom.ai, docs.infercom.ai, status.infercom.ai and the CSA registry
were fetched directly (HTTP 200) with a browser user agent, so the 403 and PDF blocks recorded in earlier passes
no longer apply. The DPA v1.4 PDF was read in full for the first time (text extracted with macOS PDFKit); the
v1.3 PDF that the stored entry rested on is superseded. Clause extracts are in the `*__2026-11-19.md` files in
this folder. Earlier rows from the 2026-07-25 and 2026-08-06 passes are superseded where a 2026-11-19 row exists.

## _sources.md
```
doc_type       | source_url                                                              | retrieval_date | exists | retrieved | notes
privacy_policy | https://infercom.ai/privacypolicy/                                      | 2026-11-19     | yes    | yes       | Version 2.4, Last Updated 2026-10-30 (entry held v2.2). Zero content retention, no training (Sec 4.3, 11.2); metadata 90 days; sub-processors now named in Sec 7.1 (SambaNova, Auth0, Stripe, Metronome, TECLIB); SambaManaged note; Global Catalog routes prompt content outside the EEA, primarily US (Sec 8.1). See privacy_policy__v2.4__2026-11-19.md
terms          | https://infercom.ai/termsconditions/                                    | 2026-11-19     | yes    | yes       | Version 2.1, 2026-03-09, unchanged. Sec 2.1 US operator SambaNova; Sec 2.4 no training; Sec 6 customer owns Input/Output; Sec 8.2 SLAs only for Reserved/Dedicated; no confidentiality clause over inputs. See terms__v2.1__2026-11-19.md
dpa            | https://infercom.ai/Infercom_DPA_v1.4_dl.pdf                            | 2026-11-19     | yes    | yes       | v1.4, 24 September 2026 (entry held v1.3). First full read. EU-only inference, Non-EU Models excluded and need a separate addendum, SambaNova remote access under SCCs Module Three, 5-entry sub-processor table that does not match the Privacy Statement table, 48-hour breach notice. See dpa__v1.4__2026-11-19.md
security       | https://infercom.ai/iso-27001-certificate.pdf                           | 2026-11-19     | yes    | yes       | Proks Certification GmbH, LU-IS-20250253, valid 2025-12-16 to 2028-12-15, scope Inference as a Service. Third-party attestation read at source. See security__iso-27001-csa-star__2026-11-19.md
security       | https://cloudsecurityalliance.org/star/registry/infercom/services/infercom-inference-as-a-service | 2026-11-19 | yes | yes | STAR for AI Level 1, AI CAIQ self-assessment v1.1.0, listed 2026-07-02. Self-assessment, not an audit
security       | https://infercom.ai/trust/                                              | 2026-11-19     | yes    | yes       | Server-rendered. "SOC 2: Not yet"; SambaNova is "a US company with operational access to the Munich facility"; no private connectivity; vulnerability reports by e-mail to the DPO
sla            | https://status.infercom.ai/                                             | 2026-11-19     | yes    | yes       | Atlassian Statuspage, component since 2025-12-31; one public major incident (2026-06-19); no SLA on the page. See docs__catalogue-pricing-status__2026-11-19.md
sla            | (SLA for Reserved Capacity and Dedicated Rack)                          | -              | yes    | no        | Terms Sec 8.2: available "under separate agreement"; the SLA text itself is not public
marketing      | https://infercom.ai/pricing                                             | 2026-11-19     | yes    | yes       | EUR per-token rates for 4 EU models and 1 Global model; Dedicated and On-Premises per engagement
docs           | https://docs.infercom.ai/en/models/infercomcloud-models ; /rate-limits ; /deprecations ; /dedicated/models | 2026-11-19 | yes | yes | Current catalogue, rate limits, deprecation policy (2 to 3 weeks notice), dedicated catalogue
docs           | https://infercom.ai/on-premises ; https://infercom.ai/sovereign-ai      | 2026-11-19     | yes    | yes       | On-prem and air-gap still shipped; sovereign-ai page states SambaNova remote access
subprocessors  | (SambaNova Annex III further sub-processors)                            | -              | yes    | no        | DPA Sec 7(6): available to customers on request only
third_party    | https://sambanova.ai/blog/infercom-qna                                  | 2026-11-19     | yes    | yes       | Partner Q&A re-read; no longer carries the Equinix, BF16 or 10x statements the entry cited
third_party    | https://opper.ai/blog/infercom-partnership                              | 2026-11-19     | yes    | yes       | Updated October 2026; lists EU, US and JP regions and repeats "no exposure to the US CLOUD Act" (partner marketing)
third_party    | https://www.businesswire.com/news/home/20251022464116/en/SambaNova-Powers-the-AI-Backbone-for-Three-Sovereign-AI-Providers-Across-Australia-Europe-and-the-UK | 2026-11-19 | yes | no | Connection failed (curl HTTP code 000) from this session; not re-read
```
