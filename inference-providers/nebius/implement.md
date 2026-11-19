# Implement - Nebius (Token Factory)

_How do we integrate it? API integration, region/ZDR configuration, rate limits and portability
live here; authentication is a documented gap below._

<!-- item: integration -->
## API integration

Nebius Token Factory is called with the standard OpenAI client libraries; the quickstart points
the OpenAI SDK at `https://api.tokenfactory.nebius.com/v1/` (docs and product page, re-read
2026-11-19).

<!-- item: authentication -->
## Authentication & account setup

Public docs confirm API-key-based access via the OpenAI-compatible client libraries, but
org/project key-scoping granularity was not detailed in the sources read this pass - confirm the
exact setup in the Nebius console.

<!-- item: region-config -->
## Region & ZDR configuration

A dedicated endpoint takes its region from the templates API at deployment; the Token Factory
data-plane page documents base URLs for eu-north1 (Finland), eu-west1 (France) and us-central1,
and the DPA pins dedicated endpoints to that region. **Public endpoints show Region "Global"**,
and the processing location can change without notice, so a region-specific base URL may stop
working. **Zero Data Retention is enabled per organisation in account settings**, not by default,
with a documented speed trade-off, and it also opts you out of Speculative Decoding.

<!-- item: rate-limits -->
## Rate limits, tiers & quotas

Limits are dynamic and visible only in the console. The docs give an illustrative baseline of 60
requests and 400,000 tokens per minute, raise the limit by 20 percent when average use over a
rolling 15-minute window reaches 80 percent, cut it by a third at 50 percent or less, and cap it
at 4x the base allocation, beyond which an Enterprise plan is required. Over the limit you get
HTTP 429, though requests may still be served at lower priority (header
`x-ratelimit-over-limit: yes`); busy endpoints return HTTP 529. Dedicated endpoints have no rate
limits.

<!-- item: portability -->
## Portability & exit

The DPA commits to **deleting or returning Customer Personal Data** on termination, at the
customer's choice. An OpenAI-compatible API over a predominantly open-weight catalogue keeps
served checkpoints portable. Serverless models are removed on dated notices with no automatic
rerouting, and dedicated endpoints for removed models stay available. Fine-tuned and distilled
models can be deleted by Nebius on three days' notice (Supplemental Terms 2.10).
