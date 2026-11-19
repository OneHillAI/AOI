doc_type: docs
entity: nebius
source_urls: https://docs.tokenfactory.nebius.com/ai-models-inference/rate-limits.md ; .../ai-models-inference/dedicated-endpoints/capacity-and-scaling.md ; .../ai-models-inference/dedicated-endpoints/control-data-plane.md ; .../public-serverless.md ; .../ai-models-inference/dedicated-endpoints/billing-policy.md ; https://docs.nebius.com/legal/dpa-inc ; https://docs.nebius.com/legal/dpa-il
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher
read_by: refresh agent 2026-11-19 (curl on the .md renderings listed in docs.tokenfactory.nebius.com/llms.txt)

## Rate limits (rate-limits.md) - closes the earlier "no rate-limit table" gap
"Every user is provided with a default rate limit cap. This limit grows automatically when you consistently operate close to your capacity and current limit." Defaults are shown only inside the logged-in console ("tokenfactory.nebius.com/project/rate-limits"). The page gives rules and an ILLUSTRATIVE baseline of 60 RPM and 400,000 TPM.
Rules (VERBATIM headings): scale-up when average usage in a rolling 15-minute window is 80 percent or more of the limit (next window x1.2); scale-down at 50 percent or less (divided by 1.5); "Hard ceiling - The limit can grow to 4x your base allocation. Beyond that we require an Enterprise plan." Exceeding the limit returns HTTP 429; "requests that exceed your rate limit may still be processed" at lower priority with header "x-ratelimit-over-limit: yes"; busy endpoints return HTTP 529 "System is overloaded". "Dedicated Endpoints don't have rate limits."
"Enterprise removes the soft caps described below and gives you dedicated capacity plus an SLA." (This is page text about an Enterprise Tier; no Enterprise terms are published.)

## Capacity and SLA for dedicated endpoints (capacity-and-scaling.md)
"Self-service dedicated endpoints do not include a formal SLA unless covered by contract." Capacity "is not a long-term reservation"; after a stop, incident or maintenance the GPUs are released to a shared pool and "recovery after maintenance or an incident does not restore the capacity your endpoint used before". Guaranteed capacity needs a sales contract. Minimum replicas are "reserved and non-preemptible" only while the endpoint is running; scaling above the minimum "is not guaranteed indefinitely".
This matches Supplemental Terms 7.4 ("unless agreed otherwise in writing"): the standard terms carry no SLA, a negotiated contract can.

## Regions as Token Factory documents them
Control & Data Plane page: the control plane has one base URL (api.tokenfactory.nebius.com); the data plane has regional base URLs and the table lists exactly three: eu-north1 (https://api.tokenfactory.nebius.com), eu-west1 (https://api.tokenfactory.eu-west1.nebius.com) and us-central1 (https://api.tokenfactory.us-central1.nebius.com). Valid region and GPU combinations come from the templates API (login needed): "Use the template response as the source of truth for valid combinations of model_name, flavor_name, gpu_type, gpu_count and region."
Public Serverless Endpoints page: the Region field shows "Global"; "the processing location is decided dynamically and can change at any time, without notice"; "Dedicated endpoints always process requests in the region they're deployed to".
Sub-processor list (read 2026-11-19, effective 2026-09-23): Nebius B.V. processing location for Token Factory inference is "France, Iceland, Finland, United Kingdom"; Nebius Inc. "United States"; Nebius Israel Ltd. "Israel"; RunPod "Iceland"; BoostRun and Shadeform "United States"; Axe Compute "Canada". Spain (eu-south1) and the second French region (eu-west2) are named in no Token Factory document read; they appear only on the Nebius AI Cloud regions page and as template components on the status page.
=> For Token Factory, the documents name two EU data-plane regions (Finland, France). The AI Cloud regions page shows four public EU region IDs in three countries, but a Token Factory deployment in Spain or eu-west2 is not shown in any Token Factory document, so "four EU regions" must not be stated for this service.

## Billing policy (unchanged)
"A dedicated endpoint is considered active, accessible, and billable when at least one replica is running." "Charges may vary depending on your custom contract or work order." No GPU-hour rate is published.

## Three DPA variants (docs.nebius.com/legal/dpa, /dpa-inc, /dpa-il; all "Effective date: November 18, 2026")
The Services Agreement Sec 17 sends customers to the DPA for their contracting entity: Nebius B.V. (not US or Israel), Nebius Israel Ltd (Israel; Israeli law, Tel Aviv courts) or Nebius Inc (US; Delaware law, JAMS arbitration in New York). Sec 6.1 (Token Factory paragraph) and Sec 4.3 (15 days' notice of sub-processor changes) were read in the B.V. and Inc. variants and the 6.1 location text and 4.3 notice period also appear in the Israel variant. The Inc. variant adds a CCPA section. The Israel variant words its confidentiality clause (2.5) differently ("only persons ... legally bound to protect the confidentiality of the Personal Data").
Annex 3 (Token Factory): "Encryption keys are Nebius-managed, and Customer-managed keys are not currently offered."
