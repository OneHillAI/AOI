#!/usr/bin/env python3
"""Validate registry entries: JSON Schema + evidence/doc rules + freshness + score/completeness consistency.

Walks models/, inference-providers/, hosting-providers/, finds every `data.yaml` (v1) and
`entry.yaml` (v2 library entry), and checks it. This is what the CI job runs.

Errors (fail CI):
  1. Schema         — validates against the matching schema (dispatched by schema_version).
  2. Evidence rule  — a dimension scored 5 needs a non-'publisher' evidence ref.
  3. Ref integrity  — every evidence_ref / doc-item ref resolves in evidence[].
  4. Documentation  — (v2) domain/item rules, aggregated⇒refs, onehill_generated⇒verified ref,
                      and markdown ↔ yaml item-key parity across the four domain .md files.
  5. Consistency    — stored headline/grade == score.py; stored completeness/originality == completeness.py.
  6. Freshness      — last_verified within the fast-moving SLA (default 30 days).

Warnings (reported, do not fail CI):
  - Evidence audit  — onehill_verified evidence lacking a `method`, or whose claim looks documentary.
  - Checklist       — a required expected item missing, or an item key not in the checklist.

Usage:
    python scripts/validate.py                 # everything
    python scripts/validate.py models/foo      # one entry dir or file
    python scripts/validate.py --no-freshness  # skip the freshness check (offline)
    python scripts/validate.py --today 2026-07-25

Dependencies: PyYAML, jsonschema.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover
    sys.exit("Requires PyYAML and jsonschema: pip install pyyaml jsonschema")

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schema"
sys.path.insert(0, str(ROOT / "scripts"))

SCHEMA_BY_TREE = {
    "models": "model.schema.json",
    "inference-providers": "inference-provider.schema.json",
    "hosting-providers": "hosting-provider.schema.json",
}
DOC_DOMAINS = ["assess", "implement", "use", "support"]
# Five cross-cutting "assessed signals" surfaced at the top of every v2 entry (Track C).
# Each has its own ordered level vocabulary (best → worst); the schema only checks shape,
# so this is the source of truth for the allowed levels.
SIGNAL_LEVELS = {
    "trainability": ["full", "partial", "limited", "none"],
    "knowledge_structure": ["strong", "moderate", "weak"],
    "specialization": ["strong", "moderate", "weak"],
    "exchangeability": ["high", "medium", "low"],
    "misuse_exposure": ["benchmarked", "partial", "unbenchmarked"],
}
# Closing verdict — real ownership (methodology/ownership.md). A single level built from four
# factors. Required for model and inference-provider entries.
OWNERSHIP_LEVELS = ["full", "substantial", "partial", "limited", "none"]
OWNERSHIP_FACTORS = ["use_modify", "transparency", "reliability", "data_control"]
FACTOR_LEVELS = ["strong", "moderate", "weak"]
# Binding primary documents that can justify a top rating; marketing cannot.
BINDING_DOCS = {"terms", "privacy_policy", "dpa", "license", "security", "technical_report", "model_card"}
ITEM_MARKER_RE = re.compile(r"<!--\s*item:\s*([a-z0-9-]+)\s*-->")
DOCUMENTARY_CLAIM_RE = re.compile(r"\b(licen[cs]e|hosted|available|published|downloadable|checksums?)\b", re.I)
DEFAULT_FAST_SLA_DAYS = 30


def load_schema(name: str) -> Draft202012Validator:
    return Draft202012Validator(json.loads((SCHEMA_DIR / name).read_text()))


def tree_for(path: Path) -> str | None:
    for tree in SCHEMA_BY_TREE:
        if tree in path.parts:
            return tree
    return None


SCHEMA_V2_BY_TREE = {
    "models": "model.v2.schema.json",
    "inference-providers": "inference-provider.v2.schema.json",
    "hosting-providers": "hosting-provider.v2.schema.json",
}


def schema_for(path: Path, data: dict) -> str | None:
    tree = tree_for(path)
    if not tree:
        return None
    if str(data.get("schema_version")) == "2.0" and tree in SCHEMA_V2_BY_TREE:
        return SCHEMA_V2_BY_TREE[tree]
    return SCHEMA_BY_TREE[tree]


def is_v2(data: dict) -> bool:
    return str(data.get("schema_version")) == "2.0" and "documentation" in data


# --- errors -------------------------------------------------------------------------

def check_evidence(data: dict) -> list[str]:
    """A dimension scored 5 needs at least one non-publisher evidence reference."""
    errs = []
    evidence = {e.get("id"): e for e in data.get("evidence", []) if e.get("id")}
    for name, dim in data.get("score", {}).get("dimensions", {}).items():
        if dim.get("score") == 5:
            refs = dim.get("evidence_refs", []) or []
            if not any(evidence.get(r, {}).get("source_type") in {"onehill_verified", "third_party"} for r in refs):
                errs.append(f"dimension '{name}' scored 5 but has no onehill_verified/third_party evidence ref")
    return errs


def check_ref_integrity(data: dict) -> list[str]:
    """Every evidence_ref (score dims) and doc-item ref must exist in evidence[]."""
    errs = []
    ids = {e.get("id") for e in data.get("evidence", []) if e.get("id")}
    for name, dim in data.get("score", {}).get("dimensions", {}).items():
        for r in dim.get("evidence_refs", []) or []:
            if r not in ids:
                errs.append(f"dimension '{name}' references unknown evidence id '{r}'")
    if is_v2(data):
        for domain in DOC_DOMAINS:
            for it in data["documentation"].get(domain, {}).get("items", []):
                for r in it.get("refs", []) or []:
                    if r not in ids:
                        errs.append(f"{domain} item '{it.get('key')}' references unknown evidence id '{r}'")
    return errs


def check_documentation(data: dict, path: Path) -> list[str]:
    """v2 documentation rules + markdown/yaml item-key parity."""
    errs = []
    evidence = {e.get("id"): e for e in data.get("evidence", []) if e.get("id")}
    for domain in DOC_DOMAINS:
        items = data["documentation"].get(domain, {}).get("items", [])
        seen = set()
        for it in items:
            key = it.get("key")
            if key in seen:
                errs.append(f"{domain}: duplicate item key '{key}'")
            seen.add(key)
            st = it.get("source_type")
            if st == "aggregated" and not (it.get("refs") or []):
                errs.append(f"{domain} item '{key}': aggregated content needs at least one refs[] citation")
            if st == "onehill_generated":
                strong = any(evidence.get(r, {}).get("source_type") == "onehill_verified"
                             for r in (it.get("refs") or []))
                if not strong:
                    errs.append(f"{domain} item '{key}': onehill_generated must cite an onehill_verified evidence ref")

        # markdown <-> yaml parity: no orphan prose, and every non-gap item has a section.
        md = path.parent / f"{domain}.md"
        markers = set(ITEM_MARKER_RE.findall(md.read_text())) if md.exists() else set()
        item_keys = {it.get("key") for it in items}
        for m in markers - item_keys:
            errs.append(f"{domain}.md has a section '<!-- item: {m} -->' with no matching item in entry.yaml")
        for it in items:
            if it.get("source_type") != "gap" and it.get("key") not in markers:
                errs.append(f"{domain} item '{it.get('key')}' has no '<!-- item: {it.get('key')} -->' section in {domain}.md")
    return errs


def check_signals(data: dict) -> list[str]:
    """v2 assessed-signals rules: all five present, level in its vocabulary, refs resolve."""
    errs = []
    signals = data.get("signals")
    if not isinstance(signals, dict):
        return ["signals: block is missing or not a mapping"]
    ids = {e.get("id") for e in data.get("evidence", []) if e.get("id")}
    for key, allowed in SIGNAL_LEVELS.items():
        s = signals.get(key)
        if not isinstance(s, dict):
            errs.append(f"signals: missing signal '{key}'")
            continue
        if s.get("level") not in allowed:
            errs.append(f"signals.{key}: level {s.get('level')!r} not one of {allowed}")
        for r in s.get("refs", []) or []:
            if r not in ids:
                errs.append(f"signals.{key} references unknown evidence id '{r}'")
    for key in set(signals) - set(SIGNAL_LEVELS):
        errs.append(f"signals: unknown signal '{key}' (expected only {list(SIGNAL_LEVELS)})")
    return errs


def check_ownership(data: dict) -> list[str]:
    """The single closing verdict: level in vocabulary, four factors each with a level+rationale,
    non-empty verdict."""
    own = data.get("ownership")
    if not isinstance(own, dict):
        return ["ownership: block is missing (required for models and inference providers)"]
    errs = []
    if own.get("level") not in OWNERSHIP_LEVELS:
        errs.append(f"ownership.level: {own.get('level')!r} not one of {OWNERSHIP_LEVELS}")
    factors = own.get("factors")
    if not isinstance(factors, dict):
        errs.append("ownership.factors: missing or not a mapping")
    else:
        for f in OWNERSHIP_FACTORS:
            fv = factors.get(f)
            if not isinstance(fv, dict):
                errs.append(f"ownership.factors: missing factor '{f}'")
                continue
            if fv.get("level") not in FACTOR_LEVELS:
                errs.append(f"ownership.factors.{f}.level: {fv.get('level')!r} not one of {FACTOR_LEVELS}")
            if not str(fv.get("rationale") or "").strip():
                errs.append(f"ownership.factors.{f}.rationale: is empty")
        for extra in set(factors) - set(OWNERSHIP_FACTORS):
            errs.append(f"ownership.factors: unknown factor '{extra}'")
    if not str(own.get("verdict") or "").strip():
        errs.append("ownership: verdict is empty")
    return errs


def check_grounding(data: dict) -> list[str]:
    """Primary-document grounding gate (fires only for entries that use the doc_type vocabulary):
    a dimension scored 5 must cite a retrieved binding document or a third-party attestation —
    a marketing page or an unretrieved doc cannot justify a top rating."""
    errs = []
    ev = {e.get("id"): e for e in data.get("evidence", []) if e.get("id")}
    entry_uses_doc_type = any(e.get("doc_type") is not None for e in data.get("evidence", []))
    if not entry_uses_doc_type:
        return errs
    for name, dim in data.get("score", {}).get("dimensions", {}).items():
        if dim.get("score") != 5:
            continue
        refs = [ev.get(r, {}) for r in (dim.get("evidence_refs") or [])]
        strong = any(
            (e.get("source_type") in {"third_party", "onehill_verified"})
            or (e.get("retrieved") is True and e.get("doc_type") in BINDING_DOCS)
            for e in refs
        )
        if not strong:
            errs.append(f"dimension '{name}' scored 5 but no ref is a retrieved binding document "
                        f"({sorted(BINDING_DOCS)}) or a third-party attestation — marketing/unverified "
                        f"cannot justify a 5")
    return errs


def check_freshness(data: dict, today: dt.date) -> list[str]:
    lv = data.get("last_verified")
    if not lv:
        return ["missing last_verified"]
    try:
        d = dt.date.fromisoformat(str(lv))
    except ValueError:
        return [f"last_verified not an ISO date: {lv!r}"]
    sla = (data.get("freshness_sla") or {}).get("fast_days", DEFAULT_FAST_SLA_DAYS)
    age = (today - d).days
    return [f"stale: last_verified {lv} is {age}d old (fast SLA {sla}d)"] if age > sla else []


def check_score_consistency(data: dict) -> list[str]:
    try:
        from score import compute  # type: ignore
        result = compute(data)
    except Exception as e:  # noqa: BLE001
        return [f"could not compute score: {e}"]
    stored = data.get("score", {})
    errs = []
    if stored.get("headline") not in (None, result["headline"]):
        errs.append(f"stored headline {stored.get('headline')} != computed {result['headline']}")
    if stored.get("grade") not in (None, result["grade"]):
        errs.append(f"stored grade {stored.get('grade')} != computed {result['grade']}")
    return errs


def check_completeness_consistency(data: dict) -> list[str]:
    try:
        from completeness import compute  # type: ignore
        result = compute(data)
    except Exception as e:  # noqa: BLE001
        return [f"could not compute completeness: {e}"]
    errs = []
    for d in DOC_DOMAINS:
        stored = data["documentation"].get(d, {})
        for meter in ("completeness", "originality"):
            if stored.get(meter) != result[d][meter]:
                errs.append(f"documentation.{d}.{meter}: stored {stored.get(meter)} != computed {result[d][meter]}")
    return errs


# --- warnings -----------------------------------------------------------------------

def audit_evidence(data: dict) -> list[str]:
    warns = []
    for e in data.get("evidence", []):
        if e.get("source_type") == "onehill_verified":
            if not e.get("method"):
                warns.append(f"evidence '{e.get('id')}' is onehill_verified but has no `method` "
                             f"(what did OneHill actually run?)")
            if DOCUMENTARY_CLAIM_RE.search(e.get("claim", "")):
                warns.append(f"evidence '{e.get('id')}' tagged onehill_verified but its claim reads "
                             f"documentary — likely should be publisher/third_party")
    return warns


def audit_checklist(data: dict) -> list[str]:
    if not is_v2(data):
        return []
    warns = []
    try:
        from completeness import CHECKLIST_BY_PROFILE, entry_profile  # type: ignore
        name = CHECKLIST_BY_PROFILE[entry_profile(data)]
        checklist = yaml.safe_load((ROOT / "checklists" / name).read_text())
    except Exception:  # noqa: BLE001
        return []
    for domain in DOC_DOMAINS:
        expected = {x["key"]: x for x in checklist["domains"][domain]["expected"]}
        present = {it.get("key") for it in data["documentation"].get(domain, {}).get("items", [])}
        for key, spec in expected.items():
            if spec.get("required") and key not in present:
                warns.append(f"{domain}: required checklist item '{key}' is not documented")
        for key in present - set(expected):
            warns.append(f"{domain}: item '{key}' is not in checklists/model.yaml (typo? or update the checklist)")
    return warns


# --- driver -------------------------------------------------------------------------

def find_entry_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    found = list(target.rglob("data.yaml")) + list(target.rglob("entry.yaml"))
    return sorted(found)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("targets", nargs="*", type=Path)
    ap.add_argument("--no-freshness", action="store_true")
    ap.add_argument("--today", type=str)
    args = ap.parse_args()

    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    targets = args.targets or [ROOT / t for t in SCHEMA_BY_TREE]
    files: list[Path] = []
    for t in targets:
        files.extend(find_entry_files(t if t.is_absolute() else ROOT / t))
    files = sorted(set(files))

    if not files:
        print("no entry files found (nothing to validate yet).")
        return 0

    schemas: dict[str, Draft202012Validator] = {}
    total_errors = total_warnings = 0
    for f in files:
        data = yaml.safe_load(f.read_text())
        schema_name = schema_for(f, data)
        if not schema_name:
            print(f"[skip] {f} — not under a known tree")
            continue
        schemas.setdefault(schema_name, load_schema(schema_name))

        errs: list[str] = [f"schema: {e.message}" for e in schemas[schema_name].iter_errors(data)]
        errs += check_evidence(data)
        errs += check_ref_integrity(data)
        errs += check_score_consistency(data)
        if is_v2(data):
            errs += check_documentation(data, f)
            if "signals" in data:  # model-specific highlight lens; providers use their own
                errs += check_signals(data)
            try:
                from completeness import entry_profile  # type: ignore
                profile = entry_profile(data)
            except Exception:  # noqa: BLE001
                profile = "model"
            if profile in ("model", "inference"):  # hosting is hidden; ownership not required there
                errs += check_ownership(data)
            errs += check_grounding(data)
            errs += check_completeness_consistency(data)
        if not args.no_freshness:
            errs += check_freshness(data, today)

        warns = audit_evidence(data) + audit_checklist(data)

        rel = f.relative_to(ROOT)
        if errs:
            total_errors += len(errs)
            print(f"[FAIL] {rel}")
            for e in errs:
                print(f"       - {e}")
        else:
            print(f"[ ok ] {rel}")
        for w in warns:
            total_warnings += 1
            print(f"       ! warn: {w}")

    n = len(files)
    print(f"\n{n} entr{'y' if n==1 else 'ies'} checked, {total_errors} error(s), {total_warnings} warning(s).")
    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
