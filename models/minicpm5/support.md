# Support - MiniCPM5-1B

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

The list is drawn from the model card and cookbooks (`ev-card`, `ev-github`) and is not exhaustive:

- Old stacks fail to load the model. The card sets floors of vLLM 0.21, SGLang 0.5.12 and transformers 5.6, so upgrade before debugging anything else.
- Tool calls come back as raw XML. Use SGLang with `--tool-call-parser minicpm5`, or the repository's parser on other servers.
- Answers ramble or truncate. Set `enable_thinking` explicitly and use the card's sampling for each mode (0.9 Think, 0.7 No Think, top_p 0.95). The publisher reports that RL and OPD cut max-token hits by 29 percentage points on its own set.
- A small device runs out of memory. Use the Q4_K_M GGUF or MLX 4-bit and cap the context (the cookbook example uses 8192).
- Older MiniCPM checkpoints are under the General Model License and not Apache-2.0 (`ev-legacy-gml`).

<!-- item: release-versioning -->
## Versions, changelog & cadence

The GitHub README log dates MiniCPM5-1B at 2026-05-19 and MiniCPM5-2B at 2026-09-07. Other sources say 25 May (`ev-github`, `ev-aa`), and the Hub repos were created 2026-05-21. The Hub repos show last-modified dates of 2026-11-09 to 2026-11-11. The cadence since 2024 is a new generation roughly every 8 to 12 months (Feb 2024, Sep 2024, Jun 2025, May 2026) plus point releases. The repository has no GitHub releases or tags, so the Hub commit hash is the changelog anchor; pin it.

<!-- item: channels -->
## Community & support channels

GitHub issues with bug-report, bad-case and feature-request templates, GitHub Discussions, a Discord server, a Feishu or Lark group and a Chinese wiki at openbmb.cn/docs (`ev-github`). Commercial authorisation by email applies only to older generations.

<!-- security-disclosure is a `gap` item in entry.yaml - no SECURITY.md or process exists (404). -->

<!-- deprecation is a `gap` item in entry.yaml - no deprecation or end-of-life policy published. -->

<!-- item: known-issues -->
## Tracked known issues

No tracker exists for the model, so these come from the card and table (hence partial). There is no safety evaluation. The GPQA-Diamond, IFEval, Multi-IF, MultiChallenge and BFCLv4 rows are weaker than some baselines. No long-context result exists for the 1B, and the SFT dataset sits behind a Hub gate. The shared MiniCPM repository had 24 open issues on 2026-11-19, which are not triaged. Follow-ups are MiniCPM5-2B (separate release) and older MiniCPM generations (General Model License).
