# Implement - Kimi K2 (Moonshot AI)

_How do we deploy and run it? Install, hardware, serving, quantization, fine-tuning, and
the safe-deployment controls & Deployment Ceiling (**T2, conditional**)._

<!-- item: install -->
## Install & run

Kimi K2 weights are **block-FP8 safetensors** on the verified `moonshotai` org. This is not a
single-command local model - plan for a multi-GPU/multi-node serving stack. Always pin an exact
revision.

```bash
# vLLM (OpenAI/Anthropic-compatible server), tensor/pipeline parallel across a node/cluster
vllm serve moonshotai/Kimi-K2-Instruct --revision <sha> \
  --tensor-parallel-size 8 --trust-remote-code

# SGLang (alternative high-throughput engine)
python -m sglang.launch_server --model-path moonshotai/Kimi-K2-Instruct --revision <sha>
```

KTransformers (heavy CPU-offload) and TensorRT-LLM are also supported for teams optimising for
constrained GPU memory or maximum throughput respectively. Verify per-file checksums after
download.

<!-- item: hardware -->
## Hardware & VRAM requirements

Kimi K2 is a **1T-parameter MoE (32B active)**. Even in **block-FP8** the weights are on the
order of **~1 TB**, so serving requires a **multi-GPU / multi-node cluster** (e.g. a full
8×80-141 GB node or more) or heavy **CPU-offload via KTransformers**. There are **no small
variants** - single-GPU or laptop deployment is not possible. Budget substantial additional
headroom for the KV cache at the full 128K context.

<!-- item: serving -->
## Serving stacks

The publisher documents first-class support across the high-end serving engines:

| Stack | Use it for |
|---|---|
| **vLLM** | High-throughput serving + OpenAI/Anthropic-compatible API |
| **SGLang** | High-throughput serving, structured generation |
| **KTransformers** | GPU-constrained deployment via CPU/GPU offload |
| **TensorRT-LLM** | Maximum-throughput NVIDIA-optimised serving |

There is no llama.cpp/Ollama single-box path at full precision; the model's scale is the gating
factor, which is why Operational Readiness scores 3.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Applying the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md), the
model-specific gate rows are:

- **Supply chain:** pin the exact `moonshotai` revision hash and verify block-FP8 checksums;
  weights are safetensors (no pickle load).
- **Model layer:** deploy the **Instruct** variant, never the Base checkpoint; set conservative
  decoding defaults.
- **Input/output layers:** add input/output guardrails and your **own** guard classifier for any
  customer-facing path - Kimi K2 ships no companion guard model; add prompt-injection defences
  and treat retrieved/tool content as untrusted (important given the native tool-use focus).
- **Behaviour:** account for **China-aligned topic censorship**; do not assume neutral coverage
  on politically sensitive prompts.
- **Compliance:** you must self-assemble the copyright policy and training-content material -
  they are not available upstream.

**Deployment Ceiling: T2 (customer-facing, human-reviewed) - conditional.** With the Instruct
variant plus input/output guardrails, a guard model, and prompt-injection defences, Kimi K2
reaches customer-facing, human-reviewed use. T3+ (bounded autonomous) - which its agentic
positioning invites - additionally needs a deterministic action-policy engine, per-action human
approval for irreversible operations, and external guard tooling beyond what the release itself
provides.

<!-- item: quantization -->
## Available quantizations

Kimi K2 is **natively distributed in block-FP8**, which is already the practical serving format.
Community lower-bit / GGUF quants circulate to make the trillion-parameter model tractable on
smaller clusters, but these are **community artifacts** rather than a broad official quantization
program - verify the source and re-check quality before relying on a third-party quant in
production. Coverage is *partial* for that reason.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

A released **Kimi-K2-Base** checkpoint plus the permissive modified MIT license make adaptation
possible, and standard **SFT/LoRA** is the practical path for most teams. Two honest limits keep
this *partial*: the **training data and code are not released**, so continued pre-training or
from-scratch reproduction is not possible; and **full fine-tuning of a 1T-parameter MoE is
resource-intensive**, so most adopters will be limited to parameter-efficient methods. Note the
EU AI Act provider implications of placing a derivative on the market (see Assess).

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve Kimi K2 behind **vLLM's (or SGLang's) OpenAI/Anthropic-compatible endpoint** for a drop-in
integration with existing client code:

```bash
vllm serve moonshotai/Kimi-K2-Instruct --revision <sha> --tensor-parallel-size 8 --port 8000
# then point any OpenAI-compatible SDK at http://localhost:8000/v1
```

Kimi K2's **native tool-calling** maps directly onto the function-calling API, so agentic clients
and tool routers carry over unchanged - no model-specific client is required.
