# Support - DeepSeek-V3 (MIT)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

The recurring issues are multi-node OOM and sharding for the 671B model, V3.1 hybrid-mode output parsing, and quant-engine version mismatches on lower-bit builds. The list is not exhaustive. The large community ecosystem is the practical first stop for deployment questions.

<!-- item: release-versioning -->
## Versions, changelog & cadence

V3-0324 and V3.1 are published on the verified `deepseek-ai` organisation. There is no formal changelog document, so the Hugging Face revision hash is the changelog anchor: pin it and diff revisions when a refresh lands. The licence line differs from the original December-2024 V3 (the `deepseek-v3-original` entry).

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

No formal vulnerability-disclosure or security policy is published for DeepSeek-V3. The only contact is the general `deepseek-ai` organisation presence. This is a gap that the deployer's own incident-response plan must cover.

<!-- item: channels -->
## Community & support channels

The `deepseek-ai` Hugging Face organisation and GitHub are the primary channels for usage and deployment questions, backed by a large third-party community.

<!-- item: deprecation -->
## Deprecation / end-of-life policy

No deprecation or end-of-life policy is published for DeepSeek-V3 checkpoints. Older revisions remain downloadable, but no sunset commitment is documented.

<!-- item: known-issues -->
## Tracked known issues

The standing issues are China-aligned censorship on sensitive topics, lighter safety coverage with no first-party guard model, and the operational burden of a 671B model. Assess has the behavioural detail.
