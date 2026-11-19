# Assess - GLM (Zhipu AI / Z.ai)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

GLM is Zhipu AI's open-weight family. Zhipu is the Beijing company, spun out of Tsinghua's
THUDM lab, that ships internationally under the Z.ai brand. The largest model tracked here,
GLM-4.6, is a 355B-total / 32B-active Mixture-of-Experts model with a 200K context window,
tuned for coding and agentic use. The family also includes GLM-4.5 (355B/32B), the lighter
GLM-4.5-Air (106B/12B), and the dense GLM-4-32B-0414 and GLM-4-9B-0414.

Intended use is general-purpose assistant work, with a clear tilt toward coding, tool use and
agentic workloads, where GLM-4.6 is strongest. Deploy the instruct checkpoints behind your own
guardrails. Out of scope without additional controls: EU high-stakes use of the 355B MoE while
the systemic-risk question is unresolved (see EU AI Act below), and any deployment that
assumes MIT terms without checking the per-checkpoint LICENSE, because the original `glm-4-9b`
used a custom non-OSI license.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The hosted Z.ai API applies Chinese content moderation on politically sensitive topics, and
the open weights carry China-aligned alignment. Account for this behaviourally instead of
assuming Western-lab defaults.

Safety tuning is lighter than at the large Western labs. Instruct alignment withstands casual
jailbreaks, and no companion guard or classifier model ships.

Capability leadership is strongest in coding and agentic tasks and is not uniform across
domains.

The training corpus is not released, so it cannot be inspected for known problem sources and
the model is an opaque artifact.

<!-- item: openness -->
## Openness tier & components

GLM is `open_weights`. Open: downloadable weights, model cards, released inference code and
technical reports. Closed: the training data and the training pipeline. Partial: evaluation is
only partially reproducible.

The GLM-4.5/4.6 and 0414 series ship under the OSI-approved MIT license (`ev-license-mit`), an
advantage over the restrictive community licenses some China peers use. No independent
openness classification backs this here, so Dimension 1 rests on publisher evidence and scores
3.

<!-- item: license -->
## License terms & permitted use

The GLM-4.5, GLM-4.6 and GLM-4-0414 series are MIT: OSI-approved, with no field-of-use
restriction and unconditional commercial use. Derivatives can be used, modified, redistributed
and commercialised subject only to the MIT attribution terms.

Verify the LICENSE per checkpoint. Licensing is per variant: the newer families are MIT, but
the original `glm-4-9b` shipped under a custom, non-OSI "glm-4" license (`ev-license-split`).
Read the LICENSE file on the exact model before use. This per-variant picture feeds the legal
score (3).

The tracked cluster is uniformly MIT and ungated. The 0414 repos ship an in-repo MIT LICENSE
file, while GLM-4.5 and GLM-4.6 rely on Hugging Face metadata and the README
(`ev-license-mit`, `ev-0414`). Outside this entry, Zhipu's newer GLM-5.3 and GLM-5.3-BF16
checkpoints carry a custom licence that requires a Z.AI security review from
Model-as-a-Service operators with more than 10 billion USD of group revenue over 12 months
(`ev-license-glm53`). GLM-5, 5.1, 5.2 and 5.3-Flash are plain MIT.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the verified `zai-org` org on Hugging Face in safetensors with
per-file checksums, and dual-published on Zhipu's ModelScope (`ev-modelscope`). Two
supply-chain surfaces need care. The dual-hub distribution requires checksums to match across
Hugging Face and ModelScope. The legacy `THUDM` org still holds older GLM/ChatGLM
checkpoints, while the current canonical org is `zai-org`.

The checkpoint trust checklist scores 5/8. Provenance scores 3: a scanned checkpoint or a
documented mirror and quantization policy would be needed for 4, and cryptographic signing for
5. There is no weight signing or SLSA attestation. No incidents are on record for the
canonical org. Pin the exact revision and verify checksums on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

GLM is a GPAI model. On licence grounds the MIT-licensed sizes are free and open-source
releases with public parameters and usage information, so they plausibly qualify for the
Article 53 open-source exemption from the Annex XI/XII technical-documentation duties. Two
caveats keep this partial.

First, systemic risk is unresolved. The 355B GLM-4.5/4.6 MoE may approach the 10²⁵-FLOPs
threshold, but this is not publicly confirmed. If it crosses, the exemption is void for that
model and the full Article 55 package (not published) would be owed. The smaller dense 9B and
32B are well under.

Second, surviving obligations are unmet. A copyright policy and a public training-content
summary survive the exemption, and neither is published. The training corpus is not released,
so a downstream provider cannot assemble the training-content summary from upstream artifacts.

A China-based provider is unlikely to furnish an EU AI Office documentation package. An EU
deployer receives an MIT licence and a usable model card, but must assemble the compliance
material and resolve or avoid the systemic-risk question for the 355B MoE.

<!-- item: evaluation -->
## Benchmarks & evaluation

GLM-4.6 evaluates as strong on real-world coding, tool use and agentic tasks and competitive
in general capability. Its coding and agentic strength is the main differentiator. The picture
is aggregated from third-party evaluation (`ev-perf-coding`). Published scores are third-party
and in-class, not a claim of uniform category leadership. GLM's own evaluation is only
partially reproducible, because the harness and data are not fully open.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. No independent
     red-team/CBRN/cyber/prompt-injection battery has been published for GLM;
     hosted-API moderation is not a substitute for a model-level eval. -->
