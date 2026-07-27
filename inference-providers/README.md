# Inference Providers

APIs that serve open models. The defining fact about this category: **your data leaves
your network to reach them.** So these entries lead with data governance, residency, and
compliance - scored on the [provider rubric](../methodology/provider-scoring-rubric.md).

## How to read an entry

- **Data governance** - default retention, whether they train on your inputs, ZDR scope
  and its caveats, and whether *third-party* (closed) models routed through them fall
  under someone else's data terms.
- **Compliance** - SOC 2 (Type I vs II matters), ISO 27001/27701, HIPAA/BAA, GDPR/DPA -
  confirmed vs merely claimed.
- **Residency & sovereignty** - EU regions, region pinning, and the standing **CLOUD
  Act** exposure that every US-headquartered provider carries even when it offers EU
  regions.

## The set (v0.1)

Six providers spanning US hyperscale, EU-sovereign, and low-cost, ranked by AOI:

| Entry | HQ | Ownership | Note |
|---|---|---|---|
| [`together-ai`](together-ai/) | United States | partial | Broad open catalogue, ZDR by default; US CLOUD Act exposure, EU and dedicated regions gated to higher tiers. |
| [`infercom`](infercom/) | Luxembourg | substantial | EU-sovereign Inference-as-a-Service on open-weight models. |
| [`berget`](berget/) | Sweden | substantial | Swedish-owned, EU-sovereign inference on open-weight models. |
| [`groq`](groq/) | United States | substantial | Very low latency on custom LPU hardware; ZDR for all. |
| [`deepinfra`](deepinfra/) | United States | partial | Low cost, roughly 80 or more open models; US-only, SOC 2 Type I only. |
| [`runware`](runware/) | United Kingdom | partial | Large open-weight catalogue on one API; the binding terms claim broad rights over inputs and outputs. |

> Aggregators (e.g. OpenRouter) are a distinct sub-type: your data crosses **two**
> boundaries (the router + the downstream provider), each with its own policy. They are
> on the [roadmap](../docs/roadmap.md) and require the third-party-routing-leakage field
> to be read carefully.

## What to actually check before sending real data

1. **Turn on ZDR / no-train** - it is often *not* the default, especially on free tiers.
2. **Pin your region** if residency matters; confirm EU-region availability applies to
   *your* tier.
3. **Get the BAA/DPA** if you handle regulated data - "HIPAA-aligned measures" is not a
   signed BAA.
4. **Know what you're routing** - a closed model served *through* an open-model provider
   may fall under the model vendor's retention and training terms rather than the
   provider's ZDR.
5. **Remember the CLOUD Act** - US jurisdiction can reach EU-region data; weigh it for
   sovereignty-critical workloads.

Adding an entry: copy [`../templates/inference-provider/`](../templates/inference-provider/).
