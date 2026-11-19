# Assess - Ai2 OLMo (OLMo 2 / OLMo 3)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

OLMo is Ai2's "open science" language-model family. It spans OLMo 2 (1B, 7B, 13B and 32B) and OLMo 3 (7B and 32B, with base, instruct and reasoning "Think" checkpoints).

Intended use is research and general-purpose assistant workloads. The differentiator is auditability: any setting where an organisation must be able to explain exactly what went into the model.

Deploy the Instruct (safety-tuned) variant. Base checkpoints are untuned research artifacts and are out of scope for customer-facing use. OLMo is not positioned as a frontier or safety-critical model, so high-stakes, autonomous or regulated decision-making is out of scope without the external control stack described in the Implement domain.

<!-- item: limitations -->
## Known limitations, bias & failure modes

Capability is solid within its class and not frontier. A same-size commercial instruct model will usually edge OLMo on raw benchmarks. Instruct alignment withstands casual jailbreaks and residual risks are documented, but coverage is lighter than at the large commercial labs and no companion guard or classifier model exists.

The Dolma corpus is English-dominant, so other-language behaviour is incidental and not a supported target. Base checkpoints have no safety tuning and are research artifacts. Because the full training data is published, it can be inspected for known problem sources.

<!-- item: openness -->
## Openness tier & components

OLMo is `fully_open`. All six openness components are Open: downloadable Apache-2.0 weights, the full Dolma training dataset, runnable training code, released evaluation code and results, complete technical reports, and an OSI-approved licence.

This is the top "Open Science / Class I" tier of the Linux Foundation Model Openness Framework, so Dimension 1 scores 5 on third-party classification (`ev-mof`) and not on publisher marketing.

<!-- item: license -->
## License terms & permitted use

Apache-2.0 covers the weights and the training code. The published data (Dolma, Dolma 3, Dolci) is ODC-By, and one Dolci subset is CC-BY-SA-4.0. Apache-2.0 is OSI-approved, its text has no field-of-use restriction, and it allows unconditional commercial use. Weights can be used, modified, redistributed and commercialised, subject only to the standard Apache attribution and notice terms.

The OLMo 3 cards and the OLMo 2 Instruct cards say the model is "intended for research and educational use in accordance with Ai2's Responsible Use Guidelines" (`ev-resp-use`). Those guidelines list disallowed uses outside "Research Use", including political campaigning, automated social-media posting and classifying people by protected characteristics. They are a separate Ai2 document and not part of the Apache-2.0 text, and the page does not say whether they bind someone who only downloaded the weights. Ai2's blog says the datasets carry no licence restrictions; the dataset cards say otherwise (`ev-dolma3`). Have counsel read the guidelines before a use case close to that list.

The caveat is scored. Legal is 4 and the use-and-modify factor is moderate, so the ownership level is partial, because substantial needs a strong use-and-modify factor. Openness (5) is unaffected, because it measures what is released and the Apache-2.0 text itself has no field-of-use limit. Ownership returns to substantial if Ai2 states that the guidelines are guidance and not a licence condition.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the verified `allenai` org on Hugging Face in safetensors (no pickle requirement) with per-file checksums. Training data, training code and intermediate checkpoints are all public, so provenance is fully auditable and the pipeline can in principle be reconstructed.

The checkpoint trust checklist scores 6/8. The two missing controls are cryptographic weight signing (Sigstore/model-signing) and SLSA build attestation, so provenance scores 4 and not 5. No incidents or malicious-mirror findings are on record for the canonical org. Pin the exact revision and verify checksums on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

OLMo is a GPAI model well under the 10²⁵-FLOPs systemic-risk threshold (models are ≤32B), so no Article 55 regime applies. Released under a free/open-source licence and not monetised, it plausibly qualifies for the Article 53 open-source exemption from the Annex XI/XII technical-documentation duties.

Two obligations survive the exemption: a copyright policy and a public training-content summary. Because Dolma is fully published, OLMo can satisfy the training-content summary directly from released artifacts. This makes OLMo the most EU-AI-Act-friendly family in the registry. A fine-tuner who places a derivative on the EU market may become a provider for that derivative, but starts from a complete upstream package.

<!-- item: evaluation -->
## Benchmarks & evaluation

Ai2's OLMo 2/3 technical reports and independent leaderboards (`ev-perf`, `ev-tech-report`) give a consistent picture: OLMo is competitive within its size class but not frontier-leading on raw capability. A same-size commercial instruct model will usually edge it.

Its value is transparency and reproducibility, since the eval harness and results are themselves open. Treat published scores as third-party, in-class results and not as a claim of category leadership.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. There is no independent
     red-team/CBRN/cyber battery to aggregate. -->
