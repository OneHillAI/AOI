doc_type: docs
entity: fireworks-ai
source_urls: https://docs.fireworks.ai/serverless/pricing ; https://fireworks.ai/pricing ; https://fireworks.ai/models ; https://docs.fireworks.ai/guides/ondemand-deployments ; https://fireworks.ai/product/sovereign ; https://status.fireworks.ai/ ; https://docs.fireworks.ai/tools-sdks/openai-compatibility
retrieval_date: 2026-11-19
exists: yes
retrieved: true (read through a fetch-and-summarise tool; figures below are as reported by that tool)
tag: publisher

## Pricing (docs.fireworks.ai/serverless/pricing), USD per 1M tokens, input / cached input / output
- Kimi K3: Standard 3.00 / 0.30 / 15.00; Priority 3.75 / 0.375 / 18.75; US 4.50 / 0.45 / 22.50
- DeepSeek V4.1 Flash: 0.30 / 0.006 / 1.20; Priority 0.375 / 0.0075 / 1.50; US 0.45 / 0.009 / 1.80
- GLM 5.3 Flash: 0.15 / 0.03 / 0.50; Priority 0.1875 / 0.0375 / 0.625; US 0.225 / 0.045 / 0.75
- gpt-oss-120b: 0.15 / 0.015 / 0.60; Priority 0.18 / 0.018 / 0.72; US not listed
- Generic size tiers (input and output): under 4B 0.10; 4B to 16B 0.20; over 16B 0.90; MoE up to 56B 0.50; MoE 56.1B to 176B 1.20
- Embeddings per 1M input tokens: up to 150M params 0.008; 150M to 350M 0.016; Qwen3 8B 0.10
- US-only serverless is a 50% premium on select models (US column is 1.5x Standard). No effective date is stated on the current page (2026-09-20 note said effective 2026-09-01).
- fireworks.ai/pricing: modes Standard, Priority, Fast, Ultra-fast (preview), Batch, Spot. Batch = 50% off input and output. Spot = 30% off Standard on select models, throughput can drop to zero. On-demand GPU per hour: H100 80GB 8.00; H200 141GB 8.00; B200 180GB 13.00; B300 288GB 15.00; GB300 288GB 20.00 (per minute 0.134 / 0.134 / 0.217 / 0.250 / 0.334). Region-restricted deployments cost 1.5x. Idle deployments scale to zero after one hour by default.
- Enterprise on the pricing page: "Reserved Throughput includes a 'Throughput SLA and 99.9% uptime terms'" (terms not public; overage not covered). Zero data retention listed as default; SOC 2 Type II, ISO 27001/27701/42001 and HIPAA with a BAA listed. Fireworks is a first-party provider in Microsoft Foundry. Fireworks Sovereign is priced by contract.

## Catalogue (fireworks.ai/models)
Serverless-tagged: Kimi K3.1 Pro (new) and Kimi K3; DeepSeek V4.1 Flash and V4.1 Flash 1017; GLM 5.3 Flash and GLM-5.3; MiniMax M3.1 Flash and M3; Qwen 3.8 Max, Qwen3 Embedding 8B, Qwen3 Reranker 8B; Muse Spark Open (new); Ember-1 (new); NVIDIA Nemotron Lightning 3.5 30B A3B (new); Rune 26B-A4B (new); Ultramarine 1 Flash (new). Other families listed without the Serverless tag: Llama 3.x, Llama 4 Scout and Maverick, Llama Guard; Mistral Large 3, Small, Nemo, Devstral; gpt-oss-120b/20b and gpt-oss-safeguard; Nemotron 3 Super/Ultra/Nano; FLUX.1 dev ControlNet and schnell; BGE-M3, Voyage 4 family, Qwen3 embedding/reranker sizes.

## On-demand regions (docs.fireworks.ai/guides/ondemand-deployments)
Verbatim: "If you do not specify `--region`, the deployment uses the `GLOBAL` multi-region."; "Only **GLOBAL** is available by default."; "Quota for **US**, **CANADA**, **EUROPE**, **APAC**, and single regions must be granted by Fireworks."; placement cannot be changed after creation. The separate Regions page (docs.fireworks.ai/guides/regions) returns 404.

## Fireworks Sovereign (fireworks.ai/product/sovereign)
"Sovereign is offered to Enterprise customers"; pricing by contract; "Fireworks operates the inference engine, and you retain ownership of the environment, cluster, GPUs, and networking."; "Inference and response handling run inside your cluster."; training "(coming soon)". A web search summary and the enterprise page call it private preview; the product page itself does not state a preview status. The 2025-06-16 Virtual Cloud blog post is still live and does not mention Sovereign.

## Status (status.fireworks.ai)
"We're fully operational"; 23 serverless components; 90-day window labelled Aug 2026 to Nov 2026; lowest Kimi K3.1 Pro 99.50%, the other 22 components 100%; no incidents listed; no SLA mentioned. (2026-09-20: 28 components, lowest Kimi K3 99.67%.)

## OpenAI compatibility
Base URL https://api.fireworks.ai/inference/v1; the page documents Completions and Chat Completions; it does not mention embeddings, the Responses API or MCP.
