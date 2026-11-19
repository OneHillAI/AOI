# sakura-ai-engine - primary-source clauses

Sakura Internet Inc. "AI Engine" (さくらのAI Engine), Japan. Gathered 2026-11-19 by an OneHill agent session. All binding documents are in Japanese and the Japanese text is authoritative (basic terms Art. 3(1)). Each file holds the verbatim Japanese text plus an English reading that is OneHill's own, not lawyer-checked. PDFs were extracted with macOS PDFKit through a Swift one-liner (nothing installed). A research report (`research/inference-providers.md`) was used only to find URLs; every row below was read directly.

```
doc_type | source_url | retrieval_date | exists | retrieved | notes
terms | https://www.sakura.ad.jp/corporate/wp-content/themes/sakura-corporate/assets/pdf/yakkan_ai-engine.pdf | 2026-11-19 | yes | yes | AI Engine service terms, in force 2025-09-24. Art. 10 handling of input/output (not stored in principle, undefined temporary encrypted retention, no use or third-party provision of inputs, no AI training on inputs). Art. 9 model sub-licensing. Art. 13 beta. File: terms__ai-engine-service-terms__2026-11-19.md
terms | https://www.sakura.ad.jp/corporate/wp-content/themes/sakura-corporate/assets/pdf/yakkan_ai-engine-private-edition.pdf | 2026-11-19 | yes | yes | Private Edition option terms, in force 2026-11-02. Japanese corporations only (Art. 3), dedicated GPU only (Art. 2(2)), best effort unless an SLA is written (Art. 11), Art. 9(4) handling of I/O "in principle not". File: terms__private-edition-service-terms__2026-11-19.md
terms | https://www.sakura.ad.jp/corporate/wp-content/themes/sakura-corporate/assets/pdf/%5Ba%5Dyakkan0_kihon.pdf | 2026-11-19 | yes | yes | Basic terms applied from 2023-10-02. Art. 2(5) referenced websites are not part of the terms; Art. 3 Japanese governs; Art. 24 secrecy of communications; Art. 29 liability caps and outage compensation; Art. 32-33 Japanese law, Tokyo District Court. File: terms__basic-terms__2026-11-19.md
terms | https://www.sakura.ad.jp/corporate/agreement/ | 2026-11-19 | yes | yes | Terms index. Confirms the three terms above are the current versions; lists upcoming 2026-11-24 and 2026-11-26 revisions that do not name AI Engine (Blooming Camp and Sakura Cloud). Not saved as a separate file.
privacy_policy | https://www.sakura.ad.jp/corporate/privacy/ | 2026-11-19 | yes | yes | Personal information policy, revised 2024-09-02. Concerns personal information Sakura collects; silent on AI Engine inputs. File: privacy_policy__personal-information-policy__2026-11-19.md
dpa | (none found) | 2026-11-19 | no | no | No data processing agreement, GDPR addendum or processor terms found on the terms index, the AI Engine pages or the manual. Not a retrieval failure: nothing published was located.
subprocessors | (none found) | 2026-11-19 | no | no | No sub-processor list or data-location statement in any binding document. Check sheet item 38 says billing, invoicing and customer support are outsourced, without naming contractors. File: security__security-checksheet-pdf__2026-11-19.md
security | https://www.sakura.ad.jp/corporate/security/ | 2026-11-19 | yes | yes | Certifications and registered scopes: ISMS ICMS-SR0063, ISMS cloud (27017) Cloud-SR0063, ISO 27018 CloudPII-SR0063, ISMAP C21-0030-2, PCI DSS (physical), Privacy Mark, SOC 2/3 for the Ishikari data centre. Scopes name Sakura Cloud, not AI Engine. File: security__information-security-initiatives__2026-11-19.md
security | https://www.sakura.ad.jp/corporate/security/cloud/ | 2026-11-19 | yes | yes | Cloud service information security policy (2018-07-01, revised 2025-01-24). File: security__cloud-security-policy__2026-11-19.md
security | https://www.sakura.ad.jp/corporate/security/policy/ | 2026-11-19 | yes | yes | Basic information security policy (revised 2025-01-24). File: security__basic-security-policy__2026-11-19.md
security | https://www.sakura.ad.jp/corporate/wp-content/themes/sakura-corporate/assets/pdf/security_checksheet.pdf | 2026-11-19 | yes | yes | Company check sheet, updated 2026-11-13; certificate expiry dates (ISMS 2027-04-12, PCI DSS 2027-03-14). File: security__security-checksheet-pdf__2026-11-19.md
security | https://www.sakura.ad.jp/corporate/security/checksheet/ | 2026-11-19 | yes | yes | Landing page for the PDF above. File: security__security-checksheet-page__2026-11-19.md
security | https://manual.sakura.ad.jp/cloud/ismap/index.html | 2026-11-19 | yes | yes | ISMAP scope is Sakura Cloud IaaS in Tokyo and Ishikari zones; AI Engine absent. File: security__ismap-scope-page__2026-11-19.md
security | https://www.sakura.ad.jp/corporate/transparency/ | 2026-11-19 | yes | yes | Transparency report scope excludes AI Engine. File: security__transparency-report-scope__2026-11-19.md
third_party | https://www.sakura.ad.jp/corporate/wp-content/themes/sakura-corporate/assets/pdf/SAKURA_internet_SOC3.pdf | 2026-11-19 | yes | yes | Independent auditor's SOC 3 report, security and availability, Ishikari data centre services, 2025-06-01 to 2026-05-31, opinion dated 2026-07-31. Scope is the data centre, not AI Engine. File: third_party__soc3-ishikari-data-centre__2026-11-19.md
third_party | (SOC 2 Type 2 report, Ishikari data centre; SOC 2 Type 1 report, Sakura Cloud) | 2026-11-19 | yes | no | Disclosed to customers and prospects on request only (per the security page). Not read.
third_party | (ISMS / ISO certificate registry entries, e.g. certification body listings) | 2026-11-19 | unknown | no | Not opened. Certification facts come from Sakura's own security page and check sheet only.
sla | (none for AI Engine) | 2026-11-19 | no | no | The manual says AI Engine is outside the SLA ("品質保証（SLA）の適用対象外です"). Private Edition terms Art. 11 give best effort unless an SLA is written into an order form. Basic terms Art. 29(3) gives limited outage compensation. File: docs__manual-service-basics__2026-11-19.md
sla | https://status.cloud.sakura.ad.jp/ | 2026-11-19 | yes | yes | Status page lists Sakura Cloud components only; no AI Engine entry, so no public uptime history for AI Engine. File: sla__sakura-cloud-status-page__2026-11-19.md
docs | https://help.sakura.ad.jp/status/ | 2026-11-19 | yes | no | Company maintenance and incident page; its incident list is script-rendered and no incident text was readable. Nothing scored on it.
docs | https://manual.sakura.ad.jp/cloud/support/notice-policy.html | 2026-11-19 | yes | yes | Incident and maintenance notice policy, written for Sakura Cloud (2025-02-20). File: docs__sakura-cloud-incident-notice-policy__2026-11-19.md
docs | https://manual.sakura.ad.jp/cloud/ai-engine/01-basics.html | 2026-11-19 | yes | yes | Service basics (2026-11-11): SLA exclusion; requests processed in domestic data centres; I/O not stored; RAG documents kept until deleted. File: docs__manual-service-basics__2026-11-19.md
docs | https://manual.sakura.ad.jp/cloud/ai-engine/03-operation-guide.html | 2026-11-19 | yes | yes | Operation guide (2026-11-11): RAG, file limits, cancellation. No rate-limit table. File: docs__manual-operation-guide__2026-11-19.md
docs | https://manual.sakura.ad.jp/cloud/ai-engine/chat-models.html | 2026-11-19 | yes | yes | Chat models, context lengths, parameter support, preview caveat (2026-11-18). File: docs__manual-chat-models__2026-11-19.md
docs | https://manual.sakura.ad.jp/cloud/ai-engine/06-closed-model.html | 2026-11-19 | yes | yes | Closed-model application flow (2025-12-02). File: docs__manual-closed-models__2026-11-19.md
docs | https://manual.sakura.ad.jp/cloud/ai-license.html | 2026-11-19 | yes | yes | Licences of served models (2026-11-18). File: docs__manual-model-licences__2026-11-19.md
docs | https://manual.sakura.ad.jp/api/cloud/portal/ai-engine-inference-api/index.html | 2026-11-19 | yes | yes | Inference API reference v1.0.1 (OpenAPI portal). Used to confirm endpoints (chat, responses, messages, embeddings, audio) and HTTP 429. Not saved as a separate file.
license | https://secure.sakura.ad.jp/ai/terms-of-use/eula_plamo-2.0.pdf | 2026-11-19 | yes | yes | PLaMo (closed) user licence: no fine-tuning, no personal information input, outputs not for training other LLMs. File: license__closed-model-eula-plamo__2026-11-19.md
license | https://secure.sakura.ad.jp/ai/terms-of-use/eula_cotomi3.pdf | 2026-11-19 | yes | yes | cotomi v3 (closed) usage conditions: internal use, no distillation, no derived models. File: license__closed-model-eula-cotomi3__2026-11-19.md
marketing | https://ai.sakura.ad.jp/sakura-ai/ai-engine/ | 2026-11-19 | yes | yes | Product page, FAQ, price list, API list. Claims "not stored", "ZDR", "completed in Japan". File: marketing__ai-engine-product-page__2026-11-19.md
marketing | https://ai.sakura.ad.jp/sakura-ai/ | 2026-11-19 | yes | yes | Top page and FAQ: "model execution, communication and storage entirely in Japan". File: marketing__sakura-ai-top-page__2026-11-19.md
marketing | https://ai.sakura.ad.jp/sakura-ai/ai-engine-private/ | 2026-11-19 | yes | yes | Private Edition page: dedicated, flat monthly fee per GPU on quote, ZDR claim. File: marketing__private-edition-page__2026-11-19.md
marketing | https://www.sakura.ad.jp/document/ai-engine/ | 2026-11-19 | yes | no | Service brochure download page; not opened.
```

Addendum (2026-11-19):

```
doc_type | source_url | retrieval_date | exists | retrieved | notes
docs | https://manual.sakura.ad.jp/cloud/support/user-support.html | 2026-11-19 | yes | yes | Sakura Cloud support tiers (standard weekdays 10:00 to 18:00 JST; premium 24x7 paid). Does not name AI Engine. File: docs__sakura-cloud-support-tiers__2026-11-19.md
```

```
doc_type | source_url | retrieval_date | exists | retrieved | notes
docs | https://manual.sakura.ad.jp/cloud/ai-engine/tips.html | 2026-11-19 | yes | yes | Tips (2026-05-14): service endpoint gateway to reach api.ai.sakura.ad.jp privately; service policies. File: docs__manual-tips__2026-11-19.md
```
