# llama.cpp / GGUF - OneHill Hosting-Provider Dossier

> **Score: 56.4/100 · Grade C** · Type: serving_engine · safetensors default: n/a (GGUF) · Signing: none native
> Last verified: 2026-07-25
>
> _A great, maximally-portable, safe-by-design local format - but the engine carries no provenance of its own, and its loaders have live RCE history, so safety comes entirely from your source discipline and version/template hygiene._

**Hard flags:** none

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Provenance & Integrity | 2/5 | Format/engine has no native verified orgs, scanning or signing; all inherited from the source hub |
| Format & Loader Safety | 3/5 | GGUF data-only is a plus, but real SSTI RCE + heap-overflow loader history means pin versions |
| License Surfacing & Governance | 2/5 | Surfaces nothing itself; license and gating inherited from wherever you got the GGUF |
| Security Track Record | 3/5 | Documented loader CVEs concentrate here, but are actively researched and promptly patched |
| Transparency & Trust Signals | 3/5 | Fully open-source, auditable engine - but the artifact exposes no provenance signal of its own |
| Ecosystem & Portability | 5/5 | The de facto local-inference standard; maximally portable, open tooling |

## 1. How weights are distributed & installed

llama.cpp is a **serving engine**, not a hub, and **GGUF** is its single-file container
(weights + tokenizer + metadata + chat template). The normal workflow: get weights
elsewhere - usually a Hugging Face repo - **convert** to GGUF with `convert_hf_to_gguf.py`,
**quantize** with `llama-quantize` (Q4_K_M, Q5_K_M, Q8_0, and friends), and **run** with
`llama-cli` or `llama-server`. Because conversion and quantization are commodity
operations, community quantizers such as **bartowski** and **unsloth** publish large
libraries of prebuilt GGUFs on HF that most people download directly. The consequence:
the engine/format supplies the *mechanics*, but the *provenance* comes entirely from
wherever the GGUF originated.

## 2. Provenance - verified orgs, signing, scanning, checksums, gating

Natively, there is essentially none. GGUF/llama.cpp has **no verified orgs**, **no malware
scanning in the format itself**, and **no native signing or attestation**. Integrity and
gating are **inherited** from the source hub - if you pulled from a verified Hugging Face
org with checksums and a commit hash, you get that hub's guarantees; if you pulled a
random community GGUF, you get whatever that source offered. Revision pinning and
checksums are therefore available *in principle* (via the source), but the artifact you
hold carries no provenance metadata of its own. That is why this dimension sits below the
score-3 anchor, which expects verified orgs plus scanning at the distribution layer.

## 3. Format & loader safety

GGUF is **tensor + metadata with no pickle-style code execution on load** - a real safety
plus over pickle, and the reason this scores at the middle anchor rather than lower. But
"data-only format" does not mean "safe loader," and the CVE history is concrete:

1. **CVE-2026-5760** - a GGUF **chat-template Jinja2 SSTI** leading to **RCE** in
   **llama-cpp-python < 0.2.72** (also affecting SGLang), patched in ≥ 0.2.72.
2. **Poisoned-template inference-time backdoors** - malicious instructions embedded in the
   template layer that execute on **every prompt**, beyond the initial load.
3. **Loader memory safety** - `gguf_init_from_file()` historically did not validate `n_kv`,
   so a crafted file could cause a **heap overflow**; JFrog, huntr and ProtectAI have
   documented multiple GGUF parsing bugs.

The takeaway: the safety is conditional on keeping loaders patched and inspecting
templates, not intrinsic to the format.

## 4. Security track record

The GGUF ecosystem is where much local-inference security research is concentrated - which
cuts both ways. It means real vulnerabilities (the SSTI RCE, the parsing/heap-overflow
class) surface here, but also that they are actively hunted and promptly fixed: the
flagship CVE was patched in ≥ 0.2.72. The correct posture is to treat any
community-uploaded GGUF like untrusted third-party software; the format's data-only design
does not neutralize template injection or loader memory bugs. That balance places this
dimension at the middle anchor.

## 5. Pulling from it safely - the practical guideline

- **Source it well.** Prefer GGUFs from the model's **canonical publisher** or a
  **reputable quantizer** (bartowski, unsloth) over anonymous uploads.
- **Pin and hash the source revision.** Record the exact source repo commit and verify
  **SHA256** - the GGUF itself won't tell you where it came from.
- **Keep `llama-cpp-python >= 0.2.72`** (and current llama.cpp) to close the chat-template
  SSTI RCE.
- **INSPECT the chat template / tokenizer config before serving.** Template injection runs
  at inference time on every prompt; check it against known-malicious signatures where
  feasible. This is the single most under-appreciated GGUF control.
- **Sandbox the loader** - no network, least privilege - especially for community files.
- **Record source, revision, quant and result** in your AI-BOM.

## 6. Sources & evidence

- ggml-org/llama.cpp (publisher) - engine, GGUF format and conversion/quantization workflow.
- JFrog research (third-party) - GGUF chat-template SSTI → RCE (CVE-2026-5760).
- gbhackers (third-party) - malicious GGUF models triggering RCE.
- huntr (third-party) - GGUF file-format parsing vulnerabilities incl. `gguf_init_from_file` heap overflows.
- Pillar Security (third-party) - inference-level backdoors via poisoned templates.

---

_Scored against [provider rubric v1.0](../../methodology/provider-scoring-rubric.md).
Data: [`data.yaml`](data.yaml)._
