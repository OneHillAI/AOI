doc_type: docs
entity: nebius
source_urls: https://tokenfactory.nebius.com/models/catalog ; https://tokenfactory.nebius.com/models/catalog/text2text/<org>%2F<model> (per-model pages) ; https://docs.tokenfactory.nebius.com/model-deprecations-december-2026.md ; .../november-2026-deprecation-notice.md ; .../august-2026-deprecation-notice.md ; .../june-2026-deprecation-notice.md
retrieval_date: 2026-11-19
exists: yes
retrieved: true (catalogue and per-model pages rendered in the in-app browser, no login; the price list at /organization/prices needs a login and was NOT read; curl still gets HTTP 403 from the Cloudflare challenge)
tag: publisher
read_by: refresh agent 2026-11-19

## Catalogue (tokenfactory.nebius.com/models/catalog, rendered)
133 model rows, each with provider, modality, quantisation, parameters, context and a platform column. The platform column shows the same three tags (Public, Dedicated, Fine-tuning) on every row, so it is NOT a reliable guide; the per-model page says whether a public endpoint exists.
Rows include: DeepSeek V4.1 Flash and V4.1 Flash 1017 (1,048K context), DeepSeek-V4-Pro (1,024K), DeepSeek-V4-Pro-0813 (979K), DeepSeek-V4-Flash-0731, DeepSeek-R1-0528, DeepSeek-V3-0324; GLM-4.5 through GLM-5.3 and GLM-5.3-Flash; Kimi-K2-Instruct, K2-Thinking, K2.5, K2.6, K2.7-Code, Kimi-K3 (1,024K) and Kimi-K3.1-Pro (1,048K); MiniMax-M2.1 to M3 and M3.1-Flash; gpt-oss-20b and gpt-oss-120b (131K); Llama 3.1/3.2/3.3 variants and Llama-Guard-3-8B; Muse Spark Open; Nemotron 3 Nano, Super, Ultra, 3.5 Super VL and 3.5-Lightning; Qwen2.5, Qwen3, Qwen3.5, Qwen3.6, Qwen3.8-27B; Gemma-2/3/4; Inkling-2-Small (Thinking Machines); Reflection Beam 1.0; Hermes-4; INTELLECT-3; embedding models (bge, e5-mistral, Qwen3-Embedding-8B). Context windows are listed per row, which closes the earlier "no per-model context table" gap.

## Per-model pages read (VERBATIM values)
- gpt-oss-120b (Apache 2.0): Public endpoint Available; "1M Input $0.15 | 1M Cached $0.10 | 1M Output $0.60"; "Current processing region eu-north1".
- DeepSeek-V4-Pro-0813 (MIT): Public endpoint Available; $1.32 input, $0.04 cached, $3.96 output; "Current processing region uk-south1".
- GLM-5.3: Public endpoint Available; $1.40 input, $0.26 cached, $4.40 output; "Current processing region us-north1".
- MiniMax-M3: Public endpoint Available; $0.30 input, $0.06 cached, $1.20 output; "Current processing region us-central1".
- DeepSeek-V4-Pro (MIT, 862B): Dedicated endpoint Available; "Public endpoint Not available". The September entry recorded this model as $1.75 / $3.50 on a public endpoint; it is no longer served publicly.
- Llama-3.3-70B-Instruct (Llama 3.3 License): Dedicated available; "Public endpoint Not available". The September browser read recorded a public price of $0.13 / $0.40 for it; that is not reproducible today.
- Kimi-K2-Instruct: Dedicated available; "Public endpoint Not available". No deprecation notice naming it was found in the August, June, November or December pages.
Public endpoints therefore show current processing regions in Finland, the UK and two US regions on the same day. Dedicated pages say: "Log in to deploy dedicated endpoints with guaranteed performance, zero-retention data flow, and full configurability"; dedicated prices are behind the login.

## Deprecation notices (docs.tokenfactory.nebius.com; the page set is titled "Model Deprecations")
Each notice states a removal date from Token Factory Serverless, that "Dedicated Endpoints for these models will be unaffected", that "Token Factory does not automatically reroute requests from deprecated models", and a recommended replacement per model.
- 2026-08-31: DeepSeek-V4-Flash, Llama-3.3-70B-Instruct, MiniMax-M2.5, Hermes-4-70B, Cosmos3-Super-Reasoner, Llama-3_1-Nemotron-Ultra-253B-v1, Nemotron-3-Nano-Omni, Qwen2.5-VL-72B-Instruct, Qwen3-32B, Qwen3-Next-80B-A3B-Thinking.
- 2026-11-09: GLM-5.1, DeepSeek-V4-Pro (replacement DeepSeek-V4-Pro-0813), DeepSeek-V4-Flash-0731, DeepSeek-V4.1-Flash, Qwen3.5-397B-A17B.
- 2026-06-22: DeepSeek-V3.2 (and fast), MiniMax-M2.5-fast, Kimi-K2.5 (and fast), gpt-oss-120b-fast, INTELLECT-3, Qwen3-235B-A22B-Thinking-2507-fast, Qwen3-Next-80B-A3B-Thinking-fast, Qwen3.5-397B-A17B-fast, GLM-5.
- 2026-12-24 (announced): NVIDIA-Nemotron-3-Nano-30B-A3B and nemotron-3-super-120b-a12b.
The notices do not state a minimum notice period. They are per-event notices, not a standing deprecation policy; the Legal Quick Guide adds that model deprecations "are announced in advance" and that account owners are told by e-mail and in the platform.
The 2026-11-09 notice explains why DeepSeek-V4-Pro lost its public price. The 2026-08-31 notice dates the Serverless removal of Llama-3.3-70B-Instruct before the 2026-09-20 browser read that recorded a public price for it; this read cannot say why the two disagree.
