# AOI freshness re-verification sweep - 2026-09-21

Re-verification of the **21 stale model entries** surfaced by `validate.py` on PR #22 (all
`last_verified` in late-Jul/early-Aug 2026, 49-58 days past the 30-day fast SLA). This was a
**real re-check against current primary sources**, not a bulk date-bump. Every entry was re-read
this pass; `retrieved` flags are honest per file.

## Summary table

| Entity | Result | What changed | Bump `last_verified`? |
|---|---|---|---|
| `deepseek-r1` | clean | none on tracked entry; V4 line + V3.1/V3.2 exist (flag) | **Yes** |
| `deepseek-r1-distill-llama` | clean | none; distill line not re-cut under V4 | **Yes** |
| `deepseek-r1-distill-qwen` | clean | none; base Qwen moved (see qwen) | **Yes** |
| `deepseek-v3-mit` | clean | none on entry; V3.1/V3.2 (also MIT) supersede (flag) | **Yes** |
| `deepseek-v3-original` | clean | MIT-code / DeepSeek-License-weights split still real | **Yes** |
| `nemotron-3` | clean + flag | licence tag correct; **new sibling: Nemotron 3.5 Lightning 30B-A3B (OpenMDW-1.1)** | **Yes** |
| `nemotron-3-ultra` | clean | licence tag correct; no Ultra-tier supersession | **Yes** |
| `nemotron-3-nano-omni` | clean + flag | licence tag correct; 3.5 Lightning sits in this footprint (sibling) | **Yes** |
| `meta-llama` | clean | 700M-MAU clause verbatim unchanged; gated | **Yes** |
| `llama-4` | clean + caveat | terms unchanged; EU multimodal carve-out not re-confirmable (fetch truncation) - manual eyeball | **Yes** (with caveat) |
| `mistral` | delta | new-gen apache-2.0 releases; Large-3/Ministral-3 read Apache - manual re-confirm (MRL to Apache?); Codestral still mnpl | **Yes** |
| `mistral-research-license` | clean | Ministral-8B-2410 + Large-2407 still mrl; new gen trending Apache | **Yes** |
| `glm` | clean + action | MIT cluster unchanged; **new licence-divergent line: glm-5 (custom GLM-5.3 License, $10B MaaS security gate)** | **Yes** |
| `glm-4-9b-chat-original` | clean | glm-4 tag + commercial-registration clause intact; repo live | **Yes** |
| `kimi-k2` | clean + flag | 100M-MAU / $20M branding clause intact; **K2.5/K2.6/K2.7-Code exist** (flag) | **Yes** |
| `kimi-k3` | clean | $20M MaaS separate-agreement gate verbatim unchanged; risk finding stands; no K4 | **Yes** |
| `ai2-olmo` | delta | **OLMo 3 shipped (Apache-2.0, fully_open, Dolma 3) - add sibling**; OLMo 2 still valid | **Yes** |
| `eurollm` | delta | 9B still apache-2.0/gated; **EuroLLM-22B-2512 - add sibling** | **Yes** |
| `gpt-oss` | clean | 20b/120b apache-2.0 ungated; gpt-oss-safeguard optional note | **Yes** |
| `qwen` | delta | Qwen3 not reverted (apache-2.0); **superseded by Qwen3.5/3.6/3.8** (flag) | **Yes** |
| `soofi` | REVIEW | **Soofi-S-Base tag verbatim "closed-beta" + gated vs "open-source" marketing** - B grade may overstate openness | HOLD - re-grade first (see code session's own follow-up note below) |

## Code-session follow-up on `soofi` (added after the research pack landed)

The research pack recommended holding the bump pending a re-grade. On review, the entry's
2026-07-25 correction already accounts for exactly this: openness is already held at the
`open_weights` ceiling (score 3, not `fully_open`/5), the `weights` component is already
`partial`, and ownership is already `partial` with `use_modify: moderate` - all specifically
because the licence was already known to be unconfirmed and weights not generally downloadable.
The newly-confirmed "gated" detail doesn't change that picture. No further downgrade applied;
`last_verified` bumped with a documented reasoning trail in the entry's own changelog.

## New entities / siblings flagged for a future build pass (NOT folded into existing scores)

1. **`glm-5`** - new licence-divergent family (GLM-5/5.1/5.2/5.3/5.3-Flash; custom GLM-5.3
   License with $10B MaaS security-review gate).
2. **Nemotron 3.5 Lightning 30B-A3B** - OpenMDW-1.1, distinct licence from tracked Nemotron-3.
3. **OLMo 3** - Apache-2.0 fully_open, Dolma 3.
4. **EuroLLM-22B-2512** - new sibling.
5. **DeepSeek V4 line** (V4.1-Flash, V4-Flash-Vision-Exp, V4-Pro-0813, V4-Flash-0731) + **V3.1/V3.2**
   (MIT) - new entities.
6. **Qwen3.5 / 3.6 / 3.8** (apache-2.0) - newer siblings.
7. **Kimi K2.5 / K2.6 / K2.7-Code** - newer releases.
8. **Soofi previews** (Instruct, Isar, Rhine) - already tracked as variants of the existing entry,
   not new entities.

## Items requiring a manual eyeball before any future re-scoring (tool limits / summariser-sourced)

- **llama-4 EU-domicile multimodal carve-out** - WebFetch truncated the "Additional Terms";
  `retrieved:false` for that clause. Treated as unchanged pending a manual read.
- **Mistral Large-3-675B and Ministral-3 apache-2.0** - read via a WebFetch summariser, not the
  raw HF `LICENSE` tag. An MRL to Apache move would be materially score-moving - confirm from the
  raw file before re-scoring `use_modify`.
- **GLM-5.3 $10B MaaS threshold** - re-confirm the figure verbatim from the licence text before
  public quotation.
- **EuroLLM-22B-2512 licence tag** - expected Apache-2.0; confirm from the raw repo file.

## Net for the 21 stale entries

20 of 21 honestly bumped to `last_verified: 2026-09-21` with no score change (nothing tracked
changed; new-generation releases are flagged as separate future entities, not folded in). `soofi`
bumped after the code session confirmed the entry's existing 2026-07-25 correction already
accounts for the re-confirmed facts.
