# Assess - Soofi (Soofi-S)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

Deploy Soofi-S for **industrial and regulated** German and English work - technical and
regulatory documents, code, and agentic workflows where European data-residency and
auditability matter. It is the first model from the German **Soofi consortium** ("Sovereign
Open Source Foundation Models"), coordinated by the KI Bundesverband and funded by the German
Federal Ministry for Economic Affairs and Energy (BMWE) under the European IPCEI-CIS programme
- a ~30B hybrid Mamba-2/Transformer Mixture-of-Experts model (30B total, ~3B active per token)
trained on ~27 trillion tokens of primarily **German and English**.

For adoption, deploy the **Instruct-Preview** (post-trained) variant; the base checkpoint is
built for fine-tuning and is out of scope for customer-facing use. Because this is an early
**preview/beta**, high-stakes, autonomous, or safety-critical decision-making is out of scope
without the external control stack described in the Implement domain - treat it as a strong
open foundation to pilot rather than a hardened production endpoint.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **Early preview/beta.** Treat capability, safety and tooling as still stabilising rather than final.
- **Incomplete safety hardening.** The Instruct-Preview model card documents privacy
  and safety features as still incomplete, and there is no companion guard/classifier model.
- **Custom architecture.** The hybrid Mamba-2/MoE ships custom modelling code and must be loaded
  with `trust_remote_code=True`; runtime support is still maturing across serving stacks.
- **Strongest on open baselines, below frontier closed labs.** Third-party coverage calls it the
  strongest "fully open" model on English + German aggregates. That is a benchmark claim relative
  to open baselines, not a statement about access: the weights are gated and not an open release.

- **Access.** Weights need publisher approval of an access request, and the closed beta is for
  selected partners; no release date or licence has been published.

The offsetting advantage is documentation: because the full per-source data accounting and code
are published, you can inspect what went into the model rather than reasoning about an opaque
artifact.

<!-- item: openness -->
## Openness tier & components

Soofi-S is aiming at the OLMo-style `fully_open` tier and is not there. Re-checked on
2026-11-19, it sits at **`gated_open`** with Dimension 1 scored **2**. The weights are not
openly available: every repo in the `Soofi-Project` org is **manually gated**, the base model card
says "It is not an open release" and describes "a closed beta with already selected partners", the
licence tag reads **closed-beta**, and the preview is "for research and development only". The
project site says only that an open-source release "is planned", with no date. Marketing and
binding text conflict: the paper title ("A Sovereign, Open-Source Foundation Model"), the
organisation name and press coverage say open-source, and the card, the tag and the gate say
closed beta. The grade follows the binding text.

What is genuinely delivered is **documentation and code**: the pretraining report publishes **full
per-source data accounting** (source identifiers, raw and effective token counts, epoch multipliers,
and even sources evaluated but excluded), the `Soofi-Pretraining` repo holds the complete training
codebase (but has no licence file, so it grants no reuse rights), and the evaluation scores are a
CC-BY-4.0 dataset. The **Open Source AI Definition (OSAID 1.0)** commitment is a future-tense pledge
("will be released") that has not been met four months after the July report. A `fully_open`/5
rating needs all six components *actually* Open; an anchor-3 rating needs open weights plus a
licence, and neither exists yet. Openness is promised and well-documented rather than delivered.
(A further caveat: ~1.3% of Phase 1 tokens, the commercially licensed Genios corpus, are reported
in aggregate rather than being redistributable, so even the committed release clears OSAID 1.0 but
is only *nearly* compliant with stricter "every token redistributable" open-data proposals.)

<!-- item: license -->
## License terms & permitted use

**No licence is in force.** The licence tag reads closed-beta, no repo in the org (and not the
training-code repo) contains a LICENSE file, the card says the model "Will be released under a
permissive license", and the preview is limited to research and development. The consortium has
committed to a permissive, OSAID-compliant licence later, but no published text today grants use,
modification, redistribution or commercial use. This is why the legal dimension scores **2**: the
documentation and jurisdiction are strong, and the missing licence is the binding gap. The schema
has no "unknown" commercial-use value, so the entry records `allowed_with_conditions`, which here
means only that no unconditional grant exists. Re-assess when a licence is published.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed, to approved accounts only, from the **verified `Soofi-Project` org** on
Hugging Face in **bf16 safetensors** (no pickle requirement), accompanied by **first-party GGUF,
FP8 and 3-bit quantizations**, with per-file checksums. Because the data accounting and training code
are public, provenance is auditable (the intermediate Megatron checkpoint repo is gated like the rest) - the checkpoint trust
checklist scores **6/8**. The two missing controls are cryptographic weight signing
(Sigstore/model-signing) and SLSA build attestation, and the base weights sit behind a
closed-beta access gate (every repo is manually gated, and the Hub reports no completed security
scan for the base repo), which is why provenance is a **4** rather than a 5. The 4 and the 6/8
checklist count were set in July and not re-derived on 2026-11-19. No incidents or
malicious-mirror findings are on record. Pin the exact revision and verify checksums on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

Soofi-S is a GPAI model but sits **well under the 10²⁵-FLOPs systemic-risk threshold** (~30B
total / ~3B active, ~27T tokens), so no Article 55 regime applies. It is
*committed* to a free/open-source release that would meet OSAID 1.0 and is not monetised, which
**would** qualify it for the **Article 53 open-source exemption** from the Annex XI/XII
technical-documentation duties - but the exemption cannot yet be relied on, because no open
licence has been published (base weights manually gated in closed beta, licence tag closed-beta, no
LICENSE file), so there is no confirmed free-and-open licence to point to today. The two
obligations that survive - a copyright policy and a **public training-content summary** - are
where Soofi-S is unusually strong: because it publishes **full per-source data accounting**, the
training-content summary can be assembled directly from released artifacts (only the ~1.3% Genios
slice is aggregate-only). Combined with an **EU/Germany jurisdiction** and training on sovereign
German infrastructure, this makes Soofi-S one of the cleaner EU-AI-Act postures in the registry. A
fine-tuner placing a derivative on the EU market may become a provider for that derivative but
inherits an unusually complete upstream package.

<!-- item: evaluation -->
## Benchmarks & evaluation

The picture below is aggregated from the
Soofi pretraining technical report and independent coverage (`ev-perf`, `ev-arxiv`). The consistent
finding: Soofi-S is the **strongest fully-open model on aggregate English and German benchmarks**,
ahead of OLMo 3 32B, Apertus 70B, EuroLLM 22B and Alia 40B, matching dense **14-27B** models and
winning **code aggregates** in both languages among open base models - remarkable at only ~3B
active parameters. This item is marked *partial* because exact per-task numbers are still being
filled in on the public model cards (some are flagged "to be measured"); treat the leaderboard-style
claims as third-party/in-class rather than a frontier-vs-closed claim.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. The Instruct model card lists
     safety features as incomplete, and there is no independent red-team/CBRN/cyber battery to aggregate. -->
