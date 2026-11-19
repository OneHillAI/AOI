# llama-cpp-gguf - primary-source clauses (2026-11-19)

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://raw.githubusercontent.com/ggml-org/llama.cpp/master/LICENSE | 2026-11-19 | yes | true | plain MIT, "Copyright (c) 2023-2026 The ggml authors"; ggml repo LICENSE identical; file license__llama-cpp-mit__2026-11-19.md
docs | https://raw.githubusercontent.com/ggml-org/ggml/master/docs/gguf.md | 2026-11-19 | yes | true | GGUF spec, format version 3, no signing/provenance field; last edit 2026-11-08 (ggml_type sync); file docs__gguf-spec__2026-11-19.md
security | https://raw.githubusercontent.com/ggml-org/llama.cpp/master/SECURITY.md | 2026-11-19 | yes | true | private disclosure disabled 2026-06-01; PoC and AI-report rules; sandbox untrusted models; file security__security-policy-and-advisories__2026-11-19.md
security | https://api.github.com/repos/ggml-org/llama.cpp/security-advisories | 2026-11-19 | yes | true | 13 advisories, newest 2026-03-26 (CVE-2026-34159); none since; same file as above
third_party | https://services.nvd.nist.gov/rest/json/cves/2.0 (cveId and keyword queries) | 2026-11-19 | yes | true | CVE-2026-5760 is SGLang, CVE-2024-34359 is the llama-cpp-python SSTI; ~30 llama.cpp/GGUF CVEs Mar-Nov 2026; file third_party__cve-register-llama-cpp-gguf__2026-11-19.md
third_party | https://research.jfrog.com/model-threats/gguf-ssti/ | 2026-11-19 | yes | true | cites CVE-2024-34359 only; no code execution in llama-cpp-python >= 0.2.72 or ollama
third_party | https://gbhackers.com/malicious-gguf-models-could-trigger-rce/ | 2026-11-19 | yes | true | article is about SGLang CVE-2026-5760, not llama.cpp
third_party | https://www.zerodayinitiative.com/advisories/ZDI-26-975/ (also -976, -954) | 2026-11-19 | yes | true | GGUF parsing RCE advisories published 2026-11-13; CVE-2026-126974/5/6
third_party | https://blog.huntr.com/gguf-file-format-vulnerabilities-a-guide-for-hackers | 2026-11-19 | yes | true | 2024-11-18 post, historical bugs
third_party | https://www.pillar.security/blog/llm-backdoors-at-the-inference-level-the-threat-of-poisoned-templates | 2026-11-19 | yes | true | 2025-07-09 post, poisoned templates
third_party | https://www.kb.cert.org/vuls/id/915947 | 2026-11-19 | yes | true | CERT/CC VU#915947 (released 2026-04-20): SGLang /v1/rerank RCE via GGUF tokenizer.chat_template, CVE-2026-5760; "No response was obtained from the project maintainers during coordination"
docs | https://huggingface.co/blog/ggml-org/llama-cpp-v1 | 2026-11-13 post, read 2026-11-19 | yes | true | v1.0.0, semantic versioning rules, ">150 architecture variants"
docs | https://huggingface.co/blog/ggml-joins-hf | 2026-02-20 post, read 2026-11-19 | yes | true | ggml/llama.cpp team joined Hugging Face
docs | https://github.com/ggml-org/llama.cpp/releases (atom feed and API) | 2026-11-19 | yes | true | v1.0.0 2026-11-13; bNNNN tags ~20-30/day; newest read b12550
docs | https://raw.githubusercontent.com/ggml-org/llama.cpp/master/CONTRIBUTING.md | 2026-11-19 | yes | true | contributor tiers, AI-use policy; file docs__release-versioning-and-governance__2026-11-19.md
```
