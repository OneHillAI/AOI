---
title: How we source it (provenance)
description: What the source badges mean, and the promise behind them - aggregate what exists, complement with our own testing, and mark what can't be provided.
---

Each documented item carries one of three source labels, shown as a badge:

- <span class="oh-badge oh-badge--aggregated">aggregated</span> - taken from an existing source (the publisher's docs, a standards body, a community resource, an independent analysis), cited and dated.
- <span class="oh-badge oh-badge--onehill_generated">OneHill-tested</span> - produced or verified by OneHill, with a reproducible method recorded. No entry carries this label yet.
- <span class="oh-badge oh-badge--gap">gap</span> - could not be gathered or provided. It is recorded with the reason.

## Gaps

A gap states that something is missing. When a publisher has not disclosed its training data, or no independent long-context evaluation exists, the entry says so. A gap counts as addressed and adds nothing to completeness.

## Fact provenance and section provenance

The badges describe the provenance of a documentation section. Every factual claim also carries its own provenance: `onehill_verified`, `third_party` or `publisher`. A section labelled OneHill-tested must cite a fact OneHill verified. CI enforces these rules.

## Freshness

Entries carry a `last_verified` date and a freshness limit of 30 days for fast-moving facts. An entry past the limit fails validation. The [full method and data](https://github.com/OneHillAI/AOI) are open.
