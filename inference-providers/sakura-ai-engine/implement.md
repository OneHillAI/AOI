# Implement - Sakura Internet AI Engine

_How do we integrate it? API surface, authentication, region configuration, limits and exit live here._

<!-- item: integration -->
## API integration

The base URL is `https://api.ai.sakura.ad.jp`. Endpoints documented in the API reference (v1.0.1): OpenAI-compatible
`/v1/chat/completions`, `/v1/responses`, `/v1/embeddings`, `/v1/audio/transcriptions`, `/v1/audio/speech`, and an
Anthropic-compatible `/v1/messages`. The product page says only one preview model is available on the Messages API
and names it as Kimi-K2.6, while the price list and manual list Kimi-K2.7-Code; check the console for what is live.

Compatibility is partial. Usable chat parameters are model, messages, max_tokens, temperature, stream, tools,
tool_choice, response_format, reasoning_effort and chat_template_kwargs. Others (top_p, top_k, stop, seed, n,
logprobs, max_completion_tokens) are silently ignored. A request is cut off after about 5 minutes. The Responses
API has no image input or multi-turn yet. Reasoning tokens count against max_tokens.

<!-- item: authentication -->
## Authentication and account setup

You need a Sakura member ID (phone-number verification), a Sakura Cloud project (credit card registered), then you
issue account tokens in the AI Engine console. Tokens may not be shared or lent (article 11). The contract,
notices and support are in Japanese (basic terms articles 3 and 4). Closed models (PLaMo, cotomi) need a corporate
account and an application that the model provider approves in about 7 business days. Private Edition is by
order form, bank transfer and Japanese corporations only.

<!-- item: region-config -->
## Region and residency configuration

There is no region parameter, no ZDR switch and no data-location setting to configure; retention and location are
whatever the terms and documentation say. A private route is documented: enable a service endpoint gateway on your
Sakura Cloud switch and tick `api.ai.sakura.ad.jp`. Service policies can restrict who in your organisation creates
resources. For Private Edition, closed-network connection is not included unless it is written in the order form
(article 2(4)).

<!-- item: portability -->
## Portability and exit

There is no minimum term and you cancel by notice (articles 7 and 8), but the plan cannot be cancelled until every
account token and every RAG document is deleted. Documents can be listed, fetched and deleted through the API. The
open models served can be run elsewhere, and the OpenAI-compatible surface makes a swap simple. The two closed models
run only on Sakura. Private Edition has a two-month or one-year initial term, no cancellation inside it, and the shared
AI Engine contract cannot be cancelled while it runs (article 5). On termination Sakura deletes your model and related
data within a reasonable period, with backups and legally retained data removed in turn (article 9(5)).
