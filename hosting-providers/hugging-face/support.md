# Support - Hugging Face Hub

_How do we keep it working and report problems? Security disclosure, tooling versioning and known issues live here; community channels are a documented gap._

<!-- item: security-disclosure -->
## Reporting malicious models & vulnerabilities

The Hub's **security documentation** and its **scanner partnerships** (JFrog, ProtectAI) are
the trust and disclosure surface. Reported malicious repositories are typically **removed
within ~24h**, and scanning findings surface as unsafe/suspicious flags. A formal coordinated
vulnerability-disclosure channel (e.g. a published `security.txt` or advisory feed) was not
separately captured, so route disclosures through the documented security
contacts.

<!-- item: release-versioning -->
## Tooling versioning & patch cadence

Loader safety tracks **client versions**, not just the Hub: **CVE-2026-4372** was patched in
**Transformers 5.3.0**, and picklescan was **hardened after nullifAI** (CVE-2025-1716). The
practical takeaway is to keep **transformers >= 5.3.0** and stay current on the scanning
stack. The Hub's own product release/changelog cadence was not separately captured here.

<!-- item: known-issues -->
## Known issues & caveats

Three recurring caveats: (1) **loader CVE history** - config-injection RCE that bypassed
`trust_remote_code=False`, plus multiple picklescan bypasses; (2) **scanning marks but does
not block**, so an unflagged file is not proven clean; and (3) **gameable trust signals** -
inflated download counts and trending enabled 2026 typosquats to reach hundreds of thousands
of downloads before removal. Pin commits, verify hashes, and prefer verified-org publishers.
