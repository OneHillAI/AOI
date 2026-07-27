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

1. **Chat-template SSTI → RCE** - CVE-2026-5760, a Jinja2 server-side template injection in the
   GGUF chat template, reached remote code execution in **llama-cpp-python < 0.2.72** (and also
   affected SGLang); it is patched in **>= 0.2.72**.
2. **Poisoned-template inference-time backdoors** - malicious instructions embedded in the
   template layer execute on **every prompt**, beyond the initial load.
3. **Loader memory safety** - `gguf_init_from_file()` historically did not validate `n_kv`, so a
   crafted file could cause a **heap overflow** (one of several GGUF parsing bugs documented by
   JFrog / huntr / ProtectAI).

The practical takeaway: pinning loader versions and inspecting templates keep this safe; the
format alone does not.

<!-- item: license-governance -->
## License surfacing & governance

The engine and format **surface and enforce no license of their own**. Whatever license and
gating attach to the weights are **inherited from wherever you obtained the GGUF** - typically a
Hugging Face repo. On its own that is minimal governance: there is no click-through, no access
request, and no EULA enforcement at the llama.cpp / GGUF layer, so license compliance is your
responsibility relative to the upstream source.

<!-- item: security-record -->
## Security track record

The GGUF ecosystem is where much local-inference **security research is concentrated**. The
flagship incident is **CVE-2026-5760**, the chat-template SSTI leading to RCE in
llama-cpp-python < 0.2.72 (and SGLang) - the most prominent GGUF loader RCE to date - patched
promptly in >= 0.2.72. Alongside it sits a class of **GGUF file-format parsing vulnerabilities**
(e.g. the `gguf_init_from_file` heap overflows) documented by huntr/JFrog. The record reads as a
format that is safe by design yet **demands version and template discipline**: bugs are found and
fixed, but the data-only design does not neutralise template-injection or loader memory bugs.

<!-- item: transparency -->
## Transparency & trust signals

The strongest transparency point is that **llama.cpp is fully open-source and independently
auditable**, and the security research on GGUF is public. The counterweight is that the
**artifact itself exposes no provenance signal of its own** - a downloader must reason about
trust entirely from the external source (source-hub provenance, which is gameable if the hub's
signals are) and from **informal quantizer reputation** (bartowski, unsloth, etc.), which is
community reputation rather than a verified identity.
