# Models

Independent documentation for open-weight models, each scored against the
[AOI rubric](../methodology/scoring-rubric.md) and resolved into an ownership verdict per
[the ownership rules](../methodology/ownership.md). Every entry renders on the site at
[ownershipindex.ai](https://ownershipindex.ai); the source is under [`../site/`](../site/).

## What an entry is

Each model is one folder: a validated `entry.yaml` (identity, the seven dimension scores
with their evidence, and the four ownership factors) plus a four-domain dossier,
`assess.md` / `implement.md` / `use.md` / `support.md`. Scores are computed by
[`../scripts/score.py`](../scripts/), never hand-typed.

## How to read an entry

- **Ownership level** - the headline verdict (`full` down to `none`), floor-weighted from
  the four factors: use and modify, transparency, reliability, and data control.
- **AOI score and grade** - the 0 to 100 analytical input behind the verdict.
- **Openness tier** - where it sits on the
  [openness spectrum](../methodology/openness-framework.md); open weights is not the same
  as open source.
- **Deployment ceiling** - the highest
  [controllability tier](../methodology/safe-deployment-playbook.md) the model can safely
  reach, and the controls that unlock it.

## The set (v0.1)

Ten models chosen to span the openness and risk spectrum, from fully open to restricted
open-weight, ranked by AOI:

| Entry | Publisher | Licence | Openness tier | Ownership |
|---|---|---|---|---|
| [`ai2-olmo`](ai2-olmo/) | Allen Institute for AI (US) | Apache-2.0 | fully open | substantial |
| [`gpt-oss`](gpt-oss/) | OpenAI (US) | Apache-2.0 | open weights | substantial |
| [`mistral`](mistral/) | Mistral AI (FR) | Apache-2.0 flagship, research licence for some | open weights | partial |
| [`soofi`](soofi/) | Soofi Consortium (DE) | OSAID-committed, pending | open weights | partial |
| [`meta-llama`](meta-llama/) | Meta Platforms (US) | Llama Community Licence | gated open | partial |
| [`eurollm`](eurollm/) | EuroLLM consortium (EU) | Apache-2.0 | open weights + recipe | substantial |
| [`qwen`](qwen/) | Alibaba, Qwen team (CN) | Apache-2.0 | open weights | partial |
| [`glm`](glm/) | Zhipu AI (CN) | MIT | open weights | partial |
| [`deepseek`](deepseek/) | DeepSeek (CN) | MIT | open weights | partial |
| [`kimi`](kimi/) | Moonshot AI (CN) | Modified MIT | open weights | partial |

Ranking is by AOI, which weights trust (openness, provenance, legal, safety) above raw
capability: a model you cannot licence, verify, or run safely is the failure mode this
index exists to catch.

Adding an entry: copy [`../templates/model/`](../templates/model/) and follow
[`../CONTRIBUTING.md`](../CONTRIBUTING.md).
