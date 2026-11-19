# Assess - Mistral AI (open-weight family)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Mistral's open-weight family is a set of general-purpose assistant, coding and multilingual
text models. It spans the dense Mistral 7B, the Mixtral 8x7B and 8x22B mixture-of-experts
models, the 128K-context Mistral Nemo (12B), the 24B Mistral Small 3.x, and specialist
variants (Codestral for code, Mathstral, Devstral, Pixtral for vision). It is the leading
European open-weight family: EU-domiciled, strongly multilingual, and with the strongest GPAI
regulatory posture in its class.

Deploy the instruct (safety-tuned) variant, not the base checkpoint, and confirm the specific
model's licence before any commercial deployment. The Apache flagship models are unconditional
and the MRL research-only models are not. Mistral is not positioned as a safety-critical
model. High-stakes, autonomous or regulated decision-making is out of scope without the
external control stack described in the Implement domain.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The main risk is the licence split. A team that assumes Mistral means Apache can trip over the
research-only MRL models (Ministral 8B, Mistral Large 2, Pixtral Large) and the
non-production MNPL Codestral, whose commercial use requires a negotiated licence. The split is
wider than Apache versus MRL: Mistral's newest large releases (Mistral Large 4, Mistral Medium
3.5, Timestral) use custom licences with their own conditions and are not covered here.

Safety tuning is historically lighter than at the largest US labs. Instruct alignment
withstands casual jailbreaks, and the companion classifier (the Moderation API) is a hosted
service, not a broadly shipped open guard-weight.

Training data and code are closed, so the training pipeline cannot be inspected or reproduced
and bias sources must be reasoned about from an opaque artifact. The hallucination and
prompt-injection profile is standard for the class, so retrieved and tool content must be
treated as untrusted.

The offsetting advantage is regulatory: an EU-domiciled, Code-of-Practice-signatory provider
with an OSI-approved licence on its flagship models.

<!-- item: openness -->
## Openness tier & components

The tier is `open_weights`. The flagship general-purpose models ship downloadable Apache-2.0
weights under an OSI-approved permissive licence, and documentation is good. Training data and
training code are closed, so there is no reproduction path. Evaluation is only partial. The
licence component is split, because a meaningful subset of the family is research-only MRL.

The open-weights tier caps Dimension 1 at 3. Mistral sits at the top of that band, below the
recipe (4) and fully-open (5) tiers.

<!-- item: license -->
## License terms & permitted use

There is no single licence, so the model card decides.

The Apache-2.0 licence (OSI-approved, unconditional commercial use) covers Mistral 7B, Mixtral
8x7B and 8x22B, Mistral Nemo, Mistral Small 3.x and Magistral/Devstral Small. These can be
used, modified, redistributed and commercialised, subject only to standard attribution and
notice terms. Mistral has publicly recommitted to Apache-2.0 for general-purpose models with
Mistral Small 3. Mistral Large 3 (675B) and Ministral 3 (3B, 8B, 14B) are also Apache-2.0, per
the raw model cards (front matter plus the card's License section; those repos have no
separate LICENSE file).

The Mistral Research Licence (MRL-0.1) is research-only and covers Ministral 8B (2410),
Mistral Large 2 (2407, 2411) and Pixtral Large (2411). Any commercial deployment needs a
separately negotiated licence from Mistral. The non-production MNPL covers Codestral-22B-v0.1,
which is still tagged mnpl on Hugging Face.

The split feeds both the openness (3) and legal (4) scores. The Apache core is clean, but the
family is not uniformly open.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the verified `mistralai` org on Hugging Face as safetensors (no
pickle requirement) with per-file checksums. The checkpoint trust checklist scores about 6/8.
The two missing controls are cryptographic weight signing (Sigstore/model-signing) and SLSA
build attestation, which is why provenance scores 4, not 5. No malicious-checkpoint incident
is on record for the canonical org.

Community GGUF/AWQ/FP8 quants and hosted cloud endpoints (Bedrock, Azure AI, Vertex,
Together, OpenRouter) are separate artifacts. Pin the exact `mistralai` revision and verify
checksums on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

The open-weight family is a GPAI model set well under the 10²⁵-FLOPs systemic-risk threshold,
so no Article 55 regime applies. The Apache releases are ≤24B dense or Mixtral MoE. Only the
123B Mistral Large 2 approaches the threshold, and it is a research-only MRL model.

The flagship Apache-2.0 models plausibly qualify for the Article 53 open-source exemption from
the Annex XI/XII technical-documentation duties. The research-only MRL models carry a
field-of-use restriction and do not qualify.

Mistral is EU-domiciled (Paris) and was an early signatory of the EU GPAI Code of Practice,
with no EU field-of-use ban of the kind that affects some competitors. Together these make it
the most EU-AI-Act-friendly non-US family in the registry. The copyright-policy and
training-content-summary obligations are only partially met, because Mistral does not publish
its training corpus. A fine-tuner placing a derivative on the EU market may become a provider
for that derivative.

<!-- item: evaluation -->
## Benchmarks & evaluation

Aggregated from independent public leaderboards and third-party coverage (`ev-leaderboard`,
`ev-wiki`), Mistral models are competitive to strong within each size class. Mistral 7B and
Mixtral were class-leading at release, and Mistral Small 3.x remains strong for a 24B. Mistral
is consistently judged the leading European open-weight family. The scores are third-party,
in-class framing, so performance is capped at 4.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. Mistral ships a Moderation
     API and guardrailing guidance, but there is no broad independent CBRN/cyber/prompt-injection
     red-team battery to aggregate. -->
