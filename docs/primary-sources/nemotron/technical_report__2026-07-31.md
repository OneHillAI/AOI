doc_type: technical_report
entity: nemotron
variant/applies-to: Nemotron 3 White Paper + per-model technical reports
source_url: https://arxiv.org/abs/2512.20856 ; Nano report arXiv 2512.20848
document_effective_date: ~2025-12
retrieval_date: 2026-07-31
exists: yes
retrieved: true (abstract + blogs) / false (full PDF text, FLOPs, safety methodology)
tag: publisher

## Captured facts (VERBATIM where quoted)
[Abstract - VERBATIM] "We introduce the Nemotron 3 family of models - Nano, Super, and Ultra ... a Mixture-of-Experts hybrid Mamba-Transformer architecture ... context lengths of up to 1M tokens. Super and Ultra models are trained with NVFP4 and incorporate LatentMoE ..."
[Total tokens - conflicting, report all] white paper "up to 25T tokens using the NVFP4 number format" (Super/Ultra) ; Ultra HF card "approximately 20T tokens" ; Ultra blog "10T token pre-training foundation ... adds 212B new tokens" ; Nano card "trained with 25T tokens".
[Architecture] Ultra = "LatentMoE - Mamba-2 + MoE + Attention hybrid with Multi-Token Prediction (MTP)", "550B (55B active)".
[Recipe/stages - VERBATIM] "continued pre-training (CPT) stage at a 512k sequence length, and supervised fine-tuning (SFT) was performed at a 256k sequence length" + "multi-environment reinforcement learning." Full Ultra program (GitHub) = "Pretrain -> SFT -> RLVR -> MOPD -> MTP Boosting."

## NOT FOUND / RE-DO (retrieved:false)
[Training COMPUTE / FLOPs] NOT stated in the white paper abstract, Nano card, Ultra card, or Ultra blog. Needed for the EU AI Act 1e25 systemic-risk check on Ultra 550B - currently UNDETERMINABLE from disclosed figures. RE-DO: fetch full PDFs (arxiv.org/pdf/2512.20856; Nano report 2512.20848).
[Red-team / safety methodology] White paper Section 3 ("Evaluation, Safety and Release") lists contributors but no methodology in the text read. RE-DO from full PDF.
[Exact per-model total-token figures] sources conflict (10T / 20T / 25T); reconcile from full PDF.
