doc_type: model_card
entity: soofi
source_url: https://huggingface.co/Soofi-Project (Soofi-S-Base, Soofi-S-Instruct, Soofi-Isar, Soofi-Rhine)
document_effective_date: current
retrieval_date: 2026-09-21
exists: yes
retrieved: true
tag: publisher

## The load-bearing contradiction
The **Soofi-S-Base** HF model card carries the tag **verbatim "closed-beta"**, and the repo is **GATED** (access-request), while the Soofi project's own marketing describes the model as **"open-source."**

- Marketing framing: "open-source".
- Actual HF signal: **"closed-beta"** tag + **gated** access - i.e. weights are NOT openly downloadable this pass.

This is a marketing-vs-availability divergence: the current AOI grade of **73.2 (B)** may be too generous if it assumed open weight availability.

## New siblings (previews)
The **Soofi-Project** org has published preview siblings: **Soofi-S-Instruct, Soofi-Isar, Soofi-Rhine** - all preview-stage. Flagged, not folded.

## Recommendation (for the code session)
**Do NOT bump `last_verified` with a clean pass for `soofi`.** Re-examine `transparency` and `use_modify` against the "closed-beta" tag and gating before re-grading. If the weights are genuinely closed-beta/gated rather than openly licensed, the B grade likely overstates openness and should come down.

retrieved: true - Soofi-Project org + Soofi-S-Base card re-read this pass; "closed-beta" tag and gating captured directly.

## Code-session follow-up (2026-09-21, after review)
See `RESEARCH-RETURN__soofi__2026-09-21.md` in this same folder: the entry's existing 2026-07-25
correction already accounts for this exact contradiction. No further downgrade applied.
