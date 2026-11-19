# Infercom - Privacy Statement v2.4 (re-read 2026-11-19, verbatim extracts)

Source: https://infercom.ai/privacypolicy/ (HTTP 200, fetched directly). Header: "Last Updated: October 30, 2026 - Version 2.4"
(the stored entry rested on v2.2, 2026-03-09). Controller: Infercom SCS, Luxembourg, RCS B298727.

## Inference data (Sec 4.3, Sec 6, Sec 11.2) - unchanged in substance
- "Infercom does not store, log, or retain the content of your prompts or model outputs. Inference data ... is
  processed transiently - it is passed to the inference engine, a response is generated, and the content is
  discarded. We do not use inference data for model training, fine-tuning, or service improvement."
- "This applies to both EU-Hosted Models and models accessed through the Global Model Catalog."
- Sec 6 retention table: inference data "Not retained - processed transiently"; API request metadata 90 days;
  authentication logs 12 months; account data "Duration of account + 30 days"; billing records 10 years;
  support tickets 3 years after resolution.

## Sub-processors (Sec 7.1) - NEW: named in the Privacy Statement
SambaNova Systems, Inc. (Platform operation, AI inference processing, usage metering; "US; EU infra at Equinix
Munich 4"); Auth0 (Okta, Inc.) (authentication; EU, AWS Frankfurt); Stripe Payments Europe, Ltd. (payments;
Ireland); Metronome, Inc. (usage tracking and billing metering; US); TECLIB SAS / GLPI Network Cloud (support
tickets; France).
- "Note on the SambaManaged platform: The cloud portal (cloud.infercom.ai) and API (api.infercom.ai) are operated
  by SambaNova as an integrated managed service ('SambaManaged'). Infercom maintains contractual control as data
  controller, and all EU-hosted inference processing takes place on Infercom-owned hardware at Equinix Munich 4,
  Germany."
- "We maintain a current list of sub-processors and will notify registered customers of any changes, providing an
  opportunity to object in accordance with our Data Processing Agreement."
- Cookie/website vendors named separately (bunny.net, Pipedrive, MessageBird, Google Analytics/Tag Manager).

## International transfers (Sec 8, 8.1) - unchanged in substance
- "For EU-Hosted Models, your inference data does not leave the EEA."
- "When you use models from Infercom's Global Model Catalog that are not hosted on EU infrastructure, your API
  requests (including prompt content) are routed to SambaNova's global infrastructure outside the EEA, primarily
  in the United States." SCCs (Decision 2021/914) primary mechanism; EU-US DPF additional basis.
- "You can restrict your usage to EU-Hosted Models only by selecting models tagged as 'EU' in the platform."

## Security (Sec 12)
"TLS 1.2+ for data in transit; AES-256 encryption for data at rest"; role-based access, least privilege, MFA for
administrative access; "ISO/IEC 27001:2022 certified"; breach notification to CNPD within 72 hours.
No confidentiality clause over customer inputs appears (personnel confidentiality only, Sec 12 "Personnel").
