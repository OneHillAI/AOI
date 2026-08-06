## Why

The index rates how much you control the inference you run, but two decision-critical, contractual
signals are not first-class schema fields - they sit only in prose, so they are invisible to the
score and to filtering:

1. **Contractual confidentiality over customer data**, distinct from retention and training. Whether
   the standard terms impose an NDA-grade duty of confidence is what decides, in trade-secret and
   patent-novelty terms, whether sending data to a provider is a confidential disclosure or a public
   one.
2. **Dedicated / single-tenant / on-prem / air-gapped availability today.** The isolation tier you
   can actually get - self-serve, shipped-but-contracted, enterprise-negotiated, or merely announced
   - is a real control/exit signal that the current schema cannot express.

A fresh primary-source pass across the six listed providers (2026-08-06; terms, DPAs, privacy
policies, product docs, with document effective dates) shows these two signals vary sharply and in
ways the current entries understate:

- **Confidentiality** ranges from an express mutual clause (Groq §10; Berget ToS §18) to no express
  duty with only functional protections (Infercom, DeepInfra), to an express disclaimer (Together
  ToS §9: "no confidentiality obligations ... unless otherwise agreed in writing"), to actively
  adverse terms (Runware: customer content deemed "non-confidential and non-proprietary" plus a
  perpetual, transferable licence over it).
- **Dedicated availability** ranges from shipped single-tenant racks plus on-prem/air-gapped BYOC
  (Infercom) and self-serve dedicated instances (DeepInfra, Together), to enterprise-only with no
  public terms (Groq GroqRack/GroqMetal; Runware), to announced-but-not-GA (Berget).

Leaving these in prose averages incompatibles into `data_governance` and `transparency_lockin` and
hides a material risk difference behind similar-looking scores.

## What Changes

1. **Add `data_governance.confidentiality`** (enum: `mutual` | `explicit` | `functional_only` |
   `none` | `disclaimed` | `adverse` | `unknown`) plus `confidentiality_caveats` to
   `schema/inference-provider.v2.schema.json`. It records the contractual confidentiality posture over
   customer data in the STANDARD terms - not the enterprise-negotiated exception.
2. **Add `dedicated_availability`** (enum: `self_serve` | `available` | `enterprise_only` |
   `coming_soon` | `none` | `unknown`) plus `dedicated_notes` as top-level provider fields.
3. **Scoring (no new dimension, no re-weighting).** The two signals refine the data feeding two
   existing dimensions:
   - `confidentiality` is an input to **`data_governance`**: an express mutual/provider-side duty is a
     positive; `disclaimed` or `adverse` is a material negative that caps the dimension.
   - `dedicated_availability` is an input to **`transparency_lockin`**: shipped self-serve or
     on-prem/air-gapped isolation strengthens control and exit; enterprise-only/coming-soon does not.
4. **Re-score every provider entry** against the two new fields and the 2026-08-06 primary sources
   (the rubric-v1.1 precedent: a scoring-input change triggers a re-score of every affected entry).
   Provider `rubric_version` moves to `1.2`; every score change is recorded in the entry changelog and
   the PR body.
5. **Populate both fields on all six provider entries** (groq, berget, infercom, together, deepinfra,
   runware) and update `methodology/provider-scoring-rubric.md` to document the two inputs.

Non-goals: no change to the model schema or model scoring; no change to the seven provider dimensions
or their weights; confidentiality and dedicated availability remain descriptive inputs, not their own
dimensions.
