# Implement - Groq

_API integration, authentication, region and zero-retention configuration, rate limits and portability._

<!-- item: integration -->
## API integration

Groq exposes an OpenAI-compatible API, documented in its OpenAI-compatibility docs. Point an existing OpenAI client at base URL `https://api.groq.com/openai/v1` with a Groq API key; the `/openai/v1/models` endpoint lists active models. Open-weight models run on Groq's custom LPU hardware for very low latency, so the integration surface is familiar and the performance profile is different. The docs flag that some advanced OpenAI features are not yet supported.

<!-- item: region-config -->
## Region & ZDR configuration

Per the your-data docs, zero data retention is available to all customers via Data Controls, so ZDR is a setting to enable and not an enterprise-gated feature. Enabling ZDR also stops the up-to-30-day troubleshooting and abuse logs.

Region control is less mature. EU capacity exists (Helsinki, launched July 2025, now listed as Vantaa and London), but retained data is stored in US GCP buckets and region pinning is unconfirmed. If EU residency is mandatory, validate the current region-pinning behaviour during onboarding.

<!-- item: rate-limits -->
## Rate limits, tiers & quotas

Groq's models page gives developer-plan quotas: gpt-oss-120B and gpt-oss-20B at 250K TPM / 1K RPM, gpt-oss-safeguard at 150K TPM and Qwen3.8-27B at 250K TPM / 1K RPM. The Llama models and enterprise preview models are contact-sales. Groq does not publish the full paid-tier throughput structure, so confirm the quotas for your account in the Groq console before sizing a production workload.

<!-- item: portability -->
## Portability & exit

At the API level Groq is portable. The OpenAI-compatible endpoint over open-weight models (per the docs and supported-models catalogue) means the same checkpoints run on other providers or self-hosted. The custom LPU hardware and a curated, narrower catalogue (no full DeepSeek / GLM / Mistral or arbitrary fine-tunes) are lock-in and coverage considerations. Moving keeps the API portability but not necessarily every model or the latency profile.
