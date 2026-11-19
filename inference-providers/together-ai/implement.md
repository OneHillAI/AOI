# Implement - Together AI

_How do we integrate it? API integration, authentication, region/ZDR configuration, rate limits
and portability live here._

<!-- item: integration -->
## API integration

Together's docs describe an **OpenAI-compatible REST API** at `api.together.ai/v1` with Python and
TypeScript SDKs, covering chat, completions, vision, image generation, text-to-speech and
speech-to-text. An existing OpenAI client integrates by changing the base URL and API key. Model
ids are namespaced (`openai/gpt-oss-120b`), so bare OpenAI model names return a 404. **Embeddings
are dedicated-only and `moderations.create` returns 404**; there is no serverless embedding model.
A Messages API and a Responses API are also listed.

<!-- item: authentication -->
## Authentication & account setup

Authentication uses a **bearer API key** (`TOGETHER_API_KEY`). Organisation admins control three
privacy toggles (Prompt storage, Passthrough models, Model training) in Organization Settings, and
the docs list roles and permissions (RBAC) and single sign-on under administration. Key rotation
and project-scoping detail was not read. An organisation on the Limited tier must add a payment
method before changing the privacy settings.

<!-- item: region-config -->
## Region & ZDR configuration

**ZDR is not the default.** An organisation admin turns off Prompt storage in the Privacy section
of Organization Settings; that also disables passthrough models, and it applies only to later
requests. For US-only processing send requests to `us-api.together.ai` (1.25x rates, 8 models; a
model that is not available there fails with 404 `region_unavailable` rather than falling back,
so do not retry against `api.together.ai`). EU residency is not self-serve: it needs a dedicated
endpoint or VPC deployment arranged with sales.

<!-- item: rate-limits -->
## Rate limits, tiers & quotas

Serverless is **best-effort**: under high demand you may see 429 or 503, and the docs advise
exponential backoff. Together may apply model-specific limits or access restrictions to models in
high demand. Purchased limits on legacy Enterprise and Scale contracts stay until the contract
expires. Committed throughput and a defined SLA come from provisioned throughput through sales.
The numeric per-tier limits were not read.

<!-- item: portability -->
## Portability & exit

Together speaks the **OpenAI-compatible API** over **portable open-weight checkpoints**, and
third-party analysis lists the same models across many providers, so exit is a base-URL change plus
output re-validation. With ZDR on, no prompt history is kept; files you uploaded for fine-tuning
or batch jobs stay stored until you delete them through the API, CLI or console.
