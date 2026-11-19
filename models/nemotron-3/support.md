# Support - NVIDIA Nemotron 3 (Super + Nano)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated pitfalls for a hybrid Mamba-Transformer MoE pair: kernel-to-engine version mismatches for
the Mamba-2 and MoE layers, MoE sharding and multi-GPU memory for Super, NVFP4/FP8
quantization-engine compatibility, and revision drift on download. Match engine and kernel versions
to each variant's documented stack, pin the revision, and verify checksums. The list is not exhaustive.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Nemotron 3 Super and Nano were released around 2025-12 on the verified `nvidia` org, each with BF16,
FP8 and NVFP4 variants. There is no single-checkpoint changelog; the Hugging Face revision hash is the
anchor, so pin it.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

NVIDIA maintains a general corporate product-security reporting path (`nvidia.com/en-us/security/`).
A model-specific vulnerability-disclosure policy for Nemotron is unconfirmed, so model-level issue reporting goes through the Hugging Face and GitHub org presence.

<!-- item: channels -->
## Community & support channels

Support is the NVIDIA open-model presence: the `nvidia` Hugging Face org (model discussions), the
`NVIDIA-NeMo` GitHub organisation (the Nemotron recipes and NeMo Guardrails), and the `NVIDIA/garak`
repository for red-team and safety-tooling questions.

<!-- item: known-issues -->
## Tracked known issues

From the cards, recipes and licence: the partial-corpus non-reproducibility and the absence of a
published model-level safety evaluation are the recurring caveats. No issue tracker is published, so track them against your own control stack and red-team.
