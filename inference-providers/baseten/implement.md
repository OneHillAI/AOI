# Implement - Baseten

_API integration, authentication, region and zero-retention configuration, rate limits and portability._

<!-- item: integration -->
## API integration

Hosted **Model APIs** support the **OpenAI Chat Completions**, **OpenAI Responses** and
**Anthropic Messages** APIs (docs.baseten.co overview). Custom deploys use customer-authored
**Truss/Docker configs**, not a Baseten-proprietary format, which aids portability of the
deployment definition.

<!-- item: authentication -->
## Authentication & account setup

Public docs describe API-key-based access but do not detail org/workspace key-scoping
granularity. Confirm the exact setup in the Baseten console.

<!-- item: region-config -->
## Region & residency configuration

Select a region **per GPU model deployment** with `baseten model push --region eu` (slugs `us` and
`eu`) or the Management API, then call the regional endpoint
(`model-{model_id}-region-eu.api.baseten.co`). All replicas of that deployment run in the chosen
region. Chains and training jobs cannot select a region, and the organisation's compliance policy
limits which regions are allowed. **Regional environments** (multi-region fallbacks, exclusion
rules) and **Model APIs compliance policies** need Baseten support to enable. **Self-Hosted** lets
the workload plane run in any customer-chosen region or VPC. Baseten operates the control plane
for every option, and the docs do not say where it runs.

<!-- item: rate-limits -->
## Rate limits, tiers & quotas

Default Model API limits are published by account tier: Basic unverified 15 RPM and 100,000 TPM,
Basic verified 120 RPM and 500,000 TPM, Pro 120 RPM and 1,000,000 TPM, Enterprise custom. A model,
service tier or organisation can differ, and the Management API and response headers report the
live limits. Cached and uncached input tokens count equally toward the token limit.

<!-- item: portability -->
## Portability & exit

Terms & Conditions give a documented exit right: **Customer Content may be exported for 30 days**
after the Term ends, and Baseten will **delete Customer Content on written request**. Open-weight
models in the Model Library and customer-authored deploy configs keep the workload itself
portable beyond Baseten.
