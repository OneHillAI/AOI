doc_type: license
entity: glm (tracked MIT cluster) plus the GLM-5.x siblings, read to test whether the cluster is still uniform
source_url: https://huggingface.co/api/models/zai-org/<repo> and https://huggingface.co/<repo>/raw/main/LICENSE (repos listed below)
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

## Per-repo licence matrix (HF API cardData.license plus raw LICENSE file where one exists)

| repo | created | HF licence tag | in-repo LICENSE file | text as read |
|---|---|---|---|---|
| zai-org/GLM-4.5, GLM-4.5-Air, GLM-4.5-Base, GLM-4.6, GLM-4.6-FP8 | 2025-07-20 to 2025-09-29 | mit | none (raw/LICENSE 404) | README of GLM-4.5: "They are released under the MIT open-source license and can be used commercially and for secondary development." |
| zai-org/GLM-4-32B-0414, GLM-4-9B-0414 (GLM-Z1-32B-0414 also lists a LICENSE file, not read) | 2025-04 | mit | yes (identical text in the two read, sha1 f7116387752848072cdee01f208e2605f5660dee) | "MIT License / Copyright (c) 2025 Zhipu AI", standard MIT text, no custom clauses |
| zai-org/GLM-4.7, GLM-4.7-FP8 | 2025-12-22 | mit | none (404) | metadata only |
| zai-org/GLM-5, GLM-5-FP8 | 2026-02-11 | mit | none (404) | metadata only |
| zai-org/GLM-5.1 (FP8 sibling tagged mit, not read) | 2026-04-03 | mit | yes | "MIT License / Copyright (c) 2026 Zhipu AI", standard MIT text |
| zai-org/GLM-5.2 (FP8 sibling tagged mit, not read) | 2026-06-16 | mit | yes (byte-identical to GLM-5.1, sha1 1e005425a9cfb4efab38b2a9834158f4980c9adb) | "MIT License / Copyright (c) 2026 Zhipu AI", standard MIT text; the GLM-5.2 README says "An MIT open-source license" |
| zai-org/GLM-5.3-Flash (GLM-5.3-Flash-BF16 is tagged mit and serves a LICENSE, not read) | 2026-08-25 | mit | yes (Flash; sha1 7b7d94a237ae0a5725e622cbc4402b97a8d69f45) | "MIT License / Copyright (c) 2026 Z.AI Co., Ltd", standard MIT text |
| zai-org/GLM-5.3, GLM-5.3-BF16 | 2026-08-25 | other (license_name: glm-5.3) | yes (sha1 8bc49e9ec1d18dded7ba9d185748c6904958b839) | custom "GLM-5.3 License", see license__glm-5.3__2026-11-19.md |

None of the repos checked is gated (API field gated: false). The exact-text rows were read from raw LICENSE files; rows marked metadata only rest on the HF API licence tag and README.

## Result
- The tracked MIT cluster (GLM-4.5, 4.5-Air, 4.6, GLM-4-32B-0414, GLM-4-9B-0414) is still uniformly MIT. Change against the 2026-07-25 note: the 0414 repos DO now show an in-repo MIT LICENSE file (the July note said none existed); GLM-4.5 and GLM-4.6 still have none, so their MIT rests on HF metadata and the README.
- The licence divergence inside the GLM-5 generation is limited to GLM-5.3 and GLM-5.3-BF16. GLM-5, 5.1, 5.2 and 5.3-Flash are MIT.
- GitHub code repos zai-org/GLM-4 and zai-org/GLM-4.5 carry an Apache-2.0 LICENSE file (raw.githubusercontent.com, first lines read); the weights are MIT. Not scored.
