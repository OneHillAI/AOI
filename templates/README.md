# templates/

Copy-to-start templates for contributing an entry. Each is a folder with a `data.yaml`
(machine-readable, validated) and a `README.md` (the human dossier).

| Template | Copy to | For |
|---|---|---|
| [`model/`](model/) | `models/<id>/` | An open-source / open-weight model family |
| [`inference-provider/`](inference-provider/) | `inference-providers/<id>/` | An API that serves open models |
| [`hosting-provider/`](hosting-provider/) | `hosting-providers/<id>/` | A place weights live / are installed from |

## Workflow

```bash
cp -r templates/model models/my-model
$EDITOR models/my-model/data.yaml          # fill in; every claim needs evidence
python scripts/score.py --write models/my-model/data.yaml
$EDITOR models/my-model/README.md          # write the dossier; match the score block
python scripts/validate.py models/my-model # must pass
```

The `data.yaml` templates carry inline comments explaining every field and the allowed
enum values. Read the [`../methodology/`](../methodology/) anchors before scoring. Full
guidance in [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
