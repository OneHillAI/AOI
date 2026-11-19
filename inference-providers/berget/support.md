# Support - Berget AI

_How do we keep it running and get help? Security disclosure, support channels and the model
deprecation policy live here; status and uptime history remain a documented gap._

<!-- item: security-disclosure -->
## Security disclosure & trust surface

Berget's **Security page** is a responsible-disclosure policy, not a trust centre. It offers
GitHub private vulnerability reporting, `security@berget.ai` with a **PGP key** and a Signal
number, a typical 48-hour response, a scope list and a safe-harbour statement. It states no
technical controls and no attestations (those are in ToS Sec 6.7 and DPA Sec 8). A published
`security.txt` or bug-bounty programme is not stated; use the PGP or Signal contact.

<!-- item: channels -->
## Support & community channels

Support comprises **developer documentation at `docs.berget.ai`** (with `llms.txt` and Markdown
versions of each page) plus a community link. Support level follows the plan: community on the
Trial, email on Starter, priority on Team and dedicated support on Enterprise. Response-time
commitments are not published; confirm them during onboarding.

<!-- item: deprecation -->
## Model deprecation policy

Berget publishes a **model lifecycle policy** in its docs. Preview models may be removed
without notice. Active models pass through Upgrading (with a named successor) or Deprecated
before retirement, with **2 or 3 weeks notice depending on usage**, and the API exposes
`lifecycle_status`, `upgrade_to` and `end_of_life`. Seven models are listed as retired between
2026-06-24 and 2026-09-18, and Kimi K3 was replaced by Kimi K3.1 Pro in a weekend maintenance
window on 2026-11-07 to 2026-11-08. Upgrades to frontier models may involve downtime.
