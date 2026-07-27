# Implement - EuroLLM (EuroLLM-9B / EuroLLM-1.7B)

_How do we deploy and run it? Install, hardware, serving, quantization, fine-tuning, and the
safe-deployment controls & Deployment Ceiling (**T2, conditional**)._

<!-- item: install -->
## Install & run

EuroLLM checkpoints are standard safetensors on the verified `utter-project` org - the usual
paths all work. Always pin an exact revision.

```python
# Hugging Face transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "utter-project/EuroLLM-9B-Instruct"   # or EuroLLM-1.7B-Instruct
rev = "<pinned-commit-sha>"                        # pin the revision, don't float on main
tok = AutoTokenizer.from_pretrained(model_id, revision=rev)
model = AutoModelForCausalLM.from_pretrained(model_id, revision=rev)
```

```bash
# vLLM (OpenAI-compatible server)
vllm serve utter-project/EuroLLM-9B-Instruct --revision <sha>

# Ollama / llama.cpp (community GGUF)
ollama run alibayram/erurollm-9b-instruct
./llama-cli -m eurollm-9b-instruct.Q4_K_M.gguf -p "Bonjour"
```

A hosted **NVIDIA NIM** endpoint (`utter-project/eurollm-9b-instruct`) also exists if you
prefer a managed API. Prefer safetensors and verify per-file checksums after download.

<!-- item: hardware -->
## Hardware & VRAM requirements

**EuroLLM-9B** runs on a single modern **24 GB GPU** - tight at full precision, comfortable
with light quantization - and needs modest headroom for the KV cache (the 4k context keeps
this small). **EuroLLM-1.7B** runs on modest GPUs and is viable on **CPU/edge** via GGUF,
making it a practical choice for local or low-resource multilingual deployments. Size to the
largest checkpoint you intend to serve.

<!-- item: serving -->
## Serving stacks

Because the checkpoints are plain safetensors with a conventional architecture, all mainstream
runtimes load them with no custom code:

| Stack | Use it for |
|---|---|
| **vLLM** | High-throughput serving + OpenAI-compatible API |
| **TGI** | Hugging Face-native production serving |
| **llama.cpp** | CPU / edge / GGUF quantized inference |
| **Ollama** | Local single-command runs |
| **transformers** | Prototyping and fine-tuning |

A hosted **NVIDIA NIM** endpoint is also available. This breadth is why Operational Readiness
scores 4; it stops short of 5 mainly on the short 4k context and the breadth of *official*
day-0 tooling versus the largest ecosystems.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Applying the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md), the
model-specific gate rows are:

- **Supply chain:** pin the exact `utter-project` revision hash and verify checksums; prefer
  safetensors (already the default - no pickle load).
- **Model layer:** deploy the **Instruct** variant, never the base checkpoint; set
  conservative decoding defaults.
- **Input/output layers:** add input/output guardrails and your **own** guard classifier for
  any customer-facing path - EuroLLM ships no companion guard model; add prompt-injection
  defences and treat retrieved/tool content as untrusted.
- **Language coverage:** run your **own per-language safety and quality evaluation** for each
  target language before relying on it - coverage is uneven across the 35 languages.
- **Compliance:** archive the (technical-report-derived) training-content summary and
  copyright posture in your AI-BOM.

**Deployment Ceiling: T2 (customer-facing, human-reviewed) - conditional.** With the Instruct
variant plus input/output guardrails, prompt-injection defences and per-language evaluation,
EuroLLM reaches customer-facing, human-reviewed use - its standout fit being **multilingual
EU-facing** applications under a clean EU-jurisdiction, Apache posture. T3+ (bounded
autonomous) additionally needs a deterministic action-policy engine, per-action human approval
for irreversible operations, and external guard tooling beyond what the release provides.

<!-- item: quantization -->
## Available quantizations

Community **GGUF** (QuantFactory, bartowski; via llama.cpp/Ollama), **MLX** 4-bit (Apple
silicon) and **GPTQ** quantizations circulate and are acknowledged, and the safetensors base
makes on-the-fly bitsandbytes 8-/4-bit straightforward. Coverage is marked *partial* because
these are largely community efforts rather than a broad first-class official quantization
program - verify the source and re-check quality (especially per-language) before relying on a
third-party quant in production.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Standard **SFT/LoRA** via `transformers` / TRL on the Apache-2.0 safetensors checkpoints is
the practical path. EuroLLM helps here in two ways: the technical report documents the recipe
(Megatron-LM, data mixture, EuroFilter), and the team releases the **EuroBlocks-Synthetic**
post-training dataset, which is directly useful for multilingual instruction adaptation. What
you do *not* get - unlike a fully-open model - is the complete pre-training corpus or an
end-to-end training repository, so from-scratch reproduction is out of reach. Note the EU AI
Act provider implications of placing a derivative on the market (see Assess).

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve EuroLLM behind **vLLM's OpenAI-compatible `/v1` server** (or use the hosted NVIDIA NIM
endpoint) for a drop-in integration with existing OpenAI-client code:

```bash
vllm serve utter-project/EuroLLM-9B-Instruct --revision <sha> --port 8000
# then point any OpenAI SDK at http://localhost:8000/v1
```

No model-specific client is required - the chat-completions surface behaves like any other
OpenAI-compatible endpoint, so routing, retries, and gateways carry over unchanged. Mind the
4k context limit when composing prompts.
