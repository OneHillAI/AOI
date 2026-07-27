# Support - DeepSeek (V3 / R1)

_How do we keep it running and get help? Troubleshooting, versions/changelog, security
disclosure, community channels, deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Two classes of issue dominate. First, **reasoning-token / chat-template handling**: R1
emits inline `<think>` spans, so blank or malformed answers usually mean the template
wasn't applied or the reasoning span wasn't parsed/stripped - always go through
`apply_chat_template` and handle the reasoning tags. Second, **large-model serving**: the
full V3/R1 needs multi-GPU sharding, careful KV-cache/memory planning, and often a
quantized distill instead of the full weights on constrained hardware. If a checkpoint
misbehaves unexpectedly, verify you pulled the canonical org and the pinned revision rather
than a third-party quant.

<!-- item: release-versioning -->
## Versions & changelog

DeepSeek ships **versioned families** - V3, its point releases (e.g. V3.1) and successors,
alongside the R1 reasoning line and the R1-Distill checkpoints - each as its own Hugging
Face repository under the `deepseek-ai` org, with commit revisions serving as the
changelog. Pin a specific revision to stay reproducible and watch the org for new
checkpoints; there is no separate SemVer-style release feed for the weights.

<!-- item: channels -->
## Support & community channels

Community support runs through **Hugging Face model-repo discussions**, DeepSeek's
**GitHub**, and general community forums. There is no first-party enterprise support
contract for the open weights - plan to rely on community channels and your own
operations team.

<!-- item: known-issues -->
## Tracked known issues

The two distinctive, well-attested known issues are **topic censorship** on certain
political topics (aligned with Chinese content rules) and the **lighter-safety-tuning**
caveats - easier jailbreaks and residual prompt-injection susceptibility - documented in
the model card and third-party reporting. Both are behavioural properties to design
controls around rather than bugs that a patch removes. Note again that the hosted app/API's
privacy issues are a separate matter from the self-hosted weights.

<!-- security-disclosure and deprecation are `gap` items in entry.yaml - their gap_reasons
     render as callouts. There is no published vulnerability-disclosure policy or security
     contact for the weights, and no deprecation/EoL policy; superseded checkpoints simply
     remain on Hugging Face. -->
