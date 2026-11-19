doc_type: docs
entity: morena
variant/applies-to: Hugging Face repos vamboai/morena-1.5b-instruct and vamboai/morena-1.5b-base, org vamboai
source_url: https://huggingface.co/api/models/vamboai/morena-1.5b-instruct ; .../tree/main ; .../commits/main ; .../discussions ; https://huggingface.co/api/organizations/vamboai/overview ; https://huggingface.co/api/models?author=vamboai ; https://huggingface.co/vamboai/morena-1.5b-instruct/raw/main/SHA256SUMS ; https://huggingface.co/api/models/vamboai/morena-1.5b-instruct-gguf
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Facts read from the Hugging Face API (platform metadata; the platform is the host, the publisher is Vambo AI)

[Org] vamboai: "fullname":"Vambo AI", "isVerified":false, "numUsers":1, "numModels":8, "numDatasets":1, "numSpaces":1. The organisation is not verified on the primary host and has one member.

[Models in the org (all created 2026-09-15, all public, none gated)] morena-1.5b-instruct, morena-1.5b-instruct-gguf, morena-1.5b-base, morena-0.5b-mini, morena-0.5b-mini-instruct, morena-0.5b-mini-gguf, morena-0.2b-nano, morena-0.2b-nano-gguf. Dataset: vamboai/fikira (MIT, created 2025-12-13).

[Instruct repo] sha b9bebd76c5725e570d6186ba400eff87f3a2382b; createdAt 2026-09-15T13:30:53Z; lastModified 2026-10-14T07:57:43Z; downloads (30-day) 197, all-time 663; likes 18; "gated": false; "inference": false in card data; inferenceProviderMapping: {} (no inference provider hosts it); no Spaces; discussions: count 0. Safetensors: BF16 1,484,900,352 parameters. Files: .gitattributes, README.md, SHA256SUMS, config.json, load_example.py, model.safetensors (2,969,826,328 bytes), modeling_morena.py (52,103 bytes), poster.png, tokenizer.json, tokenizer_config.json. No pickle, .bin or .pt file.

[Malware scan] API with securityStatus=true: "securityRepoStatus": {"scansDone": true, "filesWithIssues": []} for the instruct repo and the GGUF repo.

[Checksums] SHA256SUMS (publisher file) lists config.json, load_example.py, modeling_morena.py, model.safetensors (2ab0b7f3b88ddb22a7fc91bd674e10481f1c8eefa404595557083edf6bc8029e), tokenizer.json. The LFS oid for model.safetensors in the tree API is the same value. On 2026-11-19 OneHill recomputed sha256 locally for config.json (e46cbea0...), load_example.py (b0730bd0...) and modeling_morena.py (1b2693d8...): all three match SHA256SUMS. The 2.97 GB weights file was NOT downloaded; its hash was compared only between the two host-side records. SHA256SUMS is not signed. No sigstore or SLSA attestation exists.

[Commit history, instruct repo, newest first] 2026-10-14 "Add tokenizer_config.json with chat template"; 2026-09-18 "Remove pre-release wording now that the repo is public"; 2026-09-18 "Licence: Apache 2.0, commercial use permitted"; 2026-09-17 "Poster: emblem design"; 2026-09-17 "Release card: wording"; 2026-09-17 "Release card: status section"; 2026-09-17 "Release card: licence wording removed"; 2026-09-16 "Release card, final audit"; ... 2026-09-15 "MORENA release: morena-1.5b-instruct"; 2026-09-15 "initial commit". All authored by HF user thisisisheanesu.

[GGUF repo] vamboai/morena-1.5b-instruct-gguf files: morena-1.5b-instruct-Q4_K_M.gguf (921,791,136 bytes), -Q8_0.gguf (1,580,378,784), -f16.gguf (2,972,363,424), SHA256SUMS, README.md. HF's own GGUF header parse reports architecture "llama", context_length 4096, total 1,484,900,352 parameters.

[Stale text] load_example.py in the instruct repo opens with "Load the Morena preview weights (morena1p5b-sft16) and sample from them", and its comment says the folder ships "morena1p5b-sft16". The card's "Remove pre-release wording" commit did not touch this file.

[No security policy] No SECURITY.md or security contact exists in either repo.
