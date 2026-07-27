# Implement - Ai2 OLMo (OLMo 2 / OLMo 3)

_How do we deploy and run it? Install, hardware, serving, quantization, fine-tuning, and
the safe-deployment controls & Deployment Ceiling (**T2, conditional**)._

<!-- item: install -->
## Install & run

OLMo checkpoints are standard safetensors on the verified `allenai` org - the usual paths
all work. Always pin an exact revision.

```python
# Hugging Face transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "allenai/OLMo-2-1124-13B-Instruct"   # pick the exact variant you assessed
rev = "<pinned-commit-sha>"                       # pin the revision, don't float on main
tok = AutoTokenizer.from_pretrained(model_id, revision=rev)
model = AutoModelForCausalLM.from_pretrained(model_id, revision=rev)
```

```bash
# Ollama (community GGUF)
ollama run olmo2

# vLLM (OpenAI-compatible server)
vllm serve allenai/OLMo-2-1124-13B-Instruct --revision <sha>

# llama.cpp (GGUF)
./llama-cli -m olmo2-instruct.Q4_K_M.gguf -p "Hello"
```

Prefer safetensors; verify per-file checksums after download.

<!-- item: hardware -->
## Hardware & VRAM requirements

The **7B-13B** variants run comfortably on a single modern GPU (a 24 GB card handles the 7B
at full precision and the 13B with modest quantization). The **32B** (OLMo 3) needs
multi-GPU or heavy quantization for latency-sensitive serving; on a single 24 GB GPU it is
only practical at 4-bit. Size to the largest checkpoint you intend to serve, and budget
extra headroom for the KV cache at longer context lengths.

<!-- item: serving -->
## Serving stacks

Because the checkpoints are plain safetensors with a standard architecture, all mainstream
runtimes load them with no custom code:

| Stack | Use it for |
|---|---|
| **vLLM** | High-throughput serving + OpenAI-compatible API |
| **TGI** | Hugging Face-native production serving |
| **llama.cpp** | CPU / edge / GGUF quantized inference |
| **Ollama** | Local single-command runs |
| **transformers** | Prototyping and fine-tuning |

This breadth is why Operational Readiness scores 4; it stops short of 5 only on the breadth
of *official* day-0 quantizations versus the largest ecosystems.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Applying the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md), the
model-specific gate rows are:

- **Supply chain:** pin the exact `allenai` revision hash and verify checksums; prefer
  safetensors (already the default - no pickle load).
- **Model layer:** deploy the **Instruct** variant, never the base checkpoint; set
  conservative decoding defaults.
- **Input/output layers:** add input/output guardrails and your **own** guard classifier for
  any customer-facing path - OLMo ships no companion guard model; add prompt-injection
  defences and treat retrieved/tool content as untrusted.
- **Compliance:** archive the (readily available) training-content summary and copyright
  posture in your AI-BOM.

**Deployment Ceiling: T2 (customer-facing, human-reviewed) - conditional.** With the Instruct
variant plus input/output guardrails and prompt-injection defences, OLMo reaches
customer-facing, human-reviewed use. Its standout property is **auditability**: for regulated
or high-assurance contexts where you must inspect what went into the model, OLMo is uniquely
suitable even where raw capability trails. T3+ (bounded autonomous) additionally needs a
deterministic action-policy engine, per-action human approval for irreversible operations,
and external guard tooling beyond what the release itself provides.

<!-- item: quantization -->
## Available quantizations

Community **GGUF** (llama.cpp/Ollama) and **AWQ/GPTQ** quantizations circulate and are
acknowledged, and the safetensors base makes on-the-fly bitsandbytes 8-/4-bit
straightforward. Coverage is marked *partial* because these are largely community efforts
rather than a broad first-class official quantization program from Ai2 - verify the source
and re-check quality before relying on a third-party quant in production.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

OLMo is unusually strong here because the **entire training stack is open**: `allenai/OLMo`
and **OLMo-core** provide the runnable pre-training/adaptation code, and the released data
and intermediate checkpoints let you reproduce or extend training rather than only
fine-tune the final weights. For most adopters, standard **SFT/LoRA** via `transformers` /
TRL on the safetensors checkpoints is the practical path; teams needing deeper control can
use OLMo-core directly. Note the EU AI Act provider implications of placing a derivative on
the market (see Assess).

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve OLMo behind **vLLM's OpenAI-compatible `/v1` server** (or TGI/Ollama endpoints) for a
drop-in integration with existing OpenAI-client code:

```bash
vllm serve allenai/OLMo-2-1124-13B-Instruct --revision <sha> --port 8000
# then point any OpenAI SDK at http://localhost:8000/v1
```

No model-specific client is required - the chat-completions surface behaves like any other
OpenAI-compatible endpoint, so routing, retries, and gateways carry over unchanged.
