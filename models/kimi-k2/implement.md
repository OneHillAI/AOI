# Implement - Kimi K2 (Moonshot AI)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Kimi K2 weights are block-FP8 safetensors on the verified `moonshotai` org. This is not a
single-command local model: plan for a multi-GPU or multi-node serving stack, and pin an exact
revision.

```bash
# vLLM (OpenAI/Anthropic-compatible server), tensor/pipeline parallel across a node/cluster
vllm serve moonshotai/Kimi-K2-Instruct --revision <sha> \
  --tensor-parallel-size 8 --trust-remote-code

# SGLang (alternative high-throughput engine)
python -m sglang.launch_server --model-path moonshotai/Kimi-K2-Instruct --revision <sha>
```

KTransformers (heavy CPU offload) suits constrained GPU memory, and TensorRT-LLM suits maximum
throughput. Verify per-file checksums after download.

<!-- item: hardware -->
## Hardware & VRAM requirements

Kimi K2 is a 1T-parameter MoE (32B active). Even in block-FP8 the weights are about 1 TB, so
serving needs a multi-GPU or multi-node cluster (e.g. a full 8×80-141 GB node or more) or heavy
CPU offload via KTransformers. There are no small variants, so single-GPU or laptop deployment is
not possible. Budget substantial additional headroom for the KV cache at the full 128K context.

<!-- item: serving -->
## Serving stacks

The publisher documents support for four high-end serving engines.

| Stack | Use it for |
|---|---|
| vLLM | High-throughput serving + OpenAI/Anthropic-compatible API |
| SGLang | High-throughput serving, structured generation |
| KTransformers | GPU-constrained deployment via CPU/GPU offload |
| TensorRT-LLM | Maximum-throughput NVIDIA-optimised serving |

There is no llama.cpp or Ollama single-box path at full precision. The model's scale gates
deployment, which is why Operational Readiness scores 3.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Apply the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md). The
model-specific gate rows are:

- Supply chain: pin the exact `moonshotai` revision hash and verify block-FP8 checksums. The
  weights are safetensors, so no pickle load occurs.
- Model layer: deploy the Instruct variant, never the Base checkpoint, and set conservative
  decoding defaults.
- Input/output layers: add guardrails and your own guard classifier for any customer-facing path,
  because Kimi K2 ships no companion guard model. Add prompt-injection defences and treat
  retrieved and tool content as untrusted, which matters given the native tool-use focus.
- Behaviour: allow for China-aligned topic censorship and do not assume neutral coverage on
  politically sensitive prompts.
- Compliance: self-assemble the copyright policy and training-content material, which are not
  available upstream.

Deployment Ceiling: T2 (customer-facing, human-reviewed), conditional. With the Instruct variant,
input/output guardrails, a guard model and prompt-injection defences, Kimi K2 reaches
customer-facing, human-reviewed use. T3+ (bounded autonomous), which its agentic positioning
invites, also needs a deterministic action-policy engine, per-action human approval for
irreversible operations and external guard tooling beyond what the release provides.

<!-- item: quantization -->
## Available quantizations

Kimi K2 is distributed natively in block-FP8, which is the practical serving format. Community
lower-bit and GGUF quants make the trillion-parameter model tractable on smaller clusters, but
they are community artifacts, not a broad official quantization programme. Verify the source and
test quality before relying on a third-party quant in production. Coverage is partial for that
reason.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

A released Kimi-K2-Base checkpoint and the permissive modified MIT licence make adaptation
possible, and standard SFT or LoRA is the practical path for most teams. Two limits keep coverage
partial. The training data and code are not released, so continued pre-training and from-scratch
reproduction are not possible. Full fine-tuning of a 1T-parameter MoE is resource-intensive, so
most adopters are limited to parameter-efficient methods. Placing a derivative on the market
carries EU AI Act provider implications (see Assess).

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve Kimi K2 behind the OpenAI/Anthropic-compatible endpoint of vLLM or SGLang for drop-in
integration with existing client code:

```bash
vllm serve moonshotai/Kimi-K2-Instruct --revision <sha> --tensor-parallel-size 8 --port 8000
# then point any OpenAI-compatible SDK at http://localhost:8000/v1
```

Kimi K2's native tool calling maps onto the function-calling API, so agentic clients and tool
routers carry over unchanged and no model-specific client is required.
