# Assess - Ollama

_Can we trust weights obtained here? Provenance, format/loader safety, license governance, security history and the exposed trust signals - plus the provider score (55.2/100 · Grade C) - live here._

<!-- item: provenance-integrity -->
## Provenance & integrity signals

Provenance is Ollama's **weak spot**. There is **no verified-publisher identity** comparable
to a Hugging Face blue badge, **no documented GGUF-level malware scanning** of registry
content, and **no documented cryptographic signing**. What you do get is **SHA256
content-addressing**: the blob you pulled is provably the blob that was published. That is
**integrity, not authenticity** - it proves the bytes are intact, not who authored
them. Provenance discipline therefore falls on the operator: prefer the official library or
known publishers and cross-check against a canonical source.

<!-- item: format-safety -->
## Format & loader safety

The artifact format is a genuine safety advantage. **GGUF is data-only** and cannot execute
code on load the way pickle can, and **Ollama is NOT exposed to the llama-cpp-python
GGUF RCE (CVE-2026-5760)** because it does not use that Python binding. It is not risk-free,
though: a malicious **GGUF Jinja2 chat template** can cause **server-side template injection
/ inference-time backdoors**, and a malformed GGUF header can trigger a loader memory bug.
Pulled models are not automatically inspected for this, so **inspect the chat template**
before serving anything untrusted.

<!-- item: license-governance -->
## License surfacing & gating

License text **ships inside the model** and is viewable with **`ollama show --license`**.
Enforcement, however, is minimal: there is **no click-through gating and no access-request
flow**, so license acceptance is entirely on the operator's honour rather than enforced by
the tool. Surfacing is adequate; governance is not.

<!-- item: security-record -->
## Security incident history & response

There are **few documented malicious-upload incidents** - but that is not evidence of a
clean surface. With **no verified-org identity, no documented scanning and no signing**,
malicious content would be **harder to detect and attribute** in the first place, so the
scarcity of reports partly reflects weak detection tooling rather than a stronger security
posture.

<!-- item: transparency -->
## Exposed trust signals & their gameability

A puller sees very little to assess. The **only exposed signals** are the **registry
namespace** (namespace ownership is not an identity badge) and **official-library curation**
(curation is not per-publisher verification or a scan result). Neither is a verified
identity or a published scan, so there is **little for a downloader to independently assess**
before pulling.
