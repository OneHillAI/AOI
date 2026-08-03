# Support - NVIDIA Nemotron 3 Ultra (550B)

_How do we keep it running and get help? Troubleshooting, versioning, security disclosure, channels
and known issues live here. Deprecation policy is recorded as a gap in entry.yaml._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated pitfalls for a frontier-scale hybrid Mamba-Transformer MoE: multi-node MoE sharding and
memory, kernel-to-engine version mismatches for the Mamba-2 and MoE layers, NVFP4
quantization-engine compatibility, and revision drift on download. Match engine and kernel versions to
the documented stack, plan the sharding topology, pin the revision, and verify checksums. This is not
an exhaustive catalogue.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Nemotron 3 Ultra was released around 2025-12 on the verified `nvidia` org with BF16 and NVFP4 variants.
There is no single-checkpoint changelog; the Hugging Face revision hash is the anchor, so pin it.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

NVIDIA maintains a general corporate product-security reporting path (`nvidia.com/en-us/security/`). A
model-specific vulnerability-disclosure policy for Nemotron was not confirmed this pass, so treat
model-level issue reporting as going through the Hugging Face and GitHub org presence.

<!-- item: channels -->
## Community & support channels

Support is the NVIDIA open-model presence: the `nvidia` Hugging Face org (model discussions), the
`NVIDIA-NeMo` GitHub organisation (the Nemotron recipes and NeMo Guardrails), and the `NVIDIA/garak`
repository for red-team and safety-tooling questions.

<!-- item: known-issues -->
## Tracked known issues

From the card, recipe and white paper: the non-open intermediate checkpoints (not reproducible), the
absence of a model-level safety evaluation, and the undisclosed training compute (systemic-risk status
unresolved) are the recurring caveats. Track these against your own control stack and red-team rather
than a published issue tracker.
