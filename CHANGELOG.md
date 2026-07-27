# Changelog

All notable changes to the AI Ownership Index are recorded here. The format follows Keep a
Changelog; the standard is semantically versioned (see STANDARD.md) and the scoring
methodology is versioned separately (see methodology/versioning.md).

## [Unreleased]

Initial public foundation (v0.1).

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
