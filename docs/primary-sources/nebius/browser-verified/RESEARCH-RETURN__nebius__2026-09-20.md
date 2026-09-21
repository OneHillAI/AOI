# Research return: nebius / Token Factory (FULL grounding pass) - 2026-09-20

Confirmed reading the INFERENCE product (Token Factory, formerly AI Studio) governing docs on docs.tokenfactory.nebius.com (which 302-redirects legal pages to docs.nebius.com/legal/...), NOT the raw-GPU-cloud terms.

## Decisive questions - CONFIRM / CORRECT
1. Train-by-default + opt-out (the whole entry turns on this)? -> CONFIRMED VERBATIM. ToS Sec 7: "the Company collects and processes both Input and Output data for the purpose of training smaller Models used exclusively for Speculative Decoding," opt-out required ("If you prefer that we (i) do not store ... and (ii) do not collect and process them for Speculative Decoding, You may opt out at any time"). training-on-inputs = by_default (opt-out). The draft's central finding SURVIVES an independent human-grade read. The current grade (65.2, C) stands and is now actually grounded.
2. Legal Quick Guide vs ToS? -> GENUINE TENSION (confirmed). Quick Guide Sec 4.2 "Your content is not used to train any models in either mode" and FAQ "we do not use your content to train ... any AI models" contradict ToS Sec 7's "training smaller Models." Reconciled only by Nebius treating Speculative Decoding as non-"training." Binding doc (ToS Sec 7) governs; flag the Quick Guide as a documented inconsistency (bears on transparency).
3. DPA confidentiality scope? -> CONFIRMED: DPA Sec 2.5 attaches the duty to "Customer Personal Data" ONLY, not Customer Content generally. (ToS Sec 18 has a separate general Confidential-Information duty.)
4. Regions self-serve vs private? -> CORRECTED. Only eu-north1 (Finland) + eu-west1 (France) are PUBLIC self-serve EU. eu-south1 (Spain) and eu-north2 (Iceland) are PRIVATE/existing-deployment-only. Remove Spain + Iceland from the self-serve EU claim.
5. Committed inference SLA %? -> CONFIRMED ABSENT. sla-levels lists 7 services, none inference/Token Factory. 99.9% is marketing-only. No committed inference SLA.
6. Flagship catalogue public vs dedicated-only? -> "dedicated-only / no public price" NOT supported. Open models are publicly served per-token; the three named versions (Kimi-K2-Instruct, Llama-3.3-70B-Instruct, GLM-4.5) are largely superseded on the live catalogue, not gated. Authoritative price page auth-gated (retrieved:false) - verify a specific number there.

## Field-by-field
| Field | Value | Grounded |
|-------|-------|----------|
| training-on-inputs | BY DEFAULT (Speculative-Decoding model training), opt-out required | ToS Sec 7 (verbatim) |
| retention | inputs/outputs kept unless ZDR enabled (no fixed period in Sec 7) | ToS Sec 7 / Quick Guide |
| ZDR | available (opt-out), stops storage + Speculative Decoding + training | Quick Guide 4.1 |
| customer IP | customer owns content EXCEPT Sec 7/12/13/13A carve-out | ToS Sec 10 |
| confidentiality | ToS Sec 18 general duty (both parties); DPA duty = Customer Personal Data only | ToS/DPA |
| governing law / liability | Netherlands; liability greater of 12-mo fees or $500 | ToS Sec 16/17-19 |
| sub-processors | ~21 named (recount); incl. third-party GPU providers RunPod/BoostRun/Shadeform/Argentum/Axe (routing/residency relevance) | subprocessors page |
| residency | public self-serve EU = Finland + France only; Spain + Iceland private | regions page |
| compliance | SOC2 Type II (Deloitte) incl HIPAA; ISO 27001 scope incl AI Studio; report NDA-gated, no public dates | blog/trust (publisher + named auditor) |
| SLA | NO committed inference % (99.9% marketing-only) | sla-levels |
| status | Token Factory component Operational; incidents Sep 9-17 | status |
| pricing | open models publicly served per-token; auth-gated authoritative list | partial |

## Corrections to the draft
1. Regions: only Finland + France public self-serve EU (Spain + Iceland are private).
2. Sub-processor count ~21, not ~24 (recount from live page).
3. No committed inference SLA % - do not cite 99.9%.
4. Flagship models are publicly served per-token / superseded, not dedicated-endpoint-only.
5. Quick Guide vs ToS Sec 7 = documented inconsistency (transparency).
CONFIRMED (grade-critical): train-by-default via ToS Sec 7 - the entry's central finding is real.

## RE-DO
Authenticated read of tokenfactory.nebius.com/organization/prices for exact live per-token rates; exact sub-processor recount; confirm ToS governing-law section number.
