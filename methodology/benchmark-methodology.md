# Benchmark & Behavioural-Analysis Methodology

**Version:** `1.0` · **Baseline:** July 2026

This governs Dimension 5 (Technical Performance) and Dimension 4 (Safety & Alignment).
Its purpose is to produce **independent, reproducible** evidence - not to re-print the
publisher's numbers. Where OneHill has independently run an evaluation it is marked
`onehill_verified`; where we cite an external evaluator it is `third_party`; publisher
claims are recorded but never used to justify a top score.

---

## 1. Principles

1. **Reproducible or it doesn't count.** Every reported number ships with the harness,
   version, prompt template, decoding parameters, and date needed to re-run it.
2. **Contamination-aware.** Benchmark scores are meaningless if the test set leaked
   into training. We prefer evaluations with contamination controls and we flag
   suspiciously benchmark-specific behaviour.
3. **Judged in class.** A model is compared to peers of similar size and intended use,
   not to the absolute frontier.
4. **Behaviour over leaderboards.** A single MMLU number is nearly useless on its own;
   qualitative behavioural analysis (below) is weighted alongside quantitative scores.
5. **The same eval, run by us.** Where feasible OneHill re-runs a common core suite so
   models are comparable on *our* harness, not stitched from mismatched sources.

## 2. The evaluation stack

### 2a. Capability core (quantitative)
A fixed, versioned suite so entries are comparable. Representative axes (specific
datasets versioned in the harness):

| Axis | What it probes |
|---|---|
| General knowledge & reasoning | Broad knowledge + multi-step reasoning |
| Math & logic | Quantitative reasoning |
| Coding | Code generation & repair (e.g. SWE-bench-style, execution-based) |
| Instruction following | Adherence to complex, multi-constraint instructions |
| Long context | Retrieval & reasoning over long inputs |
| Multilingual | Non-English capability, incl. EU languages |
| Tool use / agentic | Function calling, multi-step tool workflows |

Each is run with pinned prompts and decoding settings; results stored with the harness
version and date. We report **our** score and, separately, the **publisher's claim**,
and note any gap.

### 2b. Behavioural analysis (qualitative, structured)
The part leaderboards miss. For each model we characterise:

- **Hallucination profile** - calibration, tendency to fabricate citations/facts,
  behaviour under uncertainty.
- **Sycophancy** - does it cave to user pushback against correct answers?
- **Instruction robustness** - sensitivity to prompt phrasing; format adherence.
- **Refusal behaviour** - appropriate refusals vs over-refusal; consistency.
- **Prompt-injection susceptibility** - does injected content in tool/RAG output hijack it?
- **Tool-use reliability** - malformed calls, hallucinated tools, loop behaviour.
- **Failure signature** - how it breaks (silent wrong answers vs visible errors).
- **Determinism/stability** - output variance at low temperature.

### 2c. Safety evaluation (feeds Dimension 4)
- **Elicitation / jailbreak battery** - a versioned set of known jailbreak families;
  we record what succeeds and whether a safety-tuned variant resists it.
- **Harm-domain probes** - CBRN, cyber-offensive, self-harm, child-safety, illegal
  behaviour (probes designed to measure refusal, not to produce usable harmful output).
- **Guard-model interaction** - does the family ship a classifier/guard, and does it help?
- **Base vs instruct** - base models are expected to lack safety tuning; we say so
  rather than scoring them as if deployable.
- **Residual-risk statement** - what remains after mitigations.

> **Responsible handling.** Safety probing is designed to *measure* susceptibility, not
> to generate deployable harmful content. Successful-jailbreak details are described at
> a level useful for defenders (which family, patched or not) without publishing
> working exploit strings.

## 3. What gets recorded per model

```yaml
performance:
  harness_version: "ohbench-1.0"
  last_run: "2026-07-20"
  class: "mid (30-80B active)"           # class the model is judged within
  core:
    reasoning:      {onehill: 0.71, publisher: 0.74}
    coding:         {onehill: 0.66, publisher: 0.70}
    instruction:    {onehill: 0.82, publisher: null}
    long_context:   {onehill: 0.61, publisher: null}
    multilingual:   {onehill: 0.58, publisher: null}
    tool_use:       {onehill: 0.69, publisher: null}
  contamination_flags: []                 # datasets with suspected leakage
behaviour:
  hallucination: "Moderate; fabricates citations when pushed beyond knowledge. Calibrated refusals otherwise."
  sycophancy: "Low-moderate."
  prompt_injection: "Susceptible to indirect injection via tool output; needs an input guard."
  tool_use: "Reliable JSON; occasional hallucinated tool names under ambiguity."
  refusals: "Well-calibrated; mild over-refusal on dual-use security topics."
safety:
  variant_assessed: "instruct (safety-tuned)"
  jailbreak_resistance: "Withstands casual jailbreaks; two known families succeed unpatched."
  guard_model_available: true
  harm_domains_tested: [cyber, self_harm, child_safety, cbrn]
  residual_risk: "Indirect prompt injection is the dominant residual risk; deploy behind an input classifier."
  source_type: onehill_verified
```

## 4. Honesty about coverage

OneHill cannot independently re-run the full suite on every checkpoint immediately.
Each entry states **which numbers are `onehill_verified` vs carried from third parties
or the publisher**, and the `last_run` date. A model with only publisher numbers is
capped below the top performance anchor until independently evaluated - and the entry
says so plainly.

## 5. External evaluators we cite

Where we haven't re-run an eval, we cite reputable independent evaluators (e.g.
public leaderboards and analysis orgs), always by URL and date, tagged `third_party`.
Their methodology is linked so readers can judge it. We never launder a publisher's
self-report as independent.
