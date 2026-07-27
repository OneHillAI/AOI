# Implement - Ollama

_How do we obtain and verify weights? Pulling via `ollama pull`, integrity-checking the SHA256 blob, and running locally live here; revision pinning and resource sizing are documented gaps._

<!-- item: obtain-weights -->
## Obtaining weights (ollama pull / Modelfile)

**`ollama pull`** resolves a **Modelfile** - a recipe of base weights + chat template +
parameters + an optional system prompt - and downloads the **SHA256-addressed GGUF blob**
into a local cache. You can build custom models from your own Modelfile with **`ollama
create`**. The registry is content-addressable and OCI-like (manifests plus addressed
blobs), so a pull is a straightforward one-command fetch.

<!-- item: verify-integrity -->
## Verifying integrity (SHA256 addressing)

Because blobs are **SHA256 content-addressed**, a pull is **integrity-checked** - the blob is
provably intact. But there is **no scanning and no signing** layer, and addressing proves
**integrity, not authenticity**. So verification is on you: where possible, **cross-check the
checksum against a canonical source** (for example, the publisher's Hugging Face repo) to
confirm you pulled the model you intended from the party you intended.

<!-- item: run-serve -->
## Running / serving locally

**`ollama run`** serves a pulled model locally over Ollama's CLI/API - this is the core of
the tool and its main convenience. One safety note carries over from Assess: **inspect the
chat template before serving untrusted GGUFs**, because template injection executes at
**inference time**, after the (safe) load step.
