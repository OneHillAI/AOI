# Implement - DeepInfra

_How do we integrate it? API integration, authentication, rate limits, region/ZDR configuration,
and portability live here._

<!-- item: integration -->
## API integration

DeepInfra exposes an **OpenAI-compatible API** over **NVIDIA GPUs** (public models run on H100 or
A100 per the pricing page), plus **per-hour dedicated GPU instances** (A100 to B300) for reserved
capacity. An existing OpenAI client integrates by changing the base URL and API key, giving access
to the public catalogue (232 entries across modalities, 93 text-generation) - largely a
configuration change rather than a rewrite.

<!-- item: authentication -->
## Authentication & account setup

API keys go in an `Authorization: Bearer` header. Each key carries **scopes** chosen at creation and
editable later; a new key starts with `inference`, `models:read`, `account:read`, `lora:read` and
`voice:read`. DeepInfra also issues short-lived, scope-limited **JWTs** you can hand to third
parties. Organisation-level controls beyond key scopes were not read; confirm them in the
dashboard if you need them.

<!-- item: rate-limits -->
## Rate limits, tiers & quotas

On public models every account has a default of **200 concurrent requests per model**, which you
can ask to raise; the limit is concurrency, not requests per minute. **Private dedicated endpoints
have no account rate limit** and are bounded by their GPUs, returning 429 `Model busy` when
overloaded. Per-request service tiers: Standard (best effort at peak), Priority (1.5x price) and
Flex (0.8x price, with occasional unavailability).

<!-- item: region-config -->
## Region & ZDR configuration

**Zero Data Retention is contractual and applies to every account** on DeepInfra-hosted models, so
no toggle is required; retention for batch, asynchronous media or paid cache is something you opt
into. Region control is absent: the trust-centre FAQ says **US only, no EU region and no choice of
US region**. If EU residency is a requirement, DeepInfra does not meet it.

<!-- item: portability -->
## Portability & exit

For the **open-weight** catalogue the exit path is clean: the OpenAI-compatible endpoint over
portable checkpoints means the same models run on other providers or self-hosted. The exception is
the **partner models** (94 of 232 public entries, including Anthropic Claude and Google Gemini),
which are not portable and carry the partner's data terms. Older catalogue entries carry a
`deprecated` timestamp and a `replaced_by` pointer, and the status page lists scheduled
deprecations, so pin versions you can run elsewhere.
