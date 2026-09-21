# Research return: nemotron-3 (freshness re-verification) - 2026-09-21

**Verdict: re-verified CLEAN on tracked terms -> bump `last_verified` to 2026-09-21, with a sibling flag.**

- **Licence:** unchanged and correctly tagged. Nemotron-3 remains under the **NVIDIA Nemotron Open Model License** (Apache-derived, irrevocable grant, **no** Trustworthy-AI (2.3) / revocable-guardrail (2.1) clause). Re-confirmed this pass that the Nemotron-tagged licence is *not* the generic "NVIDIA Open Model License" that does carry those clauses - the distinction the earlier pack corrected still holds and the tag is right.
- **Supersession - FLAG (do not fold):** NVIDIA has shipped **Nemotron 3.5 Lightning 30B-A3B (released 2026-08-11), licensed OpenMDW-1.1** (Linux Foundation), sitting in the Nano/compact footprint. Different licence from the tracked Nemotron-3 -> warrants a new sibling, not an in-place fold. Flagged for the code session.
- **Safety:** strengthened, not weakened - a **Nemotron 3.5 Content Safety** guard model has been added to the safety tooling. No new adverse red-team finding.

`retrieved: true` - model card + Nemotron Open Model License re-read; licence-family distinction re-verified. New sibling flagged; no correction needed to the existing entry's clauses.
