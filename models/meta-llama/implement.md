# Implement - Meta Llama (Llama 3.x / Llama 4)

_How do we deploy and run it? Install, hardware, serving, quantization, fine-tuning, and
the safe-deployment controls & Deployment Ceiling._

<!-- item: install -->
## Install & run

Access is **gated**: accept the license on the model page, then authenticate with a
Hugging Face token. Pin the revision and prefer safetensors.

```bash
# Hugging Face (gated) - accept the license first, then:
huggingface-cli login   # paste your HF token
python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; \
  m='meta-llama/Llama-3.1-8B-Instruct'; \
  AutoTokenizer.from_pretrained(m); \
  AutoModelForCausalLM.from_pretrained(m, revision='main')"

# Ollama (community-packaged, quantized):
ollama run llama3.1

# vLLM (OpenAI-compatible server):
vllm serve meta-llama/Llama-3.1-8B-Instruct

# llama.cpp (GGUF):
llama-cli -hf bartowski/Meta-Llama-3.1-8B-Instruct-GGUF -p "Hello"
```

Hosted alternatives require no local weights: Llama is served on **AWS Bedrock, Azure AI,
Google Vertex AI**, and third-party APIs (Together, Groq). Those are endpoints rather than
the weight source - pin the canonical HF revision when self-hosting.

<!-- item: hardware -->
## Hardware & VRAM requirements

- **8B** - runs on a single modern GPU (roughly 16 GB in bf16; far less quantized), and is
  usable on high-end laptops via GGUF.
- **70B (3.1 / 3.3)** - needs multi-GPU in full precision, or a single large GPU with 4-bit
  quantization.
- **405B and the large Llama 4 MoE (Maverick, Behemoth)** - require a serving cluster;
  Llama 4 Scout's mixture-of-experts keeps *active* parameters (~17B) small, but total
  weights and the very long context still demand substantial memory.

<!-- item: serving -->
## Serving stacks

Llama has **first-class, day-0** support across the entire serving ecosystem: **vLLM** and
**TGI** for high-throughput GPU serving, **llama.cpp** for CPU/edge and GGUF, **Ollama**
for local developer workflows, **MLX** for Apple Silicon, and plain **transformers** for
scripting. This breadth is the single strongest operational signal for the family - there
is effectively nothing to unlock.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Applying the safe-deployment playbook, the model-specific gate rows are: pin the revision
from `meta-llama` and verify the checksum (supply chain); confirm the license permits your
use and that you are **not** using multimodal variants in the EU (legal); deploy the
**Instruct** variant with **Llama Guard** on both input and output plus prompt-injection
defences (safety); and add a deterministic **action-policy engine with a kill switch**
before granting any autonomy (action layer).

**Deployment Ceiling: T3 (bounded autonomous), conditional.** T2 is reachable today with
the Instruct variant, Llama Guard input/output classification, and prompt-injection
defences - all available. T3 additionally requires a deterministic action-policy engine,
per-action human approval for irreversible operations, a kill switch, and scheduled
red-teaming. **T4 (regulated high-stakes autonomous) is not recommended**: the community
license, the EU multimodal restriction, and the unmet Article 55 documentation burden do
not comfortably support high-stakes regulated use.

<!-- item: quantization -->
## Available quantizations

Meta ships official low-bit releases for parts of the family, and the community adds an
enormous quantization ecosystem: **GGUF** (bartowski, unsloth) for llama.cpp/Ollama, plus
**AWQ** and **GPTQ** builds for GPU serving. Quantized checkpoints are third-party
artifacts - verify the uploader and prefer well-known maintainers, and re-test quality at
the chosen bit-width.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Fine-tuning is well supported. Meta's own **torchtune** library targets Llama directly,
and the model works cleanly with the common **LoRA/QLoRA** stacks - PEFT + Transformers,
Axolotl, and Unsloth. Parameter-efficient adaptation (QLoRA) makes 8B and even 70B
tunable on modest hardware. Note the license: a derivative placed on the EU market under
your own name can make you a provider with your own documentation obligations.

<!-- item: integration -->
## API / OpenAI-compatible usage

The fastest integration path is an **OpenAI-compatible** endpoint: both **vLLM** and
**TGI** expose `/v1/chat/completions`, so existing OpenAI-SDK code points at a self-hosted
Llama with only a base-URL change. Managed OpenAI-compatible APIs (Together, Groq, the
cloud providers) and Meta's own Llama API offer the same shape without self-hosting.
