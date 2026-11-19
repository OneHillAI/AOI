# Together AI - serverless catalogue and pricing (read 2026-11-19)

Sources: https://www.together.ai/pricing (HTTP 200, all tabs server-rendered) and
https://docs.together.ai/docs/serverless-models (HTTP 200, lists API model strings, context, quantisation).

## Chat models on serverless now (24), USD per 1M tokens, input / output (docs table; pricing page agrees except where noted)
DeepSeek V4 Pro 0813 1.32/3.96 (NVFP4); DeepSeek V4.1 Flash 0.30/1.20 (FP8); DeepSeek V4.1 Flash 1017 0.30/1.20;
Elorian Glimpse 1.0 0.60/3.00; Meta Muse Glimmer 30B 0.35/1.50; Meta Muse Spark Open 816B A42B 1.25/4.25; MiniMax M3.1
Flash 0.15/0.60; Kimi K3 3.00/15.00; Kimi K3.1 Pro 2.00/10.00; NVIDIA Nemotron 3.5 Super VL 0.15/0.50; gpt-oss-120B
0.15/0.60 (MXFP4, 131072 context); Ternary Bonsai 27B free; Qwen3.5 9B 0.17/0.25; Qwen3.6 Plus 0.50/3.00; Qwen3.7 Max
2.50/7.50; Qwen3.7 Plus 0.32/1.28; Qwen3.8 Flash 0.15/0.47; Qwen4 Max 1.425/4.275 in the docs (pricing page shows a
promotion 1.05/3.15 until 2026-11-23 against 1.50/4.50 list); Reflection Beam 1.0 501B A23B 0.40/1.20; Ricursive Ripple
65B Preview 0.20/0.60; Thinking Machines Inkling 2 Small 0.30/1.00; Together Tev1 4B Experimental 0.042/free; GLM-5.2
1.40/4.40; GLM-5.3 1.40/4.40; GLM-5.3 Flash 0.15/0.50. Cached-input rates are published for most.
Gone from the serverless chat list since the entry's last pass: Llama 3.3 70B, Gemma 4 31B, Cogito v2.1 671B, MiniMax
M3 and M2.7, Qwen3.5-397B, Qwen3-235B. Llama 3.3 70B, Llama 4, Gemma 4 and Mixtral remain fine-tuning base models only.
Vision list: Kimi K3 and K3.1 Pro, Nemotron 3.5 Super VL, Qwen3.5 9B, Qwen4 Max, Inkling 2 Small.
Embeddings, rerank, moderation: docs verbatim "There are currently no embedding models offered via serverless", same
for rerank (dedicated only) and moderation.
Image, video and audio: dozens of models including wrapped third-party APIs (GPT Image 1.5 and 2, Gemini image
variants, Veo 3.1, Cartesia Sonic, Seedance, Wan, Vidu, PixVerse); Whisper Large v3 0.0015 per audio minute.
US-only endpoint: +25% on 8 models (see the data-handling extract).

## Other products on the pricing page
Provisioned Throughput (PTUs, sales). Dedicated Inference single-tenant GPU instances on demand per GPU hour: H100
5.49, H200 5.99, B200 9.29, B300 11.49, GB300 NVL72 15.79 (reserved via sales). GPU Clusters on demand H100 3.99, H200
5.99, B200 9.29, B300 11.49; reserved and preemptible tiers. Fine-tuning LoRA from 0.34 per 1M tokens (Qwen3.5 0.8B)
to 40.00 (GLM-5.1/5.2), minimum charges 4.00 to 60.00. Post-training B200 promo 9.00 per GPU hour until 2026-12-14.
