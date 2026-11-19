doc_type: docs
entity: morena
variant/applies-to: modeling_morena.py in vamboai/morena-1.5b-instruct and vamboai/morena-1.5b-base (identical file, sha256 1b2693d823e709a4614f091025448febc19ca0e32aa6a431c28f090e3b486de9, 52,103 bytes)
source_url: https://huggingface.co/vamboai/morena-1.5b-instruct/raw/main/modeling_morena.py
retrieval_date: 2026-11-19
exists: yes
retrieved: true (file read in outline: docstring, imports, function and class index, argparse block; not line-by-line audited for security)

## What the file is

[Docstring - VERBATIM] "Morena production trainer - single file, dependency-light. Dense Llama-style decoder (RMSNorm, RoPE, GQA, SwiGLU, tied embeddings) trained with FSDP2 (per-parameter sharding, bf16 compute / fp32 master+reduce), Muon (2-D hidden weights) + AdamW (embeddings, norms), WSD schedule, document-packed sequences with cross-document masking (FlashAttention-2 varlen when available), a deterministic mixture sampler, rotating + milestone checkpoints (torch.distributed.checkpoint), bit-exact resume and a walltime-aware clean exit for 24h SLURM chunks. Usage (single node): torchrun --nproc_per_node 4 train.py --config configs/proxy200m.json --mix configs/mix_330b.json --data-root /scratch/morena/data --out runs/proxy  See TRAIN_README.md."

[Contents] Classes ModelConfig, TrainConfig, RMSNorm, Attention, MLP, Block, Transformer, Source, MixtureSampler, Loader, Muon; functions for batch building, LR schedule, checkpoint save and load, and main() with argparse flags (--config, --mix, --data-root, --out, --resume, --anneal, --loss-mask, --ckpt-minutes, --wandb, ...). The only network-capable import is an optional wandb call that defaults to offline mode. No subprocess, socket, urllib or requests use was found by grep.

[What is NOT in the repo] TRAIN_README.md, the configs/ directory, the mixture JSON files, the data-preparation and machine-translation pipeline, the SFT pipeline, the evaluation harness and the corpus. The model card describes this file only as "reference implementation, plain PyTorch, no transformers dependency" and does not say it contains the full training loop.

[Loading] load_example.py (read in full): the model is not a transformers architecture; it is loaded with `M.Transformer(M.ModelConfig(**cfg["model"]), "sdpa")` and `load_state_dict(load_file("model.safetensors"), strict=True)`. Its docstring says the class "has NO .generate() and a training-shaped forward"; sampling is a hand-written loop with no KV cache. Using the weights therefore means running publisher-supplied Python (modeling_morena.py), not the transformers library.
