# Research return: soofi (freshness re-verification) - 2026-09-21

**Verdict: DELTA / REVIEW -> do NOT auto-bump; flag for the code session, possible re-grade.**

- **Openness contradiction - load-bearing:** the **Soofi-S-Base** model card carries the HF tag **verbatim "closed-beta"** and the repo is **GATED**, while the project's marketing describes it as **"open-source."** The current AOI entry grades `soofi` at **73.2 (B)** - that grade may be **too generous** if the actual weight availability is closed-beta/gated rather than openly downloadable. This is exactly the kind of "marketing not-equal licence tag" divergence AOI exists to catch. **Recommend the code session re-examine `transparency`/`use_modify` for this entry before honestly bumping `last_verified`** - a clean bump is not warranted here.
- **Supersession:** the **Soofi-Project** org has published new preview siblings - **Soofi-S-Instruct, Soofi-Isar, Soofi-Rhine** - as previews. Flagged; not folded.
- **Availability:** Soofi-S-Base **gated** (access-request), not openly downloadable this pass.

`retrieved: true` - Soofi-Project org + Soofi-S-Base card re-read; "closed-beta" tag + gating captured verbatim. Clause file: `model_card__soofi__2026-09-21.md`. **Recommend hold on the bump pending re-grade.**

## Code-session follow-up (2026-09-21, after review)

On review against the existing `soofi` entry, this recommendation is superseded: the entry's
2026-07-25 correction already accounts for exactly this contradiction (openness held at the
`open_weights` ceiling/score 3, `weights` component already `partial`, ownership already
`partial`, `use_modify` already `moderate` - all specifically because the licence was already
known unconfirmed and weights not generally downloadable). No further downgrade applied;
`last_verified` bumped with the reasoning documented in the entry's own changelog.
