# Assess - DeepSeek-R1

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

DeepSeek-R1 is DeepSeek's open-weight **reasoning** line - the 671B-total / 37B-active
Mixture-of-Experts model (128K context) and the R1-0528 refresh - intended as a strong
reasoning, maths, coding, and analysis engine that exposes an explicit chain-of-thought
mode. It is split into its own entry from DeepSeek-V3 and the R1-Distill checkpoints
because it is the **pure-MIT** reasoning release: the licence expressly permits commercial
use, any modification, and distillation into other LLMs.

Out-of-scope, in OneHill's read: any use requiring topic-neutral factuality (the model
exhibits documented censorship on certain political topics), and any unguarded
customer-facing or high-stakes deployment - the lighter safety tuning means the weights
must be wrapped in your own safety system rather than trusted to self-police. Separate the
open weights (this entry's subject) from DeepSeek's hosted app/API, which is a different
product with its own privacy profile.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The distinctive limitation is not hallucination (typical for the class) but **topic
censorship**: refusals and steered answers aligned with Chinese content rules on certain
political topics, which affects neutrality for some use cases. Safety tuning is lighter
than at Western frontier labs, so known jailbreaks are easier to elicit and no first-party
guard/classifier model ships. As a reasoning model it emits explicit think-tag traces you
must parse and, usually, strip before showing users. Recorded factually: this is a
China-origin model; some organisations restrict China-origin models by policy - a
governance consideration, not a capability judgment.

<!-- item: openness -->
## Openness tier & components

DeepSeek-R1 sits in the `open_weights` tier (dimension ceiling 3). The weights are open and
**MIT-licensed**, and the documentation - a detailed technical report - is a genuine
strength. But training data is closed, training code is only partially available, and
evaluation is partial. That mix meets the open-weights anchor rather than the fully-open
top anchor: you get runnable, redistributable weights and a strong write-up, but not a
reproducible training recipe or open data.

<!-- item: license -->
## License terms & what you may do

R1's weights are released under the **OSI-approved MIT License** - permissive, with
commercial use and even distillation expressly allowed, and no field-of-use restriction or
scale threshold. Verbatim from the model card: "DeepSeek-R1 series support commercial use,
allow for any modifications and derivative works, including, but not limited to,
distillation for training other LLMs." This is the cleanest licence in the DeepSeek family
and the single biggest legal plus of the release - materially more open than the
DeepSeek-V3-original weights (a custom agreement) or the Llama-based distils. It is what
lifts use-and-modify to strong and ownership to substantial.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified `deepseek-ai` organisation on Hugging Face,
distributing safetensors with checksums and no malicious-checkpoint incident on the
canonical org (checklist ~5/8, earning a 3-4). Safetensors matters: the format is
data-only, so loading the canonical weights cannot execute code. Short of a higher score
only for the absence of cryptographic signing or provenance attestation. The important
caveat is the sprawling ecosystem of third-party quantizations and the R1-Distill
checkpoints - these are **separate artifacts** (their own entries) whose trust equals their
uploader, not this release. Pin the revision, verify the checksum, and prefer the canonical
org.

**Open weights vs the hosted service - read this.** This entry documents the *open
weights*, which you run on your own infrastructure with no data leaving your box. That is
distinct from DeepSeek's *hosted app and API*, which has faced data-privacy scrutiny and
bans in several jurisdictions. Those hosted-service issues are **not** inherited by
locally-run weights, but they **are** relevant if you call DeepSeek's own API. Self-hosting
the safetensors sidesteps that concern entirely.

<!-- item: eu-ai-act -->
## EU AI Act posture

DeepSeek-R1 is a GPAI model. At 671B total the systemic-risk question is live, but DeepSeek
publishes no FLOP budget, so the 1e25 crossing is not a grounded figure. On the licence
*alone*, MIT is a real free-and-open-source licence, so R1 is a strong candidate for the
Article 53 open-source exemption. But the surviving obligations are unmet: no Article 55
documentation, no copyright policy, no training-content summary, and a China-based provider
is unlikely to furnish an EU documentation package. For a downstream EU deployer this is a
concrete compliance **gap** despite the permissive licence, and it is why legal scores 2
and the grade is held at **C**.

<!-- item: evaluation -->
## Benchmarks & evaluation

On public-leaderboard evidence R1 is among the strongest open-weight **reasoning** models
(maths, coding, analysis). OneHill has **not** re-run these benchmarks this cycle, so
performance is capped at 4 and no specific figures are asserted as verified - the framing
is third-party only. Evaluate against your own task before adoption, particularly where
topic-neutral factuality matters.

<!-- safety-eval is a `gap` item in entry.yaml - its gap_reason renders as a callout; no
     prose section is required. There is no independent, methodologically-documented
     red-team of the R1 open weights we can aggregate, and OneHill ran no safety eval this
     cycle; the behavioural caveats are captured under limitations above. -->
