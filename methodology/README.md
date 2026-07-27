# Methodology

The public, versioned method behind every score, flag, and Deployment Ceiling in the
registry. Scores are **opinions with receipts** - this folder is the receipt.

| Document | What it defines |
|---|---|
| [`scoring-rubric.md`](scoring-rubric.md) | The **AI Ownership Index (AOI)** - 7 weighted dimensions, letter grades, hard flags, evidence rules. |
| [`openness-framework.md`](openness-framework.md) | How openness is graded on a spectrum (6 components, tiers) and how licenses are classified. |
| [`supply-chain-risk.md`](supply-chain-risk.md) | Checkpoint/provenance/security framework - who distributes it, format safety, signing, what has gone wrong. |
| [`eu-ai-act-mapping.md`](eu-ai-act-mapping.md) | GPAI obligations, the open-source exemption and its limits, systemic-risk, and a downstream-deployer checklist. |
| [`benchmark-methodology.md`](benchmark-methodology.md) | Independent, reproducible benchmarking + structured behavioural & safety analysis. |
| [`safe-deployment-playbook.md`](safe-deployment-playbook.md) | Controllability tiers, the layered control stack, the pre-deployment gate, and how Deployment Ceilings are set. |
| [`provider-scoring-rubric.md`](provider-scoring-rubric.md) | Adapted rubric for inference and hosting providers. |
| [`update-automation.md`](update-automation.md) | The data-first refresh pipeline that keeps entries current. |

## How the pieces fit

```
Openness Framework ─┐
Supply-chain Risk ──┤
EU AI Act Mapping ──┼──►  Scoring Rubric (AOI)  ──►  per-entry score + grade + hard flags
Benchmark Method  ──┘                                       │
                                                            ▼
                              Safe-Deployment Playbook  ──►  per-entry Deployment Ceiling
                                                            │
                              Update Automation  ──────────►  keeps all of it current
```

## Versioning

Each document carries a version. Changing an anchor, weight, or tier bumps the relevant
version and triggers a deterministic re-score via [`scripts/score.py`](../scripts/).
Entries record which method versions produced their scores, so any rating is traceable
to the exact method that generated it.

## Contributing to the methodology

The rubric is meant to be **contested**. Propose changes via PR against these files with
a rationale; a version bump and a re-score plan are part of the review. See
[`../CONTRIBUTING.md`](../CONTRIBUTING.md).
