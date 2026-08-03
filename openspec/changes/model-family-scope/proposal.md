## Why

The registry mixes two incompatible entry granularities. Some entries are a single release
(`kimi-k3`, `gpt-oss`); others aggregate many generations, and even several licences, under one
family name. This breaks the scoring model, because an entry carries exactly one `openness.tier`,
one `license` block, and one floor-weighted ownership verdict and headline. That can only be honest
if every checkpoint in the entry shares those attributes, and today they do not:

- `mistral` puts Apache-2.0 models (7B, Mixtral, Nemo, Small) and MRL non-commercial models
  (Ministral, Large 2) under one `commercial_use` value and one legal score. One is necessarily
  wrong.
- `deepseek` folds in R1-Distill, whose licence is the Llama or Qwen base, not DeepSeek's, so the
  entry's licence field cannot be true for its own members.
- `meta-llama` spans Llama 3.1, 3.3, 4 and the Guard tools under one score.

An aggregated entry whose members differ on the scored attributes produces an average of
incompatibles, the exact failure the index exists to prevent. The naming was inconsistent too:
`kimi` scored Kimi K2 but wore the bare family name, while `kimi-k3` was version-named.

## What Changes

Define the entry scope and a family relation, resolve the family-versus-single question with an
explicit relevance test, and specify the full implementation this change delivers once built.

1. **Only a release is scored; a family is never scored.** A family is a grouping over release
   entries and carries no score, grade, tier, licence, or ownership verdict. Only a release entry (a
   model) is scored. A family is not a model, so it cannot be scored.
2. **Every entry always carries a `family` relation `{id, name}`.** The relation is present for
   every entry unconditionally, including a single-release family, not only when releases within the
   family differ. It is added as a REQUIRED field in `schema/model.v2.schema.json`, and every entry
   is tagged with its family.
3. **The scored unit is a RELEASE:** checkpoints with uniform openness tier, licence, provenance and
   safety posture. Co-released uniform variants share one entry via `variants`.
4. **The split rule (relevance test):** a family is split into multiple entries when, and only when,
   its releases diverge on a scored attribute (licence first, also openness tier, provenance,
   safety). The family relation is always present either way; only the number of entries is
   conditional.
5. **Entries are named by release, not a bare family name.** Rename `kimi` to `kimi-k2` (done in
   this change).
6. **The site showcases every release and groups by family,** and the family node itself is never
   scored.
7. **Splits:** split the mixed-licence families (mistral, meta-llama, deepseek) and review the rest
   (glm, qwen, ai2-olmo, eurollm), each split grounded per release.

## Non-Goals

- No new scoring dimensions and no re-weighting; each split release keeps its evidence-grounded score
  under the existing rubric.
- No family-level score of any kind is introduced; the family is a relation only.

## Impact

- Affected specs: capability `registry` (only-release-scored, family-always, schema requirement, site
  showcase, entry scope, naming, split rule).
- Affected code (the build): `schema/model.v2.schema.json` (add the required `family` object),
  every `models/*/entry.yaml` (tag with `family`), `site/src/lib/entries.ts` (group the showcase by
  family, family node unscored), and the aggregated entries (split per the rule).
- Delivered in this change already: the Kimi rename (`models/kimi` to `models/kimi-k2`,
  `docs/primary-sources/kimi` to `docs/primary-sources/kimi-k2`), `scripts/validate.py` 0 errors.
- Governance: this OpenSpec change is published to the PUBLIC AOI repo so the pipeline is publicly
  visible, humans and agents both shown, per ASDD STANDARD 1.4 (SHOULD) - adoption is verifiable,
  not asserted. The follow-on `schema/**` and `site/**` edits remain protected-path build steps done
  with a named human.
- `family` is a REQUIRED field once the schema lands. The schema edit (task 2.1) and the tagging of
  every entry (task 2.2) MUST land atomically in the build change, or `scripts/validate.py` would see
  a required field on untagged entries. This proposal change touches neither the schema nor the
  entries beyond the Kimi rename, so it does not break validation.
