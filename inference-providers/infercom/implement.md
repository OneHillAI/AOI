# Implement - Infercom

_How do we integrate it? API integration, region/sovereignty configuration, and portability
live here; authentication and rate limits are documented gaps below._

<!-- item: integration -->
## API integration

Infercom exposes **OpenAI-compatible APIs**, so an existing OpenAI client integrates by
changing the base URL and API key - chat/completions follow familiar shapes, making
integration largely a configuration change rather than a rewrite. Infercom is also reachable
via the **Opper AI gateway** for teams already routing through a gateway.

<!-- item: region-config -->
## Region & sovereignty configuration

**EU sovereignty is the default**: EU-hosted models run in **Munich** and **never leave the
EU**. The platform spans **EU/US/JP** regions and **jurisdiction follows the region chosen**,
so the key configuration decision is to select EU-hosted models when EU data residency is
mandatory. There is no separate ZDR toggle to manage - zero retention is the platform default.

<!-- item: portability -->
## Portability & exit

**The customer-facing exit path is clean.** Infercom speaks the **OpenAI-compatible API** over
**portable open-weight models**, so the same checkpoints run on GPU-based providers or
self-hosted stacks - switching cost is dominated by re-pointing the base URL and re-validating
outputs. The **SambaNova RDU is a provider-side hardware dependency**, not a customer-model
dependency - it does not lock your model choice in. Note that **explicit data-export/exit
terms were not fully confirmed**; confirm them contractually.
