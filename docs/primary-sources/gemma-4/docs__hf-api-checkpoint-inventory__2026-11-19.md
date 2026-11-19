# Hugging Face inventory of Gemma 4 checkpoints: licence tags, gating, files

source_url: https://huggingface.co/api/models?author=google&search=gemma-4 ; https://huggingface.co/google/gemma-4-31B-it ; https://huggingface.co/api/organizations/google/overview
retrieval_date: 2026-11-19
doc_type: docs
retrieved: true


Method: Hugging Face public JSON API (no login) and raw README files, fetched with curl on 2026-11-19. All requests were anonymous and returned HTTP 200 for every Gemma 4 repository, including config.json (resolve/main/config.json), which means no gate applies.

## Gemma 4 repositories in the verified `google` organisation (API search `author=google&search=gemma-4`, 38 Gemma 4 repositories listed)

Organisation record: https://huggingface.co/api/organizations/google/overview returned `"name":"google","isVerified":true,"plan":"enterprise"`.

Result rows (id | licence tag | gated | createdAt | lastModified), reduced to the checkpoint families that matter:

```
google/gemma-3-4b-it | license:gemma | gated=manual | created 2025-02-20 | modified 2025-03-21
google/gemma-4-12B | license:apache-2.0 | gated=False | created 2026-05-23 | modified 2026-10-30
google/gemma-4-12B-it | license:apache-2.0 | gated=False | created 2026-05-23 | modified 2026-10-30
google/gemma-4-26B-A4B | license:apache-2.0 | gated=False | created 2026-03-12 | modified 2026-07-15
google/gemma-4-26B-A4B-it | license:apache-2.0 | gated=False | created 2026-03-11 | modified 2026-07-20
google/gemma-4-31B | license:apache-2.0 | gated=False | created 2026-03-12 | modified 2026-07-15
google/gemma-4-31B-it | license:apache-2.0 | gated=False | created 2026-03-11 | modified 2026-07-20
google/gemma-4-E2B | license:apache-2.0 | gated=False | created 2026-03-02 | modified 2026-11-03
google/gemma-4-E2B-it | license:apache-2.0 | gated=False | created 2026-03-02 | modified 2026-11-03
google/gemma-4-E4B | license:apache-2.0 | gated=False | created 2026-03-02 | modified 2026-11-03
google/gemma-4-E4B-it | license:apache-2.0 | gated=False | created 2026-03-02 | modified 2026-11-03
```

Every one of the 38 Gemma 4 repositories listed (instruction-tuned, base, `-assistant` multi-token-prediction drafters, and all `-qat-*` quantised checkpoints) carried `license:apache-2.0` and `gated=False`. Counts by suffix: base and it checkpoints 10 (five sizes, base and it); the rest are drafters and quantised releases.

## README front matter (license fields), read verbatim from raw README.md

```
google/gemma-4-31B: license: apache-2.0 ; license_link: https://ai.google.dev/gemma/docs/gemma_4_license
google/gemma-4-12B: license: apache-2.0 ; license_link: https://ai.google.dev/gemma/docs/gemma_4_license
google/gemma-4-12B-it: license: apache-2.0 ; license_link: https://ai.google.dev/gemma/docs/gemma_4_license
google/gemma-4-26B-A4B: license: apache-2.0 ; license_link: https://ai.google.dev/gemma/docs/gemma_4_license
google/gemma-4-26B-A4B-it: license: apache-2.0 ; license_link: https://ai.google.dev/gemma/docs/gemma_4_license
google/gemma-4-E2B: license: apache-2.0 ; license_link: https://ai.google.dev/gemma/docs/gemma_4_license
google/gemma-4-E2B-it: license: apache-2.0 ; license_link: https://ai.google.dev/gemma/docs/gemma_4_license
google/gemma-4-E4B: license: apache-2.0 ; license_link: https://ai.google.dev/gemma/docs/gemma_4_license
google/gemma-4-E4B-it: license: apache-2.0 ; license_link: https://ai.google.dev/gemma/docs/gemma_4_license
google/gemma-4-12B-it-assistant: license: apache-2.0 ; license_link: https://ai.google.dev/gemma/docs/gemma_4_license
google/gemma-4-31B-it-qat-q4_0-gguf: license: apache-2.0 ; license_link: https://ai.google.dev/gemma/docs/gemma_4_license
```

## Files in the repositories (tree API)

```
gemma-4-31B-it: .eval_results .gitattributes README.md chat_template.jinja config.json generation_config.json model-00001-of-00002.safetensors model-00002-of-00002.safetensors model.safetensors.index.json processor_config.json tokenizer.json tokenizer_config.json
gemma-4-31B: .gitattributes README.md config.json generation_config.json model-00001-of-00002.safetensors model-00002-of-00002.safetensors model.safetensors.index.json processor_config.json tokenizer.json tokenizer_config.json
gemma-4-12B-it: .gitattributes README.md chat_template.jinja config.json generation_config.json model.safetensors processor_config.json tokenizer.json tokenizer_config.json
gemma-4-12B: .gitattributes README.md config.json generation_config.json model.safetensors processor_config.json tokenizer.json tokenizer_config.json
gemma-4-26B-A4B-it: .eval_results .gitattributes README.md chat_template.jinja config.json generation_config.json model-00001-of-00002.safetensors model-00002-of-00002.safetensors model.safetensors.index.json processor_config.json tokenizer.json tokenizer_config.json
gemma-4-E2B-it: .gitattributes README.md chat_template.jinja config.json generation_config.json model.safetensors processor_config.json tokenizer.json tokenizer_config.json
gemma-4-E4B-it: .gitattributes README.md chat_template.jinja config.json generation_config.json model.safetensors processor_config.json tokenizer.json tokenizer_config.json
```

There is no LICENSE, LICENSE.md, NOTICE or USE_POLICY file in any of these repositories. The licence is stated only in the README front matter (`license: apache-2.0`, `license_link: https://ai.google.dev/gemma/docs/gemma_4_license`) and the README header line "License: Apache 2.0".

## Contrast: Gemma 3

API record for google/gemma-3-4b-it: `license:gemma`, `"gated":"manual"` (manual approval required). Its raw README.md and config.json returned HTTP 401 ("Access to model google/gemma-3-4b-it is restricted. You must have access to it and be authenticated to access it.") on 2026-11-19. The same pattern holds for every Gemma 3 and 3n repository in the search results (`license:gemma`, gated manual). Gemma 4 is therefore published ungated and not under the Gemma Terms of Use, unlike every Gemma 3 repository seen.

## Other Google "gemma" releases created in 2026 (API search, author=google) and their licence tags

```
google/embeddinggemma-2 | license:apache-2.0 | created 2026-09-14
google/translategemma-27b-it | license:gemma | created 2026-01-12
google/translategemma-12b-it | license:gemma | created 2026-01-12
google/medgemma-1.5-4b-it | license:other | created 2026-01-07
```

These are not Gemma 4 checkpoints and were not assessed; they show the Gemma family is still split across licences.
