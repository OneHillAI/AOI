# Implement - Berget AI

_How do we integrate it? API integration, authentication, region/ZDR configuration, and
portability live here._

<!-- item: integration -->
## API integration

Berget exposes an **OpenAI-compatible chat/completions API at `https://api.berget.ai/v1`** -
point an existing OpenAI client at the base URL and API key. Because the surface is
OpenAI-shaped, it **works with LangChain, LlamaIndex** and the standard OpenAI SDKs.
Integration is a configuration change, not a rewrite.

<!-- item: authentication -->
## Authentication & account setup

Authentication uses **bearer API keys**; migrating from OpenAI is a matter of switching the
API key and endpoint. Fine-grained organisation/project key scoping and rotation policy are
not documented; if key-scoping is a control requirement, confirm the available granularity
in the account console before rollout.

<!-- item: region-config -->
## Region & ZDR configuration

There is **no region toggle to configure** - all inference runs in **Sweden/EU by default**
per the Privacy page, and **zero data retention is the default** under the Terms of Service
(Berget never stores prompt input or model output content). EU residency and no-store behaviour
are the out-of-the-box posture rather than a gated enterprise add-on, which removes the most
common EU-residency onboarding friction: there is no non-EU region to accidentally route to,
and no sales step required to enable ZDR.

<!-- item: portability -->
## Portability & exit

**The exit path is clean.** Berget speaks the **OpenAI-compatible API** over **portable
open-weight checkpoints** (Llama, Mistral, Gemma, gpt-oss, GLM), so the same models run on
other providers or self-hosted stacks. Switching cost is dominated by re-pointing the base URL
and re-validating outputs, not re-engineering. On exit, the Terms give a **30-day
post-termination export window** for Customer Data before it is irreversibly deleted.
