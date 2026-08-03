## 1. Convention and the Kimi rename (done)
- [x] 1.1 Record the entry-scope, only-release-scored, family-always, site-showcase, naming and split
      rules in the spec delta (`specs/registry/spec.md`).
- [x] 1.2 Rename `models/kimi` to `models/kimi-k2`: `id: kimi-k2`, `name: "Kimi K2 (Moonshot AI)"`,
      dossier headers, and `docs/primary-sources/kimi` to `docs/primary-sources/kimi-k2`. Score
      unchanged (62.8, grade C); `scripts/validate.py` 0 errors.

## 2. Schema and entry tagging (build; `schema/**` is a protected path; land 2.1-2.3 ATOMICALLY so `validate.py` never sees a required `family` on untagged entries)
- [ ] 2.1 Add a REQUIRED `family` object `{ id: string, name: string }` to
      `schema/model.v2.schema.json` (top-level `additionalProperties` is `false`).
- [ ] 2.2 Tag every entry with its `family` so none lacks the relation, for example
      `kimi-k2` and `kimi-k3` -> `{id: kimi, name: Kimi}`, the Nemotron entry -> `{id: nemotron,
      name: NVIDIA Nemotron}`, `gpt-oss` -> `{id: gpt-oss, name: OpenAI gpt-oss}`. A single-release
      family still gets the relation.
- [ ] 2.3 `scripts/validate.py` 0 errors with `family` required and present on all entries.

## 3. Site showcase and grouping (build; `site/**`)
- [ ] 3.1 `site/src/lib/entries.ts` exposes the `family` relation; the site lists every release (the
      full showcase) and groups them by family, a reader navigating family -> releases.
- [ ] 3.2 The family node is never scored: no score, grade, tier or verdict is rendered on a family,
      only on its release entries. `cd site && npm run build` clean.

## 4. Split the mixed-licence families (build; needs the research handover)
- [ ] 4.1 Split `mistral` into per-licence entries (Apache-2.0 releases vs MRL non-commercial:
      Ministral, Large 2), each carrying `family: {id: mistral, name: Mistral}`.
- [ ] 4.2 Split `meta-llama` by release and licence (Llama 3.1/3.3, Llama 4, Guard tools), each under
      `family: {id: meta-llama, name: Meta Llama}`.
- [ ] 4.3 Split `deepseek` (V3, R1, R1-Distill whose licence is the Llama/Qwen base), each under
      `family: {id: deepseek, name: DeepSeek}`.
- [ ] 4.4 Review `glm`, `qwen`, `ai2-olmo`, `eurollm`: split only where releases diverge on a scored
      attribute; otherwise keep one entry, still tagged with `family`.

## 5. Verification
- [ ] 5.1 After the build, `scripts/validate.py` 0 errors, `openspec validate --strict` valid, and
      every entry's licence, openness tier and ownership verdict is true for all checkpoints it
      covers; no family carries a score.
