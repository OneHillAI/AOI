# Assess - EuroLLM (EuroLLM-9B / EuroLLM-1.7B)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Deploy EuroLLM for multilingual, EU-facing text generation, assistant workloads and machine
translation across all 24 official EU languages plus roughly 11 more. Its realistic
differentiator is language breadth in a European, Apache-2.0 model, not raw capability. It is an
EU-funded, open-weight family (EuroLLM-9B and EuroLLM-1.7B, each in base and instruction-tuned
form) built by a European consortium (Unbabel, Instituto Superior Técnico / Instituto de
Telecomunicações, the University of Edinburgh and partners) on EuroHPC compute under Horizon
Europe.

Deploy the Instruct (safety-tuned) variant; the base checkpoints are untuned research artifacts
and out of scope for customer-facing use. EuroLLM is not a frontier model and is not positioned
for high-stakes, autonomous or safety-critical decision-making without the external control stack
described under Implement. Per-language quality and safety are uneven, so treat any single target
language as unverified until you evaluate it.

<!-- item: limitations -->
## Known limitations, bias & failure modes

EuroLLM-9B leads its size class for multilingual EU coverage, but a 9B model's raw
single-language reasoning is well below frontier. Do not expect category-topping performance on
hard English reasoning. Both sizes use a 4,096-token context window, short by current standards:
chunk or retrieve instead of relying on long-context recall. With 35 languages sharing capacity,
quality and safety behaviour vary by language and are not uniformly evaluated. Base checkpoints
have no safety tuning and are research artifacts.

The offsetting advantage is EU-native multilingual breadth under a permissive open licence.

<!-- item: openness -->
## Openness tier & components

EuroLLM earns `open_weights_recipe`. The weights (base and Instruct) are Apache-2.0 and the
documentation is open. A detailed technical report (arXiv 2506.04079) covers the tokenizer,
architecture, the ~4T-token data mixture and the training procedure, and the team also releases
the EuroFilter multilingual data-filter classifier and the EuroBlocks-Synthetic post-training
dataset. It stops short of the top "fully open" tier because the complete pre-training corpus and
an end-to-end training repository are not published as downloadable artifacts (training ran on
the open Megatron-LM codebase). `training_data`, `training_code` and `evaluation` are therefore
partial, not open. This is more open than a plain open-weights release but short of a full
open-science reproduction.

That description covers the tracked 2024 releases (EuroLLM-9B and 1.7B). The later 2512
generation (22B and the refreshed 9B) goes further, with a released web pre-training corpus
(`EuroWeb-2512`) and released pre-training and evaluation code per its report (arXiv 2602.05879).
That generation is a separate entity and is not scored here.

<!-- item: license -->
## License terms & permitted use

Apache-2.0 across base and Instruct weights. It is OSI-approved, with no field-of-use
restriction and unconditional commercial use, so no "community licence" caveats apply. You may use, modify, redistribute and commercialise
derivatives, subject only to the standard Apache attribution and notice terms. The licence feeds
the openness (4) and legal (4) scores.

No EuroLLM repo carries a standalone LICENSE file, so the licence statement is the Hugging Face
card (front matter and the line "License: Apache License 2.0."). The 9B repos are behind an
auto-approved Hugging Face gate that asks for your account username and email, which are shared
with the publisher; it adds no licence term. The 1.7B repos are not gated.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the verified `utter-project` org on Hugging Face in safetensors (no
pickle requirement) with per-file checksums. The technical report documents the pipeline and
names the data sources, so provenance is well described. The checkpoint trust checklist scores
5/8. The missing controls are cryptographic weight signing (Sigstore/model-signing), SLSA build
attestation and full-corpus publication for independent reconstruction, so provenance scores 3.
No incidents or malicious-mirror findings are on record for the canonical org. Pin the exact
revision and verify checksums on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

EuroLLM is a GPAI model well under the 10²⁵-FLOPs systemic-risk threshold (a 9B model trained on
~4T tokens is on the order of 10²³ FLOPs), so no Article 55 regime applies. It is EU-domiciled,
released under an OSI free/open-source licence and not monetised, so it plausibly qualifies for
the Article 53 open-source exemption from the Annex XI/XII technical-documentation duties.

Two obligations survive the exemption: a copyright policy and a public training-content summary.
The technical report partly covers them. It documents the data mixture (FineWeb-edu, HPLT,
MADLAD-400, CulturaX, mC4, The Stack) and the EuroFilter pipeline, though no fully published
corpus backs it. With EU domicile and Apache licensing, this is one of the cleaner EU AI Act
postures in the registry. A fine-tuner who places a derivative on the EU market may become a
provider for that derivative and receives a well-documented upstream package.

<!-- item: evaluation -->
## Benchmarks & evaluation

Aggregated from the EuroLLM-9B technical report (`ev-tech-report`) and independent reviews
(`ev-moonlight`, `ev-index-bench`). EuroLLM-9B is on par with Gemma-2-9B on multilingual
EU-language benchmarks (Arc-challenge, Hellaswag, MMLU via Okapi), ahead on WMT24++ translation
(COMET), and matches Mistral-7B on English. Its value is breadth of EU-language coverage at 9B,
not category-topping raw capability. Treat published scores as third-party and in-class, not as a
claim of frontier leadership.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. There is no independent
     multilingual red-team/CBRN/cyber battery to aggregate. -->
