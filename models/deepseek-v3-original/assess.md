# Assess - DeepSeek-V3 (original, DeepSeek License)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

The original DeepSeek-V3 (December 2024) is the 671B-total / 37B-active Mixture-of-Experts
Base and Chat model, 128K context, that established the V3 line. It is intended as a general
assistant (Chat) or a foundation for further training (Base). It is a **separate entry from
the later MIT-licensed V3 generations** because its weights are governed by the custom
"DeepSeek License Agreement v1.0", not MIT.

Out-of-scope: any use that violates the licence's field-of-use restrictions (see License);
any use requiring topic-neutral factuality (documented political censorship); the **Base**
variant in any customer-facing role (it is not safety-tuned); and any unguarded high-stakes
deployment. For new work, prefer the MIT V3 generations (`deepseek-v3-mit`) unless you
specifically need this checkpoint.

<!-- item: limitations -->
## Known limitations, bias & failure modes

Beyond the class-typical hallucination, the distinctive limitations are **topic censorship**
aligned with Chinese content rules, lighter safety tuning than Western frontier labs, no
first-party guard model, and - unique to this entry versus the MIT generations - a
**use-restricted licence** that constrains what you may deploy it for. The Base variant is a
raw completion model with no safety tuning. Recorded factually: China-origin model, which
some organisations restrict by policy.

<!-- item: openness -->
## Openness tier & components

Original V3 sits in the `open_weights` tier (dimension ceiling 3). The weights are openly
downloadable (ungated) and the documentation - a detailed technical report - is a strength,
but the **licence is conditional** (use-restricted), training data is closed, and training
code partial. The restrictions bite on legal and ownership rather than dropping the openness
tier, because download is ungated and the grant is irrevocable.

<!-- item: license -->
## License terms & what you may do

This is the load-bearing difference from the MIT generations. The **code repository is MIT**,
but the **weights** are governed by the "DeepSeek License Agreement, Version 1.0" (non-OSI).
The grant is genuinely generous in structure - "perpetual, worldwide, non-exclusive,
no-charge, royalty-free, irrevocable", commercial use allowed, and "DeepSeek claims no rights
in the Output You generate" - but it is **conditioned on RAIL-style use restrictions**
(Section 5 / Attachment A): no use violating applicable law, no military application, no harm
to minors, no generating verifiably false content to harm others, no unauthorised PII
distribution, no defamation/harassment, no discrimination, no automated decisions affecting
legal rights. These flow down to derivatives. The patent licence terminates if you sue
DeepSeek over the work. Because of the field-of-use restrictions, use-and-modify is
**moderate** and ownership is **partial** - one step below the MIT V3 generations.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified `deepseek-ai` organisation on Hugging Face,
distributing safetensors with checksums and no malicious-checkpoint incident (checklist
~5/8). Safetensors is data-only, so loading the canonical weights cannot execute code. Short
of a higher score only for the absence of cryptographic signing. The caveat: third-party
quantizations are separate artifacts whose trust equals their uploader, and any
redistribution must carry the DeepSeek License restrictions (not MIT). Pin the revision,
verify the checksum, prefer the canonical org.

**Open weights vs the hosted service.** This entry documents the *open weights*, run on your
own infrastructure - distinct from DeepSeek's *hosted app and API*, which has faced
data-privacy scrutiny and bans in several jurisdictions. Those issues are not inherited by
locally-run weights but are relevant if you call DeepSeek's own API.

<!-- item: eu-ai-act -->
## EU AI Act posture

Original V3 is a GPAI model. Unlike the MIT generations, its weight licence is **not**
free-and-open-source (it carries field-of-use restrictions), so the Article 53 open-source
exemption does **not** apply on the licence axis at all. The surviving obligations are also
unmet: no Article 55 documentation, no copyright policy, no training-content summary, and the
corpus is closed. The technical report cites ~2.788M H800 GPU-hours; at 671B the
systemic-risk question is live but not grounded on a disclosed FLOP figure. For a downstream
EU deployer this is a concrete compliance **gap**, and the grade holds at **C**.

<!-- item: evaluation -->
## Benchmarks & evaluation

On public-leaderboard evidence the original V3 was competitive among large open-weight models
at release. OneHill has **not** re-run these benchmarks this cycle, so performance is capped
at 4 and no specific figures are asserted as verified. Evaluate against your own task,
particularly where topic-neutral factuality matters.

<!-- safety-eval is a `gap` item in entry.yaml - its gap_reason renders as a callout; no
     prose section is required. There is no independent, methodologically-documented
     red-team of the original V3 open weights we can aggregate, and OneHill ran no safety
     eval this cycle; the behavioural caveats are captured under limitations above. -->
