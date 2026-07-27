# Use - llama.cpp / GGUF

_What is available and in what formats? The GGUF container format and downstream integration
live here; catalogue scope is a documented gap below._

<!-- item: formats-supported -->
## Formats supported

The one format here is **GGUF**: a **single-file container** bundling weights, tokenizer,
metadata and the chat template. It is the **de facto local-inference standard**. GGUFs are
produced from upstream weights with `convert_hf_to_gguf.py` and reduced in size with
`llama-quantize` across a range of quantization levels (Q4_K_M, Q5_K_M, Q8_0, and others), so
the same model is available at several size/quality trade-offs.

<!-- item: integration -->
## Downstream integration

GGUF's value is its **portability**: the format is consumed across the local-inference ecosystem -
**Ollama, LM Studio, text-generation-webui** and many others - and the conversion tooling is
open. A GGUF you produce or download is not tied to llama.cpp alone; it plugs into whichever of
those downstream runners you prefer, which is the main reason ecosystem lock-in is minimal.
