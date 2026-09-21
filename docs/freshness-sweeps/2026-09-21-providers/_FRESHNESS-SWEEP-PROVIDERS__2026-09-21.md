# AOI freshness re-verification sweep - hosting/inference providers - 2026-09-21

The second half of the PR #22 freshness debt: **8 stale provider entries** (3 hosting/distribution, 5 inference), all 46-58 days past SLA. Real re-check against current primary sources, not a bulk date-bump. Every entry re-read this pass; `retrieved` flags honest per file. This lands `validate.py` at 0 errors registry-wide.

## Summary table

| Entity | Type | Result | What changed | Action |
|---|---|---|---|---|
| `hugging-face` (79.2 B) | hosting | clean | scanning policy verbatim unchanged; no HF-native signing; July intrusion predates window | bump, hold |
| `llama-cpp-gguf` (56.4 C) | hosting | delta | new CVE-2026-52131 (2026-09-01, CVSS 7.5, `gguf_reader::read` reachable assertion) | bump, hold C |
| `ollama` (55.2 C) | hosting | delta | new CVE-2026-85180 (2026-09-03, tensor-blob redirect SSRF); OMS signing PR #11573 in-progress, not merged | bump, hold C |
| `berget` (70.4 B) | inference | clean + positive | explicit confidentiality intact; refreshed DPA 2026-09-10 (EEA-only + customer region choice + 5 named sub-processors); ISO 27001 still a claim | bump, hold B |
| `groq` (70.0 B) | inference | clean | Sec 10 mutual confidentiality verbatim unchanged; training prohibited; "Eligible Customers" ZDR gap persists; Helsinki ~14-mo track record (no contractual region-pinning); Trust Center Vanta-gated | bump, hold B |
| `infercom` (76.0 B) | inference | clean | on-prem/air-gap still shipped (load-bearing strength); functional_only confirmed; no training (Sec 2.4); ISO 27001:2022 dated cert; DPA v1.3 PDF gated | bump, hold B |
| `deepinfra` (52.0 D) | inference | **DELTA - material positive** | ToS rewrite 2026-08-17: Section 17 mutual confidentiality (was functional_only); Section 7(b) Zero Data Retention contractual + controlling; training opt-in (hard flag lifted). Residual: disclosed Google/Anthropic model routing | RE-GRADED up: 52.0 D -> 56.8 C |
| `runware` (45.6 D) | inference | **DELTA - material** | current ToS has no adverse SUBMISSIONS clause; §2 user owns Outputs; §3 no-train commitment; private-model confidentiality - adverse cap no longer supported | RE-GRADED up: 45.6 D -> 50.4 D (hard flag lifted) |

## Code-session application (2026-09-21)

Both re-grade recommendations were applied, each with the flagged caveats carried into the entry:

- **deepinfra**: confidentiality functional_only -> mutual; data_governance 3 -> 4; headline 52.0 -> 56.8 (D -> C). Compliance (SOC 2/ISO dated status, DPA/SCCs) was NOT re-examined this pass (trust centre 403'd again) and stays unchanged pending a future check. Open caveat carried into the entry: the rewritten ToS reads as an enterprise/Service-Order MSA at the canonical /terms URL - credited to the base self-serve product as the standard reading of a canonical Terms page, flagged for explicit re-confirmation if a separate self-serve-only ToS surfaces.
- **runware**: confidentiality adverse -> functional_only (not mutual/explicit - no general confidentiality clause covers ordinary prompts/outputs, only the pre-existing Private Model Protection clause); adverse hard flag lifted; trains_on_inputs unclear -> never; customer_data_ownership provider_may_use -> customer_retains; data_governance 2 -> 3; headline 45.6 -> 50.4 (stays D - other dimensions, notably compliance at 1 and residency at 2, were not re-examined and remain the binding constraints). Load-bearing caveat carried into the entry: the confidentiality-clause removal is inferred from the current text's absence of the old clauses, not a verbatim historical diff - all web archives (web.archive.org, archive.ph, timetravel.mementoweb) were proxy-blocked this pass.

## New security findings (hosting) - no grade change

- **CVE-2026-52131** (llama-cpp-gguf, 2026-09-01, CVSS 7.5) - reachable assertion in `gguf_reader::read`. Reinforces the existing C rationale.
- **CVE-2026-85180** (ollama, 2026-09-03) - tensor-blob redirect SSRF to internal/metadata hosts, a separate code path from the earlier fix. Offset by the not-yet-merged OMS signing PR #11573.

## Items still requiring a manual eyeball / re-attempt (tool limits, gated sources)

- **runware Aug-2026 archive diff** - all web archives proxy-blocked; adverse removal inferred, not verbatim-diffed. Retry when the proxy allows if a verbatim diff is later required.
- **deepinfra trust center** (trust.deepinfra.com/compliance) - 403 Sprinto/JS-gated; SOC 2 / ISO 27001 dates not re-confirmed.
- **deepinfra MSA scope** - confirm the rewritten ToS genuinely governs standard self-serve API users, not only enterprise Service Orders.
- **groq Trust Center** (trust.groq.com) - Vanta JS-gated; SOC 2 Type II remains claim-grade this pass, dated certificate not read.
- **infercom DPA v1.3** - full text gated behind a redirect; substantive clauses not read this pass (not load-bearing, since functional_only already stands on the Terms).

## Net result

`python scripts/validate.py` now reports **0 errors registry-wide** for the first time this session. Two material re-grades (deepinfra, runware) and six clean re-verifications, all independently checked against current primary sources rather than bulk-dated.
