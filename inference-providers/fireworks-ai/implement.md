# Implement - Fireworks AI

_How do we integrate it? API integration, region configuration, and portability live here;
authentication and rate limits are documented gaps below._

<!-- item: integration -->
## API integration

Fireworks exposes an **OpenAI-compatible API** at base URL **`https://api.fireworks.ai/inference/v1`**
(Chat Completions and Completions) - independently browser-confirmed 2026-09-21. **Correction:** a
prior claim of a Responses API with MCP support was not found on the compatibility docs page and
has been removed; do not rely on it.

<!-- item: authentication -->
## Authentication & account setup

Public docs confirm API-key-based access via the OpenAI-compatible client libraries, but
org/project key-scoping granularity is not documented in the sources read this pass - confirm the
exact setup in the Fireworks console.

<!-- item: region-config -->
## Region & residency configuration

On-demand deployments default to **GLOBAL** routing; pinning to **US, Europe, or APAC** (or a
single specific region) requires a **sales-granted quota**, per the on-demand-deployment docs. A
separate **"US-only serverless"** tier and the enterprise **BYOC/Virtual-Cloud** option sit at the
two ends of the residency spectrum - default serverless in between is not itself region-pinned.

<!-- item: rate-limits -->
## Rate limits, tiers & quotas

Public docs describe pricing tiers (serverless per-token, on-demand per-GPU-second, batch at 50%
off) in detail, but a rate-limit/quota table for the serverless API was not surfaced in the
sources read this pass - confirm current throughput limits in the console before sizing a
production workload.

<!-- item: portability -->
## Portability & exit

**Correction:** a prior claim of a DPA Sec 11.2 30-day data-export/deletion right is unconfirmed -
`fireworks.ai/dpa` is noindexed and unreachable to a real browser. What remains structurally true
and independently confirmed: an **OpenAI-compatible API** over a predominantly **open-weight
catalogue** keeps workloads portable, even without a confirmed documented exit clause.
