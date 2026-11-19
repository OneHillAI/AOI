# Assess - Boldt-DC (350M and 1B base models)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Use Boldt-DC as a German research and fine-tuning starting point. Both models are base models for text completion, and the cards say they are not tuned for chat or instruction following (`ev-card-350m`, `ev-card-1b`). The organisation page calls the 350M model suited to constrained environments (`ev-project`).

No out-of-scope list is published. Treat any assistant, safety-relevant or customer-facing use as out of scope until you have tuned and evaluated the model yourself.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The publisher states that it ran no toxicity, demographic-bias or stereotype evaluation, and that repeated epochs could amplify encoded bias (`ev-card-1b`, `ev-paper`).

- The models are German only, and the paper tests no other language.
- Context is 2,048 tokens.
- The largest model is 1.2B parameters, trained on at most 200B tokens, and the paper says it is unclear whether the results hold at larger scale.
- Absolute scores are low: MMLU is 29.29 (350M) and 31.06 (1B) against a 25 floor.
- The paper describes no check for benchmark contamination.

<!-- item: openness -->
## Openness tier & components

The tier is `open_weights`, which caps the openness score at 3. Weights, the training dataset and the documentation are open. Training code and evaluation code are partial.

- Weights: open. Safetensors, ungated (`ev-hf-platform`).
- Training data: open. The 28B-token Dense-Core dataset is public under ODC-By, and the models repeat it to 200B tokens (`ev-dataset`).
- Training code: partial. The paper names Nanotron, Datatrove and TRL and lists hyperparameters. No configs or scripts are released and no repository is linked (`ev-paper`).
- Evaluation: partial. The translated benchmarks are public and results are in the paper. No harness code is released (`ev-paper`).
- Documentation: open. Two cards and a peer-reviewed paper with limitations (`ev-card-1b`, `ev-paper`).
- Licence: open. Apache-2.0 is declared (`ev-licence`).

The three filter classifiers are public, but the 500k Llama-written labels they were trained on are not. Releases that add other data are separate entries (`ev-siblings`).

<!-- item: license -->
## Licence terms & permitted use

Apache-2.0 is declared in the front matter of both cards, and the repos are ungated (`ev-licence`). That allows commercial use, modification and redistribution. Three points limit how far the declaration can be trusted.

1. No LICENSE, NOTICE or copyright-holder file exists in any Boldt repo, and the card bodies carry no licence text. The paper says only that the weights "will be made available under licenses compatible with their upstream sources". Apache-2.0 section 4 expects recipients to receive the licence text, so a redistributor must add it.
2. The training data is ODC-By 1.0 web text from Common Crawl and carries Common Crawl's Terms of Use. The weights' declaration mentions neither (`ev-dataset`).
3. Llama-3.3-70B-Instruct wrote the labels that trained the three released classifiers. Llama 3.3 section 1.b.i asks that a model trained on its outputs carry "Llama" in its name (`ev-llama-terms`). The classifier repos have no licence and no such name. The Boldt base models were trained on filtered web text, so the clause attaches most directly to the classifiers. Boldt does not address the question, and this entry does not decide it.

<!-- item: provenance -->
## Supply-chain & provenance

The canonical source is `huggingface.co/Boldt`. The organisation is unverified and has two members, who are the paper's first and last authors (`ev-hf-platform`). The chair's project page links to it (`ev-project`).

Weights are safetensors only. Hugging Face shows LFS hashes, and its scan flagged no files, although `scansDone` is false on the 1B repo. The repos hold plain Llama-architecture files and no custom code. Nothing is signed. That is about 4 of 8 checklist boxes, and the score is 2 because anchor 3 needs a verified organisation.

"Trained from scratch" is a claim in the cards and the paper, and no document names a base model or an initial checkpoint (`ev-card-350m`, `ev-paper`). The models use their own 32k BPE tokenizer trained on the subset. OneHill has not verified the claim and no independent party has attested it.

<!-- item: eu-ai-act -->
## EU AI Act posture

Boldt-DC is a general-purpose AI model. OneHill's arithmetic from the paper's figures (6 x 1.2B parameters x 200B tokens) gives about 1.4e21 FLOPs, far below the 1e25 systemic-risk threshold, so no Article 55 duties apply (`ev-paper`).

Whether the Article 53 open-source exemption applies is uncertain. Apache-2.0 would normally qualify and the weights and architecture are public. No licence text ships, and the Llama 3.3 question is open. The exemption never covers the copyright policy or the public training-content summary. No copyright policy exists. The paper and the dataset card describe the corpus but are not in the AI Office template (`ev-dataset`). No code-of-practice signatory status appears in any document examined. This is guidance, not legal advice.

<!-- item: evaluation -->
## Benchmarks & evaluation

Every figure is the authors' own, on a German suite they re-translated with Tower+ 72B. Global MMLU was used as published. No independent re-run was found (`ev-card-1b`, `ev-paper`, `ev-no-independent`).

Scores are MMLU, ARC-Challenge, ARC-Easy, HellaSwag, LAMBADA and OpenBookQA, then the average.

- Boldt-DC-350M (200B tokens): 29.29, 32.24, 52.87, 43.21, 37.48, 45.86. Average 40.16.
- Boldt-DC-1B (200B tokens): 31.06, 35.99, 57.30, 48.69, 42.80, 48.48. Average 44.05.
- LLaMmlein-1B (1T tokens): 29.26, 30.27, 48.19, 44.80, 44.89, 47.27. Average 40.78.
- Gemma-3-1B (2T* tokens): 30.01, 30.55, 47.89, 43.43, 41.71, 45.05. Average 39.77.
- Llama-3.2-1B (9T* tokens): 28.58, 29.90, 40.51, 40.07, 44.31, 44.04. Average 37.90.

In the cards a * marks token counts of multilingual data mixtures. On this suite the 1B model beats the 1B-class references on average, while LLaMmlein-1B and Llama-3.2-1B score higher on LAMBADA. The 350M model beats Gemma-3-1B and Llama-3.2-1B on average. Larger models score higher: Gemma-2-2B averages 46.62 and Qwen3-1.7B-Base 44.89. The cards and project page call the results state-of-the-art, which is marketing wording (`ev-project`).

<!-- safety-eval is a `gap` item. The publisher ran no toxicity or bias evaluation and no independent safety evaluation exists. -->
