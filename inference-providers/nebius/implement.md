# Implement - Nebius (Token Factory)

_How do we integrate it? API integration and region/ZDR configuration live here; authentication
and rate limits are documented gaps below._

<!-- item: integration -->
## API integration

Nebius Token Factory exposes **"a simple, OpenAI-compatible API"** usable with standard OpenAI
client libraries (product page and docs, read directly).

<!-- item: authentication -->
## Authentication & account setup

Public docs confirm API-key-based access via the OpenAI-compatible client libraries, but
org/project key-scoping granularity was not detailed in the sources read this pass - confirm the
exact setup in the Nebius console.

<!-- item: region-config -->
## Region & ZDR configuration

Region selection is documented for **AI Cloud** and **dedicated Token Factory endpoints**
(docs.nebius.com/overview/regions, independently re-read): **two** public self-serve EU regions
(Finland, France), plus US, Israel, and UK. **Correction:** Spain and Iceland are private,
existing-deployment-only regions, not self-serve - a prior draft counted them as public. **Zero
Data Retention is enabled per-account in settings**, not by default, with a documented latency
trade-off. Shared/public endpoints do not carry the same region-pinning guarantee as dedicated
endpoints - confirm which applies to your workload before relying on a residency claim.

<!-- item: rate-limits -->
## Rate limits, tiers & quotas

Public docs describe dedicated-endpoint autoscaling and pay-as-you-go-by-replica billing, but a
serverless rate-limit/quota table was not located in the sources read this pass - confirm current
throughput limits for your account before sizing a production workload.

<!-- item: portability -->
## Portability & exit

The DPA commits to **deleting or returning Customer Personal Data** on termination, at the
customer's choice. An OpenAI-compatible API over a predominantly open-weight catalogue keeps
served checkpoints portable. **Correction:** a prior claim that many flagship models are
dedicated-endpoint-only is not supported - they are publicly served per-token, simply superseded
by newer catalogue entries.
