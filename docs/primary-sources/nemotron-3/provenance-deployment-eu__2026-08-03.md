doc_type: provenance
entity: nemotron-3
variant/applies-to: HF org verification, formats, gating; NIM self-hosted deployment; EU AI Act posture
source_url: https://huggingface.co/nvidia ; https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/ ; https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai
document_effective_date: n/a
retrieval_date: 2026-08-03
exists: yes
retrieved: true
tag: publisher (org / NIM) / third_party (EU list)

## Provenance (VERBATIM where quoted)
[HF org verification] https://huggingface.co/nvidia shows a "Verified" badge; the org "nvidia" is
VERIFIED.
[Formats] Super and Nano weight repos are safetensors, with official BF16 / FP8 / NVFP4 quant
variants; weights are ungated (some training DATASETS are gated, not the weights).
[Not captured this pass] Published checksums / model signing / attestation not specifically
verified; checkpoint trust checklist about 4/8.

## Deployment - NIM self-hosted (data control)
[VERBATIM] NVIDIA NIM "provides prebuilt, optimized inference microservices for rapidly deploying
the latest AI models on any NVIDIA-accelerated infrastructure" and runs in "the cloud or data center
of your choice," so "data never leaves your secure enclave". NVIDIA is therefore NOT an AOI
inference-provider entry; self-hosting via NIM supports the data_control factor.

## EU AI Act
[GPAI Code of Practice signatory list] https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai :
NVIDIA is NOT listed. No NVIDIA training-content summary or copyright policy for Nemotron located.
GPAI; the licence is irrevocable and carries no field-of-use restriction, but the absence of a
formal GPAI documentation package, a public training-content summary and a copyright policy, plus
the non-OSI status, most likely keeps it short of a clean open-source exemption. Training FLOPs are
undisclosed (tokens only).
