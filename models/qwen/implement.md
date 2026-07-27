# Implement - Qwen (Qwen3 family)

_How do we deploy it? Install, hardware, serving, safe-deployment controls, quantization,
fine-tuning and integration live here._

<!-- item: install -->
## Install & run

Qwen3 checkpoints load with standard tooling: **`from_pretrained`** on the safetensors
weights, **`ollama pull`** for quantized local use, **vLLM** for serving, or **llama.cpp**
on a GGUF quant. They are also available on **Alibaba's ModelScope**. Whichever hub you
pull from, **pin the exact revision** and **verify checksums** - ideally cross-checking that
they match between Hugging Face and ModelScope.

<!-- item: hardware -->
## Hardware & VRAM requirements

The size ladder is wide: **dense 0.5B-32B** run from a laptop to a single modern GPU, while
the **235B MoE** and **480B-Coder** need **multi-GPU / serious infrastructure** or
aggressive quantization for latency-sensitive serving.

<!-- item: serving -->
## Serving stacks

Qwen has **first-class, broad serving support** - vLLM, llama.cpp, Ollama, TGI, MLX and
transformers - so no custom runtime is required and day-0 availability across the stack is
reliable.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

The **Deployment Ceiling is T3 (conditional)**. To deploy responsibly:

- Supply **your own input/output guardrails** and a **guard/classifier model** - do not rely
  on built-in alignment.
- Add **prompt-injection defences** for agentic and coding use.
- **Verify checksums** across HF/ModelScope and **pin the revision**.
- For the **systemic-risk large variants**, close the **EU Article 55** gap yourself or
  avoid EU high-stakes use.

<!-- item: quantization -->
## Available quantizations

There are **abundant community GGUF/AWQ quants** (via Ollama and others) across the size
range. These are community artifacts rather than a single official quantization program, so
validate the specific quant you adopt.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The Apache-2.0 safetensors checkpoints support standard **SFT / LoRA** via
transformers/TRL, and the wide size ladder plus the strong coder base make Qwen a good
target for domain specialisation and distillation. Because **training data and code are not
released**, continued pre-training from scratch is not possible - you adapt the released
weights.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve Qwen behind **vLLM's OpenAI-compatible `/v1` server** (or TGI/Ollama endpoints) for
drop-in client integration. Account for **Qwen3's thinking / non-thinking output modes** in
your parsing - the thinking-mode format is the main behaviour to handle when treating Qwen
as a drop-in for another model.
