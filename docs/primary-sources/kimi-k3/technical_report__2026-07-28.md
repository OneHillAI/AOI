doc_type: technical_report
entity: kimi-k3
variant/applies-to: Kimi K3 technical report ("Kimi K3: Open Frontier Intelligence")
source_url: https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf
document_effective_date: 2026-07 (released with weights)
retrieval_date: 2026-07-28
exists: yes
retrieved: true

## Governing clauses

[Read method] The 47-page PDF (~1.8 MB) was fetched and text-extracted locally (not machine-readable through the plain fetch tool; not on arXiv). Facts below are read directly from the report.

[Architecture - VERBATIM] "a natively multimodal Mixture-of-Experts model with 2.8 trillion total parameters, 104 billion activated parameters, and a context window of up to one million tokens." Per-token routing activates 16 of 896 routed experts. Components: Kimi Delta Attention (KDA), Attention Residuals, Per-Head Muon. Claimed "approximately 2.5x improvement in overall scaling efficiency over Kimi K2".

[Context curriculum] pre-training begins at 8K tokens, extended to 64K in a later phase; the window grows from 256K to 1M tokens during the cooldown phase (four-stage curriculum).

[Training tokens] NOT FOUND. No total training-token count is stated in the report.

[Training FLOPs] NOT FOUND. No absolute pretraining-FLOPs figure is stated; the report gives only relative scaling-law FLOPs (Figure 7: 2.5x scaling efficiency vs K2) and RL-FLOPs scaling curves. Analytical note (not a grounded figure): a 2.8T-total / 104B-active frontier pre-train plausibly approaches or exceeds the EU AI Act 1e25-FLOP systemic-risk threshold, but the figure is unpublished.

[Safety / dangerous-capability - VERBATIM context, section 6.2.2 Cyber Security Evaluation] "We evaluate the model's cybersecurity capability along a two-tier progression of increasing operational risk: vulnerability discovery with proof-of-concept development (Tier 1), and end-to-end exploit development (Tier 2)." Targets include OS kernel components, open-source projects, and Moonshot's own production services. "Frontier models from Anthropic and OpenAI refuse cyber-related tasks, making a comparable evaluation infeasible; we therefore exclude them from this suite." This is a capability evaluation, not a mitigation section: it documents that K3 performs offensive-cyber tasks that leading frontier models refuse. No refusal-training, companion guard model, content-filtering, or independent red-team is described.
