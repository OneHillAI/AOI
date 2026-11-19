doc_type: security
entity: ggml-org/llama.cpp security policy and published advisories
source_url: https://raw.githubusercontent.com/ggml-org/llama.cpp/master/SECURITY.md ; https://api.github.com/repos/ggml-org/llama.cpp/security-advisories
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

## SECURITY.md (key clauses, VERBATIM)
- "> [!IMPORTANT] The private security disclosure program is disabled until further notice. Please submit patches with fixes directly to the repo as public PRs. Emails will be ignored."
- "A team of volunteers on a reasonable-effort basis maintains this project. As such, please give us at least 90 days to work on a fix before public exposure."
- "llama.cpp has an AI security scanner that scans the code periodically."
- "AI is only permitted in an assistive capacity as stated in AGENTS.md. We do not accept reports that are written exclusively by AI." and "Your report must include a working Proof-of-Concept in the form of a script and/or attached files."
- Covered topics: `src/**/*`, `ggml/**/*`, `gguf-py/**/*`, `tools/server/*` (excluding the built-in chat app, experimental features, features not recommended for untrusted environments such as router and MCP, and DoS bugs).
- "Denial-of-Service (DoS) bugs are generally not treated as vulnerabilities."
- "*Always execute untrusted models within a secure, isolated environment such as a sandbox* (e.g., containers, virtual machines)."
- "Do not use the RPC backend, ggml-rpc-server and llama-server functionality" when exposed to untrusted networks; "Confirm the hash of any downloaded artifact (e.g. pre-trained model weights) matches a known-good value."
- "Since there are no reliable methods to detect malicious models, sandboxing the model execution is the recommended approach".
- File history (GitHub API): 2026-06-01 "security : disable private disclosures (#23963)"; 2026-08-05 "security : clarify about AI-generated reports (#26579)"; 2026-11-16 web UI path change only.

## Published GitHub security advisories (13 listed 2026-11-19; newest dated 2026-03-26)
GHSA-3p4r-fq3f-q74v CVE-2026-27940 high 2026-03-12 gguf.cpp mem_size integer overflow, bypass of the CVE-2025-53630 fix, fixed >= b8146.
GHSA-j8rj-fmpv-wcxw CVE-2026-34159 critical 2026-03-26 unauthenticated RCE in the RPC backend (GRAPH_COMPUTE buffer=0 bypass; NVD: fixed in b8492).
GHSA-96jg-mvhq-q7q7 CVE-2026-33298 high 2026-03-18 integer overflow in GGUF tensor parsing (ggml_nbytes), fixed b7824.
GHSA-8947-pfff-2f3c CVE-2026-21869 low 2026-01-05 llama-server out-of-bounds write.
GHSA-vgg9-87g3-85w8 CVE-2025-53630 high 2025-07-10 GGUF parser integer overflow, heap out-of-bounds.
GHSA-7rxv-5jhh-j6xx CVE-2025-52566 high 2025-06-23 tokenizer heap overflow, fixed b5721.
GHSA-8wwf-w4qm-gpqr CVE-2025-49847 high 2025-06-14 malicious GGUF vocabulary loading buffer overflow, fixed >= b5662.
GHSA-wcr5-566p-9cwj CVE-2024-42479 critical, GHSA-5vm9-p64x-gqw9 CVE-2024-42478, GHSA-mqp6-7pv6-fqjf CVE-2024-42477 (RPC server and ggml_type_size, 2024-08-12, fixed b3561); GHSA-49q7-2jmh-92fp CVE-2024-41130 and GHSA-p5mv-gjc5-mwqv CVE-2024-32878 (gguf_init_from_file, 2024); GHSA-g4cc-763q-h9h6 (llama_model_load over-read, 2025-06-25).
No GitHub advisory has been published since 2026-03-26, although NVD lists many later llama.cpp CVEs (see third_party__cve-register-llama-cpp-gguf__2026-11-19.md): the project's own advisory feed is no longer the complete record.

## llama-cpp-python (separate project, abetlen/llama-cpp-python, not ggml-org)
One advisory: GHSA-56xg-wfcc-g829 / CVE-2024-34359, critical, published 2024-05-10, vulnerable >= 0.2.30 and <= 0.2.71, patched 0.2.72 ("Remote Code Execution by Server-Side Template Injection in Model Metadata"). PyPI latest 0.3.37 (2026-11-15; 0.3.36 2026-10-01; 0.3.35 2026-08-17). Repo pushed 2026-11-15, not archived.

## Reading (OneHill)
- The entry said there is "no first-party formal vulnerability-disclosure policy". That is wrong: SECURITY.md exists and defines scope, a PoC requirement, a 90-day window and an AI-report rule. The accurate current position is that the private channel was switched off on 2026-06-01, so reporters are told to send public PRs, which weakens coordinated disclosure; third-party programmes (ZDI, VulnCheck, huntr) are filling the gap.
- The project explicitly says it cannot detect malicious models and recommends sandboxing, which matches the entry's guidance.
