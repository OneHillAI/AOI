# Implement - OpenAI gpt-oss (gpt-oss-120b / gpt-oss-20b)

_How do we deploy and run it? Install, hardware, serving, quantization, fine-tuning, and
the safe-deployment controls & Deployment Ceiling (**T2, conditional**)._

<!-- item: install -->
## Install & run

gpt-oss checkpoints are safetensors on the verified `openai` org, shipped natively in MXFP4.
The usual paths all work - always pin an exact revision.

```python
# Hugging Face transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "openai/gpt-oss-20b"        # or openai/gpt-oss-120b
rev = "<pinned-commit-sha>"            # pin the revision, don't float on main
tok = AutoTokenizer.from_pretrained(model_id, revision=rev)
model = AutoModelForCausalLM.from_pretrained(model_id, revision=rev, torch_dtype="auto")
```

```bash
# Ollama (single command)
ollama run gpt-oss:20b

# vLLM (OpenAI-compatible server)
vllm serve openai/gpt-oss-120b --revision <sha>

# llama.cpp / LM Studio (MXFP4 or GGUF)
./llama-cli -m gpt-oss-20b-mxfp4.gguf -p "Hello"
```

Prefer the safetensors from the `openai` org; verify per-file checksums after download.

<!-- item: hardware -->
## Hardware & VRAM requirements

Because only a small fraction of parameters are active per token, gpt-oss is cheaper to serve
than its total-parameter counts suggest:

- **gpt-oss-120b** (~117B total, 5.1B active) fits on a **single 80GB GPU** (H100/MI300-class)
  in native MXFP4.
- **gpt-oss-20b** (~21B total, 3.6B active) runs in about **16GB**, i.e. high-end consumer /
  edge hardware.

Budget extra headroom for the KV cache at long context lengths (both models support 128K).

<!-- item: serving -->
## Serving stacks

The checkpoints have day-0, first-class runtime support with native MXFP4 kernels - which is
why Operational Readiness scores **5**:

| Stack | Use it for |
|---|---|
| **vLLM** | High-throughput serving + OpenAI-compatible API |
| **llama.cpp** | CPU / edge / GGUF & MXFP4 inference |
| **Ollama** | Local single-command runs |
| **transformers** | Prototyping and fine-tuning |
| **MLX** | Apple-silicon inference |

Hosted endpoints are also available on major providers, so you can swap between self-hosted
and managed serving without changing the client contract.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Applying the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md), the
model-specific gate rows are:

- **Supply chain:** pin the exact `openai` revision hash and verify checksums; prefer the
  canonical safetensors (no pickle load).
- **Prompt layer:** render prompts with the **harmony** response format via `openai/harmony`
  - the models are trained only for it - and **never surface raw chain-of-thought** to end
  users.
- **Model layer:** these are safety-tuned, but the tuning is fine-tunable-away on open
  weights; set conservative decoding defaults.
- **Input/output layers:** add input/output guardrails and your **own** guard classifier for
  any customer-facing path (the base release ships no guard model; OpenAI's separate
  `gpt-oss-safeguard` classifier can fill that role), add prompt-injection defences, and treat
  retrieved/tool content as untrusted.
- **Compliance:** archive OpenAI's training-content summary and copyright posture in your
  AI-BOM (you depend on OpenAI for the training-content summary - the data is not published).

**Deployment Ceiling: T2 (customer-facing, human-reviewed) - conditional.** With
harmony-correct prompts, input/output guardrails, a guard classifier and no raw-CoT exposure,
gpt-oss reaches customer-facing, human-reviewed use. Its strong native tool use makes it a
capable agentic backbone, but T3+ (bounded autonomous) additionally needs a deterministic
action-policy engine, per-action human approval for irreversible operations, and external
guard tooling beyond what the release itself provides - held conservatively at T2 because the
base release ships no companion guard model.

<!-- item: quantization -->
## Available quantizations

gpt-oss is **natively quantized in MXFP4** - the mixture-of-experts weights are released at
4-bit, which is what lets the 120b fit on one 80GB GPU and the 20b in 16GB. This is a
first-class publisher quantization rather than an afterthought. Community **GGUF** conversions for
llama.cpp/Ollama also circulate; note that quant *type codes* have differed between runtimes
(e.g. llama.cpp vs Ollama), so verify a third-party GGUF loads and behaves correctly before
relying on it in production.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The Apache-2.0 weights fine-tune with the standard open stack - **PEFT/LoRA/QLoRA via
`transformers`/TRL** on the safetensors checkpoints - and OpenAI's reference repo
(`openai/gpt-oss`) documents fine-tuning. Adaptation is therefore straightforward, but note
two ceilings: the **pre-training data and code are not released**, so you can fine-tune and
continue-train but not reproduce from scratch; and fine-tuning can remove safety behaviour, so
re-apply guardrails and re-evaluate any derivative. Placing a derivative on the EU market has
provider implications (see Assess).

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve gpt-oss behind **vLLM's or Ollama's OpenAI-compatible endpoint** for drop-in
integration with existing OpenAI-client code:

```bash
vllm serve openai/gpt-oss-120b --revision <sha> --port 8000
# then point any OpenAI SDK at http://localhost:8000/v1
```

The one model-specific requirement is the **harmony response format**: use the
`openai/harmony` renderer to construct the role hierarchy and channels rather than passing
plain role strings. With that in place, routing, retries and gateways carry over unchanged.
