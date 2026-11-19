# Support - LLM-jp-4.1 thinking (8B, 32B-A3B, 33B)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

From the cookbook and cards (`ev-cookbook`, `ev-gguf`); not an exhaustive catalogue:

- Garbled or unparsed output, broken tool calls: You are using the wrong tokenizer or
  skipping the template. Load the bundled tokenizer, call `apply_chat_template`, and do not use the
  `openai-harmony` tokenizer.
- Reasoning text mixed into the answer on vLLM: Start the server with the `llmjp4` reasoning
  parser from `llm-jp-vllm` 0.1.1 or later and vLLM 0.30.0 or later.
- llama.cpp chat parsing fails: Use upstream v0.6.0 or later and a 4.1 GGUF; the GGUF card
  still says a fork is needed, so if upstream fails, try the publisher fork named on the card.
- Special-token text in user input: Input that resembles `<|...|>` may need custom encoding;
  parse token IDs instead of decoded text.
- Wrong whitespace in decoded text: The vLLM example documents that `output.text` loses
  whitespace; decode `output.token_ids` with the model tokenizer.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Hugging Face creation dates (`ev-hub-api`), the corpus pages (`ev-corpus-v41`) and the announcement
(`ev-blog`, `ev-pcwatch`):

| Date | Release |
|---|---|
| 2026-03-15 and 16 | LLM-jp-4 8B base, 8B thinking, 32B-A3B base and thinking |
| 2026-03-30 | llm-jp-4-8b-instruct |
| 2026-08-14 | LLM-jp-4 33B base and thinking |
| 2026-09-15 and 16 | LLM-jp-4.1 8B, 32B-A3B and 33B thinking |
| 2026-09-24 | official 4.1 GGUF builds |
| 2026-09-28 | 4.1 announcement on the NII blog; the repositories were last modified the same day |
| 2026-10-14 | LLM-jp-4 technical report on arXiv (v1; 33B results to follow) |

Revisions are Hugging Face commits; there is no tagged changelog for the weights. The cards link
corpus changelogs (for example corpus v4.1 on 2026-03-31 and 2026-04-14). Pin the commit hash.

<!-- item: channels -->
## Community & support channels

The cards give `llm-jp(at)nii.ac.jp` for questions and a survey form for reporting how the
models are used (`ev-card-41`). Hugging Face discussion tabs exist on the model repositories (none
had been opened on the 33B repository on 2026-11-19). The release page lists tools and corpora on
GitHub and GitLab (`ev-release-page`). NII announced a trial API and chat service through the
University of Tokyo mdx-MaaS, mainly for researchers (`ev-pcwatch`). No community forum or
commercial support is listed.

<!-- item: known-issues -->
## Tracked known issues

No public issue tracker exists for the models; these are issues stated in publisher documents:

- the GGUF card and the cookbook disagree on whether llama.cpp needs a fork (`ev-gguf`);
- LLM-jp-4.1 uses a modified Harmony template and is not compatible with the `openai-harmony`
  library tokenizer (`ev-card-41`);
- original 4.0 GGUF chat templates lack the declaration needed to select the 4.1 parser
  (`ev-cookbook`);
- AIME, GPQA Diamond and long-context tool use remain well behind Qwen3.5 (`ev-blog`);
- the models "may still generate inaccurate, inappropriate, or otherwise undesirable outputs"
  (`ev-card-41`).
