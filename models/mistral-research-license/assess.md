# Assess - Mistral (research / non-production licence)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

These are the Mistral models that are not Apache-2.0, shipped under Mistral's two non-commercial
licences. Under the Mistral Research Licence (MRL, research-only): Ministral 8B, Mistral Large 2
(123B), and the multimodal Pixtral Large. Under the Mistral AI Non-Production Licence (MNPL,
non-production-only): Codestral. They are intended for research and evaluation. They are a
separate entry from the Apache-2.0 flagship line (the `mistral` entry) because the licence bars
commercial and production use.

Out-of-scope: any production or commercial deployment without a separately negotiated commercial
licence from Mistral. For commercial work, use the Apache Mistral models or take a commercial
licence.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The dominant limitation is the non-commercial licence, which is the reason to use the Apache line
for anything beyond research. Other limitations are historically lighter safety tuning than some
peers, no first-party guard model, closed training data and code, and serious infrastructure needs
for the 123B/124B models.

<!-- item: openness -->
## Openness tier & components

`open_weights` tier with a conditional (non-commercial) licence (dimension score 2). The weights
are openly downloadable and inspectable for research, but commercial/production use is barred,
and training data and code are closed. That puts it a notch below the Apache Mistral line's
open-weights 3.

<!-- item: license -->
## License terms & what you may do

Two non-commercial licences apply. The MRL (Ministral 8B, Mistral Large 2, Pixtral Large) grants
use "solely for (a) personal, scientific or academic research, and (b) for non-profit and
non-commercial purposes", excluding revenue activity and SaaS distribution. The licence text also
excludes employee or contractor use in daily tasks and any revenue-intended proof-of-concept.

The MNPL (Codestral) permits only "testing, research, Personal, or evaluation purposes in
Non-Production Environments", with no commercial supply including SaaS/cloud. In both cases
production or commercial use requires a separately negotiated commercial licence from Mistral.
Outputs are not claimed by Mistral, and France/Paris jurisdiction applies. The non-commercial bar
is why use-and-modify is weak and ownership is limited.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified `mistralai` organisation on Hugging Face, with a public
per-model licence table, safetensors and checksums, and no malicious-checkpoint incident
(checklist ~5/8). Community quantizations circulate, but their use stays bound by the MRL/MNPL
non-commercial terms, and a quant confers no commercial rights. Pin the revision, verify the
checksum, and confirm the per-model licence tier.

<!-- item: eu-ai-act -->
## EU AI Act posture

These are GPAI models. Unlike the Apache Mistral line, the MRL/MNPL are not FOSS (they bar
commercial/production use), so the Article 53 open-source exemption does not apply on the licence
axis. Mistral is EU-domiciled (France), an early GPAI Code of Practice signatory, and documents
its models well, so the surviving obligations are partially met. An EU research or evaluation user
is well served; a commercial deployer must negotiate a licence first. Legal scores 2.

<!-- item: evaluation -->
## Benchmarks & evaluation

Mistral Large 2 and Pixtral Large are strong open-weight models, and Ministral 8B is strong for
its size. The benchmarks are not reproduced, so performance is capped at 4 and no specific
figures are asserted as verified.

<!-- safety-eval is a `gap` item in entry.yaml; its gap_reason renders as a callout and no prose
     section is required. No independent red-team of these Mistral models is published, and
     historically lighter safety tuning is noted under limitations above. -->
