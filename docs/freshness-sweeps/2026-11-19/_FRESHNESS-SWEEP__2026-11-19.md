# AOI freshness re-verification sweep - 2026-11-19

Re-verification of all 33 entries (21 models, 9 inference providers, 3 hosting providers), each 59 days past the 30-day
fast SLA (`last_verified` 2026-09-21). Every entry was re-read against current primary documents:
raw licence files, model cards, live Terms, Privacy Policies, DPAs and provider catalogues. The work
was done by automated sessions (one per family or provider group), then checked by a lead session:
`validate.py` reports 0 errors on all 33, the site builds, and eight score-moving claims were
re-confirmed against the live source. No evaluation was run by OneHill; every performance and
safety figure is a publisher or third-party figure, as in the earlier entries. A maintainer has not
yet confirmed the cited text against the changed scores (CONTRIBUTING.md, "Changing a score").

## Entries that changed score, grade or ownership level (12 of 33)

| Entry | Before | After | Reason |
|---|---|---|---|
| soofi | 73.2 B, partial | 63.2 C, partial | All 20 repos gated (manual), licence tag `closed-beta`, no SPDX; openness 3 to 2, legal 4 to 2 |
| ai2-olmo | 80.8 B, substantial | 77.6 B, partial | Cards tie use to Ai2's Responsible Use Guidelines; legal 5 to 4, use_modify strong to moderate (maintainer decision) |
| fireworks-ai | 64.8 C, partial | 71.6 B, substantial | Terms and DPA read: both redirect to text PDFs, so the September "unreachable" finding was a browser limit |
| together-ai | 70.4 B, partial | 69.6 C, partial | Prompt storage and third-party passthrough on by default; only region guarantee is US processing; residency 4 to 3 |
| berget | 70.4 B, substantial | 67.2 C, substantial | DPA binds data to the EEA, not Sweden, and excludes serverless inference from data-centre choice; residency 5 to 4 |
| baseten | 73.6 B, substantial | 76.8 B, substantial | Customer-selectable `us` or `eu` region for dedicated deployments; residency 2 to 3 |
| infercom | 76.0 B, substantial | 78.4 B, substantial | DPA v1.4 read in full, public status page, ISO 27001 certificate read; reliability 2 to 3 |
| deepinfra | 56.8 C, partial | 61.6 C, partial | DPA now exists by reference; status page; dedicated prices up 59 to 75 percent; compliance 2 to 3, reliability 2 to 3, cost 5 to 4 |
| nebius | 60.8 C, partial | 64.4 C, partial | SOC 3 report and ISO 27001 certificate read; compliance 4 to 5 |
| groq | 70.0 B, substantial | 72.4 B, substantial | Terms, DPA, BAA and AUP re-read; AUP now read |
| runware | 50.4 D, partial | 54.4 D, partial | Terms of 29 September re-read in full; confidentiality duty added for Serverless |
| ollama (hosting) | 55.2 C | 48.4 D | Its own GGUF loader has a critical CVE (CVE-2026-7482, fixed in 0.17.1), four CVE records report no vendor response, no security advisories are published; loader safety 4 to 3, security track record 3 to 2. Hosting entries carry no ownership level |

The other 21 entries are unchanged in score and level (Hugging Face stays 79.2 B and llama.cpp 56.4 C). Their changes are evidence, wording and
date corrections only (see each entry's `changelog`).

## Corrections to the 2026-09-21 sweep

- Qwen: Qwen3.8-2.4T-A95B ("Qwen3.8-Max License") and Qwen3.8-Flash-Next ("Qwen Community License
  1.0") carry custom licences, and Qwen-Image-2.1 a non-commercial research licence. The September
  sweep said all of Qwen3.5, 3.6 and 3.8 were Apache-2.0.
- GLM-5.3: the USD 10 billion threshold is the group revenue of the licensee and its affiliates, not
  "MaaS revenue", and only GLM-5.3 carries the custom licence. GLM-5.3-Flash, 5.2 and 5.1 are plain MIT.
- Llama 4: the EU multimodal carve-out is in the Acceptable Use Policy, not in a licence section called
  "Additional Terms". It is read verbatim now.
- OLMo 3 was already named in the OLMo entry. EuroLLM-22B-2512 is Apache-2.0 and ungated.
- Nemotron 3.5 Content Safety was created in May 2026, not after September.
- Kimi K3: the licence is byte-identical to its first commit, but the earlier extract printed a
  paraphrase as verbatim. GLM-4-9B: a quoted sentence was not in the licence. Both are corrected.
- The Mistral weights documentation page cited as evidence now returns HTTP 404.
- The meta-llama entry (text-only Llama 3.1 and 3.3) still counted the multimodal EU restriction after
  the Llama 4 split; that is removed, with no score change.

- Hosting providers (the September sweep did not cover them): CVE-2026-5760 is an SGLang flaw, not an Ollama or llama-cpp-python one (the llama-cpp-python flaw is CVE-2024-34359), so that claim is removed from the Ollama and llama.cpp entries. Hugging Face holds SOC 2 Type 2 only; its own blog says ISO 27001 "is not currently held", so the certificate is removed. Hugging Face's October 2026 Load/Mine attack (31 malicious repos, one passing the platform's scans) and its July 2026 infrastructure intrusion are recorded. llama.cpp shipped v1.0.0 on 2026-11-13, moved under Hugging Face on 2026-02-20, and disabled private vulnerability reporting on 2026-06-01. The Ollama registry holds GGUF and MLX builds since 0.40.0.

## New releases found and not yet entered (licence as read from the raw file unless noted)

| Family | Release | Licence as read |
|---|---|---|
| Mistral | Large 4 (1T, 49B active) and NVFP4 build | Mistral Ecosystem Open-Weight License, modified MIT, separate licence for Model-as-a-Service operators |
| Mistral | Timestral 5M to 209M; Medium 3.5 128B; Devstral 2 123B | Modified MIT with a USD 20M monthly revenue cap |
| Mistral | Voxtral 4B TTS | CC-BY-NC-4.0 |
| Mistral | Large 3, Ministral 3, Small 4, Devstral Small 2, Shieldstral, Leanstral, LIDstral Arabic | Apache-2.0 (card front matter; no LICENSE file) |
| Qwen | 3.5, 3.6, 3.8-27B | Apache-2.0, unmodified |
| Qwen | 3.8-2.4T-A95B; 3.8-Flash-Next; Image 2.1 | Custom: Max License; Community License 1.0; Research License (non-commercial) |
| Kimi | K3.1 Pro (2.8T, 104B active) | Kimi K3.1-Pro License: K3 terms, new title; internal cyber benchmark drops from 90.5 to 81.0 percent after data filtering only |
| Kimi | K2.5, K2.6, K2.7 Code | Modified MIT, K2 text with year and display string changed |
| DeepSeek | V4 line (V4.1-Flash-1017, V4.1-Flash, V4-Pro-0813, V4-Flash-0731, Vision-Exp, previews, DSpark), V3.1 and V3.2 | MIT |
| GLM | 5.3 and 5.3-BF16; 5.3-Flash, 5.2, 5.1; 5 and 4.7 | Custom GLM-5.3 License; MIT; MIT by tag only |
| Nemotron | 3.5 Lightning, Super VL, Bolt 74B, Transcribe, Embed, Rerank, Parse, Content Safety | OpenMDW-1.1 |
| Nemotron | 3.5 Bolt E4B | Licence stack: OpenMDW-1.1 plus Apache-2.0 (Gemma 4 base) |
| Nemotron | Labs Sigma; Labs Audex | Nemotron Open Model License; NVIDIA OneWay Noncommercial |
| Meta | Muse Glimmer 30B; Muse Spark Open 816B | Apache-2.0; Muse Model License (display requirement, USD 20M Model-as-a-Service gate; read from the gate prompt) |
| OpenAI | gpt-oss-safeguard 20b and 120b; privacy-filter; circuit-sparsity | Apache-2.0 |
| Ai2 | Olmo 3.1, Olmo-Hybrid, EMO | Apache-2.0 |
| Ai2 | OlmoEarth v1 to v1.3 | OlmoEarth Artifact License: bans military, defence and extractive use, flows down to derivatives |
| EuroLLM | 22B-2512, 9B-2512, EuroMoE, 1.5 9B Base | Apache-2.0 |
| EuroLLM | 1.5 9B SFT | No licence declared |

## Open items for a human browser session

- Together AI: trust centre (JavaScript shell), SOC 2 report, ISO certificate.
- Baseten: every document behind the trust centre "Request access" (SOC 2 and 3, ISO, HIPAA, pen test).
- Nebius: the logged-in price list and the SOC 2 Type II report.
- DeepInfra: the DPA PDF (HTTP 403), the ISO certificate, the SOC 2 Type 1 report and the pen-test report.
- Hugging Face: SOC 2 Type 2 report, DPA text (Enterprise only). Ollama: no DPA, sub-processor list or certification exists to read. llama.cpp: whether ZDI-26-975, -976 and -954 are fixed by the PR ZDI names (#31336).
- Berget: status page (JavaScript shell). Mistral: Trust Centre sub-processor list.
- Llama and Gemma-derived models: Hugging Face cards of gated repos were read by API metadata only.

## Judgement calls a maintainer should confirm

- OLMo use_modify strong to moderate and legal 5 to 4 (the guidelines may or may not bind a downloader).
- Soofi grade B to C; Nebius compliance 5; DeepInfra compliance and reliability 3 (publisher statements);
  Together AI residency 3; Berget residency 4; Nemotron 3 Nano Omni operational held at 3.
- meta-llama legal 2 now that the multimodal ban no longer counts against the text-only line.
- Hugging Face security track record held at 3 although the Load/Mine attack evaded its scanners (the platform's own report says published files stayed clean); a drop to 2 is arguable.
- llama.cpp security track record held at 3 although private disclosure is off and the advisory feed stopped in March; Ollama security track record lowered to 2 for four no-response CVE records and no advisories. Treating the two differently is a judgement a maintainer may want to align.
