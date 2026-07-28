# Research instruction: Kimi K3

## Your task
Research **Kimi K3** (Moonshot AI's new open model) and return the facts listed below. For **every
fact, give the source URL, a short quote from the page, and the date you read it.** If you cannot
find something, write "not found" - do not guess. Prefer primary sources (the model card, the LICENSE
file, the technical report, the provider's own terms) over news articles.

## What to research

**A. Identity**
1. Full model name and version; publisher name and country; the date the open weights were released.
2. Every variant released (e.g. Base, Instruct, Thinking). For each: total parameters, active
   parameters, context window.
3. Architecture in one line (Mixture-of-Experts? experts total / active per token?); modalities
   (text, image, video?).

**B. Licence and access**
4. Exact licence name. Is it OSI-certified open source (yes/no)?
5. **Every restriction, quoted word-for-word** - especially any revenue or user-count thresholds,
   branding/attribution requirements, and any "separate agreement" or "Model-as-a-Service" clause.
6. Where the weights are downloadable (URL) and the file format (safetensors? FP8?).

**C. What is open vs closed**
7. Are the training data and the training code released? Is the evaluation reproducible? Is there a
   technical report or paper (give the URL / arXiv number)?

**D. Hosted API data handling (platform.kimi.ai)**
8. Does the hosted API train on your prompts by default? Is there an opt-out, and on which tier?
9. Data retention period; server location / jurisdiction; governing law.

**E. Capabilities and benchmarks**
10. Headline benchmark results - name each benchmark and the score, especially coding / agentic and
    reasoning. Cite the source.
11. How it compares to Kimi K2 and to the frontier closed models.

**F. Safety and behaviour**
12. Is it safety-tuned? Is there a companion guard model? Any documented content filtering or
    censorship (e.g. politically sensitive topics)? Any independent red-team / safety evaluation?

**G. EU AI Act**
13. Training compute: how many training tokens, and the FLOPs estimate if stated (this decides
    whether it crosses the systemic-risk threshold).
14. Is any EU documentation published (copyright policy, training-content summary)?

**H. Running it**
15. Hardware needed to self-host (GPUs / memory); which serving stacks are supported (vLLM, SGLang,
    KTransformers, TensorRT-LLM?).

## How to return it

Paste back this table, one row per numbered fact, filled in:

```
| # | Fact | Value | Source URL | Quote from source | Date read |
|---|------|-------|-----------|-------------------|-----------|
```

Then, separately, **paste the full text of two things verbatim**: (1) the complete LICENSE, and
(2) the hosted-API clause on training/retention. Those two go in word-for-word, not summarised.
