# Implement - Ollama

_Obtaining and verifying weights, integrity checks, revision pinning and running locally._

<!-- item: obtain-weights -->
## Obtaining weights (ollama pull / Modelfile)

`ollama pull` fetches a manifest and downloads its SHA256-addressed blobs into a local cache.
Since v0.40.0 the registry can answer with a manifest list: a llama.cpp GGUF child and an MLX
safetensors-derived child (one layer per tensor). The client prefers MLX on Apple Silicon and
llama.cpp elsewhere, and an older client that does not request the list gets the GGUF manifest.

Custom models are built from a Modelfile with `ollama create` and pushed under a username with
`ollama push`. A tag such as `gemma4:cloud` is not downloaded: it runs on Ollama's servers and
needs an account. After an upgrade to 0.40 or later, models already pulled are upgraded in the
background and the old copies stay as backups. Downgrading below 0.40 means re-pulling.

<!-- item: verify-integrity -->
## Verifying integrity (SHA256 addressing)

Blobs are SHA256 content-addressed, so a pull is integrity-checked and the blob is provably
intact. There is no scanning and no signing layer (signing PR #11573 is open), and addressing
proves integrity, not authenticity. Where possible, cross-check the checksum against a
canonical source, for example the publisher's Hugging Face repo, to confirm the model came from
the intended party. The pull API also accepts an `insecure` flag that allows downloads over
insecure connections; leave it off.

<!-- item: run-serve -->
## Running / serving locally

`ollama run` serves a pulled model locally over the CLI and API, bound to `127.0.0.1` by
default. This is the core of the tool and its main convenience.

Inspect the chat template before serving untrusted models, because template injection executes
at inference time. Do not bind the API to a public interface: `/api/create` and `/api/push`
have no authentication and were the path for the loader CVE-2026-7482. Set `OLLAMA_NO_CLOUD=1`
(or `disable_ollama_cloud` in `~/.ollama/server.json`) to stop any use of `:cloud` models and
cloud web search.
