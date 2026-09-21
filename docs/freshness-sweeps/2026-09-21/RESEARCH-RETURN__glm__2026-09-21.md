# Research return: glm (freshness re-verification) - 2026-09-21

**Verdict: tracked entry re-verified CLEAN -> bump `last_verified` to 2026-09-21, with a new licence-divergent sibling ACTION for the code session.**

- **Licence (tracked MIT cluster):** unchanged. The GLM models tracked under this entry remain as recorded (MIT-cluster). No revision this pass.
- **Supersession - ACTION (new entity):** Z.ai/Zhipu has shipped a **GLM-5 generation** (**GLM-5, 5.1, 5.2, 5.3, 5.3-Flash**) governed by a **custom "GLM-5.3 License"** that is **licence-divergent** from the tracked GLM cluster - it adds a **$10B MaaS security-review gate** (a security-review requirement triggered above a large Model-as-a-Service revenue/scale threshold). This is not an MIT model and must **not** be folded into the `glm` entry - it warrants a **new `glm-5` entity/family split**. Flagged for the code session.
- **Safety / availability:** tracked repos live; no adverse finding on the tracked entry. The GLM-5.3 gate is a governance term on the *new* line, captured in its clause file.

`retrieved: true` - GLM model cards + GLM-5.3 License re-read. Clause file: `license__glm-5__2026-09-21.md`.
