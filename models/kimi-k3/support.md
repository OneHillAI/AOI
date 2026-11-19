# Support - Kimi K3 (Moonshot AI)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Recurring pitfalls for a 2.8T-parameter MoE are multi-node out-of-memory errors, sharding misconfiguration, MXFP4/MXFP8 kernel-to-engine version mismatches, and checksum or revision drift on download. Pin the revision, verify checksums, and match engine and kernel versions to the card's documented stack. The list is not exhaustive.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Kimi K3 ships as a single checkpoint on the verified `moonshotai` org (announced around 2026-07-17, open weights around 2026-07-27). There is no Base/Instruct/Thinking split. The Hugging Face revision hash is the changelog anchor; pin it.

A post-trained successor, Kimi K3.1 Pro (Hugging Face, 2026-11-02, its own licence file), is a separate release. Moonshot's hosted platform calls K3 the previous-generation flagship.

<!-- item: channels -->
## Community & support channels

Support is the general Moonshot presence: the `moonshotai` Hugging Face org (model discussions) and the `MoonshotAI/Kimi-K3` GitHub repository (issues and the technical report). There is no dedicated support SLA.

<!-- item: known-issues -->
## Tracked known issues

The model card and technical report show no built-in safety with documented offensive-cyber willingness, undisclosed training data, code and compute, and the operational burden of a 2.8T-parameter model with no small variant. No published issue tracker covers these, so they belong in the deployer's own control stack.
