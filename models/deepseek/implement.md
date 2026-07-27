# Implement - DeepSeek (V3 / R1)

_How do we deploy and run it? Install, hardware, serving, quantization, fine-tuning, and
the safe-deployment controls & Deployment Ceiling._

<!-- item: install -->
## Install & run

Pull from the canonical `deepseek-ai` org on Hugging Face and pin the revision; the
distribution is safetensors, so the load itself is safe. The realistic entry point for
most adopters is a distill or a quantized build - the full V3/R1 weights need a cluster.

```bash
# Full weights via Transformers (needs a multi-GPU box)
from transformers import AutoModelForCausalLM, AutoTokenizer
tok = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-R1", revision="<pin-a-commit>")
model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/DeepSeek-R1", revision="<pin-a-commit>", torch_dtype="auto", device_map="auto")

# A distill on a modest GPU
ollama run deepseek-r1:8b            # community distill via Ollama
```

vLLM and llama.cpp are the other common paths; use a GGUF distill under llama.cpp/Ollama
for CPU/small-GPU hosts. Verify the checksum after download.

<!-- item: hardware -->
## Hardware requirements

The full V3/R1 is a ~671B-total / ~37B-active MoE: serving the full weights requires a
multi-GPU cluster (high aggregate VRAM even though only ~37B params are active per token,
because all experts must be resident). This is the single biggest practical barrier. The
**R1-Distill-Qwen/Llama** checkpoints are dense models in the usual size range (e.g. 7B,
8B, 14B, 32B, 70B) and run on modest single GPUs - or, quantized, on a laptop. Pick the
distill that fits your hardware; they are separate artifacts (see provenance).

<!-- item: serving -->
## Serving stacks

DeepSeek has first-class ecosystem support: **vLLM** and **SGLang** for GPU serving at
scale, **llama.cpp** and **Ollama** for CPU/small-GPU and local use, and plain
**Transformers** for scripting. R1's reasoning tokens are emitted inline (`<think>`), so
whichever stack you choose, configure downstream parsing/stripping of the reasoning span
before returning text to users.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Applying the playbook to DeepSeek:

- **Supply chain:** pull the canonical safetensors and pin the revision; the data-only
  format makes the load itself safe (no unsandboxed pickle). Prefer the canonical org over
  random distill uploaders.
- **Legal:** confirm MIT applies to your exact checkpoint. Recognise the systemic-risk
  Article 53/55 gap - as an EU deployer you cannot close it from upstream documentation.
- **Safety:** because **no guard model ships**, stand up your own input/output classifiers,
  prompt-injection defences, and a content/neutrality review step given the censorship
  behaviour, before any customer contact.
- **Isolation:** **self-host** - do not route sensitive data through DeepSeek's hosted API.

**Deployment Ceiling: T2 (customer-facing, human-reviewed), conditional.** The self-hosted
open weights are supply-chain-safe (safetensors), and T2 is reachable with strong
input/output guards, prompt-injection defences, and a neutrality/content review layer.
**T3+ requires heavy guardrails** given the lighter safety tuning, and autonomy should be
granted cautiously. **T4 / EU high-stakes is not recommended**, driven by two hard
constraints: the Article 53/55 compliance gap for a systemic-risk model, and the
censorship behaviour, which is disqualifying where topic-neutral factuality is required.

<!-- item: quantization -->
## Available quantizations

An extensive community ecosystem of **GGUF** (llama.cpp/Ollama) and **AWQ/GPTQ** builds
exists, alongside the R1-Distill family that is itself the most common way to shrink the
footprint. Treat every quant/distill as a **separate-trust artifact** - its trust equals
the uploader rather than DeepSeek. Prefer builds from the canonical org or a host you trust, and
verify checksums.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The MIT license explicitly permits distillation and derivative training - this is why the
R1-Distill family exists at all. Standard supervised fine-tuning and LoRA/QLoRA adaptation
apply to the open weights (most practically to the smaller distills). If you distill or
fine-tune, you own the resulting artifact's provenance and, as a downstream provider, may
inherit your own EU AI Act obligations.

<!-- item: integration -->
## API / OpenAI-compatible integration

For application integration, self-host behind an **OpenAI-compatible endpoint** via vLLM or
SGLang (both expose `/v1/chat/completions`-style APIs), so existing OpenAI-SDK code points
at your own inference server. This keeps prompts on your infrastructure and is the
recommended alternative to calling DeepSeek's hosted API when sensitive data is involved.
