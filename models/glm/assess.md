# Assess - GLM (Zhipu AI / Z.ai)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, and evaluation live
here. The AOI score and grade are computed from the dimension anchors in `entry.yaml`._

<!-- item: intended-use -->
## Intended & out-of-scope use

GLM is Zhipu AI's open-weight family - Zhipu is the Beijing company (spun out of Tsinghua's
THUDM lab) that ships internationally under the **Z.ai** brand. The current flagship
**GLM-4.6** is a **355B-total / 32B-active Mixture-of-Experts** model with a **200K** context
window, tuned for coding and agentic use, alongside **GLM-4.5** (355B/32B), the lighter
**GLM-4.5-Air** (106B/12B), and the dense **GLM-4-32B-0414** and **GLM-4-9B-0414**.

Intended use is general-purpose assistant work, with a clear tilt toward **coding, tool use,
and agentic** workloads where GLM-4.6 is strongest. Deploy the instruct checkpoints behind
your own guardrails. Out of scope without additional controls: EU high-stakes use of the
355B MoE while the systemic-risk question is unresolved (see EU AI Act below), and any
deployment that assumes MIT terms without checking the per-checkpoint LICENSE - the original
`glm-4-9b` used a custom non-OSI license.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **China-aligned alignment and hosted-API moderation.** The hosted Z.ai API applies Chinese
  content moderation on politically sensitive topics, and the open weights carry China-aligned
  alignment. Account for this behaviourally rather than assuming Western-lab defaults.
- **Lighter safety tuning.** Instruct alignment withstands casual jailbreaks but is lighter
  than the large Western labs, with **no companion guard/classifier model** shipped.
- **Capability is domain-concentrated.** Leadership is strongest in coding/agentic tasks
  rather than uniform across all domains.
- **Opaque training data.** The corpus is not released, so you cannot inspect it for known
  problem sources - you are reasoning about an opaque artifact.

<!-- item: openness -->
## Openness tier & components

GLM is `open_weights` rather than open-science. **Open**: downloadable weights, model cards,
released **inference code**, and technical reports. **Closed**: the training data and the
training pipeline. **Partial**: evaluation is only partially reproducible. The single most
important openness fact is the license: the GLM-4.5/4.6 and 0414 series ship under a genuine
**OSI-approved MIT** license (`ev-license-mit`) - a real advantage over the restrictive
community licenses some China peers use - but this is not backed by an independent openness
classification here, so Dimension 1 rests on publisher evidence and scores 3.

<!-- item: license -->
## License terms & permitted use

The **GLM-4.5, GLM-4.6, and GLM-4-0414** series are **MIT** - OSI-approved, with no
field-of-use restriction and unconditional commercial use. You may use, modify, redistribute,
and commercialize derivatives subject only to the MIT attribution terms.

**Verify the LICENSE per checkpoint.** Licensing is per-variant: the newer families are MIT,
but the **original `glm-4-9b`** shipped under a **custom, non-OSI "glm-4" license**
(`ev-license-split`). Do not assume MIT across every GLM checkpoint - read the LICENSE file
on the exact model you pull. This clean-but-conditional picture is a load-bearing input to
the legal score (3).

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `zai-org`** org on Hugging Face in safetensors
with per-file checksums, and **dual-published on Zhipu's ModelScope** (`ev-modelscope`).
Two supply-chain surfaces to note: the **dual-hub** distribution (verify checksums match
across Hugging Face and ModelScope) and the **legacy `THUDM`** org, where older GLM/ChatGLM
checkpoints still live - the current canonical org is `zai-org`. The checkpoint trust
checklist scores **5/8**; there is no cryptographic weight signing or SLSA attestation, which
is why provenance is a 4 rather than a 5. No incidents are on record for the canonical org. Pin the
exact revision and verify checksums on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

GLM is a GPAI model. On **license** grounds the MIT-licensed sizes are genuine free/open-source
releases with public parameters and usage information, so they plausibly qualify for the
**Article 53 open-source exemption** from the Annex XI/XII technical-documentation duties.
Two caveats keep this at *partial*:

1. **Systemic risk is unresolved.** The **355B GLM-4.5/4.6 MoE may approach the 10²⁵-FLOPs
   threshold**, but this is **not publicly confirmed**. If it crosses, the exemption is void
   for that model and the full **Article 55** package (not published) would be owed. The
   smaller dense 9B/32B are well under.
2. **Surviving obligations are unmet.** A copyright policy and a **public training-content
   summary** survive the exemption, and neither is published. Because the training corpus is
   **not released**, a downstream provider cannot assemble the training-content summary from
   upstream artifacts - unlike a fully-open family.

A China-based provider is unlikely to furnish an EU AI Office documentation package, so an EU
deployer inherits a clean MIT license and a usable model card but must self-assemble the
compliance material and resolve (or avoid) the systemic-risk question for the 355B MoE.

<!-- item: evaluation -->
## Benchmarks & evaluation

GLM-4.6 evaluates as **strong on real-world coding, tool use, and agentic tasks** and
competitive in general capability - its coding/agentic strength is the standout. The picture is
aggregated from third-party evaluation (`ev-perf-coding`). Treat published scores as
third-party/in-class rather than a claim of uniform category leadership, and note that GLM's own
evaluation is only partially reproducible (the harness and data are not fully open).

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. No independent
     red-team/CBRN/cyber/prompt-injection battery has been published for GLM;
     hosted-API moderation is not a substitute for a model-level eval. -->
