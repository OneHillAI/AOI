# Assess - Kimi K3 (Moonshot AI)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

Kimi K3 is Moonshot AI's frontier open-weights release: a natively multimodal 2.8T-total /
104B-active Mixture-of-Experts model with a 1M-token context and native text, image and video
understanding. Its intended use is coding, agentic, reasoning and vision workloads where you
want open weights rather than a closed API and can afford multi-node serving.

Because the weights ship with no safety tuning, no guard model, and a technical report that
documents offensive-cyber capability the model does not refuse, high-stakes, autonomous, or
EU-regulated decision-making is out of scope without the full external control stack described
in the Implement domain, and unsandboxed agentic or cyber-capable deployment is specifically
out of scope. There is no small variant, so single-GPU or laptop use is also out of scope.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **No built-in safety.** No safety tuning, guard model, refusal training, or content filtering
  is described, and the technical report's section 6.2.2 documents offensive-cyber capability
  (vulnerability discovery and exploit development) the model performs where frontier labs refuse.
- **Closed training story.** Training data, training code, and even the training-token and FLOP
  counts are undisclosed, so you can adapt the model but cannot reproduce it or bound its compute.
- **Multi-terabyte operational burden.** There are no small variants; the smallest viable
  deployment is a multi-node cluster (~1.4 TB of weights even at native MXFP4).
- **Possible topic filtering.** China-aligned filtering on politically sensitive prompts is
  present in the K2 lineage; it is not independently confirmed for K3 this session.

The offsetting advantage is capability: Kimi K3 is behind only Claude Fable 5 and GPT-5.6 Sol
overall and leads other open models on coding and agentic benchmarks.

<!-- item: openness -->
## Openness tier & components

Kimi K3 is `open_weights`, not open-science, and it is open-weights rather than closed-frontier
because the weights are downloadable. **Weights** ship as native MXFP4/MXFP8 checkpoints with a
model card and a technical report, so weights, documentation and licence are Open/Partial. But
the **training data**, the **training code**, and even the **training-token and FLOP figures**
are not released, and evaluation is only partially reproducible. You can run, adapt and
redistribute the model; you cannot see how it was made or reproduce it.

<!-- item: license -->
## License terms & permitted use

Kimi K3 ships under a custom **Kimi K3 License** (a modified-MIT text, not OSI-certified). It
grants use, modification, redistribution and sale, but adds two scale-linked conditions: a
**Model-as-a-Service** business with more than **$20M USD aggregate revenue over any consecutive
12 months** must **secure a separate agreement** with Moonshot AI before commercial deployment,
and any product with **more than 100M monthly active users** or **more than $20M USD monthly
revenue** must **prominently display "Kimi K3"** in its user interface. Internal use and access
through Moonshot's official products or certified partners are exempt. The Model-as-a-Service
gate is new relative to Kimi K2 and is the load-bearing input to the legal (2) score.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `moonshotai` org** on Hugging Face as native
**MXFP4 weights / MXFP8 activations** (not pickle), with a clear canonical source and no
malicious-mirror incident on record. The checkpoint trust checklist scores about **4/8**: the
base tensor format (safetensors) is not explicitly stated on the card, there is no scanned
checkpoint or documented mirror/quantization policy, and there is no cryptographic weight signing
or SLSA attestation, which is why provenance is a 3, not a 4 or 5. Verify per-file checksums and
pin the exact revision on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

Kimi K3 is a **GPAI** model. Its **training compute is unpublished**: the technical report gives
only a context-length curriculum and relative scaling-law FLOPs, with no total training-token
count and no absolute FLOP figure, so whether it crosses the 1e25-FLOP systemic-risk threshold is
**unknown** (a 2.8T-total / 104B-active frontier pre-train plausibly does, but that is an
inference, not a grounded fact). The custom **Kimi K3 License** is not an OSI-certified free
licence and carries monetisation-linked commercial restrictions, so it most likely **does not**
reach the open-source exemption. No **training-content summary** and no **copyright policy** are
published, and a China-based provider is unlikely to furnish an EU documentation package, so an
EU deployer must self-assemble compliance material and inherits these gaps on any derivative it
places on the market.

<!-- item: evaluation -->
## Benchmarks & evaluation

On the model card and reputable coverage, Kimi K3 sits **behind only Claude Fable 5 and GPT-5.6
Sol overall**, **ahead of other open models on coding and agentic** benchmarks, and **1st on the
public Frontend Code Arena** (1679), with strong reasoning (GPQA-Diamond 93.5), agentic
(BrowseComp 91.2, OSWorld-Verified 84.8) and vision (Video-MME 90.0) scores. OneHill did **not**
run its own benchmarks this session; the figures are aggregated from Moonshot's model card and
secondary coverage. This is marked *partial* because the results are publisher and third-party
rather than OneHill-reproduced.

<!-- item: safety-eval -->
## Independent safety evaluation

There is **no independent red-team** for Kimi K3, and the publisher provides no safety-tuned
variant. What exists is the technical report's own section 6.2.2, which is a **dangerous-capability
evaluation, not a mitigation one**: it measures offensive-cyber performance across Tier-1
vulnerability discovery and Tier-2 end-to-end exploit development, and states that Anthropic and
OpenAI frontier models refuse these tasks and are excluded, while Kimi K3 does not refuse. Treat
this as evidence of elevated misuse exposure, not of safety coverage, and supply your own guard
and red-team before any exposed deployment.
