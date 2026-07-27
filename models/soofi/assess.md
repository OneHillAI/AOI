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
- **Strong-open, below frontier closed labs.** It is the strongest *fully open* model on English +
  German aggregates, a claim relative to open baselines rather than the largest closed labs.

The offsetting advantage is transparency: because the full per-source data accounting and code
are published, you can inspect what went into the model rather than reasoning about an opaque
artifact.

<!-- item: openness -->
## Openness tier & components

Soofi-S is aiming at the OLMo-style `fully_open` tier but has not landed
there, so it sits at **`open_weights`** with Dimension 1 scored **3** rather than 5. What is
genuinely delivered is the **documentation**: the pretraining report publishes **full per-source
data accounting** (source identifiers, raw and effective token counts, epoch multipliers, and even
sources evaluated but excluded) and commits the project to the **Open Source AI Definition (OSAID
1.0)**. That is a *pledge*, and the release has not followed: the **base weights are in a closed-beta phase**
("open model weights coming soon" on the `soofi-project/Soofi-Pretraining` README), the **training
and evaluation code is not yet released**, and the **open licence is unconfirmed** (no SPDX; the
LICENSE file returned HTTP 401). A `fully_open`/5 rating requires all six components
*actually* Open (downloadable weights under a permissive licence with runnable code), none of
which the preview yet meets. Openness is promised and well-documented rather than delivered. (A further
caveat: ~1.3% of Phase 1 tokens, the commercially licensed Genios corpus, are reported
in aggregate rather than being redistributable, so even the committed release clears OSAID 1.0 but
is only *nearly* compliant with stricter "every token redistributable" open-data proposals.)

<!-- item: license -->
## License terms & permitted use

Soofi-S is committed to a **permissive, OSAID-compliant open license** with **unconditional
commercial use** and no field-of-use restriction - you may use, modify, redistribute and
commercialise derivatives. Two honest caveats keep this from being a fully settled Apache-style
story: the **final license SPDX is not yet published**, and the **base weights are currently in a
closed-beta access phase** transitioning to the committed open release. This is why the legal
dimension scores **4** rather than 5 - the openness intent and released artifacts are excellent,
but the terms are still being finalised.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `Soofi-Project` org** on Hugging Face in **bf16
safetensors** (no pickle requirement), accompanied by **first-party GGUF and 3-bit
quantizations**, with per-file checksums. Because the data accounting, training code and
intermediate checkpoints are all public, provenance is highly auditable - the checkpoint trust
checklist scores **6/8**. The two missing controls are cryptographic weight signing
(Sigstore/model-signing) and SLSA build attestation, and the base weights sit behind a
closed-beta access gate, which is why provenance is a **4** rather than a 5. No incidents or
malicious-mirror findings are on record. Pin the exact revision and verify checksums on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

Soofi-S is a GPAI model but sits **well under the 10²⁵-FLOPs systemic-risk threshold** (~30B
total / ~3B active, ~27T tokens), so no Article 55 regime applies. It is
*committed* to a free/open-source release that would meet OSAID 1.0 and is not monetised, which
**would** qualify it for the **Article 53 open-source exemption** from the Annex XI/XII
technical-documentation duties - but the exemption cannot yet be relied on, because the open
licence is not finalised (base weights in closed beta, no SPDX), so there is no confirmed
free-and-open licence to point to today. The two
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
