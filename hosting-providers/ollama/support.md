# Support - Ollama

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: security-disclosure -->
## Reporting malicious models & vulnerabilities

`SECURITY.md` asks reporters to open a vulnerability report through GitHub security advisories
and to give the team time to respond; the contact for other questions is hello@ollama.com.
There is no security page (`ollama.com/security` returns 404) and no bug bounty. No route for
reporting a malicious model in the registry is published beyond the DMCA clause in the Terms.

Several CVE records (CVE-2026-5530, CVE-2026-5757, CVE-2026-42248 and the reporter of
CVE-2026-85180) say the vendor did not respond, and no GitHub security advisory has been
published for any of them.

<!-- item: release-versioning -->
## Tooling versioning & changelog

Releases are on GitHub. The latest stable is v0.40.16 (2026-11-09), with v0.40.17-rc1
(2026-11-10) as a pre-release. The v0.40 line began on 2026-09-25 and ships one to four
releases a week. Release notes are short feature lists with no security section and have not
flagged the 2026 security fixes (the v0.17.1 notes do not mention CVE-2026-7482).

A pre-0.40 client cannot select the new MLX builds and gets the llama.cpp GGUF manifest.
Downgrading below 0.40 needs a re-pull of upgraded models. No official statement explains why
v0.30.10 refuses new models; the registry behaviour that would explain it is recorded in the
primary-source folder.

<!-- item: channels -->
## Community & support channels

The project has GitHub issues, a Discord, an X account, a Support link and support@ollama.com
for accounts and billing. The community is large. No support commitment is published for the
free tier; the Team plan lists priority support and the Enterprise plan a private Slack channel
and custom security questionnaires.

<!-- item: known-issues -->
## Known issues & caveats

The main caveats are provenance and the tool's own security record. Provenance has no
verified-org identity, no documented scanning and no shipped signing, so SHA256 gives
integrity, not authenticity. The security record includes a critical GGUF loader CVE fixed in
0.17.1, an unresolved similar CVE, pull-path SSRF and Windows updater CVEs.

A GGUF Jinja2 chat template can carry server-side template injection and inference-time
backdoors even though the formats are data-only. Keep Ollama current and the API on localhost,
inspect chat templates, prefer the official library or known publishers, and cross-check
checksums against a canonical source. Upgrading to 0.40 migrates stored models in the
background.
