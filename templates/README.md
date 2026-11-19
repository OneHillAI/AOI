# templates/

Copy-to-start templates for contributing an entry. Each current template is a folder with an `entry.yaml`
(machine-readable, validated) and four dossier pages: `assess.md`, `implement.md`, `use.md` and `support.md`.

| Template | Copy to | For |
|---|---|---|
| [`model-v2/`](model-v2/) | `models/<id>/` | An open-weight model release |
| [`inference-provider-v2/`](inference-provider-v2/) | `inference-providers/<id>/` | An API that serves open models |
| [`hosting-provider-v2/`](hosting-provider-v2/) | `hosting-providers/<id>/` | A place weights live or are installed from |

The folders `model/`, `inference-provider/` and `hosting-provider/` are the earlier `data.yaml` layout and are
not used for new entries.

## Workflow

```bash
cp -r templates/model-v2 models/my-model
$EDITOR models/my-model/entry.yaml                          # fill in; every claim needs evidence
python scripts/score.py --write models/my-model/entry.yaml
python scripts/completeness.py --write models/my-model/entry.yaml
$EDITOR models/my-model/assess.md                           # and implement.md, use.md, support.md
python scripts/validate.py                                  # must report 0 errors
```

The `entry.yaml` templates carry comments on every field and the allowed enum values. Read the
[`../methodology/`](../methodology/) anchors before scoring. Full guidance is in
[`../CONTRIBUTING.md`](../CONTRIBUTING.md).
