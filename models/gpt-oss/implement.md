# Implement - OpenAI gpt-oss (gpt-oss-120b / gpt-oss-20b)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

gpt-oss checkpoints are safetensors on the verified `openai` org, shipped natively in MXFP4.
The usual paths all work. Always pin an exact revision.

```python
# Hugging Face transformers.
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "openai/gpt-oss-20b"        # Or openai/gpt-oss-120b.
rev = "<pinned-commit-sha>"            # Pin the revision; do not float on main.
tok = AutoTokenizer.from_pretrained(model_id, revision=rev)
model = AutoModelForCausalLM.from_pretrained(model_id, revision=rev, torch_dtype="auto")
```

```bash
# Ollama (single command).
ollama run gpt-oss:20b

# vLLM (OpenAI-compatible server).
vllm serve openai/gpt-oss-120b --revision <sha>

# llama.cpp / LM Studio (MXFP4 or GGUF).
./llama-cli -m gpt-oss-20b-mxfp4.gguf -p "Hello"
```

Prefer the safetensors from the `openai` org and verify per-file checksums after download.

<!-- item: hardware -->
## Hardware & VRAM requirements

Only a small fraction of parameters are active per token, so gpt-oss is cheaper to serve than
its total-parameter counts suggest. gpt-oss-120b (~117B total, 5.1B active) fits on a single
80GB GPU (H100/MI300-class) in native MXFP4. gpt-oss-20b (~21B total, 3.6B active) runs in
about 16GB, which is high-end consumer or edge hardware.

Budget extra headroom for the KV cache at long context lengths (both models support 128K).

<!-- item: serving -->
## Serving stacks

The checkpoints have day-0, first-class runtime support with native MXFP4 kernels, which is
why Operational Readiness scores 5.

| Stack | Use it for |
|---|---|
| vLLM | High-throughput serving and OpenAI-compatible API |
| llama.cpp | CPU, edge, GGUF and MXFP4 inference |
| Ollama | Local single-command runs |
| transformers | Prototyping and fine-tuning |
| MLX | Apple-silicon inference |

Hosted endpoints are also available on major providers, so serving can move between
self-hosted and managed without changing the client contract.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

The model-specific gate rows from the
[safe-deployment playbook](../../methodology/safe-deployment-playbook.md) are below.

- Supply chain: pin the exact `openai` revision hash and verify checksums. Prefer the
  canonical safetensors (no pickle load).
- Prompt layer: render prompts with the harmony response format via `openai/harmony`,
  because the models are trained only for it, and never surface raw chain-of-thought to end
  users.
- Model layer: the models are safety-tuned, but the tuning can be fine-tuned away on open
  weights. Set conservative decoding defaults.
- Input/output layers: add input/output guardrails and your own guard classifier for any
  customer-facing path. The base release ships no guard model, and OpenAI's separate
  `gpt-oss-safeguard` classifier can fill that role. Add prompt-injection defences and treat
  retrieved and tool content as untrusted.
- Compliance: archive OpenAI's training-content summary and copyright posture in the AI-BOM.
  The deployment depends on OpenAI for the training-content summary because the data is not
  published.

Deployment Ceiling: T2 (customer-facing, human-reviewed), conditional. With harmony-correct
prompts, input/output guardrails, a guard classifier and no raw-CoT exposure, gpt-oss reaches
customer-facing, human-reviewed use. Its strong native tool use makes it a capable agentic
backbone. T3+ (bounded autonomous) additionally needs a deterministic action-policy engine,
per-action human approval for irreversible operations, and external guard tooling beyond what
the release provides. It is held at T2 because the base release ships no companion guard
model.

<!-- item: quantization -->
## Available quantizations

gpt-oss is natively quantized in MXFP4. The mixture-of-experts weights are released at 4-bit,
which lets the 120b fit on one 80GB GPU and the 20b in 16GB. This is a first-class publisher
quantization. Community GGUF conversions for llama.cpp and Ollama also circulate. Quant type
codes have differed between runtimes (for example llama.cpp and Ollama), so verify that a
third-party GGUF loads and behaves correctly before production use.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The Apache-2.0 weights fine-tune with the standard open stack, PEFT/LoRA/QLoRA via
`transformers` and TRL on the safetensors checkpoints, and OpenAI's reference repo
(`openai/gpt-oss`) documents fine-tuning.

Two ceilings apply. The pre-training data and code are not released, so the weights can be
fine-tuned and continue-trained but not reproduced from scratch. Fine-tuning can also remove
safety behaviour, so re-apply guardrails and re-evaluate any derivative. Placing a derivative
on the EU market has provider implications (see Assess).

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve gpt-oss behind vLLM's or Ollama's OpenAI-compatible endpoint for drop-in integration
with existing OpenAI-client code.

```bash
vllm serve openai/gpt-oss-120b --revision <sha> --port 8000
# Then point any OpenAI SDK at http://localhost:8000/v1.
```

The one model-specific requirement is the harmony response format. Use the `openai/harmony`
renderer to construct the role hierarchy and channels instead of passing plain role strings.
With that in place, routing, retries and gateways carry over unchanged.
