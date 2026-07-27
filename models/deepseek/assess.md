# Assess - DeepSeek (V3 / R1)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

DeepSeek V3 and R1 are large mixture-of-experts language models intended as general
assistant, reasoning, and coding engines. V3 is the general-purpose instruct model;
R1 is the reasoning-tuned sibling that exposes an explicit chain-of-thought mode and
put the lab on the global map. The community R1-Distill checkpoints (Llama and Qwen
bases) target the same reasoning/coding tasks on far smaller hardware.

Out-of-scope: any use requiring topic-neutral factuality (the models
exhibit documented censorship on certain political topics), and any unguarded
customer-facing or high-stakes deployment - the lighter safety tuning means the weights
must be wrapped in your own safety system rather than trusted to self-police. Adopters
should also separate the open weights (this entry's subject) from DeepSeek's hosted
app/API, which is a different product with its own privacy profile.

<!-- item: limitations -->
## Known limitations, bias & failure modes

Hallucination is typical for the class; the distinctive limitation is
**topic censorship**: refusals and steered answers aligned with Chinese content rules on
certain political topics, a documented behaviour that affects neutrality and factuality
for some use cases. Safety tuning is lighter than at Western frontier labs, so known
jailbreaks are easier to elicit and residual prompt-injection susceptibility is present.
No first-party guard/classifier model ships. Separately, and recorded factually, this is
a China-origin model; some organisations restrict China-origin models by policy - a
governance consideration that does not reflect a capability judgment.

<!-- item: openness -->
## Openness tier & components

DeepSeek sits in the `open_weights` tier (dimension ceiling 3). The weights are open and
MIT-licensed, and the documentation - detailed technical reports - is a genuine strength.
But training data is closed, training code is only partially available, and evaluation is
partial. That mix meets the open-weights anchor rather than the fully-open top anchor: you
get runnable, redistributable weights and strong write-ups, but not a reproducible
training recipe or open data.

<!-- item: license -->
## License terms & what you may do

The V3/R1 weights are released under the **OSI-approved MIT license** - permissive, with
commercial use and even distillation allowed, and no field-of-use restriction or scale
threshold. That is a materially more open posture than the community-license families and
is the single biggest legal plus of the release. One caveat: some earlier DeepSeek
releases used a custom license, so confirm the MIT grant per checkpoint - for the V3/R1
weights it holds.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified `deepseek-ai` organisation on Hugging Face,
distributing safetensors with checksums and no malicious-checkpoint incident on the
canonical org (checklist ~5/8, earning a 4). Safetensors matters here: the format is
data-only, so loading the canonical weights cannot execute code - the self-hosted open
weights are supply-chain-safe to load. Short of a 5 only for the absence of cryptographic
signing or provenance attestation. The important caveat is the sprawling ecosystem of
third-party distills and quantizations (for example R1-Distill-Llama-70B): these are
**separate artifacts whose trust equals their uploader** rather than the canonical org. Pin the
revision, verify the checksum, and prefer the canonical org or a host you already trust.

**Open weights vs the hosted service - read this.** This entry documents the *open
weights*, which you run on your own infrastructure with no data leaving your box. That is
distinct from DeepSeek's *hosted app and API*, which has faced data-privacy scrutiny and
outright bans in several jurisdictions and government bodies. Those hosted-service issues
do not apply to locally-run weights; they apply directly if you
call DeepSeek's own API, where your prompts leave your control. Self-hosting the
safetensors sidesteps that concern entirely.

<!-- item: eu-ai-act -->
## EU AI Act posture

DeepSeek is a GPAI model, and V3/R1's training compute very likely exceeds the 1e25-FLOP
threshold, triggering the **systemic-risk** presumption. This produces a subtle but
important outcome. On the license *alone*, MIT is a real free-and-open-source license, so
V3/R1 would qualify for the Article 53 open-source exemption. But the exemption is **void**
for systemic-risk models - so the full Article 53 + 55 obligations apply, and they are not
met: no Article 55 documentation, no copyright policy, no training-content summary. For a
downstream EU deployer this is a concrete compliance **gap** - a systemic-risk GPAI model
shipping without the documentation you would need to assemble your own obligations. This
is the entry's hard flag, and it caps the grade at **C**.

<!-- item: evaluation -->
## Benchmarks & evaluation

On public-leaderboard evidence, R1 is a strong reasoning model and V3 is competitive among
large open-weight models. Performance is capped at 4 and no specific figures are asserted
as verified; the framing here is third-party only. Evaluate against your own task before adoption, particularly
where topic-neutral factuality matters.

<!-- safety-eval is a `gap` item in entry.yaml - its gap_reason renders as a callout; no
     prose section is required. There is no independent, methodologically-documented
     red-team to aggregate; the behavioural
     caveats are captured under limitations above. -->
