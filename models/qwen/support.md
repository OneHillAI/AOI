# Support - Qwen (Qwen3 family)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Common pitfalls from the model cards and ecosystem are out-of-memory errors on the large variants (235B MoE, 480B-Coder), chat-template or thinking-mode mismatch, and checksum drift across hubs.

Quantise or add GPUs for the first. Apply the tokenizer's chat template and choose thinking or non-thinking mode explicitly for the second. Verify that Hugging Face and ModelScope weights match and pin the revision for the third. The list is a starting catalogue.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Qwen ships on a rapid generational cadence (Qwen3 dense, MoE and Coder lines), tracked as immutable revisions on the verified Qwen org across Hugging Face and ModelScope. Pin a specific revision for reproducibility.

<!-- item: channels -->
## Community & support channels

Support is community-driven: Qwen Hugging Face and ModelScope org discussions, plus a broad presence across serving-stack ecosystems (Ollama, vLLM). No enterprise support desk is documented for the open weights.

<!-- item: known-issues -->
## Tracked known issues

Known issues are China-aligned topic censorship, lighter safety coverage than at frontier labs, and an unclosed EU Article 55 gap on the largest (systemic-risk) variants.
