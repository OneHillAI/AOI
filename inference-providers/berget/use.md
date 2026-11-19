# Use - Berget AI

_What can it do and how do we use it? The served model catalogue and inference features live
here._

<!-- item: models-served -->
## Models served

The live API listing (2026-11-19) shows 15 entries, hosted in EEA data centres:

- **Gemma 4 31B**, **Mistral-Small-3.2-24B**, **GLM-5.3-Flash** and **Kimi K3.1 Pro** for text
  (the last carries a licence listed only as "Other")
- **bge-reranker-v2-m3** for reranking and two **multilingual-e5** embedding models
- four speech-to-text models (kb-whisper, nb-whisper, faster-whisper-large-v3, pianissimo)
- three Preview models (Qwen3.5-2B, laya, clef-flash), which sit outside the SLA and may be
  removed without notice

Llama 3.1 8B, Llama 3.3 70B, gpt-oss-120B and GLM-4.7 are no longer served; they were retired
between 2026-06-24 and 2026-09-11. For adopters the appeal is an EEA-hosted endpoint fronting
current open-weight families, so you can A/B a workload across models without changing
integration code.

<!-- item: features -->
## Inference features

The endpoints are **OpenAI-compatible chat/completions**, plus **embedding, reranking and
speech-to-text** endpoints. The API listing flags per model whether function calling, JSON mode,
streaming and vision are supported; for example Kimi K3.1 Pro, GLM-5.3-Flash and Gemma 4 list
function calling and vision. Berget also ships **"Berget Code"**, a seat-priced agentic coding
product that DPA Appendix 2 covers under the same zero-retention and no-training terms.
Confirm behaviour per model on your own prompts.
