# Llama 4 on Hugging Face - gating, licence metadata and versions (API read 2026-11-19)

source_url: https://huggingface.co/api/models/meta-llama/Llama-4-Scout-17B-16E-Instruct and .../Llama-4-Maverick-17B-128E-Instruct (public API metadata; raw README and licence files return 401 without a gated-access token, not downloaded)
exists: yes | retrieved: true (metadata) | model weights not downloaded

- gated: "manual" on both repos. The card front matter reads license: other, license_name: llama4; the extra_gated_prompt is the Llama 4 Community License text with "Llama 4 Version Effective Date: April 5, 2025".
- The repo tags carry license:other (not a license:llama4 tag) and a library tag llama4. The earlier wording "llama4 licence tag" should be read as license_name llama4.
- Scout Instruct: created 2025-04-02, last modified 2025-05-22. Maverick Instruct: created 2025-04-01, last modified 2025-05-22. Scout base: last modified 2025-04-09. Files are safetensors.
- Org listing (https://huggingface.co/api/models?author=meta-llama&sort=createdAt&direction=-1): the newest repos are Llama-Prompt-Guard-2 (2025-04-28), Llama-Guard-4-12B (2025-04-23) and the Llama 4 Scout/Maverick repos (2025-04-01 to 2025-04-04). No Llama 4 Behemoth repo and no repo of any kind created after 2025-04-28.
