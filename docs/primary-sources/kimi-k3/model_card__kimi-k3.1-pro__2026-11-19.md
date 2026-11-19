doc_type: model_card
entity: kimi-k3.1-pro  (NEW ENTITY candidate, NOT scored or folded into kimi-k3)
source_url: https://huggingface.co/moonshotai/Kimi-K3.1-Pro
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Facts as read

[Repo] huggingface.co/moonshotai/Kimi-K3.1-Pro on the verified moonshotai org. Created 2026-11-02 (initial commit 6d0a0202), one later commit 2026-11-05 (d9e99b07, "Update encoding_k3.py"). Not gated, not private. HF downloads 60,920 and likes 2,270 at read time.
[Licence metadata] front matter: license: other; license_name: "kimi-k3.1-pro". Body: "Kimi K3.1 Pro is released under the [Kimi K3.1 Pro License]".
[What it is - VERBATIM] "Kimi K3.1 Pro is an open-weight, natively multimodal agentic model, and our most capable 3T-class model to date. Post-trained from Kimi K3 with large-scale joint reinforcement learning across hundreds of downstream domains, it is the first model in the K3.1 series."
[Size] 2.8T total / 104B active, 93 layers (69 KDA + 24 Gated DSA; the Gated MLA full-attention layers of K3 are replaced by Gated DeepSeek Sparse Attention), 896 experts with 16 selected and 2 shared, 1,048,576-token context, vision encoder MoonViT-V2 (401M), modality "Text, Image", quantisation MXFP4 weights / MXFP8 activations (QAT). HF safetensors metadata: 2,780,110,363,392 parameters (U8 2.72T, BF16 57.4B), 96 shards.
[Serving] vLLM, SGLang, TokenSpeed (recipes linked). Hosted API id kimi-k3.1-pro (and kimi-k3.1-pro-highspeed on the platform).
[Reasoning control] top-level reasoning_effort "low", "high" or "max" (default max); the full assistant message including reasoning_content must be passed back in multi-turn use.
[Documents] The card links a Tech Blog and an API quickstart only. No standalone technical report and no GitHub repository were found (github.com/MoonshotAI/Kimi-K3.1-Pro returns 404).
[Safety text on the card] None. The card has no safety-tuning, refusal, guard-model or red-team statement. It does publish a "Cybersecurity benchmarks" block (ExploitBench 74.7, ExploitGym 20.7, xdev-bench-hard 81.0 for K3.1 Pro) with footnotes. The only safety-relevant description is in the tech blog, see marketing__k3.1-pro-blog__2026-11-19.md.
[Not disclosed] Training data, training code, training-token count and pretraining compute are not stated.
