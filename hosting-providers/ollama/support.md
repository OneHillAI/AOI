# Support - Ollama

_How do we keep it working and report problems? Known issues and caveats are documented here; security disclosure, release versioning and support channels are now documented._

<!-- item: security-disclosure -->
## Reporting malicious models & vulnerabilities

**`SECURITY.md`** asks reporters to open a vulnerability report through **GitHub security
advisories** and to give the team time to respond; the contact for other questions is
hello@ollama.com. No security page exists (**`ollama.com/security` returns 404**), there is no
bug bounty, and no route for reporting a **malicious model** in the registry is published
beyond the DMCA clause in the Terms. Several CVE records (CVE-2026-5530, CVE-2026-5757,
CVE-2026-42248 and the reporter of CVE-2026-85180) say the vendor did not respond, and no
GitHub security advisory has been published for any of them.

<!-- item: release-versioning -->
## Tooling versioning & changelog

Releases are on **GitHub**. At 2026-11-19 the latest stable is **v0.40.16 (2026-11-09)** with
**v0.40.17-rc1** (2026-11-10) as a pre-release; the v0.40 line began on 2026-09-25 and ships
one to four releases a week. Release notes are short feature lists with **no security
section** and have not flagged the 2026 security fixes (the v0.17.1 notes do not mention
CVE-2026-7482). A pre-0.40 client cannot select the new MLX builds and gets the llama.cpp GGUF
manifest; downgrading below 0.40 needs a re-pull of upgraded models. We found no official
statement about v0.30.10 refusing new models; the registry behaviour that would explain it is
recorded in the primary-source folder.

<!-- item: channels -->
## Community & support channels

The project has **GitHub issues**, a **Discord**, an **X account**, a **Support** link and
**support@ollama.com** for accounts and billing. The community is large. No support
commitment is published for the free tier; the Team plan lists priority support and the
Enterprise plan a private Slack channel and custom security questionnaires.

<!-- item: known-issues -->
## Known issues & caveats

The dominant caveats are **provenance** (no verified-org identity, no documented scanning, no
shipped signing, so SHA256 gives **integrity, not authenticity**) and the **tool's own
security record** (a critical GGUF loader CVE fixed in 0.17.1, an unresolved similar CVE,
pull-path SSRF and Windows updater CVEs). A **GGUF Jinja2 chat template** can carry **server-side
template injection / inference-time backdoors** even though the formats are data-only.
Practical discipline: **keep Ollama current and the API on localhost**, **inspect chat
templates**, prefer the official library or known publishers, and **cross-check checksums**
against a canonical source. Upgrading to 0.40 migrates stored models in the background.
