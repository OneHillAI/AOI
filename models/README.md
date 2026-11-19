# Models

Open-weight models, each scored against the [AOI rubric](../methodology/scoring-rubric.md) and resolved into an ownership verdict under [the ownership rules](../methodology/ownership.md). The ranked list of every entry is at [ownershipindex.ai/library](https://ownershipindex.ai/library).

## What an entry is

A model release is one folder. `entry.yaml` holds the identity, the seven dimension scores with their evidence, and the four ownership factors. Four dossier pages sit beside it: `assess.md`, `implement.md`, `use.md` and `support.md`. Scores are computed by [`scripts/score.py`](../scripts/) and are never typed by hand.

A family groups releases and carries no score. Only a release is scored, and a family is split into separate entries when its releases differ on a scored attribute, licence first.

## How to read an entry

- Ownership level: the verdict, from `full` to `none`, floor-weighted from four factors (use and modify, transparency, reliability, data control).
- AOI score and grade: the 0 to 100 input behind the verdict.
- Openness tier: the position on the [openness spectrum](../methodology/openness-framework.md). Open weights are not open source.
- Deployment ceiling: the highest [controllability tier](../methodology/safe-deployment-playbook.md) the model reaches, and the controls that unlock it.

## Adding an entry

Copy [`../templates/model-v2/`](../templates/model-v2/) and follow [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
