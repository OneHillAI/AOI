# Implement - DeepInfra

_How do we integrate it? API integration, region/ZDR configuration, and portability live
here; authentication and rate limits are documented gaps below._

<!-- item: integration -->
## API integration

DeepInfra exposes an **OpenAI-compatible API** over **NVIDIA GPUs**, plus **per-hour dedicated
GPU instances** for reserved capacity. An existing OpenAI client integrates by changing the
base URL and API key, giving access to the ~77-90+ served models through familiar
chat/completions shapes - integration is largely a configuration change rather than a rewrite.

<!-- item: region-config -->
## Region & ZDR configuration

**Zero-retention is the default** posture, so no toggle is required for the core no-store
behaviour on DeepInfra's own open-model serving. Region control, by contrast, is effectively
absent: there is **no EU region to select** (US-only data centres) and **region pinning is
unconfirmed**. If EU residency is a requirement, DeepInfra does not meet it.

<!-- item: portability -->
## Portability & exit

For the **open-weight** catalogue the exit path is clean: the **OpenAI-compatible endpoint**
over portable checkpoints means the same models run on other providers or self-hosted, so
switching cost is dominated by re-pointing the base URL and re-validating outputs. The
exception is the **re-sold closed models** (Anthropic Claude, Google) - those are **not
portable** and carry different data terms, so any workload that leans on them does not inherit
the open-model portability.
