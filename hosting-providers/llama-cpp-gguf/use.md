# Use - llama.cpp / GGUF

_Available models, supported formats and downstream integration._

<!-- item: formats-supported -->
## Formats supported

The one format here is GGUF, a single-file container bundling weights, tokenizer, metadata and the chat template. It is the de facto local-inference standard (format version 3). llama.cpp states support for more than 150 architecture variants, and conversion code is registered for the open-weight families tracked in this index, such as Llama 4, gpt-oss, GLM, DeepSeek, Kimi K3, Qwen3.x, Nemotron, OLMo 3 and Mistral.

GGUFs are produced from upstream weights with `convert_hf_to_gguf.py` and reduced in size with `llama-quantize` across a range of quantization levels (Q4_K_M, Q5_K_M, Q8_0, and others), so the same model is available at several size and quality trade-offs.

<!-- item: integration -->
## Downstream integration

GGUF is portable: Ollama, LM Studio, text-generation-webui and many other tools consume it, and the conversion tooling is open. A GGUF is not tied to llama.cpp alone and plugs into any of those downstream runners, which is the main reason ecosystem lock-in is minimal.
