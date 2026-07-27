# Methodology versioning

The scoring methodology is versioned so a rating can always be read against the exact rules
that produced it. Every entry stamps the `rubric_version` it was scored under, and the site
shows it, so a score is never floating free of its criteria.

## Scheme

The methodology uses semantic versioning:

- **MAJOR** - a change to a dimension anchor, a weight, an ownership-factor cutoff, or the
  grade bands. A change like this can move scores, so it requires re-scoring every affected
  entry in the same change, and a note in the changelog listing the moves.
- **MINOR** - a new dimension, a new evidence `doc_type`, or a clarified anchor that does not
  move existing scores.
- **PATCH** - wording and typo fixes with no scoring effect.

## Process

A version bump is proposed as a pull request against the methodology with a rationale and a
re-score plan for the entries it touches. The score-change steps are in
[../CONTRIBUTING.md](../CONTRIBUTING.md); the standard's own version is incremented per
[../STANDARD.md](../STANDARD.md), and [../CHANGELOG.md](../CHANGELOG.md) records the bump and
the resulting score moves. Because scores are derived by `scripts/score.py` from the dimension
anchors, a bump plus a re-score is reproducible: anyone can recompute the new headline from the
changed rules.

## Current version

The current rubric version is **1.1**. Every dimension defines all six rungs (0 to 5), and the
ownership-factor cutoffs are stated explicitly (see [ownership.md](ownership.md) and
[scoring-rubric.md](scoring-rubric.md)). All sixteen entries carry `rubric_version: '1.1'`.

### Version log

- **1.1** - Every rung 0 to 5 defined for all fourteen dimensions; ownership-factor cutoffs
  tightened (reliability needs two of three at 4 or more; use-and-modify strong requires an
  ungated licence; a lone moderate on use-and-modify or data-control caps ownership at partial).
  All sixteen entries re-scored.
- **1.0** - Initial rubric: seven model and seven inference-provider dimensions, anchored at
  0, 3 and 5 with the middle rungs interpolated.
