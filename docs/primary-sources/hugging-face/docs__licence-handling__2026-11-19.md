# Hugging Face - Licence handling on the Hub (re-read 2026-11-19, extracts)

Source: https://huggingface.co/docs/hub/repositories-licenses.md (HTTP 200, read in full).

- The licence is declared by the repository owner in the model card (README.md) metadata. The docs say users should "seek out and respect a project's license".
- The Hub keeps a list of selectable licence identifiers (for example apache-2.0, mit, the CreativeML, BigScience and OpenRAIL families, the cc-by family, openmdw-1.0 and openmdw-1.1, h-research, intel-research, apple-amlr). The list also carries vendor licences (llama2 to llama4, gemma, grok2-community, deepfloyd-if-license), `unknown` and `other`. For `license: other` the docs ask the author to put the licence text in a LICENSE file in the repo and name it in `license_name`.
- The Terms of Service say a licence notice on Content "is intended to remain under the terms of such license" and that Hugging Face does not override open source licences (see terms__2026-11-19.md).
- Nothing in the docs read says the Hub validates that a declared licence is correct; correctness rests on the publisher.
