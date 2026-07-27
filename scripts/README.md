# scripts/

Tooling that keeps the registry consistent, scored, and current. Pure Python; deps in
[`../requirements.txt`](../requirements.txt) (`pip install -r requirements.txt`).

## `score.py` - compute the AOI

Scores are **derived** from an entry's dimension anchors, never hand-typed, so they can't
drift from the evidence. Implements the weights from
[`../methodology/scoring-rubric.md`](../methodology/scoring-rubric.md) and
[`../methodology/provider-scoring-rubric.md`](../methodology/provider-scoring-rubric.md),
including hard-flag grade ceilings.

```bash
python scripts/score.py models/<id>/data.yaml           # print
python scripts/score.py --check models/<id>/data.yaml   # exit 1 if stored != computed
python scripts/score.py --write models/<id>/data.yaml   # write headline+grade back
```

It auto-detects the profile (model vs inference vs hosting) from the data file and picks
the right weights.

## `completeness.py` - documentation coverage meters (v2 entries)

Computes two per-domain meters for a four-domain library entry (`entry.yaml`), derived from
its documentation items and [`../checklists/model.yaml`](../checklists/) - never hand-typed:

- **completeness** - coverage of the domain's expected items (aggregated and
  onehill_generated count equally; a documented `gap` counts 0 but is still "addressed").
- **originality** - share of the domain's credited items that OneHill generated/verified
  itself.

```bash
python scripts/completeness.py models/<id>/entry.yaml           # print
python scripts/completeness.py --check models/<id>/entry.yaml   # exit 1 if stored != computed
python scripts/completeness.py --write models/<id>/entry.yaml   # patch the 8 meter lines in place
```

Mirrors `score.py`'s line-patch `--write` (never round-trips YAML), patching each domain's
`completeness:`/`originality:` line in its own block.

## `validate.py` - the CI gate

Walks the three trees, and for every `data.yaml` checks:

1. **Schema** - validates against `../schema/`.
2. **Evidence** - a dimension scored 5 must cite `onehill_verified`/`third_party`
   evidence (publisher-only can't justify the top anchor).
3. **Score consistency** - stored headline/grade equals `score.py`'s computed value.
4. **Freshness** - `last_verified` within the entry's fast SLA (default 30 days).

```bash
python scripts/validate.py                    # everything
python scripts/validate.py models/<id>        # one entry
python scripts/validate.py --no-freshness     # skip the freshness check (offline)
python scripts/validate.py --today 2026-07-25 # pin "today" for reproducible checks
```

Exit code is non-zero if anything fails - that's what the
[`../.github/workflows/validate.yml`](../.github/workflows/validate.yml) job keys on,
including a daily scheduled freshness sweep.

## Roadmap (see [update-automation.md](../methodology/update-automation.md))

Planned collectors/watchers that turn change signals (new versions, CVEs, cert changes,
regulatory updates) into diff PRs. Score/flag/ceiling changes always require human review.
