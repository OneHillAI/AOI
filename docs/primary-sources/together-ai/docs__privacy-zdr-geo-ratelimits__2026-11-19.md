# Together AI - product docs on data handling, ZDR, geo inference, rate limits (read 2026-11-19, verbatim extracts)

Sources (HTTP 200, Mintlify docs, not contracts): https://docs.together.ai/docs/privacy-and-security ;
/docs/zero-data-retention ; /docs/serverless/geo-specific-inference ; /docs/serverless/rate-limits.
The docs say "The privacy policy is the authoritative legal statement of Together's data practices."

## Default behaviour (privacy-and-security, zero-data-retention) - NEW detail versus the stored entry
- "By default, Together stores the prompts you send and the responses models return, and may use them for product
  improvements. This data is not shared with third parties, and you can delete it at any time."
- Three org-admin toggles: "Prompt storage: On by default. Stores prompts and model responses for product
  improvements. Turn it off to enable ZDR, which also turns off passthrough models." "Passthrough models: On by
  default. Allows your organization to use models that forward prompts and responses to third-party providers."
  "Model training: Off by default."
- "Some models are offered as passthrough, which means Together forwards your prompts and responses directly to the
  upstream provider. The provider handles that data under its own data policy."
- ZDR: "ZDR is not enabled by default." Applies at the organization level and only to requests after enabling.
  "Request content may pass through volatile memory and temporary caches while your request is served, but it is not
  persisted to non-volatile storage." Retained under ZDR: request metadata (token counts, model IDs, timestamps),
  account data, and files you upload for fine-tuning or the batch API until you delete them.
- "Together AI accepts security vulnerability reports through its HackerOne program. The program is private."
- "Models on Together are hosted at full precision." (The chat catalogue table on the same site lists FP4, FP8, NVFP4
  and MXFP4 quantisation for most models, so this line is contradicted by Together's own catalogue.)
- "DeepSeek models are hosted in Together's secure North America data centers."

## Residency
- "Geo-specific inference keeps inference processing for supported serverless models inside one geography." Only the
  United States is offered: https://us-api.together.ai/v1 at 1.25x standard rates, for 8 models (Kimi K3, Kimi K3.1
  Pro, GLM-5.3, GLM-5.3 Flash, DeepSeek V4.1 Flash and 1017, DeepSeek V4 Pro 0813, MiniMax M3.1 Flash).
- "Requests to api.together.ai do not guarantee US processing." "The guarantee covers where your request is processed.
  It doesn't cover where data is stored, where logs are written, or how network traffic is routed." No fallback: a
  missing model returns 404 region_unavailable.
- "For other data-residency, regulatory, or compliance requirements, such as GDPR, Together supports private
  networking and virtual private cloud (VPC) deployments, including in EU regions. Use a dedicated endpoint, or
  contact sales." No EU serverless endpoint is documented.
- Support KB (https://support.together.ai/articles/8079447813-eu-data-centres-and-dedicated-model-deployment, "Last
  updated 1 year ago"): EU data centres available; dedicated endpoints on targeted data centres including EU "is only
  available on Scale and Enterprise tier plans".

## Rate limits and SLA
- "Serverless performance is best-effort. For committed throughput and reliability guarantees, see provisioned
  throughput" (reserved capacity "with a defined service level agreement (SLA)", via sales; SLA text not public).
- "Enterprise and Scale contracts: If you have an active Enterprise or Scale contract, your purchased rate limits stay
  in place until the contract expires." (The tier names now read as legacy contracts; the privacy docs mention a
  "Limited tier".)
