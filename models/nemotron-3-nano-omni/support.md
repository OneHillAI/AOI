# Support - NVIDIA Nemotron 3 Nano Omni (multimodal)

_How do we keep it running and get help? Troubleshooting, versioning, security disclosure, channels
and known issues live here. Deprecation policy is recorded as a gap in entry.yaml._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated pitfalls for a small multimodal hybrid Mamba-Transformer MoE: multimodal preprocessing and
processor-config mismatches, kernel-to-engine version mismatches for the Mamba-2 and MoE layers, using
the wrong repo path because of the missing "NVIDIA-" prefix, and revision drift on download. Match
engine and kernel versions to the documented stack, confirm the processor config, pin the revision, and
verify checksums. This is not an exhaustive catalogue.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Nemotron 3 Nano Omni was released on 2026-04-20 (BF16; FP8 and NVFP4 followed on 2026-04-24, and
build.nvidia.com on 2026-04-28) on the verified `nvidia` org. There is no single-checkpoint
changelog; the Hugging Face revision hash is the anchor, so pin it. The licence version line is
"v. March 9, 2026" while its web page shows an April 2, 2026 release date.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

NVIDIA maintains a general corporate product-security reporting path (`nvidia.com/en-us/security/`). A
model-specific vulnerability-disclosure policy for Nemotron was not confirmed this pass, so treat
model-level issue reporting as going through the Hugging Face and GitHub org presence.

<!-- item: channels -->
## Community & support channels

Support is the NVIDIA open-model presence: the `nvidia` Hugging Face org (model discussions), the
`NVIDIA-NeMo` GitHub organisation (the `omni3` recipe and NeMo Guardrails), and the `NVIDIA/garak`
repository for red-team and safety-tooling questions.

<!-- item: known-issues -->
## Tracked known issues

From the card and recipe: the weaker open-data posture and unadvertised recipe, the absence of a
model-level safety evaluation over the multimodal input path, and the two dates on the licence page are the
recurring caveats. Track these against your own control stack and red-team rather than a published issue
tracker.
