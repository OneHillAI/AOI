# Assess - Ollama

_Provenance, format and loader safety, licence governance, security record and trust signals, with the provider AOI score._

<!-- item: provenance-integrity -->
## Provenance & integrity signals

Provenance is Ollama's weak spot. There is no verified-publisher identity comparable to a
Hugging Face blue badge, no documented GGUF-level malware scanning of registry content, and no
signing that has shipped (PR #11573 is open, last updated 2026-09-08). Any user can push a
model under a username.

SHA256 content-addressing proves the blob pulled is the blob that was published. That is
integrity, not authenticity: it shows the bytes are intact, not who authored them. Provenance
discipline therefore falls on the operator, who should prefer the official library or known
publishers and cross-check against a canonical source.

<!-- item: format-safety -->
## Format & loader safety

GGUF and the safetensors-derived MLX layers are data-only and cannot execute code on load the
way pickle can. Ollama's own loader is not clean, though. CVE-2026-7482 is a critical
(CVSS 9.1) heap out-of-bounds read in the GGUF loader and quantiser, fixed in 0.17.1 per NVD.
CERT/CC lists a similar CVE-2026-5757 with no vendor status. CVE-2026-5760 is an SGLang flaw,
not an Ollama one.

A malicious GGUF Jinja2 chat template can also cause server-side template injection and
inference-time backdoors, so inspect the chat template before serving anything untrusted.

<!-- item: license-governance -->
## License surfacing & gating

The software is MIT-licensed. Each library model ships its licence text as a registry layer
(Apache-2.0 for qwen3.8, gemma4 and gpt-oss; the Llama 3.3 and Llama 4 community licences for
those models), viewable with `ollama show --license`. Enforcement is minimal: there is no
click-through and no access-request flow, and the Terms say nothing about model licences or
user-uploaded models, so acceptance is on the operator's honour. Surfacing is adequate;
governance is not.

<!-- item: security-record -->
## Security incident history & response

No malicious-model incident on ollama.com is known, but that is not evidence of a clean
surface: with no verified-org identity, no documented scanning and no signing, such content
would be harder to detect and attribute.

The tool's own 2026 record is serious: a critical GGUF loader CVE (7482), an unresolved similar
CVE (5757), SSRF on the pull path (5530, 85180) and two Windows updater CVEs (42248, 42249).
Four CVE records say the vendor did not respond, release notes do not flag the fixes, no GitHub
security advisory is published and `ollama.com/security` returns 404. Current code contains
fixes for the updater and the tensor-layer redirect, which keeps the score at 2, not 1.

<!-- item: transparency -->
## Exposed trust signals & their gameability

A puller sees very little to assess. The only exposed signals are the registry namespace (any
user can push under a username), official-library curation (not a per-publisher verification or
a scan result) and the licence text layer. There is no trust centre, security page, DPA,
sub-processor list or certification.

For `:cloud` models, the binding Privacy Policy promises transient processing and no training.
The "zero data retention" wording in the docs and pricing page is stronger than that and is not
backed by a published agreement.
