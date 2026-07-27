# Assess - EuroLLM (EuroLLM-9B / EuroLLM-1.7B)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

Deploy EuroLLM for multilingual, EU-facing text generation, assistant workloads and machine
translation across **all 24 official EU languages plus roughly 11 more** - its realistic
differentiator is language breadth in a genuinely European, Apache-2.0 model rather than raw
capability. It is an EU-funded, open-weight family - EuroLLM-9B and EuroLLM-1.7B, each in base
and instruction-tuned form - built by a European consortium (Unbabel, Instituto Superior
Técnico / Instituto de Telecomunicações, the University of Edinburgh and partners) on EuroHPC
compute under Horizon Europe.

For adoption, deploy the **Instruct (safety-tuned)** variant; the base checkpoints are
untuned research artifacts and are out of scope for customer-facing use. EuroLLM is not a
frontier model and is not positioned for high-stakes, autonomous, or safety-critical
decision-making without the external control stack described in the Implement domain. Because
per-language quality and safety are uneven, treat any single target language as unverified
until you evaluate it.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **9B capability ceiling.** EuroLLM-9B leads its size class for multilingual EU coverage,
  but a 9B model's raw single-language reasoning is well below frontier; do not expect
  category-topping performance on hard English reasoning.
- **Short 4k context.** Both sizes use a 4,096-token context window, short by current
  standards - chunk or retrieve rather than relying on long-context recall.
- **Uneven per-language quality and safety.** With 35 languages sharing capacity, quality and
  safety behaviour vary by language and are not uniformly evaluated.
- **Base checkpoints are untuned.** No safety tuning; treat them as research artifacts.

The offsetting advantage is EU-native multilingual breadth under a clean open licence.

<!-- item: openness -->
## Openness tier & components

EuroLLM earns `open_weights_recipe`. The **weights** (base + Instruct) are Apache-2.0 and the
**documentation** is genuinely open: a detailed technical report (arXiv 2506.04079) covers the
tokenizer, architecture, the ~4T-token data mixture and the training procedure, and the team
additionally releases the **EuroFilter** multilingual data-filter classifier and the
**EuroBlocks-Synthetic** post-training dataset. It stops short of the top "fully open" tier
because the complete pre-training corpus and an end-to-end training repository are **not**
published as downloadable artifacts (training was run on the open Megatron-LM codebase), so
`training_data`, `training_code` and `evaluation` are **partial** rather than open. This is
more open than a plain open-weights release but short of a full open-science reproduction.

<!-- item: license -->
## License terms & permitted use

Apache-2.0 across base and Instruct weights. It is **OSI-approved**, with no field-of-use
restriction and unconditional commercial use - no "community licence" caveats. You may use,
modify, redistribute, and commercialize derivatives, subject only to the standard Apache
attribution/notice terms. This clean licence is a load-bearing input to the openness (4) and
legal (4) scores.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `utter-project` org** on Hugging Face in
safetensors (no pickle requirement) with per-file checksums. The technical report documents
the pipeline and names the data sources, so provenance is well-described. The checkpoint
trust checklist scores **5/8**; the missing controls are cryptographic weight signing
(Sigstore/model-signing), SLSA build attestation, and full-corpus publication for independent
reconstruction - which is why provenance is a 4 rather than a 5. No incidents or malicious-mirror
findings are on record for the canonical org. Pin the exact revision and verify checksums on
download.

<!-- item: eu-ai-act -->
## EU AI Act posture

EuroLLM is a GPAI model but sits **well under the 10²⁵-FLOPs systemic-risk threshold** (a 9B
model trained on ~4T tokens is on the order of 10²³ FLOPs), so no Article 55 regime applies.
It is **EU-domiciled**, released under a genuine OSI free/open-source licence and not
monetised, so it plausibly qualifies for the **Article 53 open-source exemption** from the
Annex XI/XII technical-documentation duties. The two obligations that survive the exemption -
a copyright policy and a **public training-content summary** - are **partly** dischargeable
from the technical report, which documents the data mixture (FineWeb-edu, HPLT, MADLAD-400,
CulturaX, mC4, The Stack) and the EuroFilter pipeline, though not from a fully published
corpus. Combined with EU domicile and Apache licensing, this gives EuroLLM one of the cleanest
EU AI Act postures in the registry. A fine-tuner who places a derivative on the EU market may
become a provider for that derivative, but inherits an unusually clean and well-documented
upstream package.

<!-- item: evaluation -->
## Benchmarks & evaluation

The figures below are aggregated from
the EuroLLM-9B technical report (`ev-tech-report`) and independent reviews (`ev-moonlight`,
`ev-index-bench`). The consistent picture: EuroLLM-9B is **on par with Gemma-2-9B on
multilingual EU-language benchmarks** (Arc-challenge, Hellaswag, MMLU via Okapi), **ahead on
WMT24++ translation** (COMET), and **matches Mistral-7B on English**. Its value proposition is
breadth of EU-language coverage at 9B rather than category-topping raw capability. Treat published
scores as third-party/in-class rather than a claim of frontier leadership.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. There is no independent
     multilingual red-team/CBRN/cyber battery to aggregate. -->
