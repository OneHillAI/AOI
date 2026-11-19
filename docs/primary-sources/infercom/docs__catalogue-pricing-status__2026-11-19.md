# Infercom - catalogue, pricing, status, deprecations, on-premises (read 2026-11-19)

## Pricing (https://infercom.ai/pricing, server-rendered). Per 1M tokens, EUR, excluding VAT
EU Sovereign Models: Gemma 4 31B (text + vision, 128K) 0.20 in / 0.35 out; gpt-oss-120b (128K) 0.22 / 0.59;
Whisper Large v3 (speech-to-text) 0.10 input only; E5-Mistral 7B (embeddings, 4K) 0.13 input only.
Global Model Catalog ("Requests processed on global infrastructure outside the EU"): MiniMax M3.1 Flash (1M)
0.60 / 2.40. "No minimums, no commitment." Dedicated Capacity and On-Premises "priced per engagement". Enterprise:
"same per-token rates ... with committed-volume discounts, custom SLAs, priority support".

## Inference API catalogue (https://docs.infercom.ai/en/models/infercomcloud-models)
EU-hosted: gpt-oss-120b, gemma-4-31B-it, E5-Mistral-7B-Instruct, Whisper-Large-v3. Global (Non-EU):
MiniMax-M3.1-Flash ("MiniMax-M3 still works as an alias"). Rate limits (docs.infercom.ai/en/models/rate-limits):
Free 20 RPM / 20 RPD; Developer e.g. gpt-oss-120b 150 RPM / 50,000 RPD, gemma-4-31B-it 80 / 20,000; Enterprise
default gpt-oss-120b 500 / 100,000.
Deprecations (docs.infercom.ai/en/models/deprecations): "Production models will receive a deprecation notice of two
to three weeks at a minimum"; recent retirements: Meta-Llama-3.3-70B-Instruct 2026-11-17, DeepSeek-V3.1 and V3.2
2026-11-03, MiniMax-M2.7 2026-09-30. (The ToS Sec 2.2 still says models may change "without prior notice".)
Dedicated Capacity catalogue (docs.infercom.ai/en/dedicated/models): GLM-5.3 (Preview), MiniMax-M3.1-Flash, MiniMax-M3,
MiniMax-M2.7/M2.5, gpt-oss-120b/20b, Whisper, gemma-4-31B-it, gemma-3, DeepSeek-V3.2 and others; "Availability depends
on the platform release. Confirm a model with us."

## Status (https://status.infercom.ai, Atlassian Statuspage; /api/v2/summary.json and /api/v2/incidents.json read)
Page updated 2026-11-19T16:24Z, all components operational; Infercom Inference Service component since 2025-12-31;
per-model components (gpt-oss-120b, gemma-4-31b-it, E5-Mistral-7B, MiniMax-M2.7, Whisper-Large-v3 as "Sovereign";
DeepSeek-V3.2, Llama-3.3-70B, DeepSeek-V3.1 as "Non Sovereign", all now deprecated per the docs above).
Incident history: one public incident, 2026-06-19 14:33Z to 2026-06-20 11:20Z, impact "major", gemma-4-31B-it
(workaround posted: max_tokens above 64k). One scheduled maintenance announced for 2026-11-20 14:00-17:00 UTC.
No SLA statement on the status page.

## On-premises (https://infercom.ai/on-premises) and Sovereign AI (https://infercom.ai/sovereign-ai)
On-prem still shipped: SambaRack SN40L, "Air-gapped deployment support", "Typically ~90 days from contract to
production", BYOC ("fine-tunes of supported architectures load immediately"), "One contract with Infercom ...
delivered together with SambaNova's engineers". Sovereign AI page: "Our US operating partner SambaNova has remote
access to run the platform; the DPA names it." "Luxembourg company, controlled in Europe, no US parent."
