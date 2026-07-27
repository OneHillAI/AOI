# Assess - Mistral AI (open-weight family)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here. The headline theme: strong European regulatory posture and a
genuine Apache-2.0 core, tempered by a per-model licence split._

<!-- item: intended-use -->
## Intended & out-of-scope use

Mistral's open-weight family is a general-purpose set of assistant, coding and multilingual
text models, spanning the dense **Mistral 7B**, the **Mixtral 8x7B / 8x22B** mixture-of-experts
models, the 128K-context **Mistral Nemo (12B)** and the 24B **Mistral Small 3.x**, plus
specialist variants (Codestral for code, Mathstral, Devstral, Pixtral for vision). Its
*realistic* differentiator is being the leading **European** open-weight family: EU-domiciled,
strong multilingual coverage, and the cleanest GPAI regulatory posture in this class.

For adoption, deploy the **instruct (safety-tuned)** variant rather than the base checkpoint, and -
uniquely for this family - **confirm the specific model's licence** before any commercial
deployment (the Apache flagship models are unconditional; the MRL research-only models are
not). Mistral is not positioned as a safety-critical model; high-stakes, autonomous or
regulated decision-making is out of scope without the external control stack described in the
Implement domain.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **Licence split is the headline risk.** A team that assumes "Mistral = Apache" can trip over
  the research-only MRL models (Ministral 8B, Mistral Large, Pixtral Large) and the originally
  non-production MNPL Codestral. Commercial use of those requires a negotiated licence.
- **Lighter safety tuning.** Instruct alignment withstands casual jailbreaks, but coverage is
  historically lighter than the largest US labs, and the companion classifier (the Moderation
  API) is a hosted service rather than a broadly-shipped open guard-weight.
- **Closed training data and code.** Unlike a fully-open family, you cannot inspect or reproduce
  the training pipeline, so bias sources must be reasoned about from an opaque artifact.
- **Standard hallucination and prompt-injection profile** for the class; treat retrieved/tool
  content as untrusted.

The offsetting advantage is regulatory: an EU-domiciled, Code-of-Practice-signatory provider
with a genuine OSI licence on its flagship models.

<!-- item: openness -->
## Openness tier & components

Mistral earns `open_weights` honestly. The flagship general-purpose models ship **downloadable
Apache-2.0 weights** - an OSI-approved permissive licence rather than a click-through community gate -
and documentation is good. But **training data and training code are closed** (no reproduction
path, unlike a fully-open family), evaluation is only partial, and the licence component is
**split**: a meaningful subset of the family is research-only MRL. That mix is why Dimension 1
scores **4**, above a gated-open family but below the fully-open exemplars.

<!-- item: license -->
## License terms & permitted use

There is no single licence - read the model card:

- **Apache-2.0 (OSI-approved, unconditional commercial use):** Mistral 7B, Mixtral 8x7B / 8x22B,
  Mistral Nemo, Mistral Small 3.x, Magistral/Devstral Small. You may use, modify, redistribute
  and commercialize derivatives subject only to standard attribution/notice terms. Mistral has
  publicly **recommitted to Apache-2.0** for general-purpose models with Mistral Small 3.
- **Mistral Research Licence (MRL-0.1), research-only:** Ministral 8B, Mistral Large, Pixtral
  Large. Any commercial deployment requires a **separately negotiated** licence from Mistral.
- **MNPL (non-production):** originally Codestral.

This split is a load-bearing input to both the openness (4) and legal (4) scores - the Apache
core is genuinely clean, but the family is not uniformly open.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `mistralai` org** on Hugging Face in **safetensors**
(no pickle requirement) with per-file checksums. The checkpoint trust checklist scores about
**6/8**; the two missing controls are cryptographic weight signing (Sigstore/model-signing) and
SLSA build attestation, which is why provenance is a **4 rather than a 5**. No malicious-checkpoint
incident is on record for the canonical org. Community GGUF/AWQ/FP8 quants and hosted cloud
endpoints (Bedrock, Azure AI, Vertex, Together, OpenRouter) are separate artifacts - pin the
exact `mistralai` revision and verify checksums on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

This is Mistral's standout. The open-weight family is a GPAI model set that sits **well under the
10²⁵-FLOPs systemic-risk threshold** (the Apache releases are ≤24B dense or Mixtral MoE; only the
123B Mistral Large 2 approaches it, and that is a research-only MRL model rather than an Apache release),
so no Article 55 regime applies. The flagship Apache-2.0 models plausibly qualify for the
**Article 53 open-source exemption** from the Annex XI/XII technical-documentation duties; the
research-only MRL models, carrying a field-of-use restriction, do **not**. Two further facts make
Mistral the most EU-AI-Act-friendly non-US family here: it is **EU-domiciled (Paris)**, and it was
an **early signatory of the EU GPAI Code of Practice** - with no EU field-of-use ban of the kind
that affects some competitors. The surviving copyright-policy and training-content-summary
obligations are only *partially* met, because Mistral does not publish its training corpus. A
fine-tuner placing a derivative on the EU market may become a provider for that derivative.

<!-- item: evaluation -->
## Benchmarks & evaluation

The picture below is aggregated from
independent public leaderboards and third-party coverage (`ev-leaderboard`, `ev-wiki`). Mistral
models are **competitive-to-strong within each size class**: Mistral 7B and Mixtral were
class-leading at release, and Mistral Small 3.x remains strong for a 24B. Mistral is consistently
judged the **leading European open-weight family**. Treat published scores as third-party/in-class
framing; performance is capped at 4 for exactly that reason.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. Mistral ships a Moderation
     API and guardrailing guidance, but there is no broad independent CBRN/cyber/prompt-injection
     red-team battery to aggregate. -->
