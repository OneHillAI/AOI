# Assess - OpenAI gpt-oss (gpt-oss-120b / gpt-oss-20b)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

gpt-oss is OpenAI's first open-weight release since GPT-2 (August 2025): two
mixture-of-experts **reasoning** models - **gpt-oss-120b** (~117B total / 5.1B active) and
**gpt-oss-20b** (~21B total / 3.6B active) - built for coding, math, agentic tool use and
general reasoning with configurable low/medium/high effort. Its intended use is
general-purpose assistant and agentic workloads where you want a strong reasoning model you
can run and customise on your own hardware under a permissive license.

Only safety-tuned reasoning checkpoints are shipped (there is no raw base release), and the
models are text-only. High-stakes, autonomous, or regulated decision-making is out of scope
without the external control stack described in the Implement domain - in particular because
these are *open weights*, downstream parties can fine-tune the safety tuning away.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **Standard hallucination profile.** Strong reasoning does not remove confabulation; treat
  factual output as unverified.
- **Raw chain-of-thought is unfiltered.** OpenAI deliberately did not align the visible
  reasoning trace; it can contain unsafe or incorrect content and must not be shown to end
  users or used as a safety signal.
- **English-centric.** The model card presents training as primarily English; other-language
  behaviour is incidental rather than a supported target.
- **Removable safety tuning.** Because the weights are open, the safety behaviour can be
  fine-tuned out - the exact risk OpenAI probed with its malicious-fine-tuning study.
- **Harmony-only.** The models are trained solely for the harmony response format; plain
  prompt strings will underperform or misbehave.

<!-- item: openness -->
## Openness tier & components

gpt-oss is honestly **`open_weights`** rather than `fully_open`. What is open is excellent:
ungated, downloadable **Apache-2.0** weights and strong public documentation (a detailed
model card / arXiv report). What is *not* open is the recipe: the **training data and
training code are not released**, and evaluation is only partially open. This is a genuine
open-weights release - materially more open than a gated community license - but it is not
the "open science" tier that publishes the data and code needed to reproduce the model from
scratch. That split is why Dimension 1 scores **4** rather than 5.

<!-- item: license -->
## License terms & permitted use

**Apache-2.0**, OSI-approved, applied to both models with **no click-through gate**. There
is no acceptable-use policy, no monthly-active-user threshold, no attribution/naming
requirement, and no field-of-use restriction - unconditional commercial use subject only to
the standard Apache attribution/notice terms. This is one of the cleanest licenses in the
registry and a load-bearing input to both the openness (4) and legal (4) scores; the legal
score is held at 4 only by the EU AI Act training-content-summary gap (see below) rather than by
anything in the license itself.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `openai` org** on Hugging Face as **safetensors**
(no pickle requirement) with per-file checksums, shipped natively in **MXFP4**. There is a
clear canonical source and no malicious-checkpoint incident on record for the canonical org;
the checkpoint trust checklist scores **6/8**. The two missing controls are cryptographic
weight signing (Sigstore/model-signing) and SLSA build attestation, which is why provenance
is a **4** rather than a 5. Community MXFP4/GGUF redistributions (Ollama, LM Studio, llama.cpp) are
convenient but are separate artifacts - pin the exact `openai` revision and verify checksums.

<!-- item: eu-ai-act -->
## EU AI Act posture

gpt-oss is a GPAI model that sits **under the 10²⁵-FLOPs systemic-risk threshold**
(gpt-oss-120b was trained on roughly 2.1M H100-hours, an estimated <1e25 FLOPs), so no
Article 55 regime applies. Released under a genuine OSI-approved license, ungated and not
monetised, it plausibly qualifies for the **Article 53 open-source exemption** from the
Annex XI/XII technical-documentation duties. The catch is the surviving obligation: a
**public training-content summary**. Unlike a fully-open family, gpt-oss does **not** publish
its training data, so that summary depends on OpenAI authoring it rather than being
reconstructable from a released corpus - the reason the legal score is capped at 4. OpenAI
has committed to the EU GPAI Code of Practice, which helps, but a fine-tuner placing a
derivative on the EU market under its own name may become a provider for that derivative and
must maintain its own documentation.

<!-- item: evaluation -->
## Benchmarks & evaluation

The figures below are aggregated
from OpenAI's model card and independent leaderboards (`ev-perf`, `ev-model-card`). The
consistent picture: **gpt-oss-120b is reported near OpenAI o4-mini** and **gpt-oss-20b near
o3-mini** on core reasoning benchmarks, and both rank strongly among open-weight models on
public leaderboards. Treat published scores as publisher/third-party framing; the
performance dimension is capped at 4 for exactly that reason.

<!-- item: safety-eval -->
## Independent safety evaluation

This is a genuine strength relative to most open-weight families, but it is *partial* rather than
independent-end-to-end. OpenAI published a substantial safety evaluation under its
**Preparedness Framework**, including a worst-case **malicious-fine-tuning** study that
fine-tuned gpt-oss on biology and cyber data to probe uplift, concluding the models did not
reach "High" capability thresholds. Critically, the **methodology was independently reviewed
by external experts - METR, SecureBio, and Daniel Kang** (`ev-metr`) - which is why
`misuse_exposure` is assessed **partial** and the safety dimension can cite a third-party
source. It stops short of a full independent red-team across all harm domains, so coverage is marked *partial*.
