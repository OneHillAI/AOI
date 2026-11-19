# Assess - Kimi K2 (Moonshot AI)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Kimi is Moonshot AI's model line; the confirmed open release is Kimi K2, a trillion-parameter
Mixture-of-Experts model (1T total, 32B active) built with an explicit agentic, tool-use and
coding focus. It is intended for frontier-adjacent assistant, agentic and coding workloads where
an open-weight model is wanted over a closed API and the serving infrastructure is affordable.

Deploy the Kimi-K2-Instruct (safety-tuned) variant. Kimi-K2-Base is a foundation checkpoint for
research and fine-tuning and is out of scope for customer-facing use. The release is China-based,
applies China-aligned topic censorship, and has no companion guard model and no EU AI Act
documentation package. High-stakes, autonomous or EU-regulated decision-making is therefore out
of scope without the external control stack described under Implement and a self-assembled
compliance package.

<!-- item: limitations -->
## Known limitations, bias & failure modes

Kimi K2 applies content filtering aligned with Chinese content rules on politically sensitive
topics, as other China-based open-weight models do. Account for it, especially on non-coding
prompts. Instruct alignment withstands casual jailbreaks, but coverage is lighter than at
Western frontier labs and there is no companion guard or classifier model. Kimi-K2-Base has no
safety tuning and is a research artifact.

There are no small variants. The smallest viable deployment is a multi-node cluster even in
block-FP8 (~1 TB of weights). The offsetting strength is capability: on independent agentic and
coding benchmarks Kimi K2 is among the strongest open-weight models.

<!-- item: openness -->
## Openness tier & components

Kimi K2 is `open_weights`, not open-science. The Base and Instruct weights are downloadable under
a permissive modified MIT licence with a detailed model card and technical report, so weights,
documentation and licence are open. The 15.5T-token training data and the training code are not
released, and evaluation is only partially reproducible, so those components are closed or
partial. The model can be run, adapted and redistributed but not reproduced.

<!-- item: license -->
## License terms & permitted use

Kimi K2 ships under a Modified MIT License: standard MIT permissions (use, modify, redistribute,
commercialise) plus one attribution clause. A commercial product or service with more than 100
million monthly active users or more than $20 million USD in monthly revenue must prominently
display "Kimi K2" on its user interface. For nearly all adopters the licence works as permissive
MIT, and only large-scale deployers trigger the clause. The modification means the licence is not
OSI-certified, so verify the LICENSE file per checkpoint. The clause is one input to the legal
score of 3.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the verified `moonshotai` org on Hugging Face as block-FP8
safetensors (no pickle requirement) with per-file checksums. The checkpoint trust checklist
scores 5/8. The missing controls include cryptographic weight signing (Sigstore/model-signing)
and SLSA build attestation, so provenance scores 3, short of 4 and 5. No incidents or
malicious-mirror findings are on record for the canonical org. The weights are large and
distributed in block-FP8, so verify per-file checksums and pin the exact revision on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

Kimi K2 is a GPAI model. On the active-parameter compute estimate (~3×10²⁴ FLOPs: 32B active ×
15.5T tokens) it sits under the 10²⁵-FLOPs systemic-risk threshold. Unlike the largest
systemic-risk peers, no Article 55 hard flag applies and it plausibly reaches the Article 53
open-source exemption from the Annex XI/XII technical-documentation duties.

The exemption stays `partial` for two reasons. The modified MIT licence is not an OSI-certified
free/open licence. The surviving obligations, a copyright policy and a public training-content
summary, are not published and cannot be reconstructed because the corpus is closed. A
China-based provider is unlikely to furnish an EU documentation package, so an EU deployer must
self-assemble compliance material and takes on these gaps if it places a derivative on the
market.

<!-- item: evaluation -->
## Benchmarks & evaluation

Kimi K2 is among the strongest open-weight models on agentic and coding benchmarks (for example
SWE-bench Verified ≈ 65.8, plus strong tool-use and agentic scores). The figures are aggregated
from Moonshot's technical report and independent evaluation (`ev-perf`, `ev-tech-report`).
Coverage is partial because the results are third-party without independent reproduction and the
evaluation harness is only partially open.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. There is no independent
     red-team/CBRN/cyber battery to aggregate for Kimi K2. -->
