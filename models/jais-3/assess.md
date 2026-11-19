# Assess - Jais 3 (0.9B, 3.7B, 7B, 32B, MoVA-36B-A4B, 375B-A23B)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

Scope. This entry scores the six Jais 3 weights repositories published by Inception42 for the Institute of Foundation Models (IFM) at MBZUAI: `Jais-3-0.9B`, `Jais-3-3.7B`, `Jais-3-7B`, `Jais-3-32B`, `Jais-3-MoVA-36B-A4B` and `Jais-3-375B-A23B`. All six declare Apache-2.0, share one card text, start from the K2 Horizon model of the same size and carry the same safety statement, so they form one release. The official FP8, MLX and GGUF builds in the IFM organisation are listed as variants and not scored separately.

Follow-ups, not scored here: K2 Horizon (the base fleet, "fully open" by its own card, unaudited), the four Jais-3 Uno adapter repositories (no licence tag, `ev-uno`) and Jais-ASR (speech).

<!-- item: intended-use -->
## Intended & out-of-scope use

Use Jais 3 for Arabic and English assistant and agentic applications, including reasoning, tool use, research and experimentation (`ev-card-32b`). The cards place four uses out of scope: illegal or harmful use, generating or inferring sensitive personal data, applications that depend on languages other than Arabic and English, and medical, legal, financial or safety-critical decisions without human oversight.

These are statements of intended use and not clauses of the Apache-2.0 licence. The cards also tell users to evaluate the model for their use case and add safeguards before deployment (`ev-cards-all`).

<!-- item: limitations -->
## Known limitations, bias & failure modes

The cards warn that the model can produce inaccurate or made-up content and may reflect biases in its training data (`ev-card-32b`). The report adds four limits.

- Long-tail factual recall is weak. At 375B the Arabic SimpleQA-Verified F-score is 8.5, and the model abstains in 77% of Arabic cases where it cannot answer correctly (`ev-report-eval`).
- Coding, tool use and deep search are tested only in English. Two of eleven agentic benchmarks are in Arabic (`ev-report-eval`).
- Some synthetic data has residual errors. The knowledge-infusion set has an estimated error rate of at least 9% after repair, and generated multiple-choice questions keep a bias toward the longest option being correct (`ev-report-data`).
- Decontamination matches token n-grams only, so translated or paraphrased benchmark items are not detected (`ev-report-data`).

At 32B and above the Qwen3.8 models lead most agentic benchmarks, and the 375B trails every frontier model on at least eight of ten (`ev-report-eval`).

<!-- item: openness -->
## Openness tier & components

The tier is `open_weights_recipe`.

| Component | Rating | Evidence |
|---|---|---|
| Weights | open | Ungated safetensors for all six sizes, Apache-2.0 declared (`ev-hub`, `ev-license`) |
| Training data | partial | A 23.8B-token Arabic sample is public; the full corpus, partner-supplied books and internal dialect data are not (`ev-data-sample`, `ev-report-data`) |
| Training code | partial | xLLM and RL360 are public under Apache-2.0, but no Jais-3 run configuration was found in them (`ev-code`) |
| Evaluation | open | Evaluation code, cleaned benchmarks and discarded items are public (`ev-report-release`, `ev-code`) |
| Documentation | open | Six cards, a 113-page report, source tables with token counts (`ev-report-data`) |
| Licence | open | Apache-2.0 (`ev-license`) |

Weights come with checkpoints from every stage. Each repository has branches `CPT`, `Cooldown`, `FTPO` and `SFT`, and `main` is presumed to be the final RLVR checkpoint, which the cards do not state (`ev-branches`). The report lists run configurations and W&B logs as released (`ev-report-release`). The configurations and the log project were not opened.

The data sample is about 10% of the continual-pretraining and SFT tokens (`ev-data-sample`). It holds four subsets: Arabic web text, style rewrites, web question-answer pairs and Arabic SFT conversations. It does not hold the dialect corpora, translated reasoning data, Arabizi corpus, agent trajectories or partner-supplied books.

The cards say "Code repository: Coming soon". The report, the GitHub repositories and the JaisVoice README contradict this, because xllm, RL360 and gen-eval-arabic are public. Their READMEs describe K2 Horizon and do not mention Jais 3 (`ev-code`). Whether the Jais-3 recipes can be rebuilt from them is unconfirmed.

<!-- item: license -->
## License terms & permitted use

The weights are Apache-2.0, which allows commercial use, modification and redistribution and includes a patent grant (`ev-license`). The grant is declared in the YAML front matter of each card and in section 7.1 of the report. No LICENSE or NOTICE file exists in any of the six weights repositories. The Apache text and unmodified LICENSE files exist only in the code repositories.

The data sample is ODC-BY (three web subsets) and CC BY 4.0 (the SFT subset). The pages behind the web subsets stay under the Common Crawl terms (`ev-data-sample`).

The training data includes outputs of other models. The report names GLM-5, Jais 2, Qwen3.8-27B, Qwen3.6-27B, gemma-4-31B-it and MiniMax-M3 (`ev-report-generators`). The MiniMax Community License grants non-commercial use and sets conditions on commercial use of the software and its derivative works. It does not mention outputs (`ev-teachers`). Nothing in the report says whether any generator licence reaches the data. Ask the publisher before relying on Jais 3 where this matters.

<!-- item: provenance -->
## Supply-chain & provenance

Download from `huggingface.co/inception42`, a verified organisation. Each repository holds safetensors shards with LFS sha256 values and reports a completed hub scan with no flagged files (`ev-hub`). Nothing is signed and there is no attestation.

Each repository ships `configuration_k2_horizon.py` and `modeling_k2_horizon.py`, and the card examples use `trust_remote_code=True`. Read both files and pin a revision before use.

The official FP8, MLX and GGUF builds are in the IFM organisation, which is not verified (`ev-quants`).

Lineage. Each size starts from the final post-trained K2 Horizon checkpoint of the same size and keeps its architecture and tokenizer (`ev-report-lineage`). Jais 3 is not trained from scratch. K2 Horizon is Apache-2.0 by card declaration, has no LICENSE file and calls itself "fully open". Its pre-training and mid-training datasets listed on the card return HTTP 401 on the hub API, so their access is unverified (`ev-k2-card`). The K2 report says about 10T of its pre-training tokens are synthetic (`ev-k2-report`). K2 Horizon needs its own entry.

Data supply. The Arabic data combines Common Crawl text, literature collections, model-translated and model-generated text, Arabizi transliterations, and 11.9B tokens of partner-supplied Arabic books with no named source (`ev-report-data`). The Egyptian, Moroccan, Tunisian and Iraqi translation and transliteration seeds are internal data.

<!-- item: eu-ai-act -->
## EU AI Act posture

Jais 3 is a general-purpose AI model. The 375B-A23B is the largest, at about 2.2e24 FLOPs including its K2 Horizon base (OneHill estimate), well below the 1e25 systemic-risk line. Article 55 duties do not apply.

The Article 53 open-source exemption plausibly applies: Apache-2.0 weights, public architecture and usage information, and a technical report. The exemption leaves the copyright policy and the public training-content summary in force. The report gives sources and token counts, but no summary in the AI Office template, no copyright policy and no statement on text-and-data-mining opt-outs. Code of Practice status is unknown. The report links a jaischat.ai web service, whose terms are unavailable, so no monetisation test is made.

A deployer who fine-tunes and ships a derivative under its own name may become a provider. Ask the publisher about the partner-supplied books and the generator-model licences before building a compliance file.

<!-- item: evaluation -->
## Benchmarks & evaluation

All results are the publisher's own. The report moves Arabic evaluation to generative scoring and audits 15 benchmark sets with three frontier judges, removing 5.3% of items (`ev-report-eval`). Evaluation code and cleaned sets are public, and some benchmarks on the cards are marked as released later.

- Arabic: the report says Jais 3 leads or matches open models of its size, with the largest margins at small sizes, and that every size scores above 88% on the new AraIFBench.
- Dialects: Jais 3 has the best dialect-identification score (QADI) at every open-weight size. Transliteration is weaker at small sizes, with Darija scores around 79 from 0.9B to 7B (`ev-report-dialect`).
- Agentic: Jais 3 leads open baselines at 3.7B and 7B. At 32B and above the Qwen3.8 models lead most benchmarks, and each frontier model beats the 375B on at least eight of ten.
- Factuality: Jais 3 abstains far more often than other models when it does not know. Its long-tail recall stays low.

No independent re-run of any benchmark was found.

<!-- item: safety-eval -->
## Independent safety evaluation

No independent safety, red-team or jailbreak evaluation exists for Jais 3. The publisher ran four evaluations (`ev-report-safety`).

- AraSafe, 1,254 human-written harmful Arabic prompts: every size refuses more than 92%.
- Arabic Regional Safety: the 0.9B, 7B, 32B, MoVA-36B-A4B and 375B-A23B score above 98% in all three settings. Every model scores lower under the government perspective than under the opposition perspective.
- HarmBench, standard and contextual prompts: refusal rates run from 89.75% (0.9B) to 98.00% (MoVA-36B-A4B and 375B-A23B).
- XSTest accuracy: 87.78% (0.9B) to 93.56% (375B-A23B).

The judge is gemma-4-26B-A4B-it, which agrees 98% with the official HarmBench classifier. Safety SFT data is about 0.22% of the SFT tokens. The report notes that safety scores vary with decoding settings and that its system-prompt ablation covers safety only.

No result tests tool, terminal or file actions, although the models are built to take them. No text guard model is released with the family.
