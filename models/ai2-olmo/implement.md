# Implement - Ai2 OLMo (OLMo 2 / OLMo 3)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

OLMo checkpoints are standard safetensors on the verified `allenai` org, so the usual paths all work. Always pin an exact revision.

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

The 7B-13B variants run comfortably on a single modern GPU (a 24 GB card handles the 7B at full precision and the 13B with modest quantisation). The 32B (OLMo 3) needs multi-GPU or heavy quantisation for latency-sensitive serving, and on a single 24 GB GPU it is only practical at 4-bit. Size to the largest checkpoint to be served, and budget extra headroom for the KV cache at longer context lengths.

<!-- item: serving -->
## Serving stacks

All mainstream runtimes load the checkpoints with no custom code, because they are plain safetensors with a standard architecture:

| Stack | Used for |
|---|---|
| vLLM | High-throughput serving + OpenAI-compatible API |
| TGI | Hugging Face-native production serving |
| llama.cpp | CPU / edge / GGUF quantized inference |
| Ollama | Local single-command runs |
| transformers | Prototyping and fine-tuning |

This breadth is why Operational Readiness scores 4. It stops short of 5 only on the breadth of official day-0 quantisations compared with the largest ecosystems.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

The model-specific gate rows follow the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md). Pin the exact `allenai` revision hash and verify checksums, and prefer safetensors (already the default, with no pickle load). Deploy the Instruct variant and never the base checkpoint, with conservative decoding defaults.

Add input/output guardrails and your own guard classifier for any customer-facing path, because OLMo ships no companion guard model. Add prompt-injection defences and treat retrieved and tool content as untrusted. Archive the training-content summary and copyright posture, both readily available, in the AI-BOM.

Deployment Ceiling: T2 (customer-facing, human-reviewed), conditional. With the Instruct variant plus input/output guardrails and prompt-injection defences, OLMo reaches customer-facing, human-reviewed use. Its auditability suits regulated or high-assurance contexts where the contents of the model must be inspected, even where raw capability trails. T3+ (bounded autonomous) additionally needs a deterministic action-policy engine, per-action human approval for irreversible operations, and external guard tooling beyond what the release provides.

<!-- item: quantization -->
## Available quantizations

Community GGUF (llama.cpp/Ollama) and AWQ/GPTQ quantisations circulate and are acknowledged, and the safetensors base makes on-the-fly bitsandbytes 8-/4-bit easy. Coverage is marked partial because these are largely community efforts and Ai2 runs no broad first-class official quantisation programme. Verify the source and test quality before relying on a third-party quant in production.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The entire training stack is open: `allenai/OLMo` and OLMo-core provide runnable pre-training and adaptation code, and the released data and intermediate checkpoints allow training to be reproduced or extended as well as the final weights fine-tuned. For most adopters, standard SFT/LoRA via `transformers` / TRL on the safetensors checkpoints is the practical path, and teams needing deeper control can use OLMo-core directly. Placing a derivative on the EU market has AI Act provider implications (see Assess).

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve OLMo behind vLLM's OpenAI-compatible `/v1` server (or TGI/Ollama endpoints) for drop-in integration with existing OpenAI-client code:

```bash
vllm serve allenai/OLMo-2-1124-13B-Instruct --revision <sha> --port 8000
# then point any OpenAI SDK at http://localhost:8000/v1
```

No model-specific client is required. The chat-completions surface behaves like any other OpenAI-compatible endpoint, so routing, retries and gateways carry over unchanged.
