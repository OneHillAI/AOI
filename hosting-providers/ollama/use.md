# Use - Ollama

_What is available and in what formats? Catalogue scope, supported formats and downstream integration live here._

<!-- item: catalog-scope -->
## Catalogue scope & publishers

Ollama offers a **curated official library** plus **user-supplied and community GGUFs** pulled
by registry namespace. Because there is **no per-publisher identity verification**, community
models rest on **user-supplied provenance** - the curation of the official library is the
main trust signal, and it is not a substitute for verified publisher identity or scanning.

<!-- item: formats-supported -->
## Formats supported

Ollama distributes **GGUF blobs** - a **data-only, portable** format - packaged via
**Modelfile** recipes. The same GGUF artifact is consumable by **other runners** such as
llama.cpp and LM Studio, so there is low format lock-in at the weights layer.

<!-- item: integration -->
## Downstream integration

Integration is via a **local CLI/API** plus **Modelfile** recipes and an **Ollama-specific
local registry layout**. You are portable at the GGUF layer, but the recipe format and the
local registry layout are **Ollama-specific conveniences** rather than an open cross-tool
standard, so those pieces do not travel to other runners unchanged.
