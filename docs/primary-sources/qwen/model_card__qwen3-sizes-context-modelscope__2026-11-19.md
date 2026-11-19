# Qwen - Qwen3 model cards: sizes, context, serving, ModelScope (re-read 2026-11-19)

- **doc_type:** model_card
- **source_url:** https://huggingface.co/Qwen/Qwen3-235B-A22B/raw/main/README.md ; https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct/raw/main/README.md ; https://huggingface.co/api/models/Qwen/<id> ; https://www.modelscope.cn/api/v1/models/Qwen/Qwen3-32B ; https://ollama.com/library/qwen3
- **retrieval_date:** 2026-11-19
- **exists:** yes
- **retrieved:** true

## Facts read

- Qwen3 dense sizes on Hugging Face: 0.6B, 1.7B, 4B, 8B, 14B, 32B. The smallest is 0.6B (751,632,384 safetensors parameters
  including embeddings). There is no 0.5B Qwen3 checkpoint; the 2026-07-25 entry text "0.5B" was wrong and is corrected.
- MoE: Qwen3-30B-A3B (30.5B total) and Qwen3-235B-A22B (235.1B total, 22B activated). 2507 updates exist for 4B, 30B-A3B and 235B-A22B.
- Coder: Qwen3-Coder-30B-A3B-Instruct (30.5B) and Qwen3-Coder-480B-A35B-Instruct (480.2B total, 35B activated).
  Later Qwen3-Coder-Next (2026-01-30, 79.7B, Apache-2.0 tag) exists as a separate release.
- Context, Qwen3-235B-A22B card: "Context Length: 32,768 natively and 131,072 tokens with YaRN."
  Qwen3-Coder-480B-A35B-Instruct card: "Context Length: 262,144 natively", 256K native, extendable to 1M with YaRN.
- Thinking mode: card "enable_thinking" switch and /think, /no_think soft switches (as stored).
- Serving named by the card: SGLang (>=0.4.6.post1), vLLM (>=0.8.5); "Ollama, LMStudio, MLX-LM, llama.cpp, and KTransformers have also supported Qwen3."
  TGI is not named on the Qwen3 card.
- Ollama library page lists qwen3 sizes 0.6b, 1.7b, 4b, 8b, 14b, 30b, 32b, 235b, "44M Downloads", "Updated 1 year ago".
- Technical report abstract (arXiv 2505.09388): multilingual support "from 29 to 119 languages and dialects".
- ModelScope: Qwen/Qwen3-32B, Qwen3-235B-A22B and Qwen3-Coder-480B-A35B-Instruct exist under the Qwen namespace
  (API Code 200, License apache-2.0). The ModelScope organisation web page itself is a JavaScript shell with no readable content;
  the record was read through the public model API.
- All checked Qwen3 repos: `gated: False`, safetensors, last modified 2025-07 to 2025-08.
