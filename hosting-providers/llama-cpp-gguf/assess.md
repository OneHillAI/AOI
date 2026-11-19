# Assess - llama.cpp / GGUF

_Can we trust weights obtained here? Provenance, format & loader safety, license governance,
security record, and transparency - plus the provider score (56.4/100 · Grade C) - live here._

<!-- item: provenance-integrity -->
## Provenance & integrity

llama.cpp / GGUF is a **serving engine and container format, not a hub**, and as such it
carries **no native provenance**: no verified organisations, no malware scanning, and no
cryptographic signing or attestation of the artifact. There is nothing intrinsic to a `.gguf`
file that tells you who produced it or whether it was tampered with.

Integrity therefore rests entirely on two external things: the **checksums of the source hub**
you pulled from (usually Hugging Face) and **your own revision-pinning discipline**. Treat a
community-uploaded GGUF as untrusted third-party software - pull from the model's canonical
publisher or a reputable quantizer, and verify the SHA256 against the exact source revision.

<!-- item: format-safety -->
## Format & loader safety

GGUF's design is a **genuine safety plus over pickle**: it is tensor data plus metadata with
**no pickle-style code-execution on load**. But "no code-exec on load" is not "safe", because
the loaders have a real, exploited weakness history:

1. **Chat-template SSTI → RCE** - **CVE-2024-34359** ("Llama Drama"), a Jinja2 server-side
   template injection in the GGUF chat template, reached remote code execution in
   **llama-cpp-python 0.2.30 to 0.2.71**; it is patched in **0.2.72**. JFrog states no code
   execution occurs on >= 0.2.72 or in other GGUF libraries such as ollama. The same bug class
   hit SGLang as **CVE-2026-5760** (`/v1/rerank`, fixed in SGLang 0.5.11); that is a separate
   flaw in a separate project. An earlier version of this entry attached CVE-2026-5760 to
   llama-cpp-python, which was wrong.
2. **Poisoned-template inference-time backdoors** - malicious instructions embedded in the
   template layer execute on **every prompt**, beyond the initial load.
3. **Loader memory safety** - `gguf_init_from_file()` historically did not validate `n_kv`, so a
   crafted file could cause a **heap overflow** (one of several GGUF parsing bugs documented by
   JFrog / huntr / ProtectAI). The class has kept recurring in llama.cpp: CVE-2026-27940 and
   CVE-2026-33298 (March 2026), CVE-2026-116829, CVE-2026-116840 and CVE-2026-116816 (October
   2026, fixed in b11301, b11275 and b10261), and on 2026-11-13 the Zero Day Initiative published
   ZDI-26-975, ZDI-26-976 and ZDI-26-954 (CVE-2026-126974, -126975, -126976), GGUF and
   multimodal-projector parsing bugs rated **remote code execution** (user interaction required;
   ZDI states llama.cpp issued an update).

The practical takeaway: keeping loaders current and inspecting templates keep this safe; the
format alone does not. The project's own SECURITY.md says there are "no reliable methods to
detect malicious models" and recommends sandboxing.

<!-- item: license-governance -->
## License surfacing & governance

The engine itself is plain **MIT** ("Copyright (c) 2023-2026 The ggml authors", raw LICENSE read
2026-11-19), which covers the code only. The engine and format **surface and enforce no license for
the weights**. Whatever license and
gating attach to the weights are **inherited from wherever you obtained the GGUF** - typically a
Hugging Face repo. On its own that is minimal governance: there is no click-through, no access
request, and no EULA enforcement at the llama.cpp / GGUF layer, so license compliance is your
responsibility relative to the upstream source.

<!-- item: security-record -->
## Security track record

The GGUF ecosystem is where much local-inference **security research is concentrated**. The
flagship template incident is **CVE-2024-34359**, the chat-template SSTI leading to RCE in
llama-cpp-python < 0.2.72, patched in 0.2.72; **CVE-2026-5760** is the same class in SGLang.
Alongside them sits a continuing class of **GGUF file-format parsing vulnerabilities** in
llama.cpp itself, with about thirty llama.cpp and GGUF CVEs published in NVD between March and
November 2026 and two ZDI RCE ratings on 2026-11-13. Most fixes land within days of a report, but
two things weaken the record: the project **disabled its private disclosure channel on
2026-06-01** (reporters are told to send public PRs) and its GitHub advisory feed **stops at
2026-03-26**, so the first-party list no longer matches NVD; and one ZDI report took about five
months from report to publication. The record reads as a format that is safe by design yet
**demands version and template discipline**: the data-only design does not neutralise template
injection or loader memory bugs.

<!-- item: transparency -->
## Transparency & trust signals

The strongest transparency point is that **llama.cpp is fully open-source (plain MIT) and
independently auditable**, and the security research on GGUF is public. The counterweight is that the
**artifact itself exposes no provenance signal of its own** - a downloader must reason about
trust entirely from the external source (source-hub provenance, which is gameable if the hub's
signals are) and from **informal quantizer reputation** (bartowski, unsloth, etc.), which is
community reputation rather than a verified identity.

**Governance note (2026-11-19).** ggml and llama.cpp joined Hugging Face on 2026-02-20; the core
maintainers are employed there with, per the announcement, "full autonomy and leadership on the
technical directions". The licence is unchanged. The GGUF specification lives as one Markdown file
in the ggml repository (format version 3, last edited 2026-11-08) and has no separate standards
body.
