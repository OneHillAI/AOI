# Implement - Berget AI

_How do we integrate it? API integration, authentication, region/ZDR configuration, and
portability live here._

<!-- item: integration -->
## API integration

Berget exposes an **OpenAI-compatible chat/completions API at `https://api.berget.ai/v1`** -
point an existing OpenAI client at the base URL and API key. Because the surface is
OpenAI-shaped, it works with LangChain, LlamaIndex and the standard OpenAI SDKs, and the Mastra
model directory lists it as an OpenAI-compatible provider. Integration is a configuration
change, not a rewrite. The API listing (`GET /v1/models`) also reports each model's
capabilities, lifecycle status and price.

<!-- item: authentication -->
## Authentication & account setup

Authentication uses **bearer API keys**; migrating from OpenAI is a matter of switching the
API key and endpoint. Fine-grained organisation/project key scoping and rotation policy are
not documented; if key-scoping is a control requirement, confirm the available granularity
in the account console before rollout. API access needs an active plan, and the free Trial
needs a card at signup.

<!-- item: region-config -->
## Region & ZDR configuration

There is **no region toggle for serverless inference**. DPA Sec 10.1 lets the customer choose a
data centre for compute and storage only, "not including serverless inference", and all Berget
data centres are in the EEA. Zero data retention is the default for serverless inference under
DPA Appendix 2 and ToS Sec 7, so no sales step or setting is needed to get it. If you need a
named data centre or reserved capacity, that is a Dedicated Inference or cluster conversation
with sales, not an API flag.

<!-- item: portability -->
## Portability & exit

**The exit path is clean.** Berget speaks the **OpenAI-compatible API** over **open-weight
checkpoints** (Gemma 4, Mistral-Small, GLM-5.3-Flash, Kimi K3.1 Pro), so the same models run on
other providers or self-hosted stacks. Switching cost is dominated by re-pointing the base URL
and re-validating outputs. On exit, the Terms give a **30-day post-termination export window**
for Customer Data before irreversible deletion. The catalogue turns over: Llama, gpt-oss-120B and
GLM-4.7 were retired between June and September 2026, with 2 to 3 weeks notice for Active models
and none for Preview models, so pin to checkpoints you can run elsewhere.
