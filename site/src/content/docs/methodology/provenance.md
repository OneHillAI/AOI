---
title: How we source it (provenance)
description: What the source badges mean, and the promise behind them - aggregate what exists, complement with our own testing, and mark what can't be provided.
---

The library's core promise is honesty about **where every piece of documentation comes
from**. Each documented item carries one of three source labels, shown as a badge:

- <span class="oh-badge oh-badge--aggregated">aggregated</span> - taken from an existing
  source (the publisher's docs, a standards body, a community resource, an independent
  analysis), **cited and dated**.
- <span class="oh-badge oh-badge--onehill_generated">OneHill-tested</span> - produced or
  verified **by OneHill**: we ran, prompted, or tested the model to obtain it, with a
  reproducible method recorded.
- <span class="oh-badge oh-badge--gap">gap</span> - **cannot be gathered nor provided.**
  Recorded explicitly, with the reason, instead of being silently omitted.

## Why a gap is a feature

A missing section is invisible; a **documented gap** is honest. When a publisher hasn't
disclosed training data, or no independent long-context evaluation exists yet, we say so -
and it counts as *addressed* (we told you) even though it counts 0 toward completeness (we
couldn't fill it).

## Fact provenance vs. section provenance

The badges describe the provenance of a documentation **section**. Underneath, every
factual **claim** also carries its own provenance - `onehill_verified`, `third_party`, or
`publisher` - and a section that claims to be OneHill-tested must cite a fact OneHill
actually verified. The rules are enforced in CI.

## Continuously updated

Entries carry a `last_verified` date and a freshness SLA; the build flags anything that has
gone stale. The [full method and data](https://github.com/OneHillAI/AOI) are open.
