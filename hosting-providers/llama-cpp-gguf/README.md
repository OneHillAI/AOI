# llama.cpp / GGUF - OneHill Hosting-Provider Dossier

> **Score: 56.4/100 · Grade C** · Type: serving_engine · safetensors default: n/a (GGUF) · Signing: none native
> Last verified: 2026-11-19
>
> _A maximally portable, safe-by-design local format. The engine carries no provenance of its own and its loaders have a live RCE history, so safety depends on source discipline and version and template hygiene._

**Hard flags:** none

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Provenance & Integrity | 2/5 | Format/engine has no native verified orgs, scanning or signing; these depend on the source hub |
| Format & Loader Safety | 3/5 | GGUF data-only is a plus, but real SSTI RCE + heap-overflow loader history means pin versions |
| License Surfacing & Governance | 2/5 | Surfaces nothing itself; license and gating depend on where the GGUF came from |
| Security Track Record | 3/5 | Documented loader CVEs concentrate here, but are actively researched and promptly patched |
| Transparency & Trust Signals | 3/5 | Fully open-source, auditable engine, but the artifact exposes no provenance signal of its own |
| Ecosystem & Portability | 5/5 | The de facto local-inference standard; maximally portable, open tooling |

## 1. How weights are distributed & installed

llama.cpp is a serving engine and not a hub. GGUF is its single-file container (weights + tokenizer + metadata + chat template). Weights come from elsewhere, usually a Hugging Face repo, and are converted to GGUF with `convert_hf_to_gguf.py`, quantized with `llama-quantize` (Q4_K_M, Q5_K_M, Q8_0, and others) and run with `llama-cli` or `llama-server`.

Community quantizers such as bartowski and unsloth publish large libraries of prebuilt GGUFs on HF that most people download directly. The engine and format supply the mechanics, and the provenance comes from wherever the GGUF originated.

## 2. Provenance - verified orgs, signing, scanning, checksums, gating

GGUF/llama.cpp has no verified orgs, no malware scanning in the format itself, and no native signing or attestation. Integrity and gating come from the source hub. A file pulled from a verified Hugging Face org with checksums and a commit hash carries that hub's guarantees. A random community GGUF carries whatever its source offered.

Revision pinning and checksums are available through the source, but the artifact carries no provenance metadata of its own. That is why this dimension sits below the score-3 anchor, which expects verified orgs plus scanning at the distribution layer.

## 3. Format & loader safety

GGUF is tensor + metadata with no pickle-style code execution on load. That is a safety plus over pickle and the reason this scores at the middle anchor and not lower. A data-only format does not make the loader safe, and the CVE history is concrete:

1. CVE-2024-34359 is a GGUF chat-template Jinja2 SSTI leading to RCE in llama-cpp-python 0.2.30 to 0.2.71, patched in 0.2.72. CVE-2026-5760 is the same class in SGLang < 0.5.11, a separate flaw.
2. Poisoned-template inference-time backdoors embed malicious instructions in the template layer that execute on every prompt, beyond the initial load.
3. Loader memory safety: `gguf_init_from_file()` historically did not validate `n_kv`, so a crafted file could cause a heap overflow. JFrog, huntr and ProtectAI have documented multiple GGUF parsing bugs. The class keeps recurring (March and October 2026 CVEs). The Zero Day Initiative published two GGUF-parsing bugs as RCE on 2026-11-13 (CVE-2026-126974, CVE-2026-126975) plus one for multimodal-projector GGUF files (CVE-2026-126976).

Safety is conditional on keeping loaders patched and inspecting templates, and is not intrinsic to the format. The project says there is no reliable way to detect a malicious model and recommends sandboxing.

## 4. Security track record

Much local-inference security research concentrates on the GGUF ecosystem. Real vulnerabilities (the SSTI RCE, the parsing and heap-overflow class) surface here, are actively hunted and are usually fixed quickly. The flagship template CVE was patched in llama-cpp-python 0.2.72.

Two weaknesses remain. llama.cpp disabled its private disclosure channel on 2026-06-01, and its GitHub advisory feed stops at 2026-03-26 while NVD lists about thirty later llama.cpp and GGUF CVEs. Community-uploaded GGUFs are untrusted third-party software, because the format's data-only design does not neutralise template injection or loader memory bugs. That balance places this dimension at the middle anchor.

## 5. Pulling from it safely - the practical guideline

- Prefer GGUFs from the model's canonical publisher or a reputable quantizer (bartowski, unsloth) over anonymous uploads.
- Record the exact source repo commit and verify the SHA256, because the GGUF does not say where it came from.
- Keep `llama-cpp-python >= 0.2.72` (and current llama.cpp) to close the chat-template SSTI RCE (CVE-2024-34359) and recent GGUF parser fixes.
- Inspect the chat template and tokenizer config before serving. Template injection runs at inference time on every prompt; check it against known-malicious signatures where feasible. This is the most neglected GGUF control.
- Sandbox the loader with no network and least privilege, especially for community files.
- Record source, revision, quant and result in the AI-BOM.

## 6. Sources & evidence

- ggml-org/llama.cpp (publisher) - engine, GGUF format and conversion/quantization workflow.
- JFrog research (third-party) - GGUF chat-template SSTI → RCE (CVE-2024-34359).
- gbhackers, NVD and CERT/CC (third-party) - the SGLang GGUF template RCE (CVE-2026-5760) and the NVD record of llama.cpp and GGUF CVEs.
- Zero Day Initiative (third-party) - ZDI-26-975, ZDI-26-976, ZDI-26-954 GGUF parsing RCE advisories.
- ggml-org SECURITY.md, LICENSE, GGUF spec, v1.0.0 release notes (publisher).
- huntr (third-party) - GGUF file-format parsing vulnerabilities incl. `gguf_init_from_file` heap overflows.
- Pillar Security (third-party) - inference-level backdoors via poisoned templates.

---

_Scored against [provider rubric v1.0](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
