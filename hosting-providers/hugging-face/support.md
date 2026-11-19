# Support - Hugging Face Hub

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: security-disclosure -->
## Reporting malicious models & vulnerabilities

The Hub's security documentation (security@huggingface.co), the Content Policy's in-platform
Report button and safety@huggingface.co, and its scanner partnerships (JFrog, Protect AI) are the
trust and disclosure surface. The nullifAI models were removed in under 24 hours after a
researcher report. The Content Policy promises no takedown time, and Load/Mine wave two stayed
live for days after a report. Scanning findings surface as unsafe/suspicious flags.

No formal coordinated vulnerability-disclosure policy or advisory feed is published, so route
disclosures through the documented contacts.

<!-- item: release-versioning -->
## Tooling versioning & patch cadence

Loader safety depends on client versions as well as the Hub. CVE-2026-4372 was patched in Transformers
5.3.0 (the current release on PyPI is 5.23.0, 2026-11-13). Picklescan changed after nullifAI and
is at 1.0.5 after a June and July 2026 wave of bypass CVEs (59 in NVD). Keep transformers >= 5.3.0
and stay current on the scanning stack.

The Hub status page shows 99.991% uptime over 90 days and no git-hosting incident since
2026-09-21. The Hub's own product release/changelog cadence is not stated.

<!-- item: known-issues -->
## Known issues & caveats

Three caveats recur. First, the loader has CVE history: a config-injection RCE that bypassed
`trust_remote_code=False`, plus dozens of picklescan bypasses. Second, scanning marks but does
not block and does not read repo Python, so an unflagged file is not proven clean (Load/Mine
scanned clean). Third, trust signals are gameable: inflated download counts and trending enabled
2026 typosquats to reach hundreds of thousands of downloads before removal. Pin commits, verify
hashes, and prefer verified-org publishers.
