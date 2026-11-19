# Inference providers

APIs that serve open models. Prompts and outputs leave your network to reach them, so entries lead with data governance, residency and compliance, scored on the [provider rubric](../methodology/provider-scoring-rubric.md). The ranked list of every entry is at [ownershipindex.ai/library](https://ownershipindex.ai/library).

## How to read an entry

- Data governance: default retention, whether the provider trains on inputs, the scope of zero data retention and its caveats, and whether third-party models routed through the provider fall under another party's data terms.
- Compliance: SOC 2 (Type I and Type II differ), ISO 27001 and 27701, HIPAA and BAA, GDPR and DPA, each marked as confirmed or only claimed.
- Residency and sovereignty: EU regions, region pinning, and the US CLOUD Act exposure of every US-headquartered provider, including when it offers EU regions.

Aggregators such as OpenRouter route data through two parties, the router and the downstream provider, each with its own policy. They are on the [roadmap](../docs/roadmap.md).

## Before sending real data

1. Turn on zero data retention and no-training. Neither is always the default, especially on free tiers.
2. Pin the region if residency matters, and confirm that EU availability covers your tier.
3. Obtain the BAA or DPA for regulated data. "HIPAA-aligned measures" is not a signed BAA.
4. Check what you route. A closed model served through an open-model provider can fall under the model vendor's retention and training terms.
5. Weigh the CLOUD Act for sovereignty-critical workloads. US jurisdiction can reach EU-region data.

## Adding an entry

Copy [`../templates/inference-provider-v2/`](../templates/inference-provider-v2/) and follow [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
