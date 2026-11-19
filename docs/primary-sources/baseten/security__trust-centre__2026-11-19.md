doc_type: security
entity: baseten
source_urls: https://trust.baseten.co/ ; https://trust.baseten.co/resources ; https://trust.baseten.co/subprocessors ; https://trust.baseten.co/updates
retrieval_date: 2026-11-19
exists: yes
retrieved: true for the trust-centre pages (rendered in the in-app browser); false for every gated document behind them (access is by "Request access" and was not requested)
tag: publisher (the vendor's own trust centre; no third-party report or certificate PDF was readable)
read_by: refresh agent 2026-11-19, in-app browser (the Vanta portal is JavaScript-only, so curl returns only a title)

## Why stored
The 2026-09-20 and 2026-11-19 curl reads could not render the Vanta Trust Center and recorded "retrieved: false". Rendered in a real browser it is readable, and it contradicts the 2026-09-21 retraction ("no trace of ISO 27001 anywhere"). Page text below is transcribed from the rendered pages, not from the earlier extracts.

## Overview page, Compliance block (verbatim labels)
"SOC 2", "ISO 27001:2022", "HIPAA", "CCPA" (marked "COMPLIANT"), "CCPA", "GDPR", "PCI DSS - SAQ D".
Reporting line: "If you believe you've discovered a security vulnerability in our services, please report it to security@baseten.co".
No ISO 27701 and no CSA STAR label appears. No FedRAMP authorisation label appears in the Compliance block; a "FedRAMP 20x" document group exists under Resources (below).

## Resources page (document names only; contents NOT read)
SOC 2: "Baseten Labs, Inc. SOC 2 Type 2 Report 5.31.26.pdf"; "Baseten Labs, Inc. SOC 3 Report 5.31.26.pdf" (both "Request access").
ISO 27001: "Baseten Labs, Inc. ISO 27001 Certificate.pdf" ("Request access").
HIPAA: "Baseten Labs, Inc. HIPAA Report 5.31.26.pdf" ("Request access").
Penetration Testing: "Baseten Penetration Test - October 2026.pdf" ("Request access").
PCI-DSS: "PCI-DSS-v4-0-1-AOC-for-SAQ-D-Service-Provider-r1.pdf" ("Request access").
Questionnaires: SIG Lite, CAIQ ("Request access").
Other Documentation: "Customer Data Retention Policy", "Regional Deployments", "Baseten Data Processing Agreement.pdf" (all "Request access").
FedRAMP 20x: "Human Readable Package Overview" PDF (button "View") and its JSON ("Download"), plus Security Decision Record, Ongoing Certification Report and sample incident-report documents ("Request access"). An attempt to open the overview PDF in the pane did not render it; it was not downloaded and not read, so the FedRAMP 20x status is UNVERIFIED. A FedRAMP 20x package is not by itself an authorisation.
Other resources: "Policy Package.zip", "Baseten Cloud Compute Providers.pdf" ("Request access").

## Updates feed (verbatim headlines and dates; the trust centre launched 2026-07-30)
- 2026-07-30 "Baseten Trust Center": launch of a centralised resource for security, privacy, compliance and data protection.
- 2026-08-04 "SOC2 and HIPAA Reports Now Available": "Our latest SOC 2 report and independent third-party HIPAA assessment report are now available ... Customers and partners can request access directly through the Trust Center."
- 2026-08-24 "ISO 27001 Certification": "We're excited to share that our ISO 27001 certification is now available in the Trust Center. ... Customers and partners can visit the Trust Center to learn more and request access to the certification."
- Sub-processor additions: 2026-08-14 Parallel AI (web search), QumulusAI and Argentum AI (cloud compute); 2026-09-03 Global AI (cloud compute); 2026-09-24 Mistral AI (cloud compute); 2026-10-15 Hugging Face (dataset and model storage); 2026-10-21 Datasection (cloud compute); 2026-11-04 additions for Baseten Sandboxes; 2026-11-06 Buzz HPC (cloud compute).

## Subprocessors page (13 results; read in full)
Amazon Web Services (Cloud Infrastructure and Compute, Global); Google Cloud (Cloud Infrastructure and Compute, Global); WorkOS (Single Sign On, United States); Pylon (Customer Support, United States); Slack (Communications, United States); Orb (Invoicing, United States); Hugging Face (Dataset and Model Storage, United States); ClickHouse (analytics database, United States, Baseten Sandboxes); Cloudflare (CDN, closest location to end user, Baseten Sandboxes); OVH Cloud (Cloud Infrastructure, United States, Baseten Sandboxes); PostHog (Product Analytics, United States, Baseten Sandboxes); SigNoz (Observability Platform, United States, Baseten Sandboxes); "Compute Providers" (Cloud Compute, Global, pointing to the gated PDF "baseten-cloud-compute-providers.pdf").
The compute vendors announced in the updates feed (Argentum AI, QumulusAI, Global AI, Mistral AI, Datasection, Buzz HPC) are not itemised on this page; they sit behind the gated compute-providers PDF. Mistral AI is named as a cloud-compute sub-processor.

## What this does and does not establish
- A first-party claim, readable on the vendor's own rendered page, that Baseten holds ISO 27001:2022 and a PCI DSS SAQ D attestation of compliance, in addition to SOC 2 Type 2 and HIPAA. The certificate, the SOC 2 and SOC 3 reports, the pen test and the PCI AOC were NOT readable, so no third-party artefact backs these labels in this entry. Scoring therefore treats them as publisher claims (a score of 5 on compliance would need a retrieved third-party attestation).
- It reverses the 2026-09-21 retraction of ISO 27001. The earlier statement "no trace of ISO 27001 anywhere" was true only of the pages that could be fetched without JavaScript; the announcement is dated 2026-08-24, before that baseline.
- The sub-processor list is now read (13 rows), but the full compute-provider roster is gated.
