# Runware - help centre and status page (read 2026-11-19)

## DPA availability - help centre (verbatim)
Source: https://help.runware.ai/articles/4921342244-does-runware-offer-a-data-processing-agreement-dpa
(page says "Last updated 1 month ago").
- "If you require a DPA for GDPR or other compliance purposes, please contact our sales team. DPAs and
  other custom data-handling terms are available as part of our enterprise agreement process for
  eligible B2B customers."
https://runware.ai/dpa and /data-processing-agreement return HTTP 404. No public DPA or sub-processor
list exists. The DPA text itself was not read.

## Where data is stored - help centre (verbatim) - CONTRADICTS the binding Terms
Source: https://help.runware.ai/articles/4781590666-where-is-runware-data-stored ("Last updated 8
months ago").
- "All data (including media and model files) is stored on secure, EU-based servers operated by our
  hosting partners. ... Runware does not sell or share user data with third parties."
Terms Sec 16 (binding, updated 2026-09-29) says: "the Services are hosted in the United States,
Germany and Romania." The help article is marketing-grade and is not relied on for residency.
It also sits uneasily with partner models, whose requests are forwarded to the model provider.

## Status page - https://status.runware.ai/ (incident.io, HTTP 200, server-rendered)
- Banner "We're fully operational" on 2026-11-19. Period shown: Aug 2026 to Nov 2026.
- Per-component uptime: API 100%, Website 100%, Dashboard 100%, Playground 100%; Models 99.93%
  (Official Models 99.94%, Third-party Models 99.98%); Serverless 99.90% (API 99.997%, Inference 100%,
  Build and Deploys 99.91%, Metrics and Logs 100%, Compute 99.97%).
- The status page separates "Official Models" from "Third-party Models", which corroborates that
  third-party models are part of the service. No SLA statement on the page. /history returned 404.

## Trust centre
- https://runware.ai/trust is now a "Trust & Safety" abuse-report form (no compliance content).
- https://trust.runware.ai/ returns an empty single-page-app shell ("Trust center"); content needs
  JavaScript. retrieved: false. No score is based on it.
- Footer of every runware.ai page (marketing, no report behind it): "ISO 27001 Certified", "SOC 2
  Certified", "GDPR Compliant", "Data residency EU & US", "SSO + SAML Enterprise", "MFA Configurable".
- https://runware.ai/security-disclosure: "Runware operates a Responsible Disclosure Program, not a
  public bug bounty." Acknowledgement target 5 business days; safe harbour for good-faith research.
