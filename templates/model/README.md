<!-- OneHill model dossier. The score block, tables, and flags should stay consistent
     with data.yaml (validated in CI). Prose sections are the independent analysis. -->

# <Model Family> - OneHill Dossier

> **Score: <NN>/100 · Grade <X>** · Openness tier: `<tier>` · Deployment Ceiling: **<T?>**
> Publisher: <name> (<country>) · License: `<classification>` · Last verified: <date>
>
> _<One-line independent verdict.>_

**Hard flags:** <none | 🚩 …>

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Openness & Transparency | ?/5 | |
| Provenance & Supply-chain | ?/5 | |
| Legal & Regulatory | ?/5 | |
| Safety & Alignment | ?/5 | |
| Technical Performance | ?/5 | |
| Operational Readiness | ?/5 | |
| Maintenance & Governance | ?/5 | |

## 1. What it is

<Independent description. Variants/sizes table. Intended use vs realistic use.>

## 2. Openness & license - what you're actually allowed to do

<Openness tier justification, component-by-component. License classification and the
restrictions that matter (commercial use, scale thresholds, field-of-use, acceptable-use).
Call out "open source" branding vs reality.>

## 3. Provenance & supply-chain - can you trust the checkpoint?

<Who distributes it, canonical source, formats (safetensors?), signing/checksums,
notable mirrors/quants, incidents. The checkpoint trust checklist result.>

## 4. EU AI Act & regulatory posture

<GPAI status, systemic-risk analysis, open-source-exemption qualification, what the
provider package contains (copyright policy, training-content summary), and what a
downstream deployer inherits.>

## 5. Technical behaviour & benchmarks

<Independent (or clearly-sourced) performance in class + the structured behavioural
analysis: hallucination, sycophancy, prompt-injection, tool use, refusals, failure mode.>

## 6. Safety & alignment

<Variant assessed, jailbreak resistance, guard model, harm-domain testing, residual risk.>

## 7. Deploying it safely - the practical guideline

<Apply the safe-deployment playbook to THIS model. The pre-deployment gate rows that
are model-specific. Concrete controls. Then the Deployment Ceiling statement.>

**Deployment Ceiling: <T?> (<conditional?>).** <Explain the highest tier reachable and
the exact controls that unlock it, and why higher is not recommended.>

## 8. Sources & evidence

<Numbered, tagged (onehill_verified / third_party / publisher) with URLs. Mirror the
evidence[] block in data.yaml.>

---

_Scored against [rubric v1.0](../../methodology/scoring-rubric.md). Data:
[`data.yaml`](data.yaml). Disagree with a score? The rubric is public - open an issue._
