doc_type: sla (status page)
entity: deepinfra
source_url: https://status.deepinfra.com/ (and https://status.deepinfra.com/maintenance)
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

The stored entry said no public status page existed. A server-rendered status page does (HTTP 200, text readable). Read 2026-11-19, "Last updated Thu, 19 Nov 2026 16:42:59 GMT":
- "Core services operational"; "All 172 monitored models operational"; "1 model is scheduled for deprecation (embeddinggemma-300m) - first one in 4 days"; scheduled deprecation listed with date, "embeddinggemma-300m -> google/embeddinggemma-2, 2026-11-23 17:09 UTC", "requests are redirected to the replacement where one is named".
- Core services, 90-day uptime: API api.deepinfra.com "100% over 86.4 of 90 days measured"; Website deepinfra.com "100% over 86.4 of 90 days measured". Per-model rows show 99.98% to 100% (for example DeepSeek-V4-Flash-0731 99.99% over 85.6 days, MiMo-V2.6-Flash 99.98% over 56.0 days).
- The page explains the measure: a 90-day strip, one bar per day coloured by minutes lost, "Maintenance ... Not counted against uptime", and "The percentage is measured, not derived from the colors".
- There is a Maintenance page and an RSS and API link. There is no incident-history page (the /history and /incidents paths return a 404 page), so incident narratives were not found; the states shown are automated health-check outcomes.
There is no uptime SLA, credit schedule or service-level document: the Terms contain only a 24-hour hardware replacement undertaking for provided servers (Sec 4(b)) and a warranty disclaimer (Sec 9(b)); https://deepinfra.com/sla and /dpa return 404.
