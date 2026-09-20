# nebius - primary-source clauses

**CORRECTED 2026-09-21** after an independent Cowork browser verification pass - see
[`browser-verified/`](browser-verified/) for the full capture and
[`RESEARCH-RETURN__nebius__2026-09-20.md`](browser-verified/RESEARCH-RETURN__nebius__2026-09-20.md)
for the field-by-field findings. **The single most important row is `ev-tos`**: the binding Terms
of Service (Sec 7) directly contradicts the marketing-adjacent Legal Quick Guide (`ev-quickguide`)
on whether customer content trains Nebius' own models - this was independently CONFIRMED VERBATIM
on re-read, and the entry's central finding stands. Three overstatements were corrected downward
(EU-region count, a claimed inference SLA, and a "dedicated-only" catalogue claim), and compliance
was strengthened (a named SOC 2 auditor).

## _sources.md
```
doc_type       | url                                                                                          | exists | retrieved | notes
terms          | https://docs.tokenfactory.nebius.com/legal/terms-of-service                                 | yes    | yes       | CONFIRMED VERBATIM on independent re-read. Sec 7: trains on Inputs/Outputs BY DEFAULT for Speculative Decoding, opt-out required; reserves right to delete Inputs/Outputs without notice; Sec 10 customer ownership.
docs           | https://docs.tokenfactory.nebius.com/legal/legal-quick-guide                                | yes    | yes       | CONFIRMS the contradiction with ev-tos: "we do not use your content to train...any AI models"; ZDR is an account-level opt-in.
terms          | https://docs.nebius.com/legal/agreement                                                     | yes    | yes       | Master Services Agreement Sec 7.11 (usage-improvement) and Sec 18 (general confidentiality, does not name Customer Content).
dpa            | https://docs.nebius.com/legal/dpa                                                           | yes    | yes       | Processor confidentiality duty scoped to Customer Personal Data; region-pinning for dedicated/AI Cloud, "may vary" for shared endpoints.
subprocessors  | https://docs.nebius.com/legal/sub-processors_tofa                                           | yes    | yes       | CORRECTED (count): ~21 named entities (page summary said 18; a prior draft said ~24) incl. Nebius Inc. (US); 15-day advance notice.
security       | https://nebius.com/blog/posts/soc-2-type-ii-hipaa-iso-27001-enterprise-security-standards   | yes    | yes       | STRENGTHENED: SOC 2 Type II audited by a NAMED firm - Deloitte; ISO 27001 scope explicitly names "AI Studio" (Token Factory). Independently re-read from the exact post (a prior draft only had a search-derived summary).
docs           | https://docs.nebius.com/overview/regions                                                    | yes    | yes       | CORRECTED: only TWO public self-serve EU regions - Finland (eu-north1), France (eu-west1). Spain (eu-south1) and Iceland (eu-north2) are PRIVATE/existing-deployment-only, not public. A prior draft counted all four as public.
sla            | https://docs.nebius.com/legal/sla                                                           | yes    | yes       | CORRECTED (downward): delegates entirely to per-service sub-pages; no number in the master doc itself.
sla            | https://docs.nebius.com/legal/sla-levels                                                    | yes    | yes       | NEW FINDING: lists exactly SEVEN services, NONE of them inference/Token Factory/AI Studio. There is NO committed inference SLA - the 99.9% figure is marketing-only. A prior draft claimed a real contractual SLA existed; this was an overstatement.
sla            | https://status.nebius.com/                                                                  | yes    | YES (upgraded) | Independently browser-read: dedicated "Token Factory" component (Operational); 7 regions; 3 incidents Sep 9-17 2026, all resolved. A prior draft had this as search-corroborated only.
docs           | https://tokenfactory.nebius.com/models/catalog                                             | yes    | yes       | CORRECTED: a prior claim that several flagship models showed "Public endpoint: Not available" (dedicated-only) is NOT supported on re-check - those specific versions are simply superseded by newer catalogue entries (ordinary churn). Open models confirmed publicly served per-token.
docs           | https://docs.tokenfactory.nebius.com/ai-models-inference/dedicated-endpoints/billing-policy | yes    | yes       | PAYG-per-replica; underlying $/GPU-hour rate not disclosed.
docs           | https://nebius.com/services/token-factory                                                  | yes    | yes       | Product page, OpenAI-compatible API framing.
```
