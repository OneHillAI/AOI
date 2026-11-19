# Assess - DeepSeek-R1

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

DeepSeek-R1 is DeepSeek's open-weight reasoning line: a 671B-total, 37B-active MoE with 128K context. The R1-0528 refresh belongs to the same line.

It targets reasoning, maths, coding and analysis, and exposes an explicit chain-of-thought mode. It has its own entry because it is the pure-MIT reasoning release, which permits commercial use, any modification and distillation into other LLMs.

Out of scope in OneHill's assessment: any use that needs topic-neutral factuality, because the model shows documented censorship on certain political topics, and any unguarded customer-facing or high-stakes deployment. Lighter safety tuning means the weights need the deployer's own safety system. The open weights are a different product from DeepSeek's hosted app and API, which has its own privacy profile.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The distinctive limitation is topic censorship: refusals and steered answers aligned with Chinese content rules on certain political topics. This affects neutrality for some use cases.

Safety tuning is lighter than at Western frontier labs, so known jailbreaks are easier to elicit, and no first-party guard or classifier model ships. As a reasoning model, R1 emits think-tag traces that clients must parse and usually strip before showing users. R1 is China-origin, and some organisations restrict China-origin models by policy. That is a governance matter with no bearing on capability.

<!-- item: openness -->
## Openness tier & components

DeepSeek-R1 sits in the `open_weights` tier (dimension ceiling 3). The weights are MIT-licensed, and the detailed technical report is a documentation strength.

Training data is closed, training code is partly available and evaluation is partial. The result is runnable, redistributable weights and a strong write-up, with no reproducible training recipe and no open data.

<!-- item: license -->
## License terms & what you may do

R1's weights are released under the OSI-approved MIT License. It is permissive, expressly allows commercial use and distillation, and sets no field-of-use restriction or scale threshold.

This is the least restricted licence in the DeepSeek family and more open than the DeepSeek-V3-original weights (a custom agreement) or the Llama-based distils. It lifts use-and-modify to strong and ownership to substantial. The model card says: "DeepSeek-R1 series support commercial use, allow for any modifications and derivative works, including, but not limited to, distillation for training other LLMs."

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified `deepseek-ai` organisation on Hugging Face. It distributes safetensors with checksums and has no malicious-checkpoint incident (checklist ~5/8, scoring 3). Safetensors is a data-only format, so loading the canonical weights cannot execute code. Cryptographic signing and provenance attestation are absent, which holds the score down.

Third-party quantisations and the R1-Distill checkpoints are separate artifacts with their own entries, and their trust equals that of their uploader. Pin the revision, verify the checksum and prefer the canonical org.

The open weights run on the deployer's own infrastructure, with no data leaving it. DeepSeek's hosted app and API are a different product, which has faced data-privacy scrutiny and bans in several jurisdictions. Those issues do not apply to locally run weights but do apply to calls to DeepSeek's own API.

<!-- item: eu-ai-act -->
## EU AI Act posture

DeepSeek-R1 is a GPAI model. At 671B total the systemic-risk question is open, but DeepSeek publishes no FLOP budget, so the 1e25 crossing is not a grounded figure.

On the licence alone, MIT is a free and open-source licence, so R1 is a strong candidate for the Article 53 open-source exemption. The surviving obligations are unmet: no Article 55 documentation, no copyright policy and no training-content summary, and a China-based provider is unlikely to furnish an EU documentation package. For a downstream EU deployer this is a concrete compliance gap despite the permissive licence. It is why legal scores 2 and the grade stays at C.

<!-- item: evaluation -->
## Benchmarks & evaluation

On public-leaderboard evidence R1 is among the strongest open-weight reasoning models (maths, coding, analysis). OneHill has not reproduced the benchmarks, so performance is capped at 4 and no specific figures are asserted as verified.

Evaluate against your own task before adoption, particularly where topic-neutral factuality matters.

<!-- safety-eval is a `gap` item in entry.yaml - its gap_reason renders as a callout; no
     prose section is required. No independent, documented red-team of the R1 open weights
     exists to aggregate; the behavioural caveats are under limitations above. -->
