# Implement - Kimi K3 (Moonshot AI)

_How do we deploy it? Install, hardware, serving, safe-deployment controls, quantization,
fine-tuning, and integration live here._

<!-- item: install -->
## Install & run

Download the native MXFP4/MXFP8 weights from the verified `moonshotai` org on Hugging Face
(`huggingface.co/moonshotai/Kimi-K3`) and serve them with vLLM, SGLang or TokenSpeed. Pin the
exact revision hash and verify per-file checksums before loading.

<!-- item: hardware -->
## Hardware & VRAM requirements

Kimi K3 is a 2.8T-parameter MoE (104B active). Even at native MXFP4 the full weights are about
**1.4 TB**, so serving needs a **multi-GPU / multi-node cluster**; there is no single-GPU or
laptop path. The model card does not state exact per-GPU VRAM, so size against your cluster's
aggregate memory and interconnect rather than a published figure.

<!-- item: serving -->
## Serving stacks

The card documents **vLLM, SGLang and TokenSpeed**. KTransformers and TensorRT-LLM are not
listed, so the supported stack is narrower than the Kimi K2 lineage; confirm current engine
support and versions before committing, because MXFP4/MXFP8 kernels are version-sensitive.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

**Deployment Ceiling: T2 (customer-facing, human-reviewed), conditional.** The weights ship with
no safety tuning, guard model, or refusal training, so the entire model, input and output control
stack must be supplied externally: a companion guard/classifier model, input and output
guardrails, prompt-injection defences, and conservative decoding. Because the technical report
documents offensive-cyber capability the model does not refuse, sandbox and tightly bound any
agentic, tool-use, or code-execution deployment, and **T3+ (autonomous) is cautioned** without
controls beyond what an open model can currently justify. Complete the pre-deployment gate in the
[safe-deployment playbook](../../methodology/safe-deployment-playbook.md), pin and checksum the
checkpoint, and red-team for your specific use case before any exposed deployment.

<!-- item: quantization -->
## Available quantizations

The weights are natively **quantization-aware-trained** (MXFP4 weights, MXFP8 activations), so
the canonical checkpoint is already a low-precision artifact. Community MXFP4/GGUF quants
circulate to make the 2.8T model more tractable, but they are community artifacts; verify them
independently.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The downloadable weights and a broadly commercial licence support SFT and LoRA adaptation, but
the training data and code are closed, so there is no from-scratch reproduction path, and full
fine-tuning at 2.8T scale is very resource-intensive. Plan for parameter-efficient adaptation
rather than full fine-tuning unless you have frontier-scale infrastructure.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind vLLM or SGLang's OpenAI-compatible endpoint for drop-in client integration. Kimi K3
is natively multimodal, so text, image and video inputs and tool calls map onto the serving
layer's APIs; confirm the exact multimodal request format against the serving engine's
documentation.
