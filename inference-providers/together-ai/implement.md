# Implement - Together AI

_How do we integrate it? API integration, authentication, region/ZDR configuration, and
portability live here._

<!-- item: integration -->
## API integration

Together's **OpenAI-compatibility docs** describe an **OpenAI-compatible
`/v1` REST API** at `api.together.ai/v1` alongside Python and TypeScript SDKs. The practical
consequence is that an existing OpenAI client integrates by changing the base URL and API key
- chat/completions, streaming, tool use and structured outputs follow familiar shapes, so
integration is largely a configuration change rather than a rewrite. One gotcha the docs flag:
Together model IDs are namespaced (e.g. `openai/gpt-oss-20b`), so bare OpenAI model strings
return a 404.

<!-- item: authentication -->
## Authentication & account setup

Per the same docs, authentication uses a **bearer API key** (`TOGETHER_API_KEY`) supplied to
the OpenAI-compatible client. Fine-grained organisation/project key scoping and rotation
policy were not detailed in the sources reviewed, so if key-scoping is a control
requirement, confirm the available granularity in the account console before rollout.

<!-- item: region-config -->
## Region & ZDR configuration

**Zero data retention is the default** posture per the Privacy Policy, so no toggle is needed
for the core no-store behaviour. Together's support KB shows that **EU region selection and
dedicated region-pinned endpoints are gated to the Scale/Enterprise tiers** - they are
provisioned commercially rather than flipped on in a self-serve settings panel. Plan for a
sales/onboarding step if EU residency is mandatory.

<!-- item: portability -->
## Portability & exit

Because Together speaks the **OpenAI-compatible API** (documented) over
**portable open-weight checkpoints**, the exit path is clean: **independent third-party
analysis** confirms the same Llama / DeepSeek / Qwen / Mistral / gpt-oss models run across many
providers and self-hosted stacks. Switching cost comes from re-pointing the base URL and
re-validating outputs rather than re-engineering - the strongest argument for adopting an
open-weight inference provider over a closed API.
