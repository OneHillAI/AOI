# Implement - Baseten

_How do we integrate it? API integration, region configuration, and portability live here;
authentication and rate limits are documented gaps below._

<!-- item: integration -->
## API integration

Hosted **Model APIs** support the **OpenAI Chat Completions API** and a **beta Anthropic Messages
API** (docs.baseten.co/overview, read directly). Custom deploys use customer-authored
**Truss/Docker configs** rather than a Baseten-proprietary format, which itself aids portability
of the deployment definition.

<!-- item: authentication -->
## Authentication & account setup

Public docs describe API-key-based access, but org/workspace key-scoping granularity was not
detailed in the sources read this pass - confirm the exact setup in the Baseten console.

<!-- item: region-config -->
## Region & residency configuration

**"Regional environments"** route a deployment exclusively to a designated geographic region, but
require Baseten to configure it - the docs say to **contact support** to confirm availability for
the region you need; there is no published, self-serve region list. **Self-Hosted** is the
alternative: the workload plane runs in any customer-chosen region/VPC, including the EU.

<!-- item: rate-limits -->
## Rate limits, tiers & quotas

Baseten's pricing page documents GPU/token rates and account tiers (Basic/Pro/Enterprise) in
detail, but a specific rate-limit/quota table was not located in the sources read this pass -
confirm current throughput limits for your account before sizing a production workload.

<!-- item: portability -->
## Portability & exit

Terms & Conditions give a documented exit right: **Customer Content may be exported for 30 days**
after the Term ends, and Baseten will **delete Customer Content on written request**. Open-weight
models in the Model Library and customer-authored deploy configs keep the workload itself
portable beyond Baseten.
