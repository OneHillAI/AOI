doc_type: docs
entity: boldt
variant/applies-to: Hugging Face organisation Boldt and the Boldt-DC-350M and Boldt-DC-1B repos
source_url: https://huggingface.co/api/organizations/Boldt/overview ; https://huggingface.co/api/organizations/Boldt/members ; https://huggingface.co/api/models?author=Boldt ; https://huggingface.co/api/models/Boldt/Boldt-DC-350M and .../Boldt-DC-1B (with ?securityStatus=true, /commits/main, /discussions) ; https://huggingface.co/api/datasets?author=Boldt
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Facts read
[Organisation] name Boldt, isVerified false, numUsers 2 (members: Ansar Aynetdinov "aynetdia", Alan Akbik "alanakbik"), 19 model repos, 8 dataset repos, 1 static space (README), 24 followers.
[Model repos, by creation date] 2026-05-02: Boldt-DC-350M, Boldt-DC-1B, Boldt-1B; 2026-05-03: Boldt-1B-IT-Preview; 2026-08-30: three classifiers and 12 research checkpoints (Random, Coherence, Sorted, Edu, IV, MKC, DC-100BT, Phased-100BT/200BT at 350M and 1B). All have transformers, safetensors; only safetensors weights, no pickle or .bin files in any repo read.
[Boldt-DC-350M] created 2026-05-02, last modified 2026-11-01 (README edit), downloads (30 days) 266, all-time 2,545, likes 2, scan: scansDone true, filesWithIssues empty, gated false, no inference provider mapping, discussions 0.
[Boldt-DC-1B] created 2026-05-02, last modified 2026-05-06, downloads 52, likes 0, scan: scansDone false, filesWithIssues empty, gated false, no inference provider mapping, discussions 0.
[Commits] Both repos: commits by "aynetdia" and "alanakbik" (README and file uploads); no later weight change after the initial upload folder commit on 2026-05-02.
[Derivatives found on the Hub] Models listing Boldt-DC-1B as base: mayflowergmbh/boldt-dc-1b-german-it-16k (and a -dpo version); Boldt-DC-350M: mayflowergmbh/Boldt-Embed-DE-350M. Third-party, not assessed. A community GGUF exists for Boldt-1B-IT-Preview (flozen1981); none was found for the DC models.
[Compute and packaging] No official GGUF, GPTQ, AWQ or ONNX repo from the publisher. No Hub Space with a demo besides the static README.
