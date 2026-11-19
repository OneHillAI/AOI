doc_type: docs
entity: baseten
source_urls: https://docs.baseten.co/inference/model-apis/pricing-and-limits.md ; https://docs.baseten.co/inference/model-apis/deprecation.md ; https://docs.baseten.co/inference/model-apis/overview.md
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

## Why stored
The 2026-09-21 entry recorded two documentation gaps: "a specific rate-limit/quota table was not located" and "No published model-deprecation/EoL policy was found". Both are now published.

## Default rate limits (VERBATIM table)
| Account tier | RPM | TPM |
| Basic (unverified) | 15 | 100,000 |
| Basic (verified) | 120 | 500,000 |
| Pro | 120 | 1,000,000 |
| Enterprise | Custom | Custom |
"These are account defaults. A model, service tier, or organization-specific configuration can set different limits."
"Baseten retains Model API usage data for 92 days." (usage counters, not prompt content)

## Deprecation policy (VERBATIM)
"Baseten announces deprecations 30 days before the deprecation date." "Baseten contacts affected users by email." "The deprecated model remains fully functional until the deprecation date." "You have 30 days to transition". "No model deprecations are currently scheduled."

## Model APIs supported-models table (overview.md, 2026-11-19)
Beam; DeepSeek V4 Pro 0813; DeepSeek V4 Flash 0731; DeepSeek V4.1 Flash; DeepSeek V4.1 Flash 1017; DeepSeek V4.1 Flash 1017 Fast; DeepSeek V4.1 Flash Fast; GLM 5.2; GLM 5.2 Fast; GLM 5.3; GLM 5.3 Fast; GLM 5.3 Flash; Kimi K3; Kimi K3.1 Pro; Muse Spark Open; Nemotron 3.5 Super VL; Nemotron 3 Ultra; OpenAI GPT 120B (openai/gpt-oss-120b). Llama 3.3 70B and Qwen3.5 are not in this table.

## Per-model context and output limits (overview.md, "Supported models", re-read 2026-11-19; context / max output, in tokens)
The page notes: "Baseten's context and output limits for a model may differ from the limits listed on its Hugging Face model card. Use the limits in this table when configuring requests."
Beam 1048k / 131k; DeepSeek V4 Pro 0813 1048k / 262k; DeepSeek V4 Flash 0731 1048k / 384k; DeepSeek V4.1 Flash 1048k / 262k; DeepSeek V4.1 Flash 1017 1048k / 262k; DeepSeek V4.1 Flash 1017 Fast 1048k / 262k; DeepSeek V4.1 Flash Fast 1048k / 131k; GLM 5.2 and 5.2 Fast 1048k / 262k; GLM 5.3, 5.3 Fast and 5.3 Flash 1048k / 262k; Kimi K3 1048k / 262k; Kimi K3.1 Pro 1000k / 1048k; Muse Spark Open 1048k / 1048k; Nemotron 3.5 Super VL 1048k / 1048k; Nemotron 3 Ultra 202k / 202k; OpenAI GPT 120B (gpt-oss-120b) 128k / 128k.
Fast variants "use the same weights as their base models with dedicated capacity for higher sustained throughput", with separate slugs, pricing and rate limits; "When Fast capacity is unavailable, Baseten uses base-model capacity and bills at the base model's rates."
Rate-limit scope note: "Cached and uncached input tokens count equally toward token rate limits." Usage counters (not prompt content) are retained 92 days.
