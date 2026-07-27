# Implement - Groq

_How do we integrate it? API integration, region/ZDR configuration, rate limits, and
portability live here; authentication is a documented gap below._

<!-- item: integration -->
## API integration

Groq exposes an **OpenAI-compatible API**, documented in its OpenAI-compatibility docs: point an
existing OpenAI client at base URL **`https://api.groq.com/openai/v1`** with a Groq API key, and
the `/openai/v1/models` endpoint lists active models. The distinguishing factor is the runtime
underneath - open-weight models served on Groq's **custom LPU hardware** for very low latency - so
the integration surface is familiar while the performance profile is not. Note the docs flag that
**some advanced OpenAI features are not yet supported**.

<!-- item: region-config -->
## Region & ZDR configuration

Per the **your-data docs**, **zero data retention is available to all customers via Data
Controls**, so ZDR is a setting you enable rather than an enterprise-gated feature. Region control
is less mature: an **EU (Helsinki) data centre exists** but launched July 2025, **default storage
is US**, and **region pinning is unconfirmed**. If EU residency is mandatory, validate the current
region-pinning behaviour during onboarding rather than assuming it.

<!-- item: rate-limits -->
## Rate limits, tiers & quotas

Groq's **rate-limits docs** give free/developer-tier quotas - for example **Llama 3.3 70B** and
**gpt-oss-120B** at **300K TPM / 1K RPM**, and **Llama 3.1 8B** at **250K TPM / 1K RPM**, with
cached tokens not counting toward limits. Groq does not publish full paid-tier throughput
structure, so confirm the exact quotas that apply to your account in the Groq console before
sizing a production workload.

<!-- item: portability -->
## Portability & exit

At the API level Groq is **portable**: the **OpenAI-compatible endpoint** over **open-weight
models** (per the docs and supported-models catalogue) means the same checkpoints run on other
providers or self-hosted. The friction is that the **custom LPU hardware** and a
**curated/narrower catalogue** (no full DeepSeek / GLM / Mistral or arbitrary fine-tunes) are lock-in
and coverage considerations - you keep the API portability, but not necessarily every model or the
latency profile, when you move.
