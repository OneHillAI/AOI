# Research return: llama-4 (freshness re-verification) - 2026-09-21

**Verdict: re-verified CLEAN on tracked terms -> `last_verified` can be bumped to 2026-09-21, with one manual-eyeball flag.**

- **Licence:** unchanged on the load-bearing terms. The **Llama 4 Community License** still carries the 700M-MAU threshold and remains gated.
- **Manual re-confirm needed (tool limitation, not a finding):** WebFetch **truncated the "Additional Terms" section**, so the **EU-domicile multimodal carve-out** (the clause restricting multimodal-model use by entities domiciled in the EU) could **not be re-confirmed verbatim this pass**. Treat as **unchanged pending a manual eyeball** of the licence page - this is an unread-section caveat, not evidence of a change. `retrieved: false` for that specific clause.
- **Supersession:** no **Behemoth GA** and no newer Llama 4 point release that changes the tracked terms.
- **Safety / availability:** repos remain gated; no new adverse safety finding.

`retrieved: true` for the model card + main licence body; `retrieved: false` for the truncated Additional Terms (EU carve-out). No new clause file - flag only.
