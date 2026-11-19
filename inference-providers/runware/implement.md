# Implement - Runware

_How do we deploy it? Integration, residency configuration and exit live here._

<!-- item: integration -->
## API integration

Runware exposes **one unified API** that addresses its catalogue behind a single schema, with the
Sonic Inference Engine as the orchestration layer, plus a **Serverless** product for running your own
code, containers and models. **OpenAI compatibility was not found in the docs**, so integrate against
Runware's own API shape and take endpoint and SDK specifics from the developer docs.

<!-- item: region-config -->
## Region & residency configuration

Terms Sec 16 name hosting in the **United States, Germany and Romania**, and the footer advertises "EU
& US" residency. No contractual region pinning was found, and the binding entity is **Runware Ltd
(UK)** under English law. The Serverless page shows eu-west and eu-central region choices in a product
mock-up, which is not a contract term. Confirm any pinning guarantee directly before relying on EU
residency.

<!-- item: portability -->
## Portability & exit

The **open and community models** are open-weight checkpoints, so they run on other providers or
self-hosted. The **closed Partner Models** (GPT, Claude, Gemini, Kling and others) cannot be moved:
they are used under the owner's Model Licence. The API is a **proprietary unified schema**, so client
code is written to Runware's shape and must be rewritten to move. Serverless runs your own
containers, which keeps that workload portable.
