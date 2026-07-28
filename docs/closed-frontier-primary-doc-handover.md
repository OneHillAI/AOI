# Research instruction: proprietary frontier models

## Your task
Research each of these six models and return the facts listed below **for every one of them**:

**grok** (xAI), **gpt** (OpenAI, the closed GPT model - not gpt-oss), **claude** (Anthropic),
**gemini** (Google), **muse** (identify the publisher first - see note), **qwen-max** (Alibaba's
closed flagship, not the open Qwen3).

For **every fact, give the source URL, a short quote from the page, and the date you read it.** If
something does not exist or you cannot find it, write "not found" or "none" - do not guess. Prefer the
provider's own binding documents (Terms, Privacy Policy, Data Processing Addendum, system card) over
blog posts or news.

These are closed models with no downloadable weights, so **the most important section is D (data
handling)** - that is what separates them.

## What to research (for each model)

**A. Identity**
1. Full model name and version; publisher name and country; is it API-only, or is there any
   open-weight version in the same family? (name it if so).

**B. Access and pricing**
2. How you access it (API, app, cloud); the price per million input and output tokens.

**C. Capabilities and benchmarks**
3. Modalities (text, image, audio, video?); context window; headline benchmark results (name the
   benchmark and score). Cite the source.

**D. Data handling - the key section (quote the binding clause for each)**
4. Does it **train on your inputs by default?** Answer separately for: the **consumer app**, the
   **paid API**, and **enterprise**. Quote the exact clause for each.
5. Data **retention**: default period. Is **zero-data-retention** available, and on which tier?
6. **Residency**: can data be pinned to a region? Which regions?
7. Is there a **Data Processing Addendum (DPA)**? Give the URL.

**E. Governance and safety**
8. Is there a published **system card / model card** (URL)? What safety evaluations does it report?
9. **Acceptable-use / usage policy** (URL) - the main prohibited uses.
10. **Security/compliance**: SOC 2, ISO 27001, etc. - what is attested, and where (trust centre URL)?

**F. EU AI Act**
11. Does the provider state a systemic-risk designation or publish EU compliance documentation? (URL)

## Notes on specific models
- **muse** - identity is not confirmed. First find out which lab ships a model called "Muse",
  whether it is a frontier LLM, its country, and whether it is closed or has open weights. Report
  that before the rest. If it has open weights, say so.
- **qwen-max** - this is the closed, API-only flagship (Qwen-Max / Qwen3-Max) served through Alibaba
  Model Studio / DashScope. Do **not** report on the open Apache-2.0 Qwen3 weights here.
- **grok** - specifically check whether it trains on X / Twitter platform data as well as API inputs.
- **gemini** - Google's free vs paid tiers are treated differently for training; report both.

## How to return it

For **each model**, paste back this table filled in, one row per numbered fact:

```
### <model>
| # | Fact | Value | Source URL | Quote from source | Date read |
|---|------|-------|-----------|-------------------|-----------|
```

Then, for each model, **paste verbatim** the single most important clause: the one that says whether
your inputs are used to train the model (for the paid API / enterprise tier). That clause goes in
word-for-word.
