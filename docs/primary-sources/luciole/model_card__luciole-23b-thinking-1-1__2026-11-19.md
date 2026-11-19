doc_type: model_card
entity: luciole
variant/applies-to: OpenLLM-France/Luciole-23B-Thinking-1.1 (sibling release, NOT the scored release; logged because it differs on safety posture)
source_url: https://huggingface.co/OpenLLM-France/Luciole-23B-Thinking-1.1 (raw README.md)
repo_sha_read: 685043b3320bebe4490ba55d625420ad57f3abb0 (created 2026-09-09, last modified 2026-11-12)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Governing clauses (verbatim extracts, README.md, 15,717 bytes)

[Front matter] "license: apache-2.0", base_model Luciole-23B-Base, datasets Luciole-PostTraining-Dataset-1.1, languages fr and en. Not gated; no LICENSE file in the repo.

[Safety note, top of card] "NOTE: Although this model has undergone safety alignment during the DPO thinking phase, it could still generate unsafe output for certain inputs. The model also has not been trained on identity prompts, so it may not correctly answer the questions about its name/origin. The Luciole models are under active development and we plan to address these issues in future versions."

[Training] "It was trained in two phases: (i) a supervised fine-tuning (SFT) phase on instruction data with thinking traces, and (ii) a final preference alignment phase using Direct Preference Optimization (DPO)." SFT 2.6M samples, DPO 103K samples.

[Tool calling] "While the model has seen some tool calling data, it has a tendency to over-refuse tool calling requests."

[Thinking switch] "Thinking can be turned off by using tokenizer.apply_chat_template(..., enable_thinking=False). This will append empty thinking tags ... However, for testing a non-thinking model, it is better to conduct experiments on Luciole-23B-Instruct-1.1." (The earlier second-hand research lead said enable_thinking=False is unsupported; the card says the opposite.)

[Evaluation] Thinking budget 5000 tokens, temperature 0; "Luciole-23B-Thinking-1.1 is comparable to Olmo-3-32B-Think-DPO on all the English benchmarks tested except GPQA." "it has the best overall performance on the French benchmarks tested." (publisher claims, figures figure_en.png and figure_fr.png not analysed)

[Serving] vLLM needs "--reasoning-parser qwen3" and "a recent vLLM (>= 0.24; prefer the latest)".

[Technical report] "Technical report: coming soon."
