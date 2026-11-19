# Implement - GLM (Zhipu AI / Z.ai)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

GLM checkpoints are standard safetensors on the verified `zai-org` org. The MoE flagships
serve best on vLLM or SGLang, and the dense 0414 sizes also run under llama.cpp and Ollama.
Always pin an exact revision.

```python
# Hugging Face transformers (dense sizes).
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "zai-org/GLM-4-32B-0414"   # Pick the exact variant to deploy.
rev = "<pinned-commit-sha>"            # Pin the revision; do not float on main.
tok = AutoTokenizer.from_pretrained(model_id, revision=rev)
model = AutoModelForCausalLM.from_pretrained(model_id, revision=rev)
```

```bash
# vLLM (OpenAI-compatible server) - MoE flagships.
vllm serve zai-org/GLM-4.6 --revision <sha>

# SGLang - also first-class for the MoE.
python -m sglang.launch_server --model-path zai-org/GLM-4.6 --revision <sha>

# Ollama (community GGUF) - dense sizes.
ollama run glm4
```

The models are also available on Zhipu's ModelScope. Verify per-file checksums after download
and confirm the LICENSE on the exact checkpoint.

<!-- item: hardware -->
## Hardware & VRAM requirements

GLM-4-9B-0414 (dense) runs on a single modern GPU. GLM-4-32B-0414 (dense) needs a single
high-memory GPU or dual GPU, and more at long context. GLM-4.5-Air (106B/12B MoE) needs a
multi-GPU node, or aggressive quantization on a single large card. GLM-4.5 and GLM-4.6
(355B/32B MoE) need serious multi-GPU infrastructure, or heavy quantization, to serve at
usable latency.

MoE total-parameter memory dominates even though only 32B are active per token, so size VRAM
to the total and budget extra headroom for the KV cache at the 200K context of GLM-4.6.

<!-- item: serving -->
## Serving stacks

| Stack | Use it for |
|---|---|
| vLLM | High-throughput MoE serving and OpenAI-compatible API |
| SGLang | First-class MoE serving (agentic/structured workloads) |
| llama.cpp | CPU, edge and GGUF for the dense 0414 sizes |
| Ollama | Local single-command runs (dense sizes) |
| transformers | Prototyping and fine-tuning |

vLLM and SGLang are the primary paths for the 355B and 106B MoE. Day-0 llama.cpp and edge
support is strongest for the dense sizes and lags for the big MoE. This breadth underpins
Operational Readiness (4), which stops short of 5 mainly on the infrastructure weight of the
largest MoE.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

The model-specific gate rows from the
[safe-deployment playbook](../../methodology/safe-deployment-playbook.md) are below.

- Supply chain: pin the exact `zai-org` revision and verify checksums (match across Hugging
  Face and ModelScope). Confirm the per-checkpoint LICENSE and do not assume MIT everywhere.
- Model layer: deploy the instruct checkpoints and set conservative decoding defaults.
- Input/output layers: add input/output guardrails and your own guard classifier, because GLM
  ships no companion guard model. Add prompt-injection defences for agentic and coding paths
  and treat retrieved and tool content as untrusted.
- Behaviour: test for China-aligned alignment and hosted-API-style moderation effects relevant
  to the use case.
- Compliance: for the 355B MoE, resolve or avoid the EU systemic-risk / Article 55 question
  before EU high-stakes use, and record the AI-BOM posture.

Deployment Ceiling: T3 (bounded autonomous), conditional. With your own input/output
guardrails, a guard model and prompt-injection defences, GLM's coding and agentic strength
supports bounded-autonomous use. T3 additionally needs a deterministic action-policy engine
and per-action human approval for irreversible operations. The release provides none of this
external tooling.

<!-- item: quantization -->
## Available quantizations

Community GGUF (llama.cpp, Ollama), AWQ/GPTQ and EXL quantizations circulate (bartowski,
turboderp and others) and are best covered for the dense 0414 sizes. Coverage is partial
because these are community efforts, with no broad first-class official quantization
programme from Zhipu. Verify the source and check quality before relying on a third-party
quant in production, especially for the MoE flagships.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The MIT-licensed safetensors checkpoints support standard SFT and LoRA via `transformers` and
TRL, and released inference code eases integration. The training data and training pipeline
are not released, so continued pre-training or reproduction from scratch is not possible. The
released weights can be adapted but not rebuilt. Placing a derivative on the EU market has EU
AI Act provider implications (see Assess).

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve GLM behind vLLM's or SGLang's OpenAI-compatible `/v1` server for a drop-in integration
with existing OpenAI-client code.

```bash
vllm serve zai-org/GLM-4.6 --revision <sha> --port 8000
# Then point any OpenAI SDK at http://localhost:8000/v1.
```

No model-specific client is required. The chat-completions surface behaves like any other
OpenAI-compatible endpoint. Account for GLM's chat template and its agentic/thinking output
format when parsing responses.
