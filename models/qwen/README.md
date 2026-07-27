<!-- OneHill model dossier. The score block, tables, and flags should stay consistent
     with data.yaml (validated in CI). Prose sections are the independent analysis. -->

# Qwen (Qwen3 family) - OneHill Dossier

> **Score: 67.6/100 · Grade C** · Openness tier: `open_weights` · Deployment Ceiling: **T3**
> Publisher: Alibaba (Qwen team) (China) · License: `osi` · Last verified: 2026-07-25
>
> _A best-in-class open coding family with a huge ecosystem, held back by an EU systemic-risk documentation gap on its largest variants._

**Hard flags:** 🚩 EU AI Act systemic-risk variants (Qwen3-235B, Qwen3-Coder-480B) likely exceed 1e25 FLOPs with no Article 55 documentation (caps grade at C)

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Openness & Transparency | 3/5 | Apache-2.0 weights + good docs, but training data/code closed. |
| Provenance & Supply-chain | 4/5 | Verified org, safetensors, checksums; dual-hub surface; no signing. |
| Legal & Regulatory | 3/5 | Permissive license is a plus; no training summary and a systemic-risk gap. |
| Safety & Alignment | 3/5 | Safety-tuned but light; China-aligned topic censorship; no guard model. |
| Technical Performance | 4/5 | Class-leading open coding; strong general capability (third-party). |
| Operational Readiness | 5/5 | HF + ModelScope + Ollama, full serving stack, laptop-to-datacentre sizes. |
| Maintenance & Governance | 3/5 | Active, accountable publisher; no formal disclosure/deprecation policy. |

## 1. What it is

Qwen is Alibaba's open-weight LLM family, and the Qwen3 generation is one of the most
widely used open model lineages in production. It spans dense models from ~0.5B to 32B,
Mixture-of-Experts variants up to 235B, and the standout **Qwen3-Coder-480B-A35B**, a
top-tier open coding model. The realistic sweet spot is internal coding and agentic
tooling, where its capability-per-dollar and ecosystem breadth are hard to beat - provided
you wrap it in your own controls.

## 2. Openness & license - what you're actually allowed to do

Qwen sits at the `open_weights` tier: weights and a solid model card are Open, but training
data and training code are Closed and evaluation is only partially reproducible. The
license story is the good news - the **mainstream Qwen3 sizes are Apache-2.0**, OSI-approved
with unconditional commercial use, which is a genuine step up from the restrictive
"community" licenses several peers ship. One caveat: some historical or very-large variants
used the "Tongyi Qianwen" community license, so **verify the LICENSE file per checkpoint**
rather than assuming Apache across the board.

## 3. Provenance & supply-chain - can you trust the checkpoint?

Weights come from the **verified Qwen org on Hugging Face** in safetensors with checksums,
and are also officially published on Alibaba's own **ModelScope** hub. That dual publication
is a convenience and a supply-chain wrinkle: two canonical-ish sources mean you should
confirm checksums match across hubs and pin the exact revision you deployed. No malicious
incident is on record for the canonical org, but there is no cryptographic signing or SLSA
attestation, and a large community-quant surface (Ollama, GGUF re-uploads) exists off the
canonical path. Checkpoint trust checklist: 5/8.

## 4. EU AI Act & regulatory posture

This is where the grade is capped. Qwen is a GPAI family, and its **largest variants (235B
MoE, Qwen3-Coder-480B) likely exceed the 10²⁵-FLOPs systemic-risk threshold** - for which
the open-source exemption does not apply and the full Article 55 package (evaluation,
adversarial testing, systemic-risk mitigation, incident reporting) is owed. No such
documentation is published, which triggers the registry's systemic-risk hard flag and caps
the family at grade C. Even for the smaller, under-threshold Qwen3 sizes there is no public
copyright policy or training-content summary, and a China-based provider is unlikely to
furnish an EU AI Office package. An EU deployer of the small models inherits a permissive
license and a usable model card but must self-assemble the compliance file; a deployer of
the large variants faces a gap it cannot close from upstream artifacts.

## 5. Technical behaviour & benchmarks

On independent evaluation Qwen3 is strong across the board and **especially strong at
coding** - Qwen3-Coder ranks among the best open coding models and is competitive with much
larger systems on agentic/code tasks. General reasoning and multilingual performance are
solid for their size. Performance here is third-party framed, which is why capability stops
at a 4 rather than a 5. Behaviourally, watch for topic censorship on
politically sensitive subjects and standard prompt-injection susceptibility in tool-use
loops.

## 6. Safety & alignment

Instruct variants are safety-tuned and withstand casual jailbreaks, but alignment coverage
is lighter than Western frontier labs, there is no companion guard/classifier model, and the
models exhibit **China-aligned content filtering** that may or may not match your policy.
Treat built-in alignment as a starting point rather than a control; deploy behind your own
input and output guards.

## 7. Deploying it safely - the practical guideline

Model-specific gate rows: pull from the verified Qwen org (or official ModelScope) and
verify checksums match across hubs; pin the revision; deploy the Instruct variant behind
input/output guardrails plus a guard model; add prompt-injection defences before any
agentic/coding autonomy; note the China-origin provenance if your organisation restricts it
by policy (state neutrally); and for the systemic-risk large variants, either close the
Article 55 gap yourself or keep them out of EU high-stakes use.

**Deployment Ceiling: T3 (bounded autonomous), conditional.** With your own guards,
prompt-injection defences, a deterministic action-policy engine, rate/impact limits, and a
kill switch, Qwen - especially Qwen3-Coder - is a strong choice for bounded internal coding
and agentic workflows. **T4 / EU-high-stakes use is not recommended** without heavy
additional controls and, for the large variants, closing the EU compliance gap that the
publisher does not close for you.

## 8. Sources & evidence

1. Verified Qwen org on Hugging Face (safetensors, checksums) - `publisher` - https://huggingface.co/Qwen
2. Mainstream Qwen3 sizes under Apache-2.0 (verify per checkpoint) - `onehill_verified` - https://huggingface.co/Qwen
3. Official ModelScope publication (dual distribution) - `publisher` - https://modelscope.cn/organisation/qwen
4. No public training-content summary / copyright policy / Article 55 docs - `onehill_verified` - https://huggingface.co/Qwen
5. China-aligned topic censorship (behavioural) - `third_party` - https://huggingface.co/Qwen
6. Qwen3-Coder among the strongest open coding models - `third_party` - https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct
7. Broad serving-stack / ecosystem support - `third_party` - https://ollama.com/library/qwen3

---

_Scored against [rubric v1.0](../../methodology/scoring-rubric.md). Data:
[`data.yaml`](data.yaml). Disagree with a score? The rubric is public - open an issue._
