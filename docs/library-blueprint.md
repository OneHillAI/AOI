# OneHill Open Source Library - Blueprint (for sign-off)

**Status: proposal / outline. Nothing here is built yet beyond the v0.1 foundation.**
Mark it up - comments, deletions, redirections all welcome.

Public deliverable: a website at **ownershipindex.ai**. Source lives in
GitHub (this repo); the site is generated from it.

---

## 1. What this is (and isn't)

- **A library, not a report.** Browsable, per-model (and per-provider) documentation
  that is *complete enough to make an informed implementation decision* - plus our own
  assessment and benchmarks.
- **Aggregation-first.** We use what already exists (publisher docs, model cards,
  standards bodies, community docs), aggregate it into one consistent place, and
  **complement it ourselves** - by testing/prompting the model - only where there's a
  gap. Where something **can't be gathered nor provided, we say so explicitly.** That
  honesty is a feature, not a footnote.
- **Standards-anchored.** We don't invent documentation structure; we conform to the
  accepted open-source-software and open-model standards (§3).

## 2. The unit of the library: a **Library Entry**

Each open-source model gets an entry organised into **four documentation domains**
(your taxonomy), mirroring the adopter's journey:

| Domain | Answers | Contains |
|---|---|---|
| **1. Assessment** | *Should we adopt this?* | Openness & license, provenance/supply-chain risk, EU AI Act posture, safety, independent + aggregated benchmarks, the **AOI** score & grade. |
| **2. Implementation** | *How do we deploy it?* | Install paths (HF/Ollama/vLLM/llama.cpp/cloud), hardware & VRAM needs, quantization, serving stacks, fine-tuning, integration, the **safe-deployment controls & Deployment Ceiling**. |
| **3. Feature** | *What can it do?* | Capabilities & modalities, context window, languages, tool/function-calling, structured output, reasoning modes, prompt/chat-template & tokenizer, task-by-task strengths and limits. |
| **4. Support / Help** | *How do we run & get help long-term?* | Support & community channels, issue tracker health, docs quality, update/release cadence, security-disclosure process, troubleshooting, known issues, deprecation policy. |

Providers (inference & hosting) get a parallel, lighter entry shape focused on
Assessment + Implementation + Support.

## 3. Anchored in accepted standards (what we aggregate & conform to)

We map each domain to recognised standards so coverage is measurable, not vibes:

| Domain | Standards we aggregate from / conform to |
|---|---|
| **Assessment** | HF/Google **Model Cards**, **Datasheets for Datasets** / Data Cards, **Model Openness Framework** (Linux Foundation), **OSI Open Source AI Definition**, Stanford **Foundation Model Transparency Index**, **EU AI Act** Annex XI/XII + training-content-summary template, **NIST AI RMF**, **OWASP LLM Top 10**, **MITRE ATLAS**, **OpenSSF** model-signing. |
| **Implementation** | Official deploy docs + **Diátaxis** "how-to guides", **OpenSSF Best Practices Badge / Scorecard**, **SLSA** provenance, serving-stack docs (vLLM/llama.cpp/Ollama/TGI), hardware/quantization references. |
| **Feature** | Model Cards intended-use/capabilities, chat-template/tokenizer specs, **Diátaxis** "reference". |
| **Support / Help** | **Standard-Readme**, **Keep a Changelog**, **SemVer**, **Contributor Covenant**, security-policy / OpenSSF vuln-disclosure norms, community-channel inventory. |
| **How every doc reads** | **Diátaxis** (tutorial / how-to / reference / explanation) - the widely-adopted technical-documentation framework - as the writing backbone across all four domains. |

> The v0.1 methodology I already wrote (scoring rubric, openness framework,
> supply-chain risk, EU AI Act mapping, benchmark method, safe-deployment playbook)
> *is* the Assessment + Implementation standards layer. It stays; it gets slotted under
> this structure rather than sitting on its own.

## 4. The provenance & completeness model (the core promise)

Every documented field carries a **source label** - this is how "aggregate → complement
→ mark gaps" becomes machine-checkable:

- `aggregated` - taken from an existing source, **cited and dated** (publisher, standards
  body, community, third party).
- `onehill_generated` - produced or verified **by us**: we ran, prompted, or tested the
  model to obtain it, with a reproducible method.
- `gap` - **cannot be gathered nor provided.** Recorded explicitly with the reason
  (e.g. "training data undisclosed by publisher", "no independent long-context eval
  exists yet").

Each domain gets a **completeness meter** (covered vs partial vs gap), and each entry a
rolled-up **Documentation Completeness score** that sits alongside AOI. A well-scored
model with big documentation gaps will *look* incomplete - deliberately.

## 5. Scoring: AOI stays, plus completeness

- **AOI** (the 7-dimension trust score you approved) = the Assessment verdict.
- **Documentation Completeness** = coverage across the four domains × source quality.
- Both are computed from the data files, not hand-typed (same engine as today).

## 6. The website

- **Source of truth:** this GitHub repo, data-first - per entry a structured `entry.yaml`
  + one markdown file per documentation domain.
- **Generator:** a static-site generator builds the public site from that data
  (per-entry pages, comparison tables, leaderboards, completeness meters, gap lists,
  search). Recommendation in §8 - needs your pick.
- **Hosting:** served at the subpath **ownershipindex.ai** (base-path aware
  build; can deploy from GitHub Pages or any static host / reverse-proxy).
- **Continuously updated:** the refresh pipeline (already designed) regenerates the site
  as sources change; freshness SLAs flag stale entries.

## 7. How the existing v0.1 foundation maps in

| v0.1 artifact | Fate under this blueprint |
|---|---|
| Methodology docs | Keep - become the standards/scoring layer under Assessment & Implementation. |
| Schema + scoring + validation + CI | Keep & **extend**: entry schema grows the 4 documentation domains + source labels + completeness scoring. |
| The 10 exemplar dossiers | **Re-shaped** into the full 4-domain library format (deepen), then broaden coverage. |
| Templates | Expanded to the 4-domain entry. |

## 8. Decisions I need from you before building

1. **Site generator** - my lean: **Astro Starlight** or **MkDocs Material** (both build a
   docs site from markdown + data, handle the `/open-model-index` base path, and give
   search/nav for free). Do you have a house preference (or an existing onehill.org
   stack I should match)?
2. **Domain taxonomy** - adopt Assessment / Implementation / Feature / Support as the
   top level exactly as above?
3. **First cut** - **deepen** the existing ~10 entries into the full 4-domain format to
   prove the library end-to-end, *then* broaden - or prioritise breadth sooner?

## 9. Phased plan (once signed off)

- **P1 - Restructure:** entry schema + templates for the 4 domains + source labels;
  completeness scoring; fold v0.1 methodology under the new structure.
- **P2 - Prove:** build 2-3 full exemplar entries (e.g. OLMo, Llama, DeepSeek) across all
  four domains, aggregated + AI-complemented + gaps marked.
- **P3 - Website:** stand up the generator, per-entry pages, comparison/leaderboard,
  completeness meters, search; deploy to the subpath.
- **P4 - Broaden & automate:** expand coverage; wire the refresh/collectors.

_Nothing proceeds past P1 without your sign-off on §8._
