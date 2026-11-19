# Support - Groq

_How do we keep it running and get help? Security disclosure, support channels, the model
deprecation policy and the status page live here._

<!-- item: security-disclosure -->
## Security disclosure & trust centre

Groq's **trust centre** (trust.groq.com) is the trust surface, covering its **SOC 2 Type II**,
GDPR and HIPAA posture and a **sub-processor list**, but it is a JavaScript-only page that could
not be read on 2026-11-19. `groq.com/security` describes a **private vulnerability disclosure
programme through HackerOne**; there is no public bug bounty.

<!-- item: channels -->
## Support & community channels

Support rests on **product and console documentation** (console.groq.com/docs). Groq does not
publish the response commitments attached to each paid tier or the breadth of its community
channels (Discord/forum), so confirm the support SLA that comes with your tier during
onboarding.

<!-- item: deprecation -->
## Model deprecation policy

Groq publishes a **model-deprecation policy** in its docs, and the recent history shows frequent
retirements (the Llama pair on 2026-08-16, Compound on 2026-09-21), with enterprise
committed-spend contracts exempt. It gives **commercially reasonable prior
notice** before deprecating a model, and for **production models** it provides a **clear migration
path and a recommended replacement**; **preview models** may be discontinued at **short notice**.
If you have prepaid for a model that is deprecated **without an alternative**, Groq offers a
**pro-rata refund** for the unused prepaid fees. Because the catalogue is open-weight, a removed model
can also generally be self-hosted or sourced from another provider - so deprecation is a migration
task, not a lock-out.

<!-- item: status-uptime -->
## Status page & uptime history

Groq runs a **public status page** at groqstatus.com (incident.io; status.groq.com redirects to it).
On 2026-11-19 it reported "fully operational", with August to November 2026 uptime of **100% for
the API and the six production model components** and 99.98% across seven preview components.
No SLA or service credits are published, and the page's history URL returned 404.
