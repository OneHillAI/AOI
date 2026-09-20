doc_type: dpa (+ subprocessors, regions)
entity: nebius
source_url: https://docs.nebius.com/legal/dpa ; https://docs.nebius.com/legal/sub-processors_tofa ; https://docs.nebius.com/overview/regions
document_effective_date: sub-processors effective 2026-09-15
retrieval_date: 2026-09-20
exists: yes
retrieved: true
tag: publisher

## DPA (VERBATIM) - Q3 confidentiality scope CONFIRMED
[Sec 2.5 - VERBATIM] "Nebius shall ensure that any person that it authorizes to process Customer Personal Data (including Nebius' staff, agents and subcontractors) ('Authorized Person') shall be subject to a strict duty of confidentiality" and "shall not permit any person to process Customer Personal Data who is not under such a duty of confidentiality."
=> The DPA confidentiality duty attaches to "Customer Personal Data" ONLY, not Customer Content generally. (General Confidential Information is covered separately in ToS Sec 18.) confidentiality scope: DPA = personal data only.
[Sec 4.1 Sub-processors] Nebius maintains written agreements imposing "data protection obligations no less protective than those set forth in this DPA."
[Sec 8.3 Governing law] points to ToS Section 17.

## Sub-processors (list - ~21 named; recount recommended)
Effective 2026-09-15. Header: "This page identifies the sub-processors engaged by Nebius to process Customer..."
Nebius Group entities: Nebius Inc. (US, cloud infra); Nebius B.V. (France/Iceland/Finland/UK, cloud infra); Nebius Israel Ltd.; Nebius DC Oy (Finland, ops); Nebius UK Ltd.; Nebius CZ s.r.o. (Czech, ops); Nebius GmbH (Germany, ops); Nebius AI Spain S.L.U.; Nebius France SAS; Tech Hub IL Ltd. (Israel, ops); EdTech Plus Tech d.o.o. Beograd (Serbia, ops).
Third-party infra/compute: RunPod Inc. (Iceland); BoostRun, LLC (US); Shadeform, Inc. (US); Argentum AI, Inc. (US); Axe Compute Inc. (Canada).
Third-party SaaS/support: Microsoft Corporation - Sentinel (EU, security monitoring); Functional Software Inc. - Sentry (US, APM); Hubspot Inc. (EU); Atlassian Pty Ltd. - Jira (EU); Slack Technologies LLC (EU).
NOTE: enumerated ~21; page summary line said "18"; draft said "~24". Count is APPROXIMATE - recommend an exact recount from the live page. NOTE the third-party compute sub-processors (RunPod, BoostRun, Shadeform, Argentum, Axe Compute) - relevant to model-routing/residency, i.e. inference may run on third-party GPU providers.

## Regions (Q4) - CORRECTION to the draft
Source: docs.nebius.com/overview/regions
PUBLIC / self-serve ("available to all Nebius users"): eu-north1 (Finland), eu-west1 (France), me-west1 (Israel), us-central1 (Kansas City, US), uk-south1 (UK), uk-south2 (UK).
PRIVATE / limited ("available only to the users who already have deployments there"): eu-north2 (Iceland), eu-south1 (Madrid, Spain), eu-west2 (France), us-north1 (Woodbury, MN, US).
=> Draft's "four EU public regions (Finland, France, Spain, Iceland)" is WRONG for two: Spain (eu-south1) and Iceland (eu-north2) are PRIVATE/existing-deployment-only, NOT self-serve. Only Finland + France are public self-serve EU regions. Correct the residency field accordingly.
