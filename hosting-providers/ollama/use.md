# Use - Ollama

_What is available and in what formats? Catalogue scope, supported formats and downstream integration live here._

<!-- item: catalog-scope -->
## Catalogue scope & publishers

Ollama offers a **curated official library**, **user-pushed community models** by registry
namespace, and **cloud-enabled `:cloud` models** (about two dozen listed with per-token prices on the
pricing page, and a published retirement list; retired cloud models do not affect local
ones). Because there is **no per-publisher identity verification**, community models rest on
**user-supplied provenance** - the curation of the official library is the main trust signal,
and it is not a substitute for verified publisher identity or scanning.

<!-- item: formats-supported -->
## Formats supported

Ollama distributes **GGUF blobs** for the llama.cpp runner and, since **v0.40.0**,
**safetensors-derived per-tensor layers** for the MLX runner (the default on Apple Silicon),
packaged with Modelfile-style recipes. Both formats are **data-only**. The same GGUF artifact
is consumable by **other runners** such as llama.cpp and LM Studio, so there is low format
lock-in at the weights layer; the MLX layout is Ollama's own packaging.

<!-- item: integration -->
## Downstream integration

Integration is via a **local CLI and API**, **OpenAI-compatible and Anthropic-compatible
endpoints**, **`ollama launch`** for coding tools, **Modelfile** recipes and an
**Ollama-specific registry layout**. You are portable at the GGUF layer, but the recipe format,
the manifest-list layout and the registry layout are **Ollama-specific conveniences** rather
than an open cross-tool standard.
