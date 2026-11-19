# Llama 3.1 / 3.3 on Hugging Face - gating, licence metadata and versions (API read 2026-11-19)

source_url: https://huggingface.co/api/models/meta-llama/Llama-3.1-8B-Instruct, .../Llama-3.1-70B-Instruct, .../Llama-3.1-405B-Instruct, .../Llama-3.3-70B-Instruct (public API metadata; raw README and licence files return 401 without a gated-access token, not downloaded)
exists: yes | retrieved: true (metadata) | model weights not downloaded

- gated: "manual" on all four repos. Licence tags: license:llama3.1 (8B, 70B, 405B Instruct) and license:llama3.3 (70B Instruct). Files are safetensors plus original/ consolidated .pth.
- Last modified: Llama-3.1-8B-Instruct 2024-09-25; 3.1-70B-Instruct 2024-12-15; 3.1-405B-Instruct 2024-09-25; Llama-3.3-70B-Instruct 2024-12-21.
- Org listing sorted by creation date: no Llama 3.x repo created after Llama-3.3-70B-Instruct (2024-11-26) and no repo of any kind after 2025-04-28 (Llama-Prompt-Guard-2). Latest modification of any repo in the org: Prompt-Guard-86M, 2025-11-12.
- Llama 4 licence metadata is license: other with license_name: llama4 (see docs/primary-sources/llama-4/).
