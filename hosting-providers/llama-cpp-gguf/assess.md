# Assess - llama.cpp / GGUF

_Provenance, format and loader safety, licence governance, security record and trust signals, with the provider AOI score._

<!-- item: provenance-integrity -->
## Provenance & integrity

llama.cpp / GGUF is a serving engine and container format and not a hub, so it carries no native provenance: no verified organisations, no malware scanning, and no cryptographic signing or attestation of the artifact. Nothing intrinsic to a `.gguf` file says who produced it or whether it was tampered with.

Integrity rests on two external things: the checksums of the source hub (usually Hugging Face) and the deployer's revision-pinning discipline. A community-uploaded GGUF is untrusted third-party software. Pull from the model's canonical publisher or a reputable quantizer, and verify the SHA256 against the exact source revision.

<!-- item: format-safety -->
## Format & loader safety

GGUF is tensor data plus metadata with no pickle-style code execution on load, which is a safety plus over pickle. The loaders still have an exploited weakness history:

1. Chat-template SSTI → RCE: CVE-2024-34359 ("Llama Drama"), a Jinja2 server-side template injection in the GGUF chat template, reached remote code execution in llama-cpp-python 0.2.30 to 0.2.71 and is patched in 0.2.72. JFrog states no code execution occurs on >= 0.2.72 or in other GGUF libraries such as ollama. The same bug class hit SGLang as CVE-2026-5760 (`/v1/rerank`, fixed in SGLang 0.5.11), a separate flaw in a separate project.
2. Poisoned-template inference-time backdoors: malicious instructions embedded in the template layer execute on every prompt, beyond the initial load.
3. Loader memory safety: `gguf_init_from_file()` historically did not validate `n_kv`, so a crafted file could cause a heap overflow (one of several GGUF parsing bugs documented by JFrog, huntr and ProtectAI). The class keeps recurring in llama.cpp. CVE-2026-27940 and CVE-2026-33298 date from March 2026, and CVE-2026-116829, CVE-2026-116840 and CVE-2026-116816 from October 2026 (fixed in b11301, b11275 and b10261). On 2026-11-13 the Zero Day Initiative published ZDI-26-975, ZDI-26-976 and ZDI-26-954 (CVE-2026-126974, -126975, -126976), GGUF and multimodal-projector parsing bugs rated remote code execution (user interaction required). ZDI states llama.cpp issued an update.

Keeping loaders current and inspecting templates keeps this safe; the format alone does not. The project's SECURITY.md says there are "no reliable methods to detect malicious models" and recommends sandboxing.

<!-- item: license-governance -->
## License surfacing & governance

The engine is plain MIT ("Copyright (c) 2023-2026 The ggml authors"), which covers the code only. The engine and format surface and enforce no license for the weights. Whatever license and gating attach to the weights come from wherever the GGUF was obtained, typically a Hugging Face repo.

On its own that is minimal governance: there is no click-through, no access request and no EULA enforcement at the llama.cpp / GGUF layer. License compliance is the deployer's responsibility relative to the upstream source.

<!-- item: security-record -->
## Security track record

Much local-inference security research concentrates on the GGUF ecosystem. The flagship template incident is CVE-2024-34359, the chat-template SSTI leading to RCE in llama-cpp-python < 0.2.72, patched in 0.2.72. CVE-2026-5760 is the same class in SGLang. A continuing class of GGUF file-format parsing vulnerabilities affects llama.cpp itself. NVD published about thirty llama.cpp and GGUF CVEs between March and November 2026, and ZDI issued two RCE ratings on 2026-11-13.

Most fixes land within days of a report. Two things weaken the record. The project disabled its private disclosure channel on 2026-06-01 (reporters are told to send public PRs), and its GitHub advisory feed stops at 2026-03-26, so the first-party list no longer matches NVD. One ZDI report also took about five months from report to publication.

The format is safe by design but demands version and template discipline, because the data-only design does not neutralise template injection or loader memory bugs.

<!-- item: transparency -->
## Transparency & trust signals

llama.cpp is fully open-source (plain MIT) and auditable, and the security research on GGUF is public. The artifact itself exposes no provenance signal of its own. A downloader must reason about trust entirely from the external source (source-hub provenance, which is gameable if the hub's signals are) and from informal quantizer reputation (bartowski, unsloth, etc.), which is community reputation and not a verified identity.

ggml and llama.cpp joined Hugging Face on 2026-02-20. The core maintainers are employed there with, per the announcement, "full autonomy and leadership on the technical directions". The licence is plain MIT. The GGUF specification is one Markdown file in the ggml repository (format version 3, last edited 2026-11-08) and has no separate standards body.
