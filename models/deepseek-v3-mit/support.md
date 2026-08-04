# Support - DeepSeek-V3 (MIT)

_Will it be maintained? Troubleshooting, versioning, security disclosure, channels, and
deprecation live here._

<!-- item: troubleshooting -->
## Common problems & fixes

The recurring issues are multi-node OOM / sharding for the 671B model, V3.1 hybrid-mode
output parsing, and quant-engine version mismatches on lower-bit builds. This list is not
exhaustive - the large community ecosystem is the practical first stop for deployment
questions.

<!-- item: release-versioning -->
## Versions, changelog & cadence

V3-0324 and V3.1 are published on the verified `deepseek-ai` organisation. There is no
formal changelog document; the **Hugging Face revision hash is the changelog anchor** - pin
it, and diff revisions when a refresh lands. Note the licence line differs from the original
December-2024 V3 (the `deepseek-v3-original` entry).

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

No formal published vulnerability-disclosure or security policy was found for DeepSeek-V3;
the only contact is the general `deepseek-ai` org presence. Recorded as a gap - factor it
into your own incident-response plan.

<!-- item: channels -->
## Community & support channels

The `deepseek-ai` Hugging Face organisation and GitHub are the primary channels for usage
and deployment questions, backed by a large third-party community.

<!-- item: deprecation -->
## Deprecation / end-of-life policy

No published deprecation or end-of-life policy for DeepSeek-V3 checkpoints. Older revisions
remain downloadable, but there is no documented sunset commitment - recorded as a gap.

<!-- item: known-issues -->
## Tracked known issues

The standing issues are China-aligned censorship on sensitive topics, lighter safety
coverage with no first-party guard model, and the operational burden of a 671B model. See
Assess for the behavioural detail.
