# Use - Infercom

_What can it do and how do we use it? The served model catalogue and inference features live
here._

<!-- item: models-served -->
## Models served

Infercom serves **major open-weight models in native BF16** on **SambaNova RDU dataflow
hardware**, across **EU/US/JP** regions. Serving in native BF16 (rather than a more aggressive
quantisation) is a quality signal for fidelity-sensitive workloads. The **exact model roster
and version list were not fully confirmed** in the public sources reviewed, so
confirm the current catalogue and per-model availability with the provider before committing.

<!-- item: features -->
## Inference features

The endpoints are **OpenAI-compatible chat/completions**, with **native BF16 serving** on
dataflow hardware. Higher-level behaviours such as **tool/function calling** and **structured
(JSON) output** depend on the specific served model's own capabilities and were not
individually re-verified on Infercom's endpoints, so treat per-feature support as
"inherited from the model, confirm per model."
