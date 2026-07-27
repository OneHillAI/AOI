# The Safe-Deployment & Controllability Playbook

**Version:** `1.0` · **Baseline:** July 2026

This is the *practical* half of the registry's mission: not "is this model good?" but
**"what do I actually have to do to run it safely, and how far can I take it before it
stops being controllable?"** It answers OneHill's second deliverable directly.

Every model entry ends with a **Deployment Ceiling** that applies this playbook to
that specific model. This document is the shared method behind those ceilings.

---

## 1. Controllability tiers - how far a model can be taken

We classify any deployment of an open model into one of five **controllability tiers**.
The tier is a function of *the controls you put around the model*, not of the model
alone - a mediocre model with strong controls can safely reach a higher tier than a
great model run naked.

| Tier | Name | Description | Typical controls required |
|---|---|---|---|
| **T0** | **Sandbox / research** | Local experimentation, no real data, no external effect. | Isolation from production data; that's it. |
| **T1** | **Internal assistant** | Employees use it on internal, non-sensitive tasks; human reads every output. | Access control, logging, acceptable-use policy, human-in-the-loop. |
| **T2** | **Customer-facing, human-reviewed** | Outputs reach customers but a human approves before they act. | + Input/output guardrails, jailbreak monitoring, PII controls, escalation path. |
| **T3** | **Customer-facing, autonomous (bounded)** | Model acts without per-output human review, but within hard, enforced limits. | + Deterministic guardrails on *actions*, rate/impact limits, kill switch, red-team sign-off, full observability. |
| **T4** | **High-stakes / regulated autonomous** | Decisions with legal, financial, safety, or fundamental-rights impact. | + Formal risk assessment (EU AI Act high-risk regime), independent eval, DPIA/FRIA, audited controls, continuous monitoring. |

> **The Deployment Ceiling** for a model is the **highest tier we assess it can reach
> with the controls in this playbook applied.** A model with an unfixable jailbreak
> problem, a pickle-only distribution, or a prohibited-use license is ceiling-capped
> regardless of capability. The ceiling is stated with the controls that unlock it.

## 2. The layered control stack (defence in depth)

Safety for an open model is **not a property of the weights** - it is a system you
build around them. Seven layers, each independently valuable:

1. **Supply-chain layer** - you deployed the artifact you think you did.
   *Pin the revision hash, verify checksum/signature, prefer safetensors, scan the
   checkpoint.* (See [supply-chain-risk.md](supply-chain-risk.md).)
2. **Isolation layer** - the model process can't reach what it shouldn't.
   *Run inference with least privilege, no ambient network/cloud credentials, egress
   controls; sandbox any tool/code execution.*
3. **Input layer** - untrusted input can't hijack the model.
   *Prompt-injection defences, input validation, treat retrieved/tool content as
   untrusted, separate system/instruction channels.* (OWASP LLM01.)
4. **Model layer** - the model itself is as aligned as it can be.
   *Use the safety-tuned variant, not the base model; keep a companion guard/classifier
   model; set conservative decoding defaults.*
5. **Output layer** - bad outputs are caught before they act.
   *Output classifiers/guardrails, PII/secret redaction, schema validation, grounding/
   citation checks for factual claims.* (OWASP LLM05, LLM09.)
6. **Action layer** - the model's *agency* is bounded and reversible.
   *Allow-list tools, human approval for high-impact actions, spending/rate limits,
   dry-run + confirm, deterministic policy engine on actions, kill switch.*
   (OWASP LLM06 Excessive Agency.)
7. **Observability layer** - you can see, alert on, and audit everything.
   *Full prompt/response logging (privacy-aware), jailbreak & anomaly detection,
   drift monitoring, incident response, red-team on a schedule.*

## 3. The pre-deployment gate (checklist)

Before any model reaches **T1 or above**, complete this gate. Each model entry
pre-fills the model-specific rows.

```
SUPPLY CHAIN
[ ] Canonical source + exact revision pinned; checksum/signature verified
[ ] safetensors/GGUF (no unsandboxed pickle load); checkpoint scanned, report kept

LEGAL / COMPLIANCE
[ ] License permits this specific use (commercial, scale, field-of-use)
[ ] EU AI Act role determined (deployer vs provider); obligations mapped
[ ] Training-content summary + copyright policy archived
[ ] Recorded in AI-BOM with owner assigned

SAFETY
[ ] Using the safety-tuned variant; safety evals reviewed
[ ] Jailbreak/red-team testing performed for THIS use case
[ ] Guard model / input+output classifiers in place
[ ] Residual-risk register written; unacceptable uses blocked

OPERATIONS
[ ] Isolation & least-privilege serving configured
[ ] Logging, monitoring, jailbreak/anomaly alerting live
[ ] Kill switch + rollback + incident runbook exist
[ ] Human-oversight / escalation path defined for the target tier
```

## 4. Model-specific safety notes (what each entry adds)

Because the playbook is generic, each model entry contributes the model-specific
reality on top of it:

- **Known jailbreaks / elicitation** observed for this model and whether they're patched.
- **Base vs instruct vs guard** variants and which to deploy.
- **Refusal behaviour & over-refusal** trade-offs.
- **Failure modes** seen in behavioural analysis (hallucination profile, sycophancy,
  prompt-injection susceptibility, tool-use reliability).
- **The assessed Deployment Ceiling** and the exact controls that unlock it.

## 5. Worked example of a Deployment Ceiling statement

> **Deployment Ceiling: T3 (bounded autonomous), conditional.**
> Reaching T2 requires the safety-tuned variant + an output guard classifier +
> prompt-injection defences, all of which are available. T3 additionally requires a
> deterministic action-policy engine, per-action human approval for irreversible
> operations, and quarterly red-teaming; the model's residual prompt-injection
> susceptibility (see Behaviour §4) means **T4 is not recommended** without controls
> beyond what an open model can currently justify. Below T1 (sandbox) no additional
> controls are required.

---

_The tiers, the control stack, and the gate are versioned here; entries reference this
version so a change to the method is traceable across every ceiling it produced._
