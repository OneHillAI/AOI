# Support - Infercom

_Status, security disclosure, support channels and model deprecation._

<!-- item: security-disclosure -->
## Security disclosure & trust centre

Infercom publishes a server-rendered Trust Centre (`infercom.ai/trust`) that links the DPA, the
ISO 27001 certificate and the CSA STAR entry. Its FAQ states plainly that SOC 2 is "Not yet"
and that SambaNova is a US company with operational access. Vulnerabilities are reported by
e-mail to dpo@infercom.ai. No bug-bounty programme or `security.txt` is published.

<!-- item: channels -->
## Support & community channels

Documentation sits at docs.infercom.ai and tickets go to support.infercom.ai (a GLPI portal
run by TECLIB). Enhanced support is offered to Reserved Capacity and Dedicated Rack customers
under separate agreement. No community forum is listed, and the response commitments for each
tier are not published.

<!-- item: status-uptime -->
## Status page & uptime history

status.infercom.ai is a live Atlassian Statuspage with per-model components, a JSON API and
email, RSS and webhook subscriptions. Its public history holds one major incident
(gemma-4-31B-it, 2026-06-19, about 21 hours). The page shows no uptime percentages and states
no SLA.

<!-- item: deprecation -->
## Model deprecation policy

Production models get at least two to three weeks' notice, by e-mail, on the docs page and in
the Playground, with a recommended replacement. Preview models may be deprecated or promoted.
The docs keep a dated record (Llama 3.3 70B 2026-11-17, DeepSeek V3.1 and V3.2 2026-11-03,
MiniMax-M2.7 2026-09-30). The Terms Sec 2.2 are weaker than the docs: they allow models to be removed "without
prior notice".
