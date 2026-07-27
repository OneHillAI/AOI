# AI Ownership Index - provider primary-document hand-off

**Who this is for:** a Cowork session (or coworker) with normal, unrestricted web access.
**Why it exists:** the coding session that builds the Index runs behind an egress proxy that blocks
or JS-fails several provider sites (trust centres on Vanta SPAs, gated DPAs/PDFs, certificate
registries). The *analysis and writing* happens in the coding session; the *gathering of the
documents the proxy can't reach* happens here.

**The goal:** every rating on a provider must trace to a real binding document that was actually
read - a DPA, a sub-processor list, a certificate - not a trust-centre headline. The test each
finished entry must pass: pick any strong rating and ask **"which primary document, read, says
so?"** There must be a concrete answer.

Companion doc: the model side is done - see [`primary-doc-handover.md`](primary-doc-handover.md).
**This pass is the provider side.**

---

## Status - what's already gathered vs. what this pass needs

The five inference providers were first grounded on 2026-07-25 against their Terms / Privacy, and a
follow-up browser pass captured **summaries** of the harder binding documents into the Drive gather
index (`_SOURCE-LINKS.md`). But two things are still missing before a code session can flip the
evidence to `retrieved: true`:

1. **The five provider folders now exist as scaffolds** - `docs/primary-sources/{berget,infercom,
   groq,deepinfra,together-ai}/` each hold a `_sources.md` that is the outstanding-document
   **checklist** (every row keyed to its entry evidence id, with `exists`/`retrieved` flags and the
   exact clauses to capture). No clause text has been gathered into them yet. Your job is to drop the
   verbatim clause files alongside each `_sources.md` and flip the matching `retrieved: no` rows.
2. **The repo needs the verbatim clause text, not the summary.** `_SOURCE-LINKS.md` captured one-line
   notes ("SCCs+DPF; 5 sub-processors; LU law"). The entries need the **actual operative clauses**
   pasted into per-document clause files so the score is auditable. Several captures were also thin
   or manual (e.g. Groq's sub-processor list scraped from a Vanta SPA) and should be re-read cleanly.

So: **for each document below, open it, paste its governing clauses into
`docs/primary-sources/<provider>/<doc_type>__<detail?>__<YYYY-MM-DD>.md`, and add a `_sources.md`
row.** The code session then grounds the entry and recomputes the ownership verdict.

### Priority order (highest binding value first)

1. **Infercom** - DPA v1.3 + Terms v2.1 (the entry has *no* grounded DPA or terms item at all).
2. **Together AI** - the ~33-entry sub-processor list (it reveals inference may route to third-party
   model APIs - an ownership/residency finding, not a footnote).
3. **Berget** - the GDPR DPA (transfer mechanism + named sub-processors).
4. **Groq** - the named sub-processor list + the Acceptable-Use Policy.
5. **DeepInfra** - the trust/compliance page, and *confirm the genuine gaps* (DPA / SLA).

A **missing document is a finding.** No DPA, no SLA, no certificate → write `exists: no`. That
honest gap is itself the answer, and it is why several dimensions are capped today.

---

## Infercom - `infercom` · highest priority

- **Already grounded (in the entry):** Privacy Policy (`privacy_policy`, infercom.ai/privacypolicy -
  zero prompt/output retention; no training on inference data; metadata-only 90-day logs; the
  **conditional-sovereignty clause**: Global-Catalogue models not on EU infrastructure route prompt
  content to SambaNova outside the EEA, primarily the US, under EC SCCs + EU-US DPF).
- **Still to land as verbatim clause files (summaries exist in `_SOURCE-LINKS.md`, entry item still
  `retrieved: false` or absent):**
  - `dpa` - **DPA v1.3**, https://infercom.ai/Infercom_DPA_v1.3_dl.pdf (proxy-blocked PDF). Capture:
    the **EU-hosted vs Global-catalogue split**, the **SCCs + EU-US DPF** transfer basis, the **five
    named sub-processors**, TLS/EEA-processing terms, and **Luxembourg governing law**. This is the
    single highest-value document in the whole provider pass - `ev-dpa` maps straight to it.
  - `terms` - **Terms of Service v2.1**, https://infercom.ai/termsconditions/ - capture the
    **no-training** commitment, **customer retains input/output**, and **30-day deletion**.
  - `security` - the **ISO 27001 certificate** (cert # LU-IS-20250253, issuer Proks, valid
    2025-12-16 → 2028-12-15) and the **CSA STAR for AI (Level 1, CAIQ v1.1.0)** registry record,
    https://cloudsecurityalliance.org/star/registry/infercom - cite the certificate itself, not just
    the trust-page claim.

## Together AI - `together-ai`

- **Already grounded:** Terms (`terms` - "you exclusively own all right, title and interest in Your
  Content and Output"; no training without explicit opt-in), Privacy (ZDR by default), DPA (EU SCCs +
  UK Addendum), security + OpenAI-compat docs.
- **Still to land:**
  - `subprocessors` - the **sub-processor list**, https://trust.together.ai/ (~33 named; manual
    capture - re-read cleanly). Capture the GPU/hosting regions (US / CA / RO / EU / Global) **and
    especially the AI sub-processors** (the list includes Anthropic, OpenAI, Perplexity, OpenRouter -
    i.e. inference can be routed to third-party model APIs). This is a real residency/ownership
    finding and currently has **no evidence item** in the entry.
  - `security` - the **SOC 2 Type II report** is **not public** (only the announcement blog is).
    Record `exists: no` for the report itself; note ZDR is separately confirmed.
  - `marketing` - the **pricing page**, https://www.together.ai/pricing.

## Berget AI - `berget`

- **Already grounded:** Terms (`terms`, berget.ai/en/terms - "never store any of the actual prompt
  content…or output"; customer retains IP; 30-day deletion; reserved right to *aggregated,
  anonymised* usage data), Privacy (`privacy_policy`, berget.ai/privacy - EU/Sweden-only servers),
  security page (`security`).
- **Still to land (entry items `retrieved: false`):**
  - `dpa` - **GDPR DPA**, https://berget.ai/dpa. Capture the **transfer mechanism** (the gather note
    says **EEA-only, no SCC/DPF** - confirm and quote it) and the **named sub-processor list**. These
    are what would let `data_governance` move back above 4.
  - `docs` - **API docs**, https://docs.berget.ai/ (GDPR / EU-residency framing).
  - `security` - confirm and record `exists: no` if still absent: any **SOC 2 / ISO 27001**
    attestation (the security page appears to be responsible-disclosure only).

## Groq - `groq`

- **Already grounded:** Services Agreement (`terms` - customer retains IP; Groq never trains on
  Customer Data; no default retention; 30-day deletion), Customer DPA, HIPAA BAA, your-data docs,
  trust centre (SOC 2 Type II).
- **Still to land (entry items `retrieved: false`):**
  - `subprocessors` - the **sub-processor list**, https://trust.groq.com/subprocessors (21 named; the
    DPA says it is published here). The prior capture was a manual scrape of a Vanta SPA - re-read and
    paste the actual named entries verbatim.
  - `terms` - the **Acceptable-Use Policy**, https://console.groq.com/docs/legal/ai-policy (effective
    2025-10-15).

## DeepInfra - `deepinfra`

- **Already grounded:** Terms (`terms`, deepinfra.com/terms - customer retains IP; closed-model
  routing carve-out for Google/Anthropic), data-privacy statement (`privacy_policy`), data docs
  (`docs` - zero-retention default, US data centres).
- **Still to land / confirm:**
  - `security` - the **trust/compliance centre**, https://trust.deepinfra.com/compliance. Resolve
    **SOC 2 Type 1 vs Type II** (the page says "Compliant" without specifying), confirm **ISO 27701**
    status, and confirm there is **no named sub-processor list** (record `exists: no` if so).
  - `dpa` / `sla` - the gather found **no signable DPA and no SLA** (the ToS disclaims uptime).
    Confirm both and record `exists: no` - that gap is why residency/compliance are capped.
  - `marketing` - the **pricing page**, https://deepinfra.com/pricing.

---

## Where to save what you find

Create one folder per provider under `docs/primary-sources/` (they don't exist yet), and save each
document's governing clauses as a small text file:

```
docs/primary-sources/
  infercom/
    dpa__v1.3__2026-07-26.md        <- paste the EU/Global split, SCC/DPF, 5 sub-processors, LU law
    terms__v2.1__2026-07-26.md      <- no-training, I/O ownership, 30-day deletion
    security__iso27001__2026-07-26.md
    _sources.md                     <- one line per document (schema below)
  together-ai/
    subprocessors__2026-07-26.md
    _sources.md
  ...
```

Three rules:

1. **One file per document.** Name it `<doc_type>__<detail?>__<YYYY-MM-DD>.md`.
2. **Paste the actual clauses, not a summary.** A short verbatim extract of the governing text
   (transfer mechanism, sub-processors, retention, training, ownership, certificate numbers) plus the
   source URL is enough - no need to commit large PDFs.
3. **Log the source in `_sources.md`.** One line per document:
   `doc_type | source_url | date | exists (yes/no) | retrieved (yes/no) | notes`. A genuine absence is
   `exists: no`.

**`doc_type` vocabulary (use these exact prefixes):**
`terms · privacy_policy · dpa · subprocessors · security · sla · model_card · license ·
technical_report · docs · marketing · third_party`

Then commit and push to the branch. Any session - including the automated weekly review - clones the
repo, so this needs no special access or connector.

---

## The rules (please follow exactly)

1. **Save the real document text**, not a summary or a screenshot of a headline.
2. **Record the source URL and the date.** Undated evidence is weak.
3. **Prefer the binding document.** Residency / training / retention / ownership claims come from the
   DPA, sub-processor list, Terms or Privacy Policy - never a trust-centre or blog page.
4. **A missing document is a finding.** No DPA, no SLA, no certificate → write `exists: no`.
5. **Capture named lists in full.** Sub-processor lists are the point - every named entity and its
   region, verbatim, because that is what the residency and ownership verdicts turn on.

## What happens next (the loop)

- The coding session reads `docs/primary-sources/<provider>/`, rewrites each affected entry's four
  domains from the real text with exact citations, flips the matching evidence to `retrieved: true`,
  and recomputes the ownership verdict.
- The weekly review Routine (`AI Ownership Index - weekly primary-doc review`) ingests new documents,
  re-grounds the affected entries, re-runs validation, and reports what changed and what is still
  outstanding.

## Deferred (not needed yet - for the later phase)

`z.ai` and `platform.moonshot.ai` as inference providers, and the closed frontier models
(GPT / Claude / Gemini) - gather these when that phase starts.
