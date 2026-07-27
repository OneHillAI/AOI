# AI Ownership Index - primary-document hand-off

**Who this is for:** a coworker (or a Cowork session) with normal, unrestricted web access.
**Why it exists:** the coding session that builds the AI Ownership Index runs behind an egress proxy
that blocks many sources (Hugging Face, several provider sites) and cannot reliably read every
model's licence or every provider's real Terms / Privacy / DPA. So the *analysis and writing* is
done in the coding session; the *gathering of the documents the proxy can't reach* is done here.

**The goal:** every claim in the Index must trace to a real primary document that was actually
read - not a marketing page. This is the standard we enforce after an entry once claimed a
provider was "EU-sovereign / adopt / A" on the strength of a trust-centre page, and it collapsed
the moment someone asked "where do the terms say that?". See
[`methodology/primary-source-grounding.md`](../methodology/primary-source-grounding.md) and
[`methodology/ownership.md`](../methodology/ownership.md).

Every piece of evidence in an entry now carries two fields that make its grounding auditable:

- `doc_type` - which kind of primary document it is (`terms · privacy_policy · dpa ·
  subprocessors · security · sla · model_card · license · technical_report · docs · marketing ·
  third_party`).
- `retrieved` - `true` only if the document's **substantive clause text was actually read**;
  `false` if the document is known to exist but was not reachable. A `retrieved: false` item may
  back only a "documented but unverified" statement in the prose.

**Your job is to turn the `retrieved: false` documents below into read text** - open each one,
save its governing clauses, and record the source. The coding session then flips the evidence to
`retrieved: true` with a citation and re-checks the verdict.

---

## Models

**Status (2026-07-25): all ten models are now grounded to the primary-document standard.** A human
coworker gathered the proxy-blocked documents (Hugging Face cards/LICENSE files, arXiv reports,
GitHub READMEs, hosted-API terms/privacy) into per-model clause files under
`docs/primary-sources/<id>/_sources.md`, and each entry's evidence now carries `doc_type` +
`retrieved`, with the ownership factors and verdict rewritten from the read text. What the grounding
changed, per model, is summarised below; the section headings are kept for the next refresh cycle.
The biggest correction: **Soofi** was overclaiming `fully_open`/openness-5 - the read GitHub README
says the weights are "coming soon" and the licence is unconfirmed, so it was re-scored to
`open_weights`/3 (headline 80.4→73.2) and its EU AI Act exemption dropped to `uncertain`.

Earlier only **Mistral** had been re-grounded. **Hugging Face is blocked by the proxy**, so the
model cards and LICENSE files hosted there are precisely what a human was needed to read; the arXiv
reports and GitHub READMEs are usually reachable but are listed so the set is complete.

### Next gather pass - outstanding `retrieved: false` binding docs

These are the only documents still marked `retrieved: false` on a binding doc-type across all ten
models. Each needs a browser a code session can't reach (Hugging Face / ModelScope are proxy-blocked;
Alibaba Model Studio is JS-rendered). Fetch the text, drop it into the matching
`docs/primary-sources/<id>/_sources.md`, and a code session will flip the evidence to
`retrieved: true` and re-check the entry. Priority order:

**P1 - would move substance (a rating or a factual claim could change):**
- [~] **qwen** - Alibaba **Model Studio / DashScope** (`alibabacloud.com/help/en/model-studio/`). *Gather pass 2 (2026-07-25):* the **Model Studio FAQ** now grounds a **no-training** commitment ("never uses your data for model training"; call data stored; AES-256 in transit) → `ev-modelstudio-faq` (docs, retrieved). **Residual:** the formal **Model Studio Service Agreement** - exact retention period, storage region, opt-out mechanics - was still not directly reachable; `ev-terms` stays `retrieved: false` for those binding specifics only.
- [ ] **soofi** - the **LICENSE file** on `huggingface.co/Soofi-Project/Soofi-S-Base` (returned **HTTP 401** this round) and any published SPDX. This is the gating item for the openness re-score: if the permissive open licence has landed and weights are downloadable, openness goes back toward 5 and the EU AI Act exemption from `uncertain` → `yes`. Re-check when the "coming soon" release lands.

**P2 - confirmation only (expected to match the current grounded claim, would just flip `retrieved` → true):**
- [~] **glm** - *Gather pass 2:* GLM-4.6 HF card **re-confirms "License: mit"** via metadata; family MIT stays grounded on the real GLM-5.2 LICENSE already captured. **Residual:** an in-repo LICENSE file was still not visible, and the `modelscope.cn/organization/ZhipuAI` mirror card is unfetched - both low-value.
- [x] **gpt-oss** - *Gather pass 2:* `huggingface.co/openai/gpt-oss-120b` card metadata "License: apache-2.0" captured (`model_card`, retrieved), corroborating the GitHub LICENSE.
- [x] **mistral** - *Gather pass 2:* `huggingface.co/mistralai` per-variant tags captured (`model_card`, retrieved) - Mistral-Small-4-119B-2603 = apache-2.0; Pixtral-Large-Instruct-2411 = mrl.
- [ ] **qwen** - `modelscope.cn/organization/qwen` mirror card (not fetched in pass 2; optional, low-value given the Apache-2.0 HF tags already grounded).

When a P1 item lands, note the changed rating in the entry's changelog and here; P2 items need no changelog beyond flipping `retrieved`.

For every model, get: **model card (per variant) · LICENSE (per variant) · technical report /
paper · acceptable-use / usage policy · repository README · published evaluations.** Where the
publisher also runs a first-party API the entry discusses, add that API's **terms + privacy** -
the hosted-service data terms are separate from the weights licence (the same split the Mistral
entry now captures).

### Mistral - `mistral` · done (the exemplar to copy)
- **Already read:** the hosted-API data terms - Privacy Policy, the training-opt-out / 30-day
  retention / ZDR help-centre articles.
- **Still outstanding:** the weights docs page (`docs`,
  docs.mistral.ai/getting-started/models/weights), the **MRL-0.1** licence text (`license`,
  mistral.ai/licenses/MRL-0.1.md) and the **MNPL** text, and the **DPA** (`dpa`,
  legal.mistral.ai/terms/data-processing-addendum).

### Ai2 OLMo - `ai2-olmo` (fully open - mostly papers + data licence)
- `model_card` - model cards on https://huggingface.co/allenai (per OLMo 2 / OLMo 3 variant).
- `license` - the Apache-2.0 LICENSE on each repo; and the **Dolma data licence**,
  https://huggingface.co/datasets/allenai/dolma.
- `technical_report` - the OLMo 2 / OLMo 3 technical reports (allenai.org/olmo + the arXiv PDFs).
- `docs` - repo README, https://github.com/allenai/OLMo.

### Meta Llama - `meta-llama` (the licence is the crux)
- `license` - the **Llama Community License** full text, https://www.llama.com/llama4/license/,
  **plus the per-version licence files** (Llama 3.1 / 3.2 / 3.3 / 4 each differ) - capture the
  **EU multimodal restriction** and the 700M-MAU clause verbatim.
- `terms` - the **Acceptable Use Policy**, https://www.llama.com/llama4/use-policy/ (and the
  Responsible Use Guide, https://www.llama.com/responsible-use-guide/).
- `model_card` - per-version cards on https://huggingface.co/meta-llama.

### DeepSeek - `deepseek` (weights vs hosted service are different documents)
- `license` - the **MIT LICENSE per checkpoint** (verify each: V3, R1, …), e.g.
  https://huggingface.co/deepseek-ai/DeepSeek-R1 - some repos carry a model-specific licence, so
  do not assume MIT everywhere.
- `technical_report` - the DeepSeek-V3 and DeepSeek-R1 papers (arXiv).
- `privacy_policy` / `terms` - the **hosted DeepSeek service** Privacy Policy + Terms
  (deepseek.com), separate from the weights and carrying the China-jurisdiction data treatment -
  the same hosted-vs-weights split as Mistral.

### Alibaba Qwen - `qwen` (per-checkpoint licence split)
- `license` - **per checkpoint**: Apache-2.0 on the mainstream Qwen3 sizes vs the **Qwen /
  Tongyi Qianwen community licence** on others - read each model card's licence on
  https://huggingface.co/Qwen; do not generalise one licence across the family.
- `technical_report` - the Qwen3 technical report (arXiv).
- `terms` / `privacy_policy` - DashScope / Alibaba Cloud Model Studio API terms + privacy, if the
  entry's hosted-use notes are to be grounded.

### OpenAI gpt-oss - `gpt-oss` (Apache, mostly reachable)
- `license` - Apache-2.0 LICENSE, https://github.com/openai/gpt-oss.
- `model_card` / `technical_report` - the model card + report, https://arxiv.org/abs/2508.10925.
- `terms` - the gpt-oss **usage policy**; `security` - the published safety report (and the METR
  third-party review, metr.org).

### Zhipu / Z.ai GLM - `glm` (per-variant licence - read each)
- `license` - **MIT** for GLM-4.5 / 4.6 / 0414
  (https://huggingface.co/zai-org/GLM-4.6/blob/main/LICENSE) **vs the custom "glm-4" licence** for
  the original 9B (https://huggingface.co/THUDM/glm-4-9b/blob/main/LICENSE) - capture both.
- `model_card` - cards on https://huggingface.co/zai-org.
- `terms` / `privacy_policy` - **api.z.ai** terms + privacy if hosted use is discussed (China
  jurisdiction).

### Moonshot Kimi - `kimi` (the Modified-MIT clause)
- `license` - the **Modified MIT** text, https://github.com/moonshotai/Kimi-K2/blob/main/LICENSE -
  capture the **100M-MAU / $20M-revenue attribution clause** verbatim (it is why this is not plain
  MIT).
- `model_card` - https://huggingface.co/moonshotai/Kimi-K2-Instruct;
  `technical_report` - https://arxiv.org/abs/2507.20534.
- `terms` / `privacy_policy` - **platform.moonshot.ai** terms + privacy if hosted use is discussed.

### Soofi-S - `soofi` (OSAID open-science release)
- `license` - the LICENSE on https://huggingface.co/Soofi-Project/Soofi-S-Base (final SPDX may be
  pending - note which).
- `technical_report` - the pretraining report, https://arxiv.org/abs/2607.09424, and the
  **data-accounting / per-source data** doc; repo https://github.com/soofi-project/Soofi-Pretraining.
- `docs` - confirm the **closed-beta access** status (is the model actually downloadable yet?).

### EuroLLM - `eurollm` (EU Apache-2.0)
- `license` - Apache-2.0, https://huggingface.co/utter-project/EuroLLM-9B-Instruct.
- `technical_report` - https://arxiv.org/abs/2506.04079; `model_card` - the 9B / 1.7B cards on
  https://huggingface.co/utter-project.
- `docs` - confirm **data and evaluation openness** (is the training data / eval released, or
  weights-only?).

---

## Inference providers (all five re-grounded 2026-07-25; a few gaps remain)

> **The active provider pass now lives in its own focused brief:
> [`provider-primary-doc-handover.md`](provider-primary-doc-handover.md).** Use that - it has the
> current per-provider outstanding docs, the priority order, and the folder setup (no provider
> folders exist under `docs/primary-sources/` yet). The section below is kept for context.

Each provider was re-grounded on 2026-07-25 against its actual documents. Below, the "already
read" line is cited in the entry; **the "still outstanding" line is what needs a human read.**

Priority order for the outstanding work: **Berget DPA → Infercom DPA → Groq sub-processors/AUP →
DeepInfra trust/compliance → Together pricing.** The two DPAs are the highest value - binding
documents the proxy could not open, carrying the sub-processor lists and transfer mechanisms the
residency/compliance scores depend on.

### Berget AI - `berget` · 76.4/B · ownership: substantial · **re-audit priority**
- **Already read:** Terms of Service (`terms`, berget.ai/en/terms - "never store any of the actual
  prompt content…or output"; customer retains IP; 30-day post-termination deletion; note the
  reserved right to *aggregated, anonymised* usage data), Privacy Policy (`privacy_policy`,
  berget.ai/privacy - EU/Sweden-only servers), the security page (`security`, berget.ai/en/security).
- **Still outstanding:**
  - `dpa` - **GDPR DPA**, https://berget.ai/dpa - **the key binding document still unread.** Its
    transfer mechanism (SCCs?) and **sub-processor list** were not reachable; they are what would
    let `data_governance` move back above 4.
  - `docs` - **API docs**, https://docs.berget.ai/ (endpoint confirmed via a third party, page not read).
  - `marketing` - **pricing**, https://berget.ai/pricing.
  - Confirm and record `exists: no` if still absent: any **SOC 2 / ISO 27001** attestation.

### Infercom - `infercom` · 80.0/B · ownership: substantial
- **Already read:** Privacy Policy (`privacy_policy`, infercom.ai/privacypolicy - zero prompt/
  output retention, no training on inference data, metadata-only 90-day logs, **and the
  conditional-sovereignty clause: Global-Catalogue models not hosted on EU infrastructure route
  prompt content to SambaNova outside the EEA, primarily the US, under EC SCCs + EU-US DPF**).
- **Still outstanding:**
  - `dpa` - **DPA v1.3**, https://infercom.ai/Infercom_DPA_v1.3_dl.pdf - **the PDF is 403 behind
    the proxy; its operative clauses (TLS/EEA-processing, SCCs, sub-processors) are unread.**
    Highest value alongside Berget's DPA.
  - `terms` - **Terms of Service** - substantive text was not recoverable; obtain it.
  - The **ISO 27001 certificate** and **CSA STAR** registry record themselves (the entry cites the
    attestation, not the certificate document).

### Groq - `groq` · 72.4/B · ownership: substantial
- **Already read:** Services Agreement (`terms` - customer retains IP; Groq never trains on
  Customer Data; no default retention; 30-day deletion), the Customer DPA, the HIPAA BAA, the
  your-data docs, the trust centre (SOC 2 Type II).
- **Still outstanding:**
  - `subprocessors` - **sub-processor list**, https://trust.groq.com/subprocessors - the DPA says
    it is published there; capture the actual named entries.
  - `terms` - **Acceptable Use Policy**, https://console.groq.com/docs/legal/ai-policy.

### DeepInfra - `deepinfra` · 62.8/C · ownership: partial
- **Already read:** Terms of Service (`terms`, deepinfra.com/terms - customer retains IP; the
  closed-model routing carve-out for Google/Anthropic), the data-privacy statement
  (`privacy_policy`), the data docs (`docs` - zero-retention default, US data centres).
- **Still outstanding:**
  - `security` - **trust / compliance centre**, https://trust.deepinfra.com/compliance - resolve
    **SOC 2 Type 1 vs Type II**, the **sub-processor list**, and ISO 27701 status.
  - `dpa` / `sla` - **no DPA and no SLA document were located.** Confirm whether either exists; if
    not, record `exists: no` (that gap is why residency/compliance are capped).
  - `marketing` - the **pricing page**, https://deepinfra.com/pricing.

### Together AI - `together-ai` · 77.6/B · ownership: substantial
- **Already read:** Terms of Service (`terms` - "you exclusively own all right, title and interest
  in Your Content and Output"; no training without explicit opt-in), Privacy Policy (ZDR by
  default), the Data Processing Addendum (EU SCCs + UK Addendum), the security + OpenAI-compat docs.
- **Still outstanding:**
  - `marketing` - **pricing page**, https://www.together.ai/pricing.
  - Record `exists: no` if still absent: a public **sub-processor list** and the **SOC 2 Type II
    report** itself (only the announcement blog is public).

---

## Where to save what you find

When you open one of the documents above, **save its governing clauses as a small text file inside
this repository**, so the build automation can read it. There is one folder per entity under
`docs/primary-sources/`:

```
docs/primary-sources/
  berget/
    dpa__2026-07-25.md          <- paste the retention / SCC / sub-processor clauses, plus the URL
    _sources.md                 <- one line per document (see below)
  meta-llama/
    license__llama4__2026-07-25.md
    _sources.md
  ...
```

Three simple rules:

1. **One file per document.** Name it `<doc_type>__<detail?>__<YYYY-MM-DD>.md` - e.g.
   `dpa__2026-07-25.md`, `license__glm-4-9b__2026-07-25.md`. The `<doc_type>` prefix is one of the
   vocabulary words below.
2. **Paste the actual clauses, not a summary.** A short verbatim extract of the governing text
   (retention, training, ownership, residency/transfer, sub-processors, licence conditions) plus
   the source URL is enough. You do not need to commit large PDFs - the clause text is what grounds
   the entry.
3. **Log the source in `_sources.md`.** One line per document:
   `doc_type | source URL | date | exists (yes/no) | notes`. If a document genuinely does not
   exist (no DPA, no SLA), write `exists: no` - that honest gap is itself a valuable finding.

Then commit and push to the branch. Any session - including the automated weekly review - clones
the repo, so this needs no special access or connector.

**`doc_type` vocabulary (use these exact prefixes):**
`terms · privacy_policy · dpa · subprocessors · security · sla · model_card · license ·
technical_report · docs · marketing · third_party`

---

## The rules (please follow exactly)

1. **Save the real document text**, not a summary or a screenshot of a headline.
2. **Record the source URL and the date.** Undated evidence is weak.
3. **Prefer the binding document.** Retention / training / ownership / residency / licence claims
   come from the Privacy Policy, DPA, Terms or LICENSE - never a trust-centre or blog page.
4. **A missing document is a finding.** No DPA, no SLA, no licence file → write `exists: no`. That
   is why several dimensions are capped today.
5. **Note per-variant differences.** Licences especially differ per model version - grab each.

## What happens next (the loop)

- The coding session reads `docs/primary-sources/<entity-id>/`, rewrites each affected entry's four
  domains from the real text with exact citations, flips the matching evidence to
  `retrieved: true`, and recomputes the ownership verdict - replacing today's `retrieved: false` /
  "documented but unverified" placeholders.
- The weekly review Routine (`AI Ownership Index - weekly primary-doc review`) ingests new documents,
  re-grounds the affected entries, re-runs validation, and reports what changed and what is still
  outstanding.
- The test every finished entry must pass: pick any strong rating and ask **"which primary
  document, read, says so?"** - there must be a concrete answer.

## Deferred (not needed yet - for the later phase)

`z.ai` and `platform.moonshot.ai` as inference providers, and the closed frontier models
(GPT / Claude / Gemini) - gather these when that phase starts.
