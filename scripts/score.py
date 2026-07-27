#!/usr/bin/env python3
"""Compute the AI Ownership Index (AOI) from an entry's data file.

Scores are DERIVED from the per-dimension anchors in a `data.yaml`, not hand-typed,
so they can never drift from the evidence. See methodology/scoring-rubric.md and
methodology/provider-scoring-rubric.md for the weights and anchors implemented here.

Usage:
    python scripts/score.py path/to/data.yaml            # print computed score
    python scripts/score.py --check path/to/data.yaml    # exit 1 if stored != computed
    python scripts/score.py --write path/to/data.yaml    # write computed score back

Dependencies: PyYAML (pip install pyyaml).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

# --- Weights (must match the rubric; changing these is a rubric version bump) ---------

MODEL_WEIGHTS = {
    "openness": 0.18,
    "provenance": 0.16,
    "legal": 0.16,
    "safety": 0.16,
    "performance": 0.14,
    "operational": 0.12,
    "governance": 0.08,
}

INFERENCE_WEIGHTS = {
    "data_governance": 0.24,
    "compliance": 0.18,
    "residency": 0.16,
    "security": 0.14,
    "reliability": 0.12,
    "transparency_lockin": 0.10,
    "cost": 0.06,
}

HOSTING_WEIGHTS = {
    "provenance_integrity": 0.26,
    "format_loader_safety": 0.18,
    "license_governance": 0.16,
    "security_track_record": 0.16,
    "transparency": 0.12,
    "ecosystem_portability": 0.12,
}

# Hard-flag ceilings: flag substring -> max grade allowed.
GRADE_ORDER = ["F", "D", "C", "B", "A"]


def grade_for(score: float) -> str:
    if score >= 85:
        return "A"
    if score >= 70:
        return "B"
    if score >= 55:
        return "C"
    if score >= 40:
        return "D"
    return "F"


def cap_grade(grade: str, ceiling: str) -> str:
    """Return the lower of grade and ceiling per GRADE_ORDER."""
    if GRADE_ORDER.index(ceiling) < GRADE_ORDER.index(grade):
        return ceiling
    return grade


def flag_ceiling(flags: list[str]) -> str | None:
    """Derive the strictest grade ceiling implied by hard flags.

    Flags are free text in the data file; we match on documented keywords so the
    ceiling logic in scoring-rubric.md is applied deterministically.
    """
    ceiling = None
    rules = [
        (("malicious", "backdoor"), "F"),
        (("no accountable publisher", "unidentifiable publisher"), "D"),
        (("systemic-risk", "article 55"), "C"),
        (("pickle-only", "pickle only", "no safetensors"), "C"),
        (("license prohibits", "prohibited use"), "C"),
        (("trains on inputs by default",), "D"),
    ]
    for kws, cap in rules:
        for f in flags:
            fl = f.lower()
            if any(k in fl for k in kws):
                if ceiling is None or GRADE_ORDER.index(cap) < GRADE_ORDER.index(ceiling):
                    ceiling = cap
    return ceiling


def weights_for(data: dict) -> dict:
    profile = data.get("profile")
    kind = data.get("kind")
    if profile == "inference":
        return INFERENCE_WEIGHTS
    if kind in {"hub", "local_runner", "serving_engine", "cloud_registry", "package_ecosystem"}:
        return HOSTING_WEIGHTS
    return MODEL_WEIGHTS


def compute(data: dict) -> dict:
    weights = weights_for(data)
    dims = data.get("score", {}).get("dimensions", {})
    missing = [d for d in weights if d not in dims]
    if missing:
        raise ValueError(f"missing dimension scores: {missing}")

    total = 0.0
    for dim, w in weights.items():
        s = dims[dim].get("score")
        if s is None or not (0 <= s <= 5):
            raise ValueError(f"dimension '{dim}' has invalid score: {s!r}")
        total += w * (s / 5.0)
    headline = round(100 * total, 1)
    grade = grade_for(headline)

    flags = data.get("score", {}).get("hard_flags", []) or []
    ceiling = flag_ceiling(flags)
    if ceiling:
        grade = cap_grade(grade, ceiling)

    return {"headline": headline, "grade": grade, "ceiling_applied": ceiling}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", type=Path)
    ap.add_argument("--check", action="store_true", help="exit 1 if stored score != computed")
    ap.add_argument("--write", action="store_true", help="write computed score back into the file")
    args = ap.parse_args()

    data = yaml.safe_load(args.path.read_text())
    result = compute(data)
    stored = data.get("score", {})

    print(f"{args.path}: {result['headline']}  grade {result['grade']}"
          + (f"  (capped by hard flag -> {result['ceiling_applied']})" if result["ceiling_applied"] else ""))

    if args.check:
        ok = (stored.get("headline") == result["headline"] and stored.get("grade") == result["grade"])
        if not ok:
            print(f"  MISMATCH: stored headline={stored.get('headline')} grade={stored.get('grade')}",
                  file=sys.stderr)
            return 1
    if args.write:
        # Patch ONLY the computed `headline:` and `grade:` lines in place. We must not
        # round-trip the whole file through safe_dump: YAML 1.1 coerces unquoted
        # yes/no/on/off enum values to booleans on load, and dumping them back would
        # silently corrupt those fields. Line-targeted replacement preserves everything.
        import re
        text = args.path.read_text()
        text, n_h = re.subn(r"(?m)^(?P<i>\s*)headline:.*$",
                            lambda m: f"{m.group('i')}headline: {result['headline']}", text, count=1)
        text, n_g = re.subn(r"(?m)^(?P<i>\s*)grade:.*$",
                            lambda m: f"{m.group('i')}grade: {result['grade']}", text, count=1)
        if n_h == 0 or n_g == 0:
            print("  WARNING: could not find headline/grade lines to patch; file unchanged.",
                  file=sys.stderr)
            return 1
        args.path.write_text(text)
        print("  written (headline/grade patched in place).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
