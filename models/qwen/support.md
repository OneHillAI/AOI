# Support - Qwen (Qwen3 family)

_How do we keep it running and get help? Troubleshooting, release/versioning, community
channels and known issues live here; security disclosure and deprecation are documented gaps
below._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated pitfalls from the model cards and ecosystem:

- **OOM on the large variants** (235B MoE, 480B-Coder) - quantize or add GPUs.
- **Chat-template / thinking-mode mismatch** - apply the tokenizer's chat template and decide
  on thinking vs non-thinking mode explicitly.
- **Checksum drift across hubs** - verify Hugging Face and ModelScope weights match and pin
  the revision.

This is a starting catalogue; it does not cover every case.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Qwen ships on a **rapid generational cadence** (Qwen3 dense, MoE and Coder lines), tracked
as **immutable revisions** on the verified Qwen org across **Hugging Face and ModelScope**.
Pin to a specific revision for reproducibility.

<!-- item: channels -->
## Community & support channels

Support is **community-driven**: Qwen **Hugging Face** and **ModelScope** org discussions,
plus a broad presence across serving-stack ecosystems (Ollama, vLLM). There is no
enterprise support desk documented for the open weights.

<!-- item: known-issues -->
## Tracked known issues

From the model-card and third-party caveats: **China-aligned topic censorship**, **lighter
safety coverage** than frontier labs, and an **unclosed EU Article 55 gap** on the largest
(systemic-risk) variants.
