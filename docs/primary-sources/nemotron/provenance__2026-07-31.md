doc_type: provenance
entity: nemotron
variant/applies-to: HF org verification, file formats, download gating
source_url: https://huggingface.co/nvidia
document_effective_date: n/a
retrieval_date: 2026-07-31
exists: yes
retrieved: true
tag: publisher

## Facts (VERBATIM where quoted)
[HF org verification - VERBATIM] https://huggingface.co/nvidia : org profile shows a "Verified" badge. HF org "nvidia" is VERIFIED.
[File format] All four Nemotron 3 weight repos are safetensors (BF16 / FP8 / NVFP4 quant variants published).
[Download gating] No Nemotron 3 WEIGHT repo (Ultra/Super/Nano/Nano Omni) requires click-through/terms acceptance to download - standard ungated safetensors. Gating applies only to SOME training-DATASET collections, not the weights (Nano card: "For all remaining code, math and multilingual data, gating and approval is required").

## Not captured this pass (RE-DO if needed)
Published checksums / model signing / attestation (e.g. sigstore, SHA manifests) not specifically
verified. RE-DO: check repo file listings for signatures / SHA manifests.
