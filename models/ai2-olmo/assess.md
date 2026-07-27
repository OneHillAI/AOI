# Assess - Ai2 OLMo (OLMo 2 / OLMo 3)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score (80.8/100 · Grade B) live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

OLMo is Ai2's "open science" language-model family, spanning OLMo 2 (roughly 7B-13B) and
OLMo 3 (up to a 32B), each shipping base and instruction-tuned checkpoints. Its intended
use is research and general-purpose assistant workloads; its *realistic* differentiator is
any setting where an organisation must be able to explain and audit exactly what went into
the model; auditability rather than raw capability is the product.

For adoption, deploy the **Instruct (safety-tuned)** variant; the base checkpoints are
honestly presented as untuned research artifacts and are out of scope for customer-facing
use. OLMo is not positioned as a frontier or safety-critical model - high-stakes,
autonomous, or regulated decision-making is out of scope without the external control stack
described in the Implement domain.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **Capability is solid-in-class rather than frontier.** A same-size commercial instruct model
  will usually edge OLMo on raw benchmarks; treat it as competitive within its parameter
  class rather than category-leading.
- **Lighter safety tuning.** Instruct alignment withstands casual jailbreaks and residual
  risks are documented, but coverage is lighter than the large commercial labs and there is
  no companion guard/classifier model.
- **English-centric.** The Dolma corpus is English-dominant; other-language behaviour is
  incidental rather than a supported target.
- **Base checkpoints are untuned.** They have no safety tuning and should be treated as
  research artifacts.

The offsetting advantage is transparency: because the full training data is published, you
can inspect it for known problem sources rather than reasoning about an opaque artifact.

<!-- item: openness -->
## Openness tier & components

OLMo earns `fully_open` honestly. All six openness components are **Open**: downloadable
Apache-2.0 weights, the **full Dolma training dataset** (not a prose gesture at the data),
runnable training code, released evaluation code and results, complete technical reports,
and an OSI-approved license. This is the top "Open Science / Class I" tier of the Linux
Foundation Model Openness Framework - which is why Dimension 1 scores 5 backed by
third-party classification (`ev-mof`) rather than publisher marketing.

<!-- item: license -->
## License terms & permitted use

Apache-2.0 across weights, training code, and the Dolma data. It is **OSI-approved**, with
no field-of-use restriction and unconditional commercial use - there is no "community
license" sleight of hand. You may use, modify, redistribute, and commercialize derivatives,
subject only to the standard Apache attribution/notice terms. This clean license is a
load-bearing input to both the openness (5) and legal (5) scores.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `allenai` org** on Hugging Face in safetensors
(no pickle requirement) with per-file checksums. Because the training data, training code,
and intermediate checkpoints are all public, provenance is *maximally auditable* - you can
in principle reconstruct the pipeline. The checkpoint trust checklist scores **6/8**; the
two missing controls are cryptographic weight signing (Sigstore/model-signing) and SLSA
build attestation, which is why provenance is a 4 rather than a 5. No incidents or malicious-mirror
findings are on record for the canonical org. Pin the exact revision and verify checksums on
download.

<!-- item: eu-ai-act -->
## EU AI Act posture

OLMo is a GPAI model but sits **well under the 10²⁵-FLOPs systemic-risk threshold** (models
are ≤32B), so no Article 55 regime applies. Released under a genuine free/open-source
license and not monetised, it plausibly qualifies for the **Article 53 open-source
exemption** from the Annex XI/XII technical-documentation duties. The two obligations that
survive the exemption - a copyright policy and a **public training-content summary** - are
where OLMo is uniquely strong: because Dolma is fully published, the training-content summary
can be satisfied directly from released artifacts. This makes OLMo the most
EU-AI-Act-friendly family in the registry. A fine-tuner who places a derivative on the EU
market may become a provider for that derivative, but inherits an unusually complete upstream
package to build on.

<!-- item: evaluation -->
## Benchmarks & evaluation

The figures below are aggregated
from Ai2's OLMo 2/3 technical reports and independent leaderboards (`ev-perf`,
`ev-tech-report`). The consistent picture: OLMo is competitive within its size class but not
frontier-leading on raw capability - a same-size commercial instruct model will usually
edge it. Its value proposition is transparency and reproducibility (the eval harness and
results are themselves open) rather than class-topping numbers. Treat published scores as
third-party/in-class rather than a claim of category leadership.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. There is no independent
     red-team/CBRN/cyber battery to aggregate. -->
