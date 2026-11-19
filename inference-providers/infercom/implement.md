# Implement - Infercom

_API integration, authentication, region and zero-retention configuration, rate limits and portability._

<!-- item: integration -->
## API integration

Infercom exposes an OpenAI-compatible API at `https://api.infercom.ai/v1`, so an existing
OpenAI client integrates by changing the base URL and API key. The docs also list Anthropic-SDK
compatibility and a Responses API. Infercom is reachable via the Opper AI gateway for teams
already routing through a gateway.

<!-- item: region-config -->
## Region & sovereignty configuration

Region is chosen by model id, and the DPA covers only the EU ones. Models tagged "EU" in
`/v1/models` run in Munich. Non-EU models run on SambaNova's global infrastructure. DPA Sec
2a(4) obliges the customer to use only EU-hosted models unless a separate addendum covers
Non-EU Models.

There is no region switch and no ZDR toggle to manage: zero content retention is the platform
behaviour. Private connectivity is not offered ("Not today"), so the API is reached over public
HTTPS.

<!-- item: rate-limits -->
## Rate limits, tiers & quotas

Limits are per model and counted in requests. The free tier (no payment method) allows 20
requests per minute and 20 per day. The developer tier (card linked) allows, for example,
gpt-oss-120b 150 per minute and 50,000 per day and gemma-4-31B-it 80 and 20,000. Enterprise
defaults are gpt-oss-120b 500 per minute and 100,000 per day, with custom limits on request.
Rate-limit headers are returned on every response.

<!-- item: portability -->
## Portability & exit

The exit path is clean and includes shipped single-tenant and air-gapped options. Infercom
speaks the OpenAI-compatible API over portable open-weight models, so the same checkpoints run
on GPU providers or self-hosted stacks. Dedicated Capacity reserves single-tenant racks in
Munich, and on-premises SambaRack deployment (air-gap capable, about 90 days from contract to
production, bring-your-own-checkpoint) removes the hosted dependency entirely.

The SambaNova RDU is a provider-side hardware dependency in hosted mode only. On termination
the DPA requires return or deletion of personal data, and account data is deleted within 30
days.
