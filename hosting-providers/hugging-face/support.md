# Support - Hugging Face Hub

_How do we keep it working and report problems? Security disclosure, tooling versioning and known issues live here; community channels are a documented gap._

<!-- item: security-disclosure -->
## Reporting malicious models & vulnerabilities

The Hub's **security documentation** (security@huggingface.co), the Content Policy's in-platform
Report button and safety@huggingface.co, and its **scanner partnerships** (JFrog, Protect AI)
are the trust and disclosure surface. The nullifAI models were **removed in under 24 hours**
after a researcher report, but the Content Policy promises no takedown time and Load/Mine wave
two stayed live for days after a report. Scanning findings surface as unsafe/suspicious flags.
A formal coordinated vulnerability-disclosure policy or advisory feed was not found, so route
disclosures through the documented contacts.

<!-- item: release-versioning -->
## Tooling versioning & patch cadence

Loader safety tracks **client versions**, not just the Hub: **CVE-2026-4372** was patched in
**Transformers 5.3.0** (the current release on PyPI is 5.23.0, 2026-11-13), and picklescan was
**changed after nullifAI** and is at 1.0.5 after a June and July 2026 wave of bypass CVEs (59
in NVD). The practical takeaway is to keep **transformers >= 5.3.0** and stay current on the
scanning stack. Status page, 2026-11-19: Hub uptime 99.991% over 90 days and no git-hosting
incident since the last check. The Hub's own product release/changelog cadence was not separately captured here.

<!-- item: known-issues -->
## Known issues & caveats

Three recurring caveats: (1) **loader CVE history** - config-injection RCE that bypassed
`trust_remote_code=False`, plus dozens of picklescan bypasses; (2) **scanning marks but does
not block and does not read repo Python**, so an unflagged file is not proven clean (Load/Mine
scanned clean); and (3) **gameable trust signals** -
inflated download counts and trending enabled 2026 typosquats to reach hundreds of thousands
of downloads before removal. Pin commits, verify hashes, and prefer verified-org publishers.
