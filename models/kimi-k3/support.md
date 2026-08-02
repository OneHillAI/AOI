# Support - Kimi K3 (Moonshot AI)

_How do we keep it running and get help? Troubleshooting, versioning, channels, and known
issues live here. Security disclosure and deprecation policy are recorded as gaps in entry.yaml._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated pitfalls for a 2.8T-parameter MoE: multi-node out-of-memory and sharding
mis-configuration, MXFP4/MXFP8 kernel-to-engine version mismatches, and checksum or revision
drift on download. Pin the revision, verify checksums, and match engine and kernel versions to the
card's documented stack. This is not an exhaustive catalogue.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Kimi K3 ships as a **single checkpoint** on the verified `moonshotai` org (announced around
2026-07-17, open weights around 2026-07-27). There is no Base/Instruct/Thinking split. The Hugging
Face revision hash is the changelog anchor; pin it.

<!-- item: channels -->
## Community & support channels

Support is the general Moonshot presence: the `moonshotai` Hugging Face org (model discussions)
and the `MoonshotAI/Kimi-K3` GitHub repository (issues and the technical report). There is no
dedicated support SLA.

<!-- item: known-issues -->
## Tracked known issues

From the model card and technical report: no built-in safety with documented offensive-cyber
willingness, undisclosed training data, code and compute, and the operational burden of a
2.8T-parameter model with no small variant. Track these against your own control stack rather than
a published issue tracker.
