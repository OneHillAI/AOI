doc_type: docs
entity: luciole
variant/applies-to: OpenLLM-France/Luciole-Training-Dataset (the pretraining data of the Luciole base models)
source_url: https://huggingface.co/datasets/OpenLLM-France/Luciole-Training-Dataset (raw README.md, 91,089 bytes)
repo_sha_read: 2ce646e333c4d8a34ebc7649534099eaf3415e64 (created 2025-11-25, last modified 2026-11-10; not gated; about 9,185 downloads)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Governing clauses (verbatim extracts)

[Licence] front matter "license: cc-by-sa-4.0". Final section: "Copyright (c) 2025-2026 LINAGORA SAS (compilation, preprocessing and project-generated data). Each source corpus remains under its original licence, listed in the 'Details on Data Sources' section. Released under CC-BY-SA-4.0."

[Open-licence claim] "The Luciole Training Dataset contains only corpora under open licenses." and, under limitations: "While we have made strong efforts to include only open corpora, it is possible that individual documents in those corpora are copyrighted." An opt-out form is offered (openllm-france.fr/delete-data).

[Size and languages] "The full dataset contains around 4.65 trillion tokens of multilingual data, including English (53.4%), French (16.3%), German (5.6%), Spanish (4.9%), Italian (2.8%), Portuguese (1.9%), Dutch (1.4%), Arabic (0.7%), and a small subset of regional languages ... (0.4%)." Code 11.3%, mathematics 4.7%.

[What is not on Hugging Face] "Due to storage constraints, the English web data from the Luciole Training Dataset is published elsewhere". "we could not directly host three subsets of the Luciole-Training-Dataset: FineWeb-edu, DCLM-dolmino, and Fineweb-HQ. These subsets can instead be downloaded from our external server" (dl.labs.linagora.com, via a login-token curl command). OpenMathInstruct-1 is shared there "under an Nvidia license". The external server was not tested here (JavaScript file browser; the zip is very large).

[Opt-outs and PII] "Robots.txt rules were applied retrospectively to all web-crawled datasets" using Common Crawl dump CC-MAIN-2025-26. Emails, IP addresses and phone numbers are replaced with placeholders for named web corpora.

[Source licences listed in "Details on Data Sources" (selection)] FineWeb2, FineWeb-HQ, FineWeb-Edu, FineMath, MegaMath, DCLM-Dolmino, Dolma3 Longmino, Common Corpus subsets, Scholar: ODC-BY or "mixed open licenses"; HPLT 2: CC-0 1.0; Common Pile v0.1 subsets: "Mixed open licenses"; Nemotron Post-Training v2 and OpenCodeReasoning: CC-BY 4.0; OpenThoughts3: Apache 2.0 ("reasoning traces annotated from QwQ-32B"); Paradocs, Aya: Apache 2.0; Pleias SYNTH: CDLA-permissive 2.0; MathPile (Commercial): CC BY-SA 4.0; Wikimedia: GFDL/CC BY-SA; Vikidia: GFDL; Eurovoc: EUPL 1.1; Etalab Open Licence 2.0 for French government sources; CulturaX: "mC4 license, OSCAR license"; Croissant Aligned original source: "License: not specified"; StarCoder and StackEdu: mixed open licences; OpenMathInstruct-1: "NVIDIA".

[Claire NC-SA data in the listing] "Claire (French and English)": sources "OpenLLM-France/Claire-Dialogue-French-0.1. License: CC BY-NC-SA 4.0" and "OpenLLM-France/Claire-Dialogue-English-0.1. License: CC BY-NC-SA 4.0". 'Claire' is one of the dataset configurations. The card does not say whether the Luciole models were trained on it. This sits against the card's own statements that the whole dataset is CC-BY-SA-4.0 and "contains only corpora under open licenses". Non-commercial sources cannot be relicensed as CC-BY-SA-4.0 by the compiler; whether the Claire config is in the training mix is not stated.

[Synthetic data in the pretraining mix] "Synth FineWeb 2: Using Qwen 3 8B, we synthetically augmented documents from FineWeb 2 by prompting the model to reformulate them". "Synth Wikipedia: Using Qwen 3 8B, we synthetically augmented documents from Wikipedia by generating question/response pairs". Configurations also include NemotronPosttraining-chat, -code, -math, -multilingual_w_thinking, -multilingual_wo_thinking, -stem; OpenCodeReasoning; OpenThoughts-code; OpenThoughts-science; and Dolma3Longmino synthetic subsets. The Nemotron French subset was translated by the Luciole team ("we translated the thinking traces into French").

## What it establishes

A large, documented, ungated pretraining corpus with per-source licences is public, which supports the training_data component, but (a) the three largest English web subsets sit on a separate server, (b) the single CC-BY-SA-4.0 label sits over sources under other licences, including NC-SA and "not specified", and (c) the mix contains model-generated text (Qwen3-8B reformulations, Nemotron, OpenThoughts) that the base model was trained on.
