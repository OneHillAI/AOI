# Assess - Kimi (Moonshot AI - Kimi K2)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

Kimi is Moonshot AI's model line; the confirmed open release is **Kimi K2**, a trillion-parameter
Mixture-of-Experts model (1T total / 32B active) built with an explicit **agentic, tool-use and
coding** focus. Its intended use is frontier-adjacent assistant, agentic, and coding workloads
where you want an open-weight model rather than a closed API - and where you can afford the
serving infrastructure.

For adoption, deploy the **Kimi-K2-Instruct** (safety-tuned) variant; **Kimi-K2-Base** is a
foundation checkpoint for research and fine-tuning and is out of scope for customer-facing use.
Because it is a China-based release with China-aligned topic censorship, no companion guard
model, and no EU AI Act documentation package, high-stakes, autonomous, or EU-regulated
decision-making is out of scope without the external control stack described in the Implement
domain and a self-assembled compliance package.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **China-aligned topic censorship.** Like other China-based open-weight models, Kimi K2
  applies content filtering aligned with Chinese content rules on politically sensitive topics
  - a behavioural quirk to account for, especially for non-coding prompts.
- **Lighter safety tuning, no guard model.** Instruct alignment withstands casual jailbreaks
  but coverage is lighter than Western frontier labs and there is no companion guard/classifier.
- **Trillion-parameter operational burden.** There are no small variants; the smallest viable
  deployment is a multi-node cluster even in block-FP8 (~1 TB of weights).
- **Base checkpoint is untuned.** Kimi-K2-Base has no safety tuning and should be treated as a
  research artifact.

The offsetting advantage is capability: on independent agentic/coding benchmarks Kimi K2 is
among the strongest open-weight models available.

<!-- item: openness -->
## Openness tier & components

Kimi K2 is `open_weights` rather than open-science. **Weights** (Base and Instruct) are downloadable
under a permissive **modified MIT** license with a detailed model card and technical report, so
weights, documentation and license are Open. But the **15.5T-token training data** and the
**training code** are not released, and evaluation is only partially reproducible - so those
components are Closed/Partial. You can run, adapt and redistribute the model, but you cannot
reproduce it.

<!-- item: license -->
## License terms & permitted use

Kimi K2 ships under a **Modified MIT License**: standard MIT permissions (use, modify,
redistribute, commercialize) **plus one attribution clause** - if the software or a derivative
is used in a commercial product or service with **more than 100 million monthly active users**
**or more than $20 million USD in monthly revenue**, you must **prominently display "Kimi K2"**
on that product's user interface. For nearly all adopters the license is effectively permissive
MIT; only large-scale deployers trigger the attribution requirement. Two caveats: the
modification means it is **not OSI-certified**, and you should verify the LICENSE file per
checkpoint. This clause is a load-bearing input to the legal (3) score.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `moonshotai` org** on Hugging Face as **block-FP8
safetensors** (no pickle requirement) with per-file checksums. The checkpoint trust checklist
scores **5/8**; the missing controls include cryptographic weight signing (Sigstore/model-signing)
and SLSA build attestation, which is why provenance is a 4 rather than a 5. No incidents or
malicious-mirror findings are on record for the canonical org. Because the weights are large and
distributed in block-FP8, verify per-file checksums and pin the exact revision on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

Kimi K2 is a **GPAI** model. On the active-parameter compute estimate (~3×10²⁴ FLOPs: 32B
active × 15.5T tokens) it sits **under the 10²⁵-FLOPs systemic-risk threshold** - so, unlike the
largest systemic-risk peers, there is **no Article 55 hard flag** and it plausibly reaches the
**Article 53 open-source exemption** from the Annex XI/XII technical-documentation duties. Two
caveats keep this at `partial`: the modified MIT license is **not an OSI-certified** free/open
license, and the surviving obligations - a **copyright policy** and a **public training-content
summary** - are **not published**, and cannot be reconstructed because the corpus is closed. A
China-based provider is unlikely to furnish an EU documentation package, so an EU deployer must
self-assemble compliance material and inherits these gaps if it places a derivative on the market.

<!-- item: evaluation -->
## Benchmarks & evaluation

Kimi K2 is **among the strongest open-weight models on agentic and coding benchmarks** (for
example SWE-bench Verified ≈ 65.8, plus strong tool-use/agentic scores), frontier-adjacent
rather than merely in-class. The
figures are aggregated from Moonshot's technical report and independent evaluation (`ev-perf`,
`ev-tech-report`). This is marked *partial* because the results are third-party without
independent reproduction and the evaluation harness is only partially open.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. There is no independent
     red-team/CBRN/cyber battery to aggregate for Kimi K2. -->
