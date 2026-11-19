---
title: Glossary
description: Plain, one-line definitions for the terms used across the index.
---

Plain definitions of the terms used on the site.

## Scores and verdicts

- **AI Ownership Index (AOI)** - this index's 0-to-100 score, with a letter grade, for how open,
  well-governed and trustworthy a model or provider is. Higher is better. It is built from seven
  weighted dimensions.
- **Grade (A to F)** - the band of the AOI score: A is 85 or above, B is 70 to 84, C is 55 to 69,
  D is 40 to 54, F is below 40.
- **Ownership verdict** - the closing level for how much you own the model or provider. For a model
  it concerns the weights (can you run, adapt and specialise them). For a provider it concerns your
  data. The levels are full, substantial, partial, limited and none.
- **Completeness** - the share of the expected documentation items that an entry covers. Below 100%
  means some items are gaps. It measures coverage and says nothing about quality.

## Provenance badges

- **aggregated** - a claim taken from an existing source, cited and dated.
- **OneHill-tested** - a claim OneHill checked or reproduced, with the method recorded. No entry
  carries one yet.
- **gap** - something that could not be gathered or provided, recorded with the reason.

## Openness

- **Open weights** - the trained model file is published, so you can download and run it yourself.
  The training data and code may still be closed, so you cannot fully reproduce it.
- **Fully open** - the weights, the training data, and the training code are all released, so the
  model can be reproduced and audited end to end.
- **Licence** - the legal terms you accept to use the weights. Some are permissive (MIT, Apache)
  with no user caps; others attach conditions.

## Data and provider terms

- **Zero data retention (ZDR)** - the provider does not store your prompts or the model's outputs.
- **DPA (Data Processing Agreement)** - the binding contract that governs how a provider handles
  your personal data.
- **Sub-processor** - a third party the provider uses to run the service, which therefore may touch
  your data.
- **CLOUD Act** - a US law that can compel US-based companies to hand over data. It is why a
  provider's country of incorporation matters for sovereignty.
- **Retrieved** - on a piece of evidence, "true" means the actual binding document was read, not
  just its marketing summary.

## Regulation

- **GPAI (General-Purpose AI)** - the EU AI Act's category for broadly capable models, which
  carries transparency duties.
- **EU AI Act Article 53** - the baseline duties for GPAI models, with a lighter path for
  open-source releases.
- **EU AI Act Article 55 and the 1e25 FLOPs threshold** - extra duties for the largest models,
  triggered when training compute crosses roughly 10^25 floating-point operations.

## Technical terms you may meet

- **safetensors** - a model file format that cannot execute code when loaded, unlike the older
  pickle format. Safer to download and run.
- **Quantisation** - shrinking a model (for example to run on smaller hardware) by storing its
  numbers at lower precision.
- **SLSA** - a standard for tamper-evidence in how software is built and released.
- **METR** - an independent organisation that evaluates AI models for dangerous capabilities.
