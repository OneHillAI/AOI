# Implement - Fireworks AI

_API integration, authentication, region and zero-retention configuration, rate limits and portability._

<!-- item: integration -->
## API integration

Fireworks exposes an OpenAI-compatible API at base URL `https://api.fireworks.ai/inference/v1`
(Chat Completions and Completions). A Responses API with MCP support is not documented on the
compatibility page, so do not rely on it.

<!-- item: authentication -->
## Authentication & account setup

Public docs confirm API-key-based access via the OpenAI-compatible client libraries. Org/project
key-scoping granularity is not documented, so confirm the exact setup in the Fireworks console.

<!-- item: region-config -->
## Region & residency configuration

On-demand deployments default to GLOBAL routing. Pinning to US, Canada, Europe, APAC (or a single
specific region) requires a quota granted by Fireworks and cannot be changed after the deployment
is created, per the on-demand-deployment docs. A separate "US-only serverless" tier and the
enterprise Sovereign / Virtual Cloud option (engine in your own cluster) sit at the two ends of
the residency spectrum. Default serverless in between is not region-pinned.

<!-- item: rate-limits -->
## Rate limits, tiers & quotas

Public docs describe pricing tiers (serverless per-token, on-demand per-GPU-second, batch at 50%
off) in detail but publish no rate-limit/quota table for the serverless API. Confirm current
throughput limits in the console before sizing a production workload.

<!-- item: portability -->
## Portability & exit

DPA Sec 11.2 documents the exit path: on request within 30 days of expiry Fireworks provides a
copy of Covered Data in a commonly used format, or a self-service download, then deletes all
copies (other than Administration Data and Usage Data). An OpenAI-compatible API over a
predominantly open-weight catalogue keeps workloads portable.
