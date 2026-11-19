# Support - Boldt-DC (350M and 1B base models)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

- Poor or off-topic output usually means a chat template was applied. Use plain completion.
- Load the tokenizer from the same repo as the weights. Each Boldt model has its own 32k tokenizer.
- The Boldt-DC-1B sample loads `Boldt/Boldt-1B`. Replace the name with `Boldt/Boldt-DC-1B`.
- The 350M card says "three models" and lists four, and calls the model "Boldt-DC-300M" in its table. The repo, the organisation page and the API all say 350M, and the config counts 468M parameters (`ev-card-350m`, `ev-hf-platform`).
- The 1B card carries a `custom_code` tag, but the repo holds no custom code.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Both repos were created on 2026-05-02. The weights have not changed since the initial upload; later commits edit the README (the last on 2026-11-01 for the 350M repo). The organisation added 15 research checkpoints and three classifiers on 2026-08-30, and the paper appeared in EMNLP 2026 proceedings. There is no changelog file, so pin the commit hash (`ev-hf-platform`, `ev-paper`).

<!-- security-disclosure is a `gap` item: no SECURITY.md, security contact or process exists. -->

<!-- item: channels -->
## Community & support channels

The Hugging Face discussions tab on both repos is open and empty. The chair's project page and the paper list the authors' university addresses, which are not a security channel (`ev-hf-platform`, `ev-project`).

<!-- deprecation is a `gap` item: no deprecation or support-window statement exists. -->

<!-- item: known-issues -->
## Tracked known issues

There is no public issue tracker. The publisher lists the missing toxicity and bias evaluation and the risk of bias amplification from repeated epochs (`ev-card-1b`, `ev-paper`). The card errors above are the other known defects.
