# kimi-k3 - primary-source clauses (2026-07-27)

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://raw.githubusercontent.com/moonshotai/Kimi-K3/main/LICENSE | 2026-07-27 | yes | partial | custom "Kimi K3 Licence"; MaaS >$20M revenue separate-agreement gate (NEW vs K2) + 100M-MAU/$20M branding clause; promote to full verbatim
technical_report | (find on arXiv; K2 was 2507.20534) | - | unknown | false | needed for training tokens/FLOPs -> EU AI Act 1e25 systemic-risk check at 2.8T
model_card | https://huggingface.co/moonshotai/Kimi-K3 | 2026-07-27 | yes | false | proxy-blocked; try /raw/main/README.md and /resolve/main/; confirm params/experts/context/modalities/variants/format
docs | https://github.com/moonshotai/Kimi-K3 | - | unknown | false | repo README - architecture + serving stacks
terms | https://platform.kimi.ai/docs/agreement/modeluse.md | 2026-07-27 | yes | false | hosted API (proxy 403); K2 = trains on user content, opt-out enterprise-only, Singapore/SIAC - confirm for K3
privacy_policy | https://platform.kimi.ai/docs/agreement/userprivacy | 2026-07-27 | yes | false | hosted API privacy (proxy 403); confirm vs K2
third_party | (find independent analysis) | - | unknown | false | China-aligned censorship? companion guard model? benchmarks
```

## Notes for the coding session
- New entry `models/kimi-k3/`; keep `models/kimi/` (K2). Copy the K2 shape.
- Two real deltas vs K2: (1) stricter licence (MaaS separate-agreement gate), (2) larger scale
  (2.8T total / ~50B active, multimodal, 1M context) - heavier self-hosting and a fresh EU AI Act
  systemic-risk calculation from the report FLOPs, not an assumption.
- See `license__2026-07-27.md` for the partial clause capture.
