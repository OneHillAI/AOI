# Research return: together-ai (FULL re-verification) - 2026-09-20

## Decisive questions - CONFIRM / CORRECT
1. Sec 9 confidentiality still expressly disclaimed? -> CONFIRMED UNCHANGED. Sec 9 (titled "Confidentiality"), current ToS Updated 2026-05-19, verbatim x2: "The parties will have no confidentiality obligations to each other unless otherwise agreed in writing." confidentiality = disclaimed; the data-governance cap at 3 remains justified. (Also captured: retention not-stored only if ZDR enabled/opt-in; training only with explicit opt-in; customer owns content+output; California law; 12-mo liability cap.)
2. No embedding models via serverless? -> CONFIRMED REAL (not a rendering artefact). Serverless-models page verbatim: "There are currently no embedding models offered via serverless." Rerank + moderation also absent (rerank dedicated-only). The prior-entry reversal is verified.
3. Mistral/Mixtral absent from serverless? -> CONFIRMED absent from serverless; present ONLY under fine-tuning (Mixtral 8x7B Instruct v0.1, supervised FT ~$1.05). Fine-tuning-only.

## Field-by-field
| Field | Value | Grounded |
|-------|-------|----------|
| confidentiality | DISCLAIMED (Sec 9, verbatim x2) - caps data-governance at 3 | terms |
| retention | not stored only if ZDR enabled (opt-in); else standard processing | terms Sec 3 / privacy 2.6 |
| training-on-inputs | only with explicit opt-in (never by default) | privacy 2.2 |
| customer IP | customer owns content + output (Sec 7) | terms |
| dpa / sub-processors | DPA = linked PDF (legal/dpa 404s); Annex III names AWS, Mailgun, Amplitude, Sentry, OpenAI, Together Software, Hotjar, Intercom, Absorb | dpa PDF |
| compliance | SOC 2 Type 2 (blog 2025-07-08), HIPAA, ISO 27001:2022 referenced; report contact/NDA-gated; trust center JS-gated | publisher; trust:false |
| SLA | no public committed SLA (enterprise-contract only); status all-online | status; sla:false |
| catalogue | NO serverless embeddings/rerank/moderation; NO Mistral/Mixtral in serverless (FT-only) | docs (verbatim x2) |
| pricing | serverless per-token published; dedicated single-tenant + on-demand GPU hourly; largest-scale "contact us" | pricing |
| governing law / liability | California; 12-mo cap (Sec 13) | terms |

## URL corrections for the entry
- together.ai/legal/dpa -> 404; DPA lives at the cdn.prod.website-files.com "Together DPA (Website).pdf" link.
- together.ai/security -> 404 (moved); use the SOC2 blog + trust.together.ai (JS-gated).

## Net
No governance reversal: confidentiality:disclaimed holds (cap at 3). The catalogue changes (no serverless embeddings/rerank; Mistral/Mixtral FT-only) are verified real. Transparency: Terms + Privacy published and legible (read directly); DPA is a findable PDF; trust center content not machine-readable.

## RE-DO
Authenticated/JS render of trust.together.ai for dated SOC2/ISO artefacts; DPA effective date is not visible on the PDF.
