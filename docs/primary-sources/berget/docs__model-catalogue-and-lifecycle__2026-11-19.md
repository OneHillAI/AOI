doc_type: docs
entity: berget
source_urls: https://api.berget.ai/v1/models ; https://docs.berget.ai/models/model-lifecycle.md ; https://docs.berget.ai/what-is-berget.md ; https://docs.berget.ai/llms.txt
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher
note: docs.berget.ai was recorded retrieved:false on 2026-07-25 (the stored ev-docs). It is readable now, including a Markdown version of every page.

## Served catalogue (GET /v1/models, 15 entries, EUR per million tokens unless stated; lifecycle_status active unless stated)
Text: mistralai/Mistral-Small-3.2-24B-Instruct-2506 (0.30 in / 0.30 out, Apache 2.0, BF16); zai-org/GLM-5.3-Flash (0.25 / 0.50, MIT, FP8); moonshotai/Kimi-K3.1-Pro (3.00 / 10.00, cached input 0.90, licence field "Other", MXFP4); google/gemma-4-31B-it (0.25 / 0.50, Apache 2.0, BF16).
Rerank: BAAI/bge-reranker-v2-m3 (0.10 / 0.10).
Embeddings: intfloat/multilingual-e5-large-instruct (0.03 / 0.02); intfloat/multilingual-e5-large (0.03).
Speech to text (EUR per second): KBLab/kb-whisper-large 0.000033; NbAiLab/nb-whisper-large 0.000033; Systran/faster-whisper-large-v3 0.000033; klang/pianissimo 0.0000583 (CC-BY-4.0).
Preview status (lifecycle_status preview, model_type system-one, 0.042 in): Qwen/Qwen3.5-2B; convaiinnovations/laya; Cloudflare/clef-flash.
No Llama, gpt-oss or GLM-4.7 entry remains.

## Model lifecycle page (VERBATIM extracts)
"Preview: This indicates that a model is available for testing, but may be unreliable. A model in Preview isn't guaranteed to graduate to Active and may be removed without notice."
"Active: The model is fully supported and recommended for production use. An Active model always passes the Upgrading or Deprecated status before it's retired."
Deprecation notice table: "Preview models | No notice"; "Active models | 2 or 3 weeks, depending on model usage".
Planned upgrade: moonshotai/Kimi-K3 retires 2026-11-06, successor Kimi K3.1 Pro, "Upgrade will take place during a maintenance window over the weekend of 2026-11-07 to 2026-11-08." (the API no longer lists Kimi-K3, so this has happened).
Retired models list: GLM-5.2 (2026-09-18); openai/gpt-oss-120b and meta-llama/Llama-3.3-70B-Instruct (2026-09-11); zai-org/GLM-4.7-FP8 (2026-09-04); moonshotai/Kimi-K2.6 (2026-08-28); mistralai/Mistral-Medium-3.5-128B (2026-08-25); meta-llama/Llama-3.1-8B-Instruct (2026-06-24).

## Marketing statements on residency (data, not fact; compare with the DPA)
docs "What is Berget AI?": "All inference, storage, and processing happens on European infrastructure. Your data never crosses borders, never touches US cloud providers, and is never used to train models." Landing page: "Open models running under Swedish jurisdiction with zero data retention." The Berget Code launch post (2026-05-13): "All data that is processed stays within Sweden's borders and Berget AI does not train any models on the code sent to the service."
Binding text says EEA, not Sweden (DPA Sec 10.1 and 10.2). Sweden-only is a marketing claim; no clause read promises it.
