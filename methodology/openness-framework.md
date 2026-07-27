# The Openness Framework

**Version:** `1.0` · **Baseline:** July 2026

"Open source AI" is not binary. A model can ship its weights but hide its data; ship a
paper but no code; carry a license that calls itself "open" while forbidding
commercial use. This framework grades **openness on a spectrum**, component by
component, so an entry's Dimension-1 score is transparent and comparable.

It builds on prior art - the Linux Foundation **Model Openness Framework (MOF)**,
Stanford's **Foundation Model Transparency Index**, the **OSI** Open Source AI
Definition, and Hugging Face / Google **Model Card** norms - and reduces them to a
practical six-component grade.

---

## The six components

Each component is graded **Open / Partial / Closed**, with a short evidence note.

| # | Component | Open | Partial | Closed |
|---|---|---|---|---|
| 1 | **Weights** | Downloadable, permissive license | Downloadable, restricted/gated | Not downloadable |
| 2 | **Training data** | Dataset released or fully reproducible recipe | Described in prose / partially released | Undisclosed |
| 3 | **Training code** | Released & runnable | Partial / reference only | Undisclosed |
| 4 | **Evaluation code & results** | Released & reproducible | Results only, no code | Undisclosed |
| 5 | **Documentation** | Complete model card + intended use + limitations + data | Basic model card | None / marketing only |
| 6 | **License** | OSI-approved or equivalently permissive | "Open weight" community license with limits | Proprietary / research-only |

## Openness tiers (derived)

The six components roll up into a tier that sets the *ceiling* for the Dimension-1
score in the [scoring rubric](scoring-rubric.md):

| Tier | Definition | D1 ceiling |
|---|---|---|
| **Fully Open** | All six components Open (or data as a fully reproducible recipe). | 5 |
| **Open Weights + Recipe** | Weights + code + docs Open; data Partial. | 4 |
| **Open Weights** | Weights Open/Partial + docs; data & training code Closed. | 3 |
| **Gated Open** | Weights downloadable but gated + restrictive community license. | 3 |
| **Open-washed** | Marketed as "open" but license forbids common uses or key components undisclosed. | 2 |
| **Closed** | Weights not available. | 0 (out of scope for this registry unless notable) |

## License classification

Licenses are tagged into one of these buckets, because the label "open" is
routinely misused:

- **OSI-approved** - Apache-2.0, MIT, BSD, etc. No field-of-use restriction.
- **Permissive-open (non-OSI)** - e.g. broadly permissive but with a lightweight
  acceptable-use policy.
- **Open-weight / community license** - e.g. Llama Community License, Gemma Terms -
  free to use with **restrictions** (acceptable-use clauses, brand terms, sometimes
  scale thresholds). *Not* open source by the OSI definition.
- **Research-only / non-commercial** - e.g. CC-BY-NC, research licenses. Commercial
  use barred.
- **Custom / ambiguous** - must be read in full; flagged for legal review.

> **Why this matters for the EU AI Act.** The Act's *open-source exemption* for GPAI
> models applies (roughly) to models released under a **free and open-source license**
> whose parameters, architecture and usage information are made public - and it does
> **not** apply to models placed on the market for a fee or with monetisation, nor to
> systemic-risk models. A "community license" with restrictions may **not** qualify for
> the exemption. This is analysed per-entry in the
> [EU AI Act mapping](eu-ai-act-mapping.md).

## How this is recorded in an entry

Each model's structured data file carries an `openness` block:

```yaml
openness:
  tier: open_weights          # fully_open | open_weights_recipe | open_weights | gated_open | open_washed | closed
  components:
    weights:        open       # open | partial | closed
    training_data:  closed
    training_code:  closed
    evaluation:     partial
    documentation:  open
    license:        open_weight
  license:
    spdx: "LicenseRef-Llama-3.1-Community"   # or a real SPDX id like Apache-2.0
    classification: open_weight              # osi | permissive_open | open_weight | research_only | custom
    commercial_use: allowed_with_conditions  # allowed | allowed_with_conditions | prohibited
    notable_restrictions:
      - "700M MAU threshold requires a separate license"
      - "Acceptable Use Policy applies"
  evidence:
    - {claim: "weights downloadable", source_type: onehill_verified, url: "..."}
```

The registry's [`scripts/score.py`](../scripts/) reads this block to compute the
Dimension-1 score and enforce the tier ceiling.
