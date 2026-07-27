# Use - Runware

_What can it do and how do we use it? The served catalogue and inference features live here._

<!-- item: models-served -->
## Models served

Runware aggregates a large **open-weight catalogue** from Hugging Face across **image, video, audio
and language** (reported on the order of 400K model variants), served through one unified API. It
includes the **FLUX / Stable Diffusion** image family, where fast, low-cost generation is an
original strength, alongside open language and multimodal checkpoints. The stated aim is to make
the broad Hugging Face open-model catalogue addressable behind a single schema.

<!-- item: features -->
## Inference features

The **Sonic Inference Engine** is a custom hardware and software stack built for fast, low-cost
inference across the catalogue, with image and video generation as a standout capability. Per-model
higher-level behaviours (tool or function calling, structured JSON output, streaming) follow each
served model's own capabilities and are not individually verified on Runware's endpoints. Treat
per-feature support as inherited from the model, and confirm per model.
