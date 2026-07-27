#!/usr/bin/env python3
"""Compute per-domain documentation completeness & originality for a v2 library entry.

Two meters per domain (Assess / Implement / Use / Support), both DERIVED from the entry's
documentation items and the expected-items checklist — never hand-typed:

  completeness = coverage of the expected items (aggregated and onehill_generated count
                 equally; a documented `gap` counts 0 but is still "addressed").
  originality  = share of this domain's credited items that OneHill generated/verified
                 itself (the "we didn't just copy the model card" signal).

Formulas (see methodology + docs/documentation-taxonomy.md and the approved plan):
  credit(item): coverage full -> 1.0, partial -> 0.5, gap or absent -> 0.0
  completeness[d] = 100 * Σ(weightᵢ · creditᵢ over EXPECTED items) / Σ(weightᵢ)
  originality[d]  = 100 * (# credited items that are onehill_generated) / (# credited items)

Usage:
    python scripts/completeness.py path/to/entry.yaml
    python scripts/completeness.py --check path/to/entry.yaml   # exit 1 if stored != computed
    python scripts/completeness.py --write path/to/entry.yaml   # patch the 8 meter lines in place

Dependencies: PyYAML. Checklist: checklists/model.yaml (models only for now).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ["assess", "implement", "use", "support"]


CHECKLIST_BY_PROFILE = {
    "model": "model.yaml",
    "inference": "inference-provider.yaml",
    "hosting": "hosting-provider.yaml",
}


def entry_profile(data: dict) -> str:
    """Which library profile an entry belongs to (selects checklist + score dimensions)."""
    if data.get("profile") == "inference":
        return "inference"
    if "format_safety" in data or "distribution_mechanism" in data:  # hosting-provider markers
        return "hosting"
    return "model"


def load_checklist(data: dict) -> dict:
    name = CHECKLIST_BY_PROFILE[entry_profile(data)]
    return yaml.safe_load((ROOT / "checklists" / name).read_text())


def credit(item: dict) -> float:
    if item.get("source_type") == "gap":
        return 0.0
    cov = item.get("coverage")
    return {"full": 1.0, "partial": 0.5}.get(cov, 0.0)


def compute(data: dict) -> dict:
    checklist = load_checklist(data)
    doc = data.get("documentation") or {}
    out = {}
    for domain in DOMAINS:
        expected = checklist["domains"][domain]["expected"]
        items = {it["key"]: it for it in (doc.get(domain, {}) or {}).get("items", [])}

        num = den = 0.0
        for exp in expected:
            w = float(exp.get("weight", 1.0))
            den += w
            it = items.get(exp["key"])
            num += w * (credit(it) if it else 0.0)
        completeness = round(100 * num / den, 1) if den else 0.0

        # Originality is computed over ALL credited items in the domain (incl. any beyond
        # the checklist), so extra OneHill work is rewarded.
        credited = [it for it in items.values()
                    if it.get("source_type") in {"aggregated", "onehill_generated"}
                    and it.get("coverage") in {"full", "partial"}]
        onehill = [it for it in credited if it.get("source_type") == "onehill_generated"]
        originality = round(100 * len(onehill) / len(credited), 1) if credited else 0.0

        out[domain] = {"completeness": completeness, "originality": originality}
    return out


def _patch(text: str, results: dict) -> tuple[str, int]:
    """Patch each domain's `completeness:`/`originality:` lines in place.

    Line-targeted (never round-trips YAML) to preserve quoting of yes/no enum values,
    exactly like score.py --write. Tracks the current domain by its 2-space header so the
    right values land in the right block.
    """
    domain_re = re.compile(r"^(\s{2})(assess|implement|use|support):\s*$")
    comp_re = re.compile(r"^(\s+)completeness:.*$")
    orig_re = re.compile(r"^(\s+)originality:.*$")
    current = None
    patched = 0
    out_lines = []
    for line in text.splitlines():
        dm = domain_re.match(line)
        if dm:
            current = dm.group(2)
            out_lines.append(line)
            continue
        if current:
            cm = comp_re.match(line)
            if cm:
                out_lines.append(f"{cm.group(1)}completeness: {results[current]['completeness']}")
                patched += 1
                continue
            om = orig_re.match(line)
            if om:
                out_lines.append(f"{om.group(1)}originality: {results[current]['originality']}")
                patched += 1
                continue
        out_lines.append(line)
    trailing = "\n" if text.endswith("\n") else ""
    return "\n".join(out_lines) + trailing, patched


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", type=Path)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    data = yaml.safe_load(args.path.read_text())
    if "documentation" not in data:
        print(f"{args.path}: no documentation block (not a v2 entry) — skipping.")
        return 0

    results = compute(data)
    line = "  ".join(f"{d}:{results[d]['completeness']}/{results[d]['originality']}" for d in DOMAINS)
    print(f"{args.path}\n  completeness/originality  {line}")

    rc = 0
    if args.check:
        for d in DOMAINS:
            stored = data["documentation"].get(d, {})
            for meter in ("completeness", "originality"):
                if stored.get(meter) != results[d][meter]:
                    print(f"  MISMATCH {d}.{meter}: stored={stored.get(meter)} computed={results[d][meter]}",
                          file=sys.stderr)
                    rc = 1
    if args.write:
        text = args.path.read_text()
        new_text, n = _patch(text, results)
        if n != 2 * len(DOMAINS):
            print(f"  WARNING: patched {n} lines, expected {2*len(DOMAINS)} "
                  f"(each domain needs a completeness: and originality: line). File unchanged.",
                  file=sys.stderr)
            return 1
        args.path.write_text(new_text)
        print("  written (8 meter lines patched in place).")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
