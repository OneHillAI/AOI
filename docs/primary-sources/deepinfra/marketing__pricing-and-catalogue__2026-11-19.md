doc_type: marketing (pricing page) and docs (model listing)
entity: deepinfra
source_urls: https://deepinfra.com/pricing ; https://api.deepinfra.com/models/list
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

## Pricing page (USD, read 2026-11-19; list price, with a discounted price shown where the page marks a percentage off)
Per million tokens, input / output: Meta-Llama-3.1-8B-Instruct-Turbo $0.02 / $0.04; Llama-3.3-70B-Instruct-Turbo $0.10 / $0.32; DeepSeek-V4-Flash $0.09 / $0.18; DeepSeek-V4-Pro $1.30 / $2.60; DeepSeek-V4.1-Flash $0.20 / $0.60 (30% off, $0.14 / $0.42); Kimi-K3.1-Pro $2.00 / $10.00 (5% off, $1.90 / $9.50); GLM-5.3 $0.90 / $4.00 (38% off, $0.5625 / $2.50); GLM-5.3-Flash $0.15 / $0.50; gemma-4-31B-it $0.20 / $0.40. gpt-oss-120b $0.037 / $0.17 comes from the model listing below (it is not on the first screen of the page).
Service tiers (VERBATIM table rows): "Standard | Default scheduling, best-effort during peak demand | 1x base price"; "Priority | Scheduled ahead of standard traffic ... | 1.5x base price"; "Flex | Lower cost for non-production and asynchronous work, in exchange for slower responses and occasional unavailability | 0.8x base price".
Dedicated GPUs (billed per minute, invoiced weekly): A100 80GB $1.49, H100 80GB $2.90, H200 141GB $3.49, B200 180GB $4.89, B300 270GB $5.89 per GPU-hour. The stored 2026-07-25 figures (A100 $0.89, H100 $1.79, H200 $2.19, B200 $2.79) are 37% to 43% lower than these (the live rates are 59% to 75% higher). "For dedicated instances, DGX H100, B200 and B300 clusters ... please contact us".
"Hardware: All models run on H100 or A100 GPUs." "By default we limit each account to 200 concurrent requests per public model; dedicated deployments are limited only by their GPUs."
"Billing: You have to add a card or pre-pay or you won't be able to use our services. Pre-paid accounts draw down their balance as they go, and invoiced accounts are billed once at the beginning of the following month. You can also set a spending limit to avoid surprises."
The pricing page lists a "Claude" family (claude-sonnet-5-5, claude-opus-5-5, claude-opus-5, claude-fable-5, claude-sonnet-5, claude-haiku-4-5, claude-sonnet-4-6) and a Gemini family alongside the open models.

## Model listing (GET https://api.deepinfra.com/models/list, 411 entries)
By type: 233 text-generation, 55 text-to-image, 39 text-to-video, 34 embeddings, 18 text-to-speech, 18 speech-to-text, 6 decision, 5 reranker, 2 zero-shot image classification, 1 text-to-music. Entries not private and not marked deprecated: 232, of which 93 are text-generation. The `is_partner` flag is true on 94 of those 232 (partner models run on the partner's infrastructure under the partner's data policy, per the trust-centre FAQ): by publisher prefix, Anthropic 9, Google 13 of 20 (the Gemma models are not flagged), Bria 20, ByteDance 9, Wan-AI 8, Lightricks 8, Qwen 6, Pixverse 4, PrunaAI 4, black-forest-labs 3, XiaomiMiMo 3, ClarityAI 3, inworld-ai 3, openai 1. Of the 93 text-generation entries, open-weight families include DeepSeek V4 and V4.1, Kimi K3 and K3.1 Pro, GLM-5.x, Qwen3.5, gpt-oss-120b and 20b, Gemma 4, Nemotron 3, MiMo V2.6, Llama 3.3 and Llama 3.1. Several older entries carry a `deprecated` timestamp and a `replaced_by` field (for example Llama-3.3-70B-Instruct to the Turbo variant, Qwen3.5-122B to Qwen3.5-397B).
The "~77 to 90+ models" figure in the stored entry came from third-party research and is superseded: the live public catalogue is 232 entries across modalities (93 text-generation).
