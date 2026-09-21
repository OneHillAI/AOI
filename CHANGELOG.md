# Changelog

All notable changes to the AI Ownership Index are recorded here. The format follows Keep a
Changelog; the standard is semantically versioned (see STANDARD.md) and the scoring
methodology is versioned separately (see methodology/versioning.md).

## [Unreleased]

Initial public foundation (v0.1).

### Added

- NVIDIA Nemotron 3, as three per-licence entries under one family: `nemotron-3` (Super + Nano,
  NVIDIA Nemotron Open Model License, AOI 66.0, grade C, ownership partial), `nemotron-3-ultra`
  (Ultra 550B, OpenMDW-1.1, AOI 63.6, grade C, ownership substantial) and `nemotron-3-nano-omni`
  (multimodal, NVIDIA Open Model Agreement, AOI 60.0, grade C, ownership partial). Ungated weights
  and, for Super/Nano/Ultra, runnable recipes and CC-BY post-training data. The governing licences
  are Apache-2.0-derived and IRREVOCABLE, with commercial use allowed and no acceptable-use or
  guardrail restriction; ownership is capped by a partly-released corpus and the absence of any
  published model-level safety evaluation.
- Kimi K3 (Moonshot AI) model entry: open-weights (2.8T total / 104B active MoE, 1M context,
  native vision), AOI 53.2, grade D. Classified open-weights, not closed-frontier; grounded to
  primary sources, with the offensive-cyber safety finding and the new Model-as-a-Service licence
  gate as the load-bearing risks.
- Three new inference-provider entries, each drafted from automated research and then
  independently re-verified by a Cowork browser session (see the "Corrected" entries below for
  what changed on verification): Fireworks AI (AOI 64.8, grade C - a Zero Data Retention posture
  and the Response API's 30-day-default retention exception are independently confirmed via
  readable docs, but the Terms of Service and DPA turned out to be unreachable to a real browser,
  so confidentiality is coded unknown rather than asserted), Baseten (AOI 73.6, grade B - Zero
  Data Retention by default plus a genuinely MUTUAL confidentiality clause, confirmed on two
  independent live fetches, and a real 99.9% SLA; no published EU region for the managed
  service), and Nebius / Token Factory (AOI 60.8, grade C - its central finding, that the binding
  Terms of Service contradict the marketing claim of no training on customer content, is
  confirmed verbatim on independent re-read; EU-region and SLA claims were corrected downward on
  the same pass).

### Changed

- Registry entries are now scoped to a single release and always grouped under a non-scored `family`
  relation; a family is split into separate entries only when its releases diverge on a scored
  attribute (OpenSpec `model-family-scope`). Renamed the Kimi K2 entry from `kimi` to `kimi-k2`.
- Split the aggregate `nemotron` entry into three per-licence entries under the `nemotron` family:
  `nemotron-3` (Super + Nano), `nemotron-3-ultra` and `nemotron-3-nano-omni`, because the three
  releases diverge on their governing licence (NVIDIA Nemotron Open Model License, OpenMDW-1.1, and
  NVIDIA Open Model Agreement) and, for Nano Omni, on their openness tier. The split also corrects a
  wrong licence reading: the Nemotron 3 licences are Apache-2.0-derived, perpetual and IRREVOCABLE
  with no Trustworthy-AI, acceptable-use or guardrail clause (they terminate only on the licensee
  bringing IP litigation over the work), not the revocable, use-restricted, guardrail-terminating
  grant the aggregate entry had described. Safety was re-scored from 4 to 3 across all three, because
  no published model-level safety evaluation was found for any release; Ultra's ownership is now
  substantial on the OpenMDW "without restriction" grant.
- Refreshed the Together AI entry's model catalogue and pricing (last verified 2026-08-06, past the
  30-day fast-moving SLA): the served catalogue moved forward a generation (DeepSeek V3/R1 to
  V4-generation, Qwen3 to 3.5/3.7/3.8, plus new GLM-5.3 and Kimi K3 entries), Mistral/Mixtral was
  removed from serverless, and the prior "embeddings" claim is corrected - Together's own docs now
  state no embedding models are offered via serverless. Score unchanged (governance terms have not
  materially changed since the last pass).
- Corrected all four inference-provider entries above against an independent Cowork browser
  verification pass, replacing draft findings from automated web-fetch research with directly
  read, human-supervised evidence. Fireworks AI: the Terms of Service and DPA turned out to be
  unreachable to a real browser (page-level noindexed) - confidentiality moved from
  `functional_only` to `unknown`, sub-processor disclosure from `true` to `false`, and
  `trains_on_inputs` from `never` to `opt_in_only` (headline 71.6 -> 64.8, grade B -> C; ownership
  substantial -> partial). Baseten: the mutual confidentiality clause was confirmed on two
  independent live fetches, and a real 99.9% SLA was found where none had been located, but a
  prior ISO 27001 claim was retracted for lack of any basis (headline 71.2 -> 73.6, grade
  unchanged at B). Nebius: the entry's central finding (training by default under the binding
  Terms of Service, contradicting marketing) was confirmed verbatim, but the EU-region count
  (four -> two public self-serve), a claimed inference SLA (retracted - none exists), and a
  "dedicated-only" catalogue claim (models were simply superseded, not gated) were all corrected
  downward, while compliance strengthened with a named SOC 2 auditor (headline 65.2 -> 60.8,
  grade unchanged at C; also corrected the ownership level from `limited` to `partial` per the
  ownership rule, independent of this pass). Together AI: the confidentiality-disclaimed finding
  and the catalogue corrections were both independently confirmed unchanged, but `zdr_available`
  was corrected from `yes_default` to `yes_optional` (Zero Data Retention is account-level opt-in,
  not the default) - a real field-level fix with no score impact, since data_governance was
  already capped at 3 by the confidentiality disclaimer.
- Freshness re-verification sweep across the 21 model entries the daily freshness cron flagged as
  49-58 days past the 30-day fast SLA (surfaced when PR #22's CI ran `validate.py` with the
  freshness check active). A Cowork browser session re-checked each entry's licence, safety
  posture, and availability against current primary sources - not a bulk date-bump. 20 of 21
  re-verified clean with no score change; several flag newer-generation releases (DeepSeek V4
  line and V3.1/V3.2, a licence-divergent GLM-5 generation, Nemotron 3.5 Lightning 30B-A3B, OLMo 3,
  EuroLLM-22B-2512, Qwen3.5/3.6/3.8, Kimi K2.5/K2.6/K2.7-Code) as new entities for a future build
  pass, deliberately not folded into the existing entries' scores. The one entry that needed real
  judgment, not just a re-check, was `soofi`: the research surfaced that Soofi-S-Base's model card
  reads "closed-beta" and the repo is gated, in tension with the project's own "open-source"
  marketing - but the entry's 2026-07-25 correction already accounts for exactly this (openness
  held at the open_weights ceiling, ownership already partial), so no further downgrade was
  warranted. Full research pack archived under
  `docs/freshness-sweeps/2026-09-21/`.
- Second freshness re-verification sweep, covering the remaining 8 stale entries (3 hosting
  providers, 5 inference providers) - the same daily cron finding, out of scope for the model
  sweep above. Six re-verified clean with no score change (Hugging Face, Berget, Groq, Infercom,
  plus two hosting providers - llama.cpp/GGUF and Ollama - where a fresh in-window CVE each
  (CVE-2026-52131, CVE-2026-85180) reinforced rather than moved their existing grade). Two needed
  real re-grades: DeepInfra's Terms of Service was rewritten (effective 2026-08-17) to add a
  genuine mutual confidentiality clause and make Zero Data Retention contractual and controlling
  with a bounded exception, lifting it from 52.0 D to 56.8 C; Runware's current Terms no longer
  contain the adverse, non-confidentiality clause a prior pass had found - the customer now owns
  Outputs outright with no broad licence granted to Runware - lifting the adverse hard flag and
  moving data_governance from 2 to 3 (45.6 D to 50.4 D; the grade itself did not cross into C
  because compliance and residency, unrelated to this finding, were not re-examined). Runware's
  correction carries a load-bearing caveat: the removal is inferred from the current text's
  absence of the old clauses, since web archives were proxy-blocked and no verbatim historical
  diff was possible. `python scripts/validate.py` now reports 0 errors registry-wide for the
  first time this session. Research pack archived under
  `docs/freshness-sweeps/2026-09-21-providers/`.

### The index

- Ownership-first model: every entry resolves to an ownership level (`full` down to `none`),
  floor-weighted from four factors (use and modify, transparency, reliability, data control).
  The AOI score, seven weighted dimensions scored 0 to 100 with a letter grade, is the
  analytical input behind the verdict, not the headline.
- Rubric 1.1: every rung 0 to 5 defined for all fourteen dimensions (seven model, seven
  inference-provider), with the ownership-factor cutoffs stated explicitly. Scores are derived
  by `scripts/score.py` and gated in CI.
- Ten models and six inference providers, each grounded to primary documents, with a
  four-domain dossier (assess, implement, use, support) and an evidence apparatus that records
  whether each source was actually read.

### The site

- Custom Astro app-shell library at ownershipindex.ai: a grade-anchored ledger, an entry sheet
  per model and provider that leads with the ownership verdict, side-by-side compare, a search
  over every entry, and reference pages for the classification matrices and the glossary.
  Cool-and-teal design in light and dark; hosted on Cloudflare Pages.

### Governance

- Evidence-first score-change process, verification over self-report, review-gated merges
  (CODEOWNERS plus branch protection), and a versioned methodology. See CONTRIBUTING.md,
  GOVERNANCE.md, and methodology/versioning.md.

This foundation supersedes the earlier internal names (OHOMS, then the Open Model Index) and
the onehill.org/open-model-index preview URL.
