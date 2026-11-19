# Assess - Soofi (Soofi-S)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Deploy Soofi-S for industrial and regulated German and English work: technical and regulatory
documents, code, and agentic workflows where European data-residency and auditability matter. It
is the first model from the German Soofi consortium ("Sovereign
Open Source Foundation Models"), coordinated by the KI Bundesverband and funded by the German Federal Ministry for Economic
Affairs and Energy (BMWE) under the European IPCEI-CIS programme. The model is a ~30B hybrid
Mamba-2/Transformer Mixture-of-Experts (30B total, ~3B active per token) trained on ~27 trillion
tokens of primarily German and English.

Deploy the Instruct-Preview (post-trained) variant; the base checkpoint is built for fine-tuning
and is out of scope for customer-facing use. This is an early preview/beta, so high-stakes,
autonomous or safety-critical decision-making is out of scope without the external control stack
described under Implement. Treat it as a strong foundation to pilot, not a hardened production
endpoint.

<!-- item: limitations -->
## Known limitations, bias & failure modes

Soofi-S is an early preview/beta, and capability, safety and tooling are still stabilising. The
Instruct-Preview model card documents privacy and safety features as still incomplete, and there
is no companion guard or classifier model. The hybrid Mamba-2/MoE ships custom modelling code and
must be loaded with `trust_remote_code=True`; runtime support is still maturing across serving
stacks.

Third-party coverage calls Soofi-S the strongest "fully open" model on English and German
aggregates, below the largest closed labs. That is a benchmark claim relative to open baselines,
not a statement about access: the weights are gated and not an open release. Access needs
publisher approval of an access request, and the closed beta is for selected partners. No
release date or licence is published.

The offsetting advantage is documentation. The full per-source data accounting and code are
published, so what went into the model can be inspected.

<!-- item: openness -->
## Openness tier & components

Soofi-S aims at the OLMo-style `fully_open` tier and is not there. It sits at `gated_open`, with
Dimension 1 scored 2. The weights are not openly available. Every repo in the `Soofi-Project` org
is manually gated. The base model card says "It is not an open release" and describes
"a closed beta with already selected partners". The licence tag reads closed-beta, and the preview
is "for research and development only". The project site says only that an open-source release
"is planned", with no date.

Marketing and binding text conflict. The paper title
("A Sovereign, Open-Source Foundation Model"), the organisation name and press coverage say open-source; the card, the tag and the gate
say closed beta. The grade follows the binding text.

Documentation and code are delivered. The pretraining report publishes full per-source data
accounting (source identifiers, raw and effective token counts, epoch multipliers, and sources
evaluated but excluded). The `Soofi-Pretraining` repo holds the complete training codebase but
has no licence file, so it grants no reuse rights. The evaluation scores are a CC-BY-4.0 dataset.
The Open Source AI Definition (OSAID 1.0) commitment is a future-tense pledge ("will be
released") that has not been met since the July report. A `fully_open`/5 rating needs all six
components actually open; an anchor-3 rating needs open weights plus a licence, and neither
exists. Openness is promised and well documented, not delivered.

About 1.3% of Phase 1 tokens (the commercially licensed Genios corpus) are reported in aggregate
and are not redistributable. The committed release would clear OSAID 1.0 but would only nearly
satisfy stricter "every token redistributable" open-data proposals.

<!-- item: license -->
## License terms & permitted use

No licence is in force. The licence tag reads closed-beta, no repo in the org (and not the
training-code repo) contains a LICENSE file, the card says the model "Will be released under a
permissive license", and the preview is limited to research and development. The consortium has
committed to a permissive, OSAID-compliant licence later, but no published text grants use,
modification, redistribution or commercial use. This is why the legal dimension scores 2:
documentation and jurisdiction are strong, and the missing licence is the binding gap. The schema
has no "unknown" commercial-use value, so the entry records `allowed_with_conditions`, which here
means only that no unconditional grant exists. Re-assess when a licence is published.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed, to approved accounts only, from the verified `Soofi-Project` org on
Hugging Face in bf16 safetensors (no pickle requirement), with first-party GGUF, FP8 and 3-bit
quantizations and per-file checksums. The data accounting and training code are public, so
provenance is auditable. The intermediate Megatron checkpoint repo is gated like the rest.

The checkpoint trust checklist scores 6/8, a July score that is unverified. The two missing
controls are cryptographic weight signing (Sigstore/model-signing) and SLSA build attestation.
The base weights also sit behind a closed-beta access gate (every repo is manually gated), and
the Hub reports no completed security scan for the base repo, so provenance scores 4, not 5. No
incidents or malicious-mirror findings are on record. Pin the exact revision and verify
checksums on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

Soofi-S is a GPAI model well under the 10²⁵-FLOPs systemic-risk threshold (~30B total, ~3B active,
~27T tokens), so no Article 55 regime applies. It is committed to a free/open-source release that
would meet OSAID 1.0 and is not monetised, which would qualify it for the Article 53 open-source
exemption from the Annex XI/XII technical-documentation duties. The exemption cannot yet be
relied on, because no open licence is published (base weights manually gated in closed beta,
licence tag closed-beta, no LICENSE file). There is no confirmed free-and-open licence to point
to.

Two obligations survive the exemption: a copyright policy and a public training-content summary.
Soofi-S is strong here. It publishes full per-source data accounting, so the training-content
summary can be assembled directly from released artifacts (only the ~1.3% Genios slice is
aggregate-only). With EU/Germany jurisdiction and training on sovereign German infrastructure,
this is one of the cleaner EU AI Act postures in the registry. A fine-tuner placing a derivative
on the EU market may become a provider for that derivative and receives a complete upstream
package.

<!-- item: evaluation -->
## Benchmarks & evaluation

Aggregated from the Soofi pretraining technical report and independent coverage (`ev-perf`,
`ev-arxiv`). The consistent finding is that Soofi-S is the strongest fully-open model on aggregate
English and German benchmarks, ahead of OLMo 3 32B, Apertus 70B, EuroLLM 22B and Alia 40B. It
matches dense 14-27B models and wins code aggregates in both languages among open base models, at
only ~3B active parameters. Coverage is partial because exact per-task numbers are still being
filled in on the public model cards (some are flagged "to be measured"). Treat the leaderboard-style
claims as third-party and in-class, not as a frontier-vs-closed claim.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. The Instruct model card lists
     safety features as incomplete, and there is no independent red-team/CBRN/cyber battery to aggregate. -->
