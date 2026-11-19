# Use - Ollama

_Available models, supported formats and downstream integration._

<!-- item: catalog-scope -->
## Catalogue scope & publishers

Ollama offers a curated official library, user-pushed community models by registry namespace,
and cloud-enabled `:cloud` models (about two dozen listed with per-token prices on the pricing
page, and a published retirement list; retired cloud models do not affect local ones).

There is no per-publisher identity verification, so community models rest on user-supplied
provenance. Curation of the official library is the main trust signal, and it does not
substitute for verified publisher identity or scanning.

<!-- item: formats-supported -->
## Formats supported

Ollama distributes GGUF blobs for the llama.cpp runner and, since v0.40.0, safetensors-derived
per-tensor layers for the MLX runner (the default on Apple Silicon), packaged with
Modelfile-style recipes. Both formats are data-only. The same GGUF artifact is consumable by
other runners such as llama.cpp and LM Studio, so format lock-in at the weights layer is low.
The MLX layout is Ollama's own packaging.

<!-- item: integration -->
## Downstream integration

Integration is through a local CLI and API, OpenAI-compatible and Anthropic-compatible
endpoints, `ollama launch` for coding tools, Modelfile recipes and an Ollama-specific registry
layout. GGUF is portable at the weights layer. The recipe format, the manifest-list layout and
the registry layout are Ollama-specific conveniences, not an open cross-tool standard.
