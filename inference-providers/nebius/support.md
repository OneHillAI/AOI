# Support - Nebius (Token Factory)

_How do we keep it running and get help? Security disclosure, status/uptime, support channels and
model deprecation live here._

<!-- item: status-uptime -->
## Status page & uptime history

A public **status page** (status.nebius.com, read 2026-11-19) shows "All Systems Operational"
with a "Token Factory" component under every region (it lists every product under every region,
so this says nothing about where Token Factory runs) and a 90-day uptime bar with no numeric
percentage. Two Token Factory incidents fall in its 14-day window, both resolved: 2026-11-05
(some models unavailable in eu-north1, 10:30 to 11:07 UTC) and 2026-11-11 (Token Factory in tf-us2
unreachable from 07:33 to 07:41 UTC, cause under investigation).

<!-- item: security-disclosure -->
## Security disclosure & trust centre

A published **Trust Center** (nebius.com/trust-center and its per-certificate pages, read
2026-11-19) lists **SOC 2 Type II** with HIPAA, a public **SOC 3** report, **ISO 27001/27701/42001**
and others, **CSA STAR Level 1** and a security-team contact. The SOC 3 PDF and the ISO 27001
certificate were read in full. No public bug-bounty programme was found.

<!-- item: channels -->
## Support & community channels

Product/console documentation (docs.tokenfactory.nebius.com and docs.nebius.com) is the primary
support surface. Support-tier response commitments were not detailed in the sources read this
pass - confirm what comes with your account tier during onboarding.

<!-- item: deprecation -->
## Model deprecation policy

Nebius publishes per-event notices rather than a standing policy. Serverless removals took place
on 2026-06-22, 2026-08-31 and 2026-11-09, and one is announced for 2026-12-24; each notice names a
replacement, says dedicated endpoints for the model are unaffected, and says requests are not
rerouted. No minimum notice period was found, and the Legal Quick Guide says only that
deprecations "are announced in advance" by e-mail and in the platform.
