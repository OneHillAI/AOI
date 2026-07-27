# Use - Berget AI

_What can it do and how do we use it? The served model catalogue and inference features live
here._

<!-- item: models-served -->
## Models served

Berget serves an **open-weight catalogue** hosted entirely in the EU:

- **Llama 3.1-8B** (fast/efficient) and **Llama 3.3-70B** (flagship)
- **Mistral-Small-3.2-24B** (efficient European-language specialist)
- **Gemma**
- **gpt-oss-120B** (advanced reasoning)
- **GLM-4.7** (code generation & reasoning)
- plus **multilingual embedding and reranking** models

For adopters the appeal is a sovereign, EU-hosted endpoint fronting mainstream open-weight
families - you can A/B a workload across models without changing integration code and without
data leaving the EU.

<!-- item: features -->
## Inference features

The endpoints are **OpenAI-compatible chat/completions**, plus **embedding and reranking**
endpoints. Berget also ships **"Berget Code"**, agentic coding assistants designed to keep
code in Sweden and not train on it. Higher-level behaviours such as **tool/function calling** and **structured
(JSON) output** depend on the specific served model's own capabilities and are not
independently verified on Berget's endpoints; treat per-feature support as
"inherited from the model, confirm per model."
