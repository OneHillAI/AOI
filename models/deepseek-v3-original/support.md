# Support - DeepSeek-V3 (original, DeepSeek License)

_Will it be maintained? Troubleshooting, versioning, security disclosure, channels, and
deprecation live here._

<!-- item: troubleshooting -->
## Common problems & fixes

The recurring issues are multi-node OOM / sharding for the 671B model, Base-vs-Chat variant
confusion (deploying the un-tuned Base by mistake), and quant-engine version mismatches on
lower-bit builds. This list is not exhaustive - the large community ecosystem is the
practical first stop for deployment questions.

<!-- item: release-versioning -->
## Versions, changelog & cadence

The original December-2024 V3 (Base + Chat) is published on the verified `deepseek-ai`
organisation. For new work it is effectively **superseded by the MIT V3-0324/V3.1
generations** (`deepseek-v3-mit`), which carry a cleaner licence. The **Hugging Face revision
hash is the changelog anchor**.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

No formal published vulnerability-disclosure or security policy was found for DeepSeek-V3;
the only contact is the general `deepseek-ai` org presence. Recorded as a gap - factor it
into your own incident-response plan.

<!-- item: channels -->
## Community & support channels

The `deepseek-ai` Hugging Face organisation and GitHub are the primary channels for usage and
deployment questions, backed by a large third-party community.

<!-- item: deprecation -->
## Deprecation / end-of-life policy

No published deprecation or end-of-life policy. The original V3 remains downloadable but is
effectively superseded by the MIT generations, with no documented sunset commitment -
recorded as a gap.

<!-- item: known-issues -->
## Tracked known issues

The standing issues are the use-restricted licence (relative to the MIT generations),
China-aligned censorship on sensitive topics, lighter safety coverage with no first-party
guard model, and the operational burden of a 671B model. See Assess for the detail.
