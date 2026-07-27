# The closing verdict - real ownership

Every model and inference-provider entry ends with **one** judgment: do you *really own* it?
The AOI 7-dimension score and the 5 signals are the analytical inputs; ownership is the
synthesis, and it is the point of the whole library - OneHill's mission is that you **own your
stuff and know what it is**.

Ownership is not one axis among several. Transparency, control, reliability and data-extraction
are not separate scores - they are what ownership *is made of*. You do not own something you
cannot see into (you don't know what you own), that you cannot change, that fails you, or that
quietly takes your knowledge and data. So the verdict is a single **level** built from four
factors.

## The four factors

Each factor is rated **strong | moderate | weak**, with a one-line rationale grounded in a
primary document (see [primary-source-grounding.md](primary-source-grounding.md)).

1. **Use & modify freely** - can you run it, modify it, develop it further, adapt it to your
   needs, with no gate and no field-of-use trap? Inputs: openness tier, the license (checked
   *per variant*), and the `trainability` + `specialization` signals.
2. **Transparency - you know what it is** - are the weights, training, data and behaviour open
   and inspectable; and (for a provider) are the actual Terms, DPA and Privacy Policy published
   *and legible*? You cannot own a black box. Inputs: the openness components, provenance, and
   documentation completeness - grounded in the real documents, not a marketing page.
3. **Reliability - it doesn't fail you** - can you run it dependably, and can misuse be excluded
   well enough to deploy it? Ownership is about *control*, not raw capability: a model you can run
   and safely deploy is fully yours even if a larger model would score higher, so **capability
   lives in the AOI score, not the ownership floor**. What *does* bite here is a genuine **safety
   gap** - unbenchmarked misuse, lighter alignment, a missing companion guard model, censorship
   that distorts output - which holds a model at *moderate* however capable it is. Inputs:
   operational/reliability and safety only.
4. **Doesn't extract your knowledge or data** - for a **self-hosted model**, weights run on your
   own infrastructure, so this is usually **strong** unless the model phones home or the license
   claws back rights; for a **provider/API**, it is the retention + training-on-inputs + data/IP
   ownership + residency analysis, read from the binding terms.

## From factors to a level

The overall **level** is `full | substantial | partial | limited | none`, and it is
**floor-weighted** - a weakness in any single factor caps the whole, because ownership is a
conjunction, not an average:

| Overall level | Rule of thumb |
|---|---|
| **full** | All four factors **strong** - you can use/modify it, you can see all of it, it performs, and nothing takes your data. |
| **substantial** | Strong on use-&-modify and data-control, no factor **weak** (one or two **moderate**). |
| **partial** | Exactly one factor **weak**; or use-&-modify or data-control only **moderate** (so the substantial bar is not met); or transparency **moderate** with real unknowns. |
| **limited** | Two factors **weak**. |
| **none** | Three or more **weak**, or a closed black box you can neither see nor modify. |

A black box can never be "full" however permissive its price; a model that fails you or a
provider that may train on your inputs can never be "full". The `verdict` is 1-3 sentences,
conclusive and concrete per [`STYLE.md`](../STYLE.md): what you own, what you don't, and the
condition that changes it.

## How to read the levels (and their limits)

Three honest caveats about what the level does and does not tell you:

- **For models, the verdict is driven by licence, transparency and safety.** Data-control is
  structural - strong for any self-hostable model - so it rarely discriminates *between* models;
  it earns its keep on providers and, in future, on closed models, where it swings. The other
  three factors do the work: **use-&-modify** (the licence), **transparency** (how open and legible
  it is), and **reliability** - which, now that raw capability is excluded, is really a *safety*
  read: only models whose misuse is genuinely controlled reach strong, so a documented safety gap
  is what most often keeps an otherwise-open model at *substantial* rather than *full*.
- **A model's level and a provider's level are not the same axis.** For a model, ownership is
  whether you own the artifact you run; for a provider it is whether the binding terms protect what
  you send. A provider rated *substantial* and a model rated *substantial* are not directly
  comparable - compare within a type, not across.
- **The AOI score and the ownership level are one system seen twice, not two independent checks.**
  The same seven dimensions feed both the 0-100 score and (mapped by the rules below) the four
  factors, so they corroborate by construction. The score is the analytical input; the level is
  the synthesis - agreement between them is expected, not a second opinion. Capability is the clearest
  case: it moves the score but, by design, not the ownership floor.

## Deriving the factors from the scored inputs (the rules)

Each factor is set by a written rule against the entry's licence, openness tier, AOI dimension
scores and (for providers) the read data terms - not by free judgement. The rules use explicit
cutoffs so two assessors reach the same rating. Where the primary documents have been retrieved
they override any inference; the rule is the floor, the documents are the ceiling.

**1. use_modify** ← licence classification + field-of-use + `trainability` signal, checked *per
variant*:
- **strong** - OSI-approved or permissive-open licence, ungated, no field-of-use restriction, and
  weights downloadable and fine-tunable (`trainability: full` or `partial` - "partial" reflects
  closed-data *reproducibility*, which is a transparency limit, not a use limit). For a
  licence-split family, the *variant in question* must itself be permissive.
- **moderate** - open-weight / community licence usable commercially but with restrictions
  (acceptable-use clauses, scale thresholds, brand terms), or a licence-split family where some
  variants are permissive and some are not.
- **weak** - research-only / non-commercial / commercial-prohibited licence, a hard access gate,
  or `trainability: limited` (you cannot meaningfully modify it).

**2. transparency** ← openness tier + weights/documentation ladder (for a provider, the read
Terms/DPA/Privacy Policy):
- **strong** - `fully_open` or `open_weights_recipe`: weights and docs open with training data at
  least described; for a provider, the actual Terms, DPA and Privacy Policy are published *and
  legible* (a retrieved binding document, per the grounding rule below).
- **moderate** - `open_weights` or `gated_open`: weights inspectable and docs good, but training
  data and code closed; for a provider, terms published but with gaps.
- **weak** - `open_washed` or `closed`, opaque training with no legible terms - a black box.

**3. reliability** ← the `operational` and `safety` dimension scores. Raw `performance`/capability is
scored elsewhere (it feeds the AOI score); this factor asks only whether you can run the model and
control its misuse:
- **strong** - `operational` ≥ 4 **and** `safety` ≥ 4 (dependable to run, and misuse is genuinely
  controlled: aligned, evaluated, guardable).
- **moderate** - `operational` = 3, or `safety` = 3 (runnable and deployable, but with a real
  dependability gap or a **safety gap you must fill yourself** - lighter alignment, unbenchmarked
  misuse, no companion guard model, censorship that distorts output).
- **weak** - `operational` ≤ 2 (you cannot run it dependably) or `safety` ≤ 2 (unsafe to deploy as
  presented). A low `performance` score never touches this factor.

**4. data_control** ← deployment model + provider `data_governance`:
- **strong** - a self-hosted model (weights on your own infra) that does not phone home and whose
  licence claws back no rights; **or** a provider that contractually never trains on inputs, offers
  zero-retention/ZDR by default and lets the customer retain data and IP (`data_governance` ≥ 4),
  grounded in the read terms.
- **moderate** - no-training-by-default but with retention or only opt-in ZDR, or unclear
  residency (`data_governance` = 3); or a self-hosted model whose licence claws back some rights.
- **weak** - a provider that may use or retain inputs, or trains by default (`data_governance`
  ≤ 2); or a model that phones home.

## How it's stored

```yaml
ownership:
  level: substantial            # full | substantial | partial | limited | none
  factors:
    use_modify:   { level: strong,   rationale: "one line, grounded in a primary doc" }
    transparency: { level: moderate, rationale: "..." }
    reliability:  { level: strong,   rationale: "..." }
    data_control: { level: strong,   rationale: "..." }
  verdict: "1-3 sentences - what you own, what you don't, and the condition that changes it."
```

The block introduces no claim not already supported in the entry. Any factor rated **strong**
on transparency or data_control must trace to a **retrieved binding document** (or an
independent attestation) - never a marketing page. That is enforced by `scripts/validate.py`
(`check_grounding`) and is the standard the Infercom entry failed.
