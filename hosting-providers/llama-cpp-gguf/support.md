# Support - llama.cpp / GGUF

_How do we keep it working and report problems? Security disclosure, release/versioning,
community channels, and known issues live here._

<!-- item: security-disclosure -->
## Security disclosure

The GGUF format specification has no disclosure policy of its own, but the llama.cpp engine does:
`SECURITY.md` defines the covered code (`src`, `ggml`, `gguf-py`, parts of `tools/server`), requires
a working proof of concept, asks for 90 days before public exposure, does not accept reports written
only by AI, and treats denial-of-service bugs as generally not vulnerabilities. Since **2026-06-01**
the private disclosure programme is **disabled**: the file says to submit fixes as public PRs and
that emails will be ignored. GGUF loader bugs are therefore also reaching the public through
third-party programmes and researchers (ZDI, VulnCheck, huntr, JFrog). The project's GitHub advisory
feed has not been updated since 2026-03-26.

<!-- item: release-versioning -->
## Release & versioning

llama.cpp ships **rolling build tags (bNNNN)** as GitHub pre-releases, about 20 to 30 a day (newest
read on 2026-11-19: b12550). On **2026-11-13** it released **v1.0.0** (with ggml v1.0.0) and adopted
semantic versioning: a breaking change to the public C API bumps the major version, features and
backend or model additions bump the minor version, bug fixes bump the patch version. ggml releases
run roughly weekly to fortnightly (v0.26.0 on 2026-10-05 to v0.29.0 on 2026-11-04). Version
discipline is **security-relevant**: NVD still tracks llama.cpp fixes by build tag, and the
chat-template SSTI RCE was fixed in **`llama-cpp-python >= 0.2.72`** (separate project; 0.3.37 on
2026-11-15). The GGUF format itself is at **format version 3** and was not revised in 2026; there is
no formal release-cadence policy for it.

<!-- item: channels -->
## Community & support channels

Support is **community-driven**: the open-source project on GitHub (issues, discussions; core
maintainers employed by Hugging Face since February 2026, and `CONTRIBUTING.md` asks contributors to
disclose AI use and include regression tests for bug fixes) plus the
informal community of quantizers (bartowski, unsloth) who publish and maintain prebuilt GGUFs.
There is **no formal support SLA** - help is best-effort from the project and community.

<!-- item: known-issues -->
## Known issues & caveats

The tracked caveats are the security ones already established elsewhere in this entry:

- **Chat-template SSTI → RCE** (CVE-2024-34359) in llama-cpp-python < 0.2.72 - fix by upgrading.
  CVE-2026-5760 is the same class in SGLang (< 0.5.11), not in llama.cpp.
- **Poisoned-template inference-time backdoors** that run on every prompt - inspect templates.
- **GGUF parser overflows** (`gguf_init_from_file` n_kv in 2024, `gguf_init_from_reader` in
  October 2026, and two ZDI-rated RCE bugs published 2026-11-13) - keep llama.cpp current and sandbox.

The common mitigations are consistent: keep loaders current, inspect templates before serving, and
sandbox the loader.
