# Support - Baseten

_How do we keep it running and get help? Status/uptime, security disclosure, support channels and
the model deprecation policy live here._

<!-- item: status-uptime -->
## Status page & uptime history

A public **status page** (status.baseten.co, statuspage JSON read 2026-11-19) lists every
component, the incident history with timestamps and resolution notes, and is the measurement
source named in the SLA. It shows all systems operational. Since 2026-09-20 it logs **7 major or
critical incidents**, all resolved: 2026-09-21, 09-24, 09-29 (11 h 45 min of elevated 500s in one
US region), 10-05, 10-20, **11-11 (all Model APIs down for 21 minutes)** and 11-18 (web app only,
inference unaffected), plus 13 minor ones.

<!-- item: security-disclosure -->
## Security disclosure & trust centre

A **Trust Center** at trust.baseten.co (Vanta, launched 2026-07-30) renders only in a browser. It
labels **SOC 2**, **ISO 27001:2022**, **HIPAA**, **GDPR**, **CCPA** and **PCI DSS SAQ D**, indexes
the underlying documents (SOC 2 and SOC 3 reports, ISO certificate, an October 2026 penetration
test, the PCI attestation, a FedRAMP 20x package) and publishes a 13-row sub-processor list and a
dated updates feed. Every document is behind "Request access" and was not read, so treat the
labels as the vendor's claims. Vulnerability reports go to security@baseten.co; no bug-bounty
programme was found.

<!-- item: channels -->
## Support & community channels

Product/console documentation (docs.baseten.co) is the primary support surface. Support-tier
response commitments were not detailed in the sources read this pass - confirm what comes with
your account tier during onboarding.

<!-- item: deprecation -->
## Model deprecation policy

Baseten publishes a Model APIs deprecation policy: deprecations are **announced 30 days before the
deprecation date** in the docs and by e-mail, the model stays fully functional until that date,
and afterwards the model ID returns an error. The stated migration paths are a dedicated
deployment of the same weights or a newer model. No deprecations were scheduled on 2026-11-19.
