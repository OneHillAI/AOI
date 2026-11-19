# Implement - Ollama

_How do we obtain and verify weights? Pulling via `ollama pull`, integrity-checking the SHA256 blob, and running locally live here; revision pinning and resource sizing remain documented gaps._

<!-- item: obtain-weights -->
## Obtaining weights (ollama pull / Modelfile)

**`ollama pull`** fetches a manifest and downloads its **SHA256-addressed blobs** into a local
cache. Since **v0.40.0** the registry can answer with a **manifest list**: a llama.cpp **GGUF**
child and an **MLX safetensors-derived** child (one layer per tensor). The client prefers MLX
on Apple Silicon and llama.cpp elsewhere, and an older client that does not request the list
gets the GGUF manifest. You can build custom models from a Modelfile with **`ollama create`**
and push them under your username with **`ollama push`**. A tag such as `gemma4:cloud` is
**not downloaded**: it runs on Ollama's servers and needs an account. If you upgrade to 0.40
or later, models you already pulled are upgraded in the background and the old copies stay as
backups; downgrading below 0.40 means re-pulling.

<!-- item: verify-integrity -->
## Verifying integrity (SHA256 addressing)

Because blobs are **SHA256 content-addressed**, a pull is **integrity-checked** - the blob is
provably intact. But there is **no scanning and no signing** layer (signing PR #11573 is
still open), and addressing proves **integrity, not authenticity**. So verification is on
you: where possible, **cross-check the checksum against a canonical source** (for example,
the publisher's Hugging Face repo) to confirm you pulled the model you intended from the
party you intended. The pull API also accepts an `insecure` flag that allows downloads over
insecure connections; leave it off.

<!-- item: run-serve -->
## Running / serving locally

**`ollama run`** serves a pulled model locally over the CLI and API, bound to `127.0.0.1` by
default - this is the core of the tool and its main convenience. Two safety notes: **inspect
the chat template before serving untrusted models**, because template injection executes at
**inference time**, and **do not bind the API to a public interface**, because `/api/create`
and `/api/push` have no authentication and were the path for the loader CVE-2026-7482. Set
**`OLLAMA_NO_CLOUD=1`** (or `disable_ollama_cloud` in `~/.ollama/server.json`) to stop any use
of `:cloud` models and cloud web search.
