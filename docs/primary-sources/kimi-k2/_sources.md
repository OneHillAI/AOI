# kimi - primary-source clauses (2026-07-25)

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://raw.githubusercontent.com/moonshotai/Kimi-K2/main/LICENSE | 2026-07-25 | yes | true | Modified MIT; 100M-MAU/$20M-revenue "display Kimi K2" clause verbatim (blob path 404, raw ok)
model_card | https://huggingface.co/moonshotai/Kimi-K2-Instruct | 2026-07-25 | yes | true | confirms Modified MIT tag
technical_report | https://arxiv.org/abs/2507.20534 | 2026-07-25 | yes | true | "Kimi K2: Open Agentic Intelligence"
terms | https://platform.kimi.ai/docs/agreement/modeluse.md | 2026-07-25 | yes | true | Singapore law/SIAC; training opt-out via enterprise agreement. platform.moonshot.ai 302s here
privacy_policy | https://platform.kimi.ai/docs/agreement/userprivacy | 2026-07-25 | yes | true | Singapore processing; trains on user content by default
license | https://raw.githubusercontent.com/moonshotai/Kimi-K2/main/LICENSE | 2026-11-19 | yes | true | Re-read: byte-identical to HF Instruct and Base LICENSE; 100M-MAU/$20M clause unchanged; K2.5/K2.6/K2.7-Code/0905/Thinking licences compared (same clause, only the display string and copyright year differ). File: license__kimi-k2__2026-11-19.md
model_card | https://huggingface.co/moonshotai/Kimi-K2-Instruct | 2026-11-19 | yes | true | Re-read: Modified MIT statement unchanged; front matter new_version -> Kimi-K2-Instruct-0905 (since 2025-09-05). File: model_card__kimi-k2-instruct__2026-11-19.md
terms | https://platform.kimi.ai/docs/agreement/modeluse.md | 2026-11-19 | yes | true | Re-read: page now dated "Last Updated: July 30th, 2026"; training/opt-out/Singapore/SIAC clauses unchanged in substance. File: terms__hosted-platform__2026-11-19.md
privacy_policy | https://platform.kimi.ai/docs/agreement/userprivacy | 2026-11-19 | yes | true | Re-read: dated April 30, 2025, unchanged (trains on user content, Singapore servers, open-ended retention). Consumer policy at kimi.ai/user/agreement/userPrivacy is a client-rendered page and was not readable. File: privacy_policy__hosted-platform__2026-11-19.md
docs | https://platform.kimi.ai/docs/models.md | 2026-11-19 | yes | true | Hosted K2 series: closed to new users from 2026-10-31, retirement planned end of December 2026 (API only, weights unaffected). File: docs__hosted-model-list__2026-11-19.md
```

## license - Modified MIT
source_url: raw.githubusercontent.com/moonshotai/Kimi-K2/main/LICENSE | exists: yes | retrieved: true
[Modification - VERBATIM] "Our only modification part is that, if the Software (or any derivative works thereof) is used for any of your commercial products or services that have more than 100 million monthly active users, or more than 20 million US dollars (or equivalent in other currencies) in monthly revenue, you shall prominently display 'Kimi K2' on the user interface of such product or service." Otherwise standard MIT.

## model_card - Kimi-K2-Instruct
source_url: huggingface.co/moonshotai/Kimi-K2-Instruct | exists: yes | retrieved: true
"Both the code repository and model weights are released under the Modified MIT License." MoE 1T total / 32B active; 15.5T tokens; Muon optimizer; 128K context.

## technical_report
source_url: https://arxiv.org/abs/2507.20534 | exists: yes | retrieved: true
[Title] "Kimi K2: Open Agentic Intelligence" - MoE; MuonClip optimizer (QK-clip); 15.5T tokens; 66.1 Tau2-Bench, 65.8 SWE-Bench Verified.

## terms - platform.kimi.ai (moonshot 302s here)
source_url: platform.kimi.ai/docs/agreement/modeluse.md | exists: yes | retrieved: true
[Training] used to improve services; opt-out via enterprise/separate written agreement. [Jurisdiction] Singapore law; SIAC arbitration (English).

## privacy_policy - platform.kimi.ai
source_url: platform.kimi.ai/docs/agreement/userprivacy | exists: yes | retrieved: true
[Training] trains on user prompts/audio/images/videos/files by default. [Location] MOONSHOT AI PTE. LTD, Singapore servers. NOTE: separate consumer policy at kimi.com (not fetched).
