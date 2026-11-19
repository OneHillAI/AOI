# Groq - served catalogue, prices and deprecations (read 2026-11-19)

Sources: https://console.groq.com/docs/models and https://console.groq.com/docs/deprecations (HTTP 200).
groq.com/pricing now redirects to the Groq home page (no pricing content); the docs models page is the
price source.

## Production models (docs/models)
| Model ID | Price per 1M tokens | Context | Notes |
|---|---|---|---|
| llama-3.1-8b-instant | Contact Sales (Enterprise) | 131,072 | |
| llama-3.3-70b-versatile | Contact Sales (Enterprise) | 131,072 | |
| openai/gpt-oss-120b | $0.15 input, $0.60 output | 131,072 | developer plan 250K TPM, 1K RPM |
| openai/gpt-oss-20b | $0.075 input, $0.30 output | 131,072 | |
| whisper-large-v3 | $0.111 per hour | | |
| whisper-large-v3-turbo | $0.04 per hour | | |

## Preview models
canopylabs/orpheus-arabic-saudi ($40.00 per 1M characters), canopylabs/orpheus-v1-english ($22.00 per 1M
characters), meta-llama/llama-prompt-guard-2-22m and 86m ($0.03 / $0.04), meta-models/muse-spark-open
(Contact Sales), minimaxai/minimax-m2.7 (Contact Sales), openai/gpt-oss-safeguard-20b ($0.075 / $0.30),
qwen/qwen3.8-27b ($0.80 input, $4.00 output). "Preview models ... may be discontinued at short notice."

## Deprecations (docs/deprecations, verbatim where quoted)
- 2026-09-21: groq/compound and groq/compound-mini shut down.
- 2026-09-14: qwen/qwen3.6-27b replaced by qwen/qwen3.8-27b.
- 2026-08-16: llama-3.1-8b-instant and llama-3.3-70b-versatile. "This deprecation applies to free and
  developer-tier usage; enterprise customers with a committed-spend contract are not affected."
  Replacements: gpt-oss-20b and gpt-oss-120b or qwen3.6-27b.
- 2026-07-17: qwen/qwen3-32b and llama-4-scout-17b-16e-instruct. 2026-04-15: kimi-k2-instruct-0905.
  2026-03-09: llama-4-maverick. 2026-03-05: llama-guard-4-12b. 2025-12-31: playai-tts.
  2025-10-08: gemma2-9b-it. 2025-10-02: deepseek-r1-distill-llama-70b. 2025-08-30: llama3-70b/8b-8192.
- Process: announcement by email and docs, transition phase, optional automatic upgrade, end of life.

The self-serve (free and developer tier) text catalogue is therefore gpt-oss 120B and 20B, gpt-oss-safeguard
and, in preview, Qwen3.8-27B. The earlier entry list (Llama 3.1 8B, Llama 3.3 70B, Qwen3, Gemma, Mixtral,
DeepSeek R1 Distill Llama 70B) is out of date: all but the two Llama models were retired earlier, and the
Llama pair is now enterprise-contract only.
