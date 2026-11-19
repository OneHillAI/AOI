# Ollama cloud: docs, FAQ and pricing (read 2026-11-19, verbatim extracts)

## How `:cloud` models differ from local models
Source: https://docs.ollama.com/cloud (HTTP 200) and https://docs.ollama.com/cloud/models.md
- "Run larger models in Ollama's cloud without requiring a powerful GPU. Inference runs on Ollama's cloud
  service."
- "Cloud models do not need to be downloaded." Example: `ollama run gemma4:cloud`. "In the Ollama app, CLI,
  official libraries, or local API, use the `:cloud` name, such as `gemma4:cloud`."
- "Both connection methods require an Ollama account."
- "Cloud models currently do not support structured outputs."
- "Use only local models ... You can also disable cloud features." Local FAQ (https://docs.ollama.com/faq.md):
  set `disable_ollama_cloud` to true in `~/.ollama/server.json`, or `OLLAMA_NO_CLOUD=1`; "you will lose the
  ability to use Ollama's cloud models and web search."
- Data handling (cloud page): "Ollama processes cloud prompts and responses to answer your requests. We do not
  use them to train models."
- Local FAQ privacy paragraph: "When using cloud-hosted models, we process your prompts and responses to
  provide the service but do not store or log that content and never train on it."

## Cloud FAQ (https://docs.ollama.com/cloud/faq.md)
"Ollama operates with a zero data retention (ZDR) policy. When you use cloud models, Ollama processes your
prompts and responses transiently to provide the service but does not store or log that content and never
trains on it. Ollama collects basic account information and limited usage metadata that does not include
prompt or response content."

## Pricing page (https://ollama.com/pricing, read 2026-11-19)
Plans: Pay as you go USD 0 (pay per token for cloud models, 3 concurrent requests); Pro USD 20/month or
USD 200/year (USD 60 usage credits per month); Max USD 100/month (USD 300 credits, 10 concurrent requests,
early access to the newest models); Team USD 500/month (labelled "Early access" on the page; unlimited users, USD 1,000 shared
credits, 10 concurrent requests); Enterprise custom (model access controls, cost budgets, "Custom security
questionnaires"). "Running models on your own hardware is always unlimited."
Per-million-token model prices are listed for about two dozen cloud models (for example kimi-k3.1-pro input USD 2.00,
output USD 10.00; gpt-oss:120b input USD 0.15, output USD 0.60; deepseek-v4-pro input USD 1.32, output
USD 3.96). Off-peak pricing applies outside 12:00 to 18:00 UTC on weekdays and all weekend.
Pricing FAQ, Privacy section (verbatim):
- "Where are models hosted? Ollama hosts models and compute resources primarily in the United States. To serve
  global demand, we may route to Europe for additional capacity."
- "Is my prompt or response data trained on? Prompt or response data is never logged or trained on."
- "Who does Ollama partner with to host models? Ollama collaborates with NVIDIA Cloud Providers (NCPs) to host
  open models."
- "When Ollama partners with providers, we require no logging, no training, and zero data retention policies in
  place."
- "Can I have multiple Ollama accounts? No. Ollama is one account per person."
No partner names, regions list, sub-processor list or contract text is published.

## Cloud model lifecycle (https://docs.ollama.com/cloud/model-lifecycle.md)
"Ollama occasionally deprecates and retires older cloud models ... Cloud model retirement does not affect
local models." No retirements scheduled on 2026-11-19. Past retirements listed: 2026-06-16, 2026-06-30,
2026-07-15, 2026-07-31, 2026-09-25 (for example `qwen3.5:397b`, `glm-5.1`, `deepseek-v4-flash:0731`).
Release v0.40.16 (2026-11-09) adds "`ollama launch` explains when a cloud model has been retired".
