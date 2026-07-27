# Implement - Runware

_How do we deploy it? Integration, residency configuration and exit live here._

<!-- item: integration -->
## API integration

Runware exposes **one unified API** that addresses its full open-model catalogue behind a single
schema, with the Sonic Inference Engine as the orchestration layer. **OpenAI compatibility is not
confirmed**, so integrate against Runware's own API shape and take endpoint and SDK
specifics from the developer docs.

<!-- item: region-config -->
## Region & residency configuration

Inference pods exist in the **US and central Europe**, and the Trust page advertises "EU & US"
residency. Whether an **EU-only region can be pinned contractually**, and how, was not found in the
read documents, and the binding entity is **Runware Ltd (UK)** under UK law. Confirm any
region-pinning guarantee directly before relying on EU residency.

<!-- item: portability -->
## Portability & exit

The catalogue is **open-weight Hugging Face models**, so the same checkpoints run on other providers
or self-hosted and the models are fully portable. The API, however, is a **proprietary unified
schema**, so client code is written to Runware's shape and must be rewritten to move. The switching
cost is in the API surface, not the model.
