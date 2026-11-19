doc_type: docs
entity: tucano-2
variant/applies-to: Polygl0t organisation and the ten Tucano 2 model repos
source_url: https://huggingface.co/api/models?author=Polygl0t ; https://huggingface.co/api/organizations/Polygl0t/overview ; https://huggingface.co/api/models/Polygl0t/<repo>
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Facts from the Hugging Face API


[Organisation] Polygl0t, full name "Polyglot", details "Developing foundation models for low-resource languages.", isVerified: false, plan team, 7 members (including nicholasKluge, shiza-fatimah, sophia-falk, aniketsen, luciana1 and fmaisen, annahoepfner), 32 models, 24 datasets, 2 spaces.
[Model repos] Ten Tucano 2 repos, all gated: false, no discussions (0 on the 3.7B Instruct, 3.7B Base and 0.6B Base repos):
  Tucano2-0.6B-Base: created 2025-12-20, last modified 2026-03-05, 670,127,616 parameters, one model.safetensors 1,340,284,304 bytes, architecture llama, 196 downloads.
  Tucano2-qwen-0.5B-Base / -Instruct / -Think: 490,799,104 parameters, one model.safetensors 981,633,328 bytes, base_model Qwen/Qwen3-0.6B-Base (Base), Polygl0t/Tucano2-qwen-0.5B-Base (Instruct, Think).
  Tucano2-qwen-1.5B-Base / -Instruct / -Think: 1,510,073,344 parameters, one model.safetensors 3,020,182,248 bytes, base_model Qwen/Qwen3-1.7B-Base (Base).
  Tucano2-qwen-3.7B-Base: 3,759,341,056 parameters (BF16 total reported 3,885,170,176), two safetensors shards 7,770,386,240 bytes total, base_model Qwen/Qwen3-4B-Base, last modified 2026-03-05, 859 downloads.
  Tucano2-qwen-3.7B-Instruct: 3,759,341,056 parameters, two safetensors shards 7,518,727,872 bytes total, last modified 2026-08-13, 1,861 downloads, 7 likes.
  Tucano2-qwen-3.7B-Think: same size, last modified 2026-08-13, 154 downloads.
[Formats] Only safetensors weights appear in the file lists. No pickle, no GGUF in any repo. Each safetensors file has a Hugging Face LFS sha256 in the tree listing (3.7B Instruct: f0de7ca637ec52e2... and babd3657a6fc657d..., first 16 characters). No checksum file, signature or attestation is published by Polygl0t.
[Security scan] The API response carries no scan status field, so the Hugging Face malware scan result was not determined.
[Commit history] 3.7B Instruct: 33 commits, all by user nicholasKluge, the last on 2026-08-13 ("Update README.md"), upload of the folder on 2026-02-21. 3.7B Base: 46 commits, last 2026-03-05. 0.6B Base: 50 commits, last 2026-03-05. Base repos carry intermediate checkpoints as branches (3.7B Base: step-2500 to step-50000 every 2,500 steps; 0.6B Base: every 5,000 steps).
[Inference providers] inferenceProviderMapping is empty for the 3.7B Instruct repo; no gguf field.
[Collection] https://huggingface.co/collections/Polygl0t/tucano2-698f35ef9be3091437086bb4 (title "Tucano2", 4 items).
[Community derivatives] Models with base_model Polygl0t/Tucano2-qwen-3.7B-Instruct: pessini/Tucano2-qwen-3.7B-Instruct-MLX-4bit (quantized, 34 downloads, modified 2026-03-13) and gutoportelaa/tucano2-3.7b-instruct-vllm-rtx3080 (deployment recipe, no weights, modified 2026-11-10).
