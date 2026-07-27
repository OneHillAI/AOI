# Assess - DeepInfra

_Should we route our data through this provider? Data governance, compliance, residency,
security, pricing, and reliability - plus the provider AOI score (60.4/100 · Grade C) -
live here._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

DeepInfra runs a **zero-retention policy** for inputs and outputs by default and **does not
train** on submitted data; per its data-privacy documentation it logs only **debugging
metadata** (request ID, cost, sampling parameters), reserving the right to log small portions
of requests for debugging or security, and batch requests may store data **temporarily,
encrypted on disk, then delete it** after inference. That is a strong default posture, and it
is grounded in the retrieved Terms and data-privacy pages rather than a marketing claim.

The decisive caveat is **scope**: this covers **DeepInfra's own open-model serving only**. The
same documents state that when you route requests to the **closed models it re-sells** -
Anthropic Claude, Google - DeepInfra **transfers your data to those endpoints to fulfil the
request**, and **that vendor's** storage and training policy applies (Google stores the output
per its Privacy Notice; Anthropic per its Trust Centre). This is the key finding for anyone
assuming a single blanket data guarantee: the guarantee is model-dependent, so segregate
open-model and closed-model traffic when governance matters.

<!-- item: data-ownership -->
## Data & IP ownership

For DeepInfra's **own open-model serving**, the ownership story is clean and now grounded in
the retrieved Terms of Service, which state you **retain any intellectual property rights over
your Submissions, which will remain private**. Combined with **zero-retention** and **no
training on submitted data**, your inputs, outputs and any derived knowledge stay yours -
**customer_retains**. But ownership is **not uniform across the catalogue**. The **closed models
DeepInfra re-sells** - Anthropic Claude, Google - are **transferred to those vendors** and route
your data under **their** storage and training terms rather than DeepInfra's, so whether your data
stays proprietary depends on which model you call. The **sub-processor list is not disclosed**.
Segregate open- and closed-model traffic and pin the terms per model.

<!-- item: compliance -->
## Compliance & attestations

DeepInfra's data-privacy documentation states **SOC 2 and ISO 27001
certification** plus **GDPR and HIPAA technical/organisational measures**. The finer **SOC 2
Type 1 (point-in-time, not Type II)** designation, the **sub-processor list** and **ISO 27701**
status live on the Sprinto-powered **trust centre**, which is unreachable -
**documented but unverified**. **HIPAA is framed as measures, not a BAA**. For healthcare or
continuous-controls procurement, confirm the SOC 2 Type and the HIPAA posture on the trust
centre directly.

<!-- item: residency -->
## Data residency & jurisdiction

DeepInfra operates **US-based data centres only** - **no EU data-residency option was
surfaced** and **region pinning is unconfirmed**. For workloads with EU residency
requirements this is a hard constraint that no plan upgrade removes. As a US-headquartered
company it also carries standing **US CLOUD Act exposure**.

<!-- item: security -->
## Security controls

Baseline controls are evidenced by **ISO 27001** and **SOC 2** certification, and the retrieved
data-privacy docs confirm batch data is **held encrypted on disk then deleted**. The assessment
is held to partial because the **SOC 2 Type-1-vs-Type-II** distinction rests on the unretrieved
trust centre and **no independent penetration test** was surfaced.

<!-- item: pricing -->
## Pricing & cost model

Cost is DeepInfra's standout: it is **among the cheapest providers on the market**. Pricing
is **mixed** - pay-as-you-go **per-token** (indicatively Llama 3.1 8B ~$0.02/M, Llama 3.3 70B
~$0.35/M, gpt-oss-120B ~$0.08/M blended) plus **dedicated GPU by the hour** (A100 $0.89, H100
$1.79, H200 $2.19, B200 $2.79). Rates are **approximate**, so confirm live pricing, but the
order of magnitude is the reason to consider DeepInfra.

<!-- item: reliability -->
## Reliability posture

No incidents have been reported, but **no public uptime SLA or failover documentation was
independently verified**. Reliability is therefore assessed conservatively: adequate on
available evidence, but without an observable status/SLA record to lean on for
availability-critical workloads.
