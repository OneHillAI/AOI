doc_type: model_card
entity: kimi-k3
variant/applies-to: Kimi K3 (single model; no separate Base/Instruct/Thinking)
source_url: https://huggingface.co/moonshotai/Kimi-K3
document_effective_date: open weights released ~2026-07-27 (announced ~2026-07-17)
retrieval_date: 2026-07-28
exists: yes
retrieved: true

## Governing clauses

[Publisher] Moonshot AI, Beijing, China.
[Size] Total "2.8T" parameters; activated "104B".
[Context] "1048576" tokens (1M).
[Architecture] Mixture-of-Experts, "16 of its 896 experts per token" active; innovations "Kimi Delta Attention" and "Attention Residuals"; claimed "2.5x improvement in scaling efficiency over Kimi K2".
[Modalities] Text + Image (native vision); video understanding mentioned.
[Weights / format] downloadable at huggingface.co/moonshotai/Kimi-K3; quantization-aware training with "MXFP4 weights and MXFP8 activations"; full weights ~1.4TB. Base tensor format (safetensors) not explicitly stated on the card; community MXFP4/GGUF quants exist.
[Serving stacks] vLLM, SGLang, TokenSpeed. (KTransformers / TensorRT-LLM not listed = not found.)
[Openness] Card does NOT disclose training-token counts, and does not state that training data or code are released. Weights-only release (consistent with open_weights). A technical report exists as a GitHub PDF (k3_tech_report.pdf), not on arXiv.
[Safety] No safety tuning, companion guard model, content filtering, or independent red-team is described on the card = not found.
