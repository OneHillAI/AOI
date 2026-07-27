# Keeping the Registry Current - The Refresh Pipeline

**Version:** `1.0` · **Baseline:** July 2026

OneHill's brief calls for documentation that is **"constantly updated."** A hand-written
wiki rots. This registry is therefore built **data-first**: each entry is a validated,
machine-readable data file, and the human dossier is generated from (and cross-checked
against) it. That design is what makes continuous refresh possible instead of a
perpetual manual rewrite.

This document describes how currency is maintained. Parts of it are implemented in
[`scripts/`](../scripts/); parts are the intended pipeline as the project scales.

---

## 1. The data-first architecture

```
schema/*.schema.json        ← the contract every entry must satisfy
        │
        ▼
<entry>/data.yaml           ← the machine-readable source of truth (scores, facts, evidence, dates)
        │  scripts/validate.py   (schema + evidence + freshness checks)
        │  scripts/score.py      (computes AOI from the rubric - scores are derived, not hand-typed)
        ▼
<entry>/README.md           ← the human dossier (carries the generated score block + prose analysis)
```

Because scores are **computed** from the data file by `score.py` against the versioned
[rubric](scoring-rubric.md), they can't drift from the evidence, and a rubric change
re-scores everything deterministically.

## 2. Freshness SLAs

Every entry carries `last_verified` and a `freshness_sla`. `validate.py` fails CI when
an entry is overdue, which turns "staleness" into a visible, actionable bug.

| Field type | Default SLA | Why |
|---|---|---|
| Fast-moving (versions, pricing, provider certs, incidents) | **30 days** | These change constantly. |
| Scores & benchmarks | **90 days** | Re-run/re-assess quarterly or on trigger. |
| Slow-moving (license class, architecture, provenance) | **180 days** | Changes rarely; still checked. |

## 3. Change signals the pipeline watches

The refresh pipeline is driven by **signals**, each mapping to a re-verification job:

| Signal source | Detects | Action |
|---|---|---|
| Model hub API (Hugging Face, etc.) | New versions, new files, license changes, gating changes, format (safetensors/pickle), download/verified-org status | Diff → open a refresh task; re-run affected checks |
| Security feeds (CVE, vendor scanners, incident reports) | New CVEs in loaders/runtimes, malicious-mirror findings, poisoning reports | Raise incident; re-score Dimension 2/4; add changelog entry |
| Regulatory feeds (EU AI Office, standards bodies) | New guidance, template changes, Code-of-Practice updates, systemic-risk designations | Re-assess Dimension 3 mapping |
| Provider status/trust pages | Cert changes, region changes, retention-policy changes, outages | Refresh provider entry |
| Benchmark/eval orgs | New independent results | Update Dimension 5; re-run core suite if warranted |
| Freshness SLA breach | Any entry past its SLA | Force a re-verify task |

## 4. The refresh loop (per entry)

1. **Collect** - pull current facts from primary sources (hub API, trust page, license
   file, security feeds).
2. **Diff** - compare against the stored `data.yaml`.
3. **Verify** - for changed fields, confirm against a primary source; set `source_type`.
4. **Re-score** - run `score.py`; the rubric recomputes affected dimensions.
5. **Changelog** - append a dated entry describing what changed and why.
6. **Stamp** - update `last_verified`.
7. **Regenerate** - rebuild the dossier's generated blocks; open a PR for human review
   of any substantive change (scores, hard flags, ceilings never merge unreviewed).

## 5. Human-in-the-loop guardrails

Automation gathers and flags; **humans approve anything that changes a score, a hard
flag, or a Deployment Ceiling.** The registry's credibility depends on not
auto-publishing a machine's guess. Automated PRs are labelled and require review.
Independent verification (`onehill_verified`) is always a human/OneHill act.

## 6. Provenance of the data itself

The registry practises what it preaches: every datum carries `source_type` and a URL;
`validate.py` rejects a `5`-anchored score backed only by `publisher` evidence
(see the [rubric](scoring-rubric.md#3-evidence--sourcing-rules)). The registry's own
supply chain (who edited what, when) is the git history.

## 7. Roadmap for automation

Implemented now: schema, validation, scoring, freshness checks, CI wiring
([`.github/workflows/validate.yml`](../.github/workflows/validate.yml)).
Planned: hub-API collectors, security-feed watchers, and a scheduled refresh job that
opens diff PRs. See [`docs/roadmap.md`](../docs/roadmap.md).
