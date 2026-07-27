# Standards the AI Ownership Index is built to

These are the public standards and frameworks the methodology grounds on. Following the same rule
we use for model and provider evidence: **link the canonical source, store a short dated extract
where the standard defines a gate we use, and never mirror the whole document** (most are
copyrighted, and a full copy goes stale). Extracts marked retrieved:no still need their verbatim
defining clause captured by a browser session; the canonical sites (opensource.org, eur-lex,
arxiv) return HTTP 403 to the code session.

## _sources.md
```
doc_type    | source_url                                                | retrieval_date | exists | retrieved | how the methodology uses it
third_party | https://arxiv.org/abs/2403.13784                          | 2026-07-26     | yes    | no        | Model Openness Framework: the openness-tier taxonomy our `openness.tier` mirrors (fully open vs open weights). Capture the tier definitions verbatim
third_party | https://opensource.org/ai/open-source-ai-definition       | 2026-07-26     | yes    | no        | OSI Open Source AI Definition 1.0: the bar for "open source AI" (usable data information, code, and weights). Informs fully_open vs open_weights and the licence reading. Capture the defining sentence + the four freedoms
third_party | https://crfm.stanford.edu/fmti/                           | 2026-07-26     | yes    | no        | Stanford Foundation Model Transparency Index: the transparency indicators behind our openness and provenance dimensions
third_party | https://eur-lex.europa.eu/eli/reg/2024/1689/oj             | 2026-07-26     | yes    | no        | EU AI Act (Regulation (EU) 2024/1689): Articles 53 and 55 GPAI duties and the ~1e25 FLOPs systemic-risk threshold, surfaced in each model's EU AI Act key fact and legal dimension. Capture the Article 53/55 text and the threshold
third_party | https://www.nist.gov/itl/ai-risk-management-framework      | 2026-07-26     | yes    | no        | NIST AI Risk Management Framework (AI 100-1): the risk framing behind the safety and governance dimensions
third_party | https://genai.owasp.org/llm-top-10/                        | 2026-07-26     | yes    | no        | OWASP Top 10 for LLM Applications: the deployment risks behind the safe-deployment and security guidance
third_party | https://atlas.mitre.org/                                   | 2026-07-26     | yes    | no        | MITRE ATLAS: the adversarial-ML threat taxonomy informing supply-chain and safety
third_party | https://openssf.org/ ; https://slsa.dev/                   | 2026-07-26     | yes    | no        | OpenSSF and SLSA: supply-chain integrity and build-provenance standards behind the provenance dimension and the format-safety checks
```
