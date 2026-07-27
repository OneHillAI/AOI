# Support - llama.cpp / GGUF

_How do we keep it working and report problems? Security disclosure, release/versioning,
community channels, and known issues live here._

<!-- item: security-disclosure -->
## Security disclosure

There is no first-party formal vulnerability-disclosure policy surfaced for the GGUF format
itself. In practice, GGUF loader and format vulnerabilities are **disclosed through community
security platforms such as huntr** and through **research firms (JFrog / ProtectAI)** - that is
how the parsing bugs and the SSTI RCE reached the public. For a suspected malicious model or a
new loader bug, the realistic path is the project's GitHub and these security-research venues
rather than a standing first-party security channel.

<!-- item: release-versioning -->
## Release & versioning

llama.cpp is **versioned on GitHub** as an open-source project. Version discipline here is
directly **security-relevant**: the chat-template SSTI RCE was fixed in
**`llama-cpp-python >= 0.2.72`**, so tracking releases and staying current is part of your
security posture, beyond ordinary feature hygiene. The format has no formal release-cadence
/ changelog policy.

<!-- item: channels -->
## Community & support channels

Support is **community-driven**: the open-source project on GitHub (issues, discussions) plus the
informal community of quantizers (bartowski, unsloth) who publish and maintain prebuilt GGUFs.
There is **no formal support SLA** - help is best-effort from the project and community.

<!-- item: known-issues -->
## Known issues & caveats

The tracked caveats are the security ones already established elsewhere in this entry:

- **Chat-template SSTI → RCE** (CVE-2026-5760) in llama-cpp-python < 0.2.72 - fix by upgrading.
- **Poisoned-template inference-time backdoors** that run on every prompt - inspect templates.
- **`gguf_init_from_file` heap-overflow** parsing bugs from unvalidated header fields - pin loader
  versions and sandbox.

The common mitigations are consistent: pin loader versions, inspect templates before serving, and
sandbox the loader.
