# Ollama - OneHill Hosting-Provider Dossier

> **Score: 55.2/100 · Grade C** · Type: local_runner · safetensors default: n/a (GGUF) · Signing: none documented
> Last verified: 2026-07-25
>
> _A convenient local runner on a safer-by-design format (GGUF), but you must bring your own provenance: no verified publishers, no documented scanning, no documented signing - SHA256 gives integrity, not authenticity._

**Hard flags:** none

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Provenance & Integrity | 2/5 | No verified orgs, no documented scanning or signing; hashing proves integrity, not authorship |
| Format & Loader Safety | 4/5 | GGUF is data-only and Ollama dodged CVE-2026-5760, but chat-template injection surface exists |
| License Surfacing & Governance | 2/5 | License viewable via `ollama show --license`, but no gating and no enforcement |
| Security Track Record | 3/5 | Few documented incidents - but partly because provenance tooling is weak |
| Transparency & Trust Signals | 2/5 | Only namespace + library curation exposed; no verified identity or scan results |
| Ecosystem & Portability | 4/5 | Huge local ecosystem on the portable GGUF format; Modelfile layout is Ollama-specific |

## 1. How weights are distributed & installed

Ollama runs models locally and distributes them through a content-addressable, OCI-like
registry of manifests and SHA256-addressed blobs. `ollama pull` resolves a **Modelfile** -
a recipe combining base weights, a chat template, parameters and an optional system
prompt - downloads the referenced **GGUF** blob, and caches it. `ollama run` then serves
it on localhost. You can build custom models with a Modelfile and `ollama create`,
including wrapping a GGUF you obtained elsewhere. The appeal is real: one command from
nothing to a running local model.

## 2. Provenance - verified orgs, signing, scanning, checksums, gating

This is the weak spot. There is **no verified-publisher identity** comparable to a Hugging
Face blue badge that could be confirmed - trust rests on namespace ownership alone.
**No GGUF-level malware scanning is documented**, and **no cryptographic signing or
identity verification is documented**. Both are recorded here as *not documented* rather
than proven-absent, but for an adopter the practical effect is the same: you cannot lean
on the platform to vouch for who made a model. The one integrity guarantee is that blobs
are **SHA256-addressed** - which proves the bytes you received match the manifest
(**integrity**) but says nothing about who published them (**authenticity**). There is no
license gating in the CLI flow.

## 3. Format & loader safety

The format choice is a genuine advantage. **GGUF is data-only**: unlike pickle, loading it
does not execute arbitrary code, so the single highest-impact supply-chain risk (code
execution on load) does not apply. **Ollama is NOT vulnerable to
CVE-2026-5760**, the llama-cpp-python GGUF chat-template RCE, because it does not use that
Python binding. That is why this dimension scores well.

It is not risk-free, which is why it is a 4 and not a 5. A malicious GGUF's **Jinja2 chat
template** can cause **server-side template injection** and **inference-time backdoors**
(malicious instructions in the template layer that run on every prompt), and malformed
GGUF headers can trigger loader memory bugs. Ollama does not automatically inspect or
block templates in pulled models, so this surface is left to the operator.

## 4. Security track record

There are **fewer documented malicious-upload incidents** than on the large public hubs.
**Weaker provenance tooling** explains the gap; the surface itself is not demonstrably
cleaner. With no verified-org identity, no documented scanning and no signing, malicious
content would be harder to detect and attribute in the first place - so the absence of
reports is, in part, an absence of detection. That reasoning holds this dimension at the
middle anchor rather than higher.

## 5. Pulling from it safely - the practical guideline

- **Prefer the official Ollama library or known publishers.** Namespace ownership is not
  an identity badge; treat unknown namespaces as untrusted third-party software.
- **Cross-check the checksum against a canonical source.** Where the same model exists on
  the publisher's Hugging Face repo, verify the pulled GGUF's SHA256 against it - remember
  content-addressing gives integrity, not authenticity.
- **Inspect the chat template before serving untrusted GGUFs.** `ollama show` the model
  and read the template; template injection runs at inference time, on every prompt.
- **Sandbox the server.** Run `ollama serve` with least privilege and no unnecessary
  network exposure, especially for community models.
- **Record what you pulled** - model, digest, source - in your AI-BOM, since the platform
  will not attest provenance for you.

## 6. Sources & evidence

- DeepWiki (third-party) - Ollama model management: OCI-like registry, Modelfile, SHA256 blobs, `ollama show --license`.
- zohaib.me (third-party) - running custom/community GGUFs relies on user-supplied provenance.
- ProtectAI GGUF-101 (third-party) - GGUF is data-only; deserialization threat model.
- JFrog / NeuralTrust (third-party) - GGUF chat-template SSTI and inference-time template risks.

---

_Scored against [provider rubric v1.0](../../methodology/provider-scoring-rubric.md).
Data: [`data.yaml`](data.yaml)._
