# Support - Ollama

_How do we keep it working and report problems? Known issues and caveats are documented here; security disclosure, release versioning and support channels are documented gaps below._

<!-- item: known-issues -->
## Known issues & caveats

The dominant caveat is **provenance**: no verified-org identity, no documented scanning and
no documented signing, so SHA256 addressing buys you **integrity, not authenticity**. The
second is the **GGUF Jinja2 chat template**, which can carry **server-side template injection
/ inference-time backdoors** even though GGUF itself is data-only and safe to load. Practical
discipline: **inspect chat templates** before serving untrusted models, prefer the official
library or known publishers, and **cross-check checksums** against a canonical source.
