doc_type: docs
entity: nebius
source_urls: https://docs.nebius.com/overview/regions ; https://docs.nebius.com/legal/sla ; https://docs.nebius.com/legal/sla-levels ; https://status.nebius.com/ ; https://nebius.com/services/token-factory
retrieval_date: 2026-11-19
exists: yes
retrieved: true (the catalogue and per-model pages were later read in the in-app browser, see docs__catalogue-prices-deprecations__2026-11-19.md; the logged-in price list was not read)
tag: publisher

## Regions (docs.nebius.com/overview/regions, Nebius AI Cloud)
Public regions "available to all Nebius users": eu-north1 Finland; eu-south1 Madrid, Spain; eu-west1 France; eu-west2 France; me-west1 Israel; us-central1 Kansas City, Missouri; us-north1 Woodbury, Minnesota; uk-south1 and uk-south2 United Kingdom.
Private: "The eu-north2 region is available only to the users who already have deployments there." eu-north2: Iceland.
CHANGE from 2026-09-20: Spain (eu-south1), the second French region (eu-west2) and us-north1 were then listed as private; the page now lists them as public. Public EU regions are now four region IDs in three countries (Finland, Spain, France x2), up from two region IDs (Finland, France). Iceland remains private. CAUTION: this is the Nebius AI Cloud region list, not a Token Factory list. Token Factory's own data-plane table names only eu-north1, eu-west1 and us-central1, and the Token Factory sub-processor list names France, Iceland, Finland and the UK for Nebius B.V.; see docs__token-factory-limits-capacity-regions__2026-11-19.md. Do not state 'four EU regions' for Token Factory. These are Nebius AI Cloud regions; Token Factory shared endpoints are "Global" and unpinned (see Quick Guide and DPA 6.1), and Token Factory dedicated endpoints do not list regions on the dedicated-endpoints overview page ("Deployment region is fixed and user-selected").
The status page lists a Token Factory component under EU-NORTH1, EU-NORTH2, EU-WEST1, EU-WEST2, EU-SOUTH1, UK-SOUTH1, US-NORTH1, US-CENTRAL1, ME-WEST1 and three Token Factory locations TF-US1, TF-US2, TF-CA1.

## SLA
[sla, effective 2026-11-02] The master SLA "applies only to the specific Services linked in this document".
[sla-levels, published 2026-10-06] Lists eight services: Compute Cloud, Disks, Managed Service for Kubernetes, Managed Service for MLflow, Managed Service for PostgreSQL, Object Storage, Shared Filesystem, Virtual Private Cloud. (September: seven; Disks and Shared Filesystem are new; Standalone Applications is no longer listed.) None is inference, Token Factory or AI Studio.
[Binding exclusion] Token Factory Supplemental Terms 7.4: "Nebius does not provide any service level commitments, uptime guarantees, or associated compensation for the Token Factory Service." So the inference SLA is not merely absent: the contract expressly excludes it. Any 99.9% figure in marketing is not backed.

## Status (status.nebius.com)
"All Systems Operational"; Token Factory components operational in every region; 90-day uptime shown without a numeric percentage on the main view.
Token Factory incidents in the past 14 days: Nov 5, 2026 "Token Factory: some models unavailable in eu-north1" (10:30 to 11:07 UTC, resolved); Nov 11, 2026 "Token Factory connectivity loss in tf-us2" (not reachable 07:33 to 07:41 UTC, resolved, cause under investigation). Other recent incidents were Compute Cloud (Nov 9, eu-north1 hosts) and "Network problems" (Nov 7).

## Product page (nebius.com/services/token-factory)
Showcases MiniMax M3, Kimi K3 and DeepSeek V4 Pro; serverless inference "through a familiar API" and dedicated endpoints "on isolated capacity ... regional placement". Prices are not on the page. The catalogue and price list returned HTTP 403 to curl; later in the day the catalogue and per-model pages were read in the in-app browser (the price list needs a login). Result: gpt-oss-120b $0.15/$0.60 confirmed; DeepSeek-V4-Pro and Llama-3.3-70B-Instruct no longer have public endpoints (see docs__catalogue-prices-deprecations__2026-11-19.md). The dedicated-endpoint billing-policy page still does not publish a GPU-hour rate.
