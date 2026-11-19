# Use - Runware

_What can it do and how do we use it? The served catalogue and inference features live here._

<!-- item: models-served -->
## Models served

Runware aggregates a large mixed catalogue across **image, video, audio, language and 3D**, behind one
API. The registry is reported at 400K+ models, and 420 had published rates on 2026-11-19. It includes
open-weight and community models (the FLUX and Stable Diffusion image families, and text models such
as Kimi K3.1 Pro, DeepSeek-V4.1-Flash and GLM-5.3-Flash), and closed **Partner Models** licensed through
the model owner (GPT, Claude, Gemini, Kling, Seedance and others). Each model's commercial-use terms
follow its own Model Licence, which Runware says it does not guarantee to be complete.

<!-- item: features -->
## Inference features

The **Sonic Inference Engine** is a custom hardware and software stack built for fast, low-cost
inference across the catalogue, with image and video generation as a standout capability, and a
Serverless product runs your own code on Runware GPUs. Per-model higher-level behaviours (tool or
function calling, structured JSON output, streaming) follow each served model's own capabilities and
are not individually verified on Runware's endpoints. Treat per-feature support as inherited from the
model, and confirm per model.
