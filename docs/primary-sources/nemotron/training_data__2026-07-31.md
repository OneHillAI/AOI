doc_type: training_data
entity: nemotron
variant/applies-to: Nemotron 3 released pretrain + post-training datasets and the openness claim
source_url: https://huggingface.co/datasets/nvidia ; per-dataset URLs below ; https://arxiv.org/abs/2512.20856
document_effective_date: Nemotron 3 datasets released ~2025-12
retrieval_date: 2026-07-31
exists: yes
retrieved: true
tag: publisher

## Pretraining datasets (the actual, PARTIAL pretrain data)
[Nemotron-CC-v2.1 - VERBATIM] https://huggingface.co/datasets/nvidia/Nemotron-CC-v2.1 : "Designed for the NVIDIA Nemotron 3 family of LLMs" ; "2.5T English tokens; 3.8B records; 4.59 TB" ; licence "NVIDIA Data Access Agreement for Model Training" (a CUSTOM NVIDIA data licence, NOT CC-BY).

## Post-training datasets (Nemotron-Post-Training-v3 collection - CONFIRMED as the data used)
[Nemotron-SFT-Safety-v1 - VERBATIM] https://huggingface.co/datasets/nvidia/Nemotron-SFT-Safety-v1 : "45,145 total samples" ; licences "CC-BY-4.0", "Apache 2.0", "MIT" ; "part of the Nemotron-Post-Training-v3 Collection of datasets used in the post-training phase of Nemotron Nano, Super, and Ultra v3". CONFIRMS post-training data is the data used AND is CC-BY-4.0.

## Licence picture
Post-training data = CC-BY-4.0 (+ Apache/MIT). Pretraining web data = custom NVIDIA licences
("NVIDIA Data Access Agreement for Model Training" / "NVIDIA Open Data License Agreement"), NOT CC-BY.

## Openness claim vs reality
[Newsroom - VERBATIM] "the NVIDIA Nemotron(TM) 3 family of open models, data and libraries" ; "Three trillion tokens of new Nemotron pretraining, post-training and reinforcement learning datasets" ; "All tools and datasets are now available on GitHub and Hugging Face".
[White paper - VERBATIM, note the qualifier + future tense] "We will openly release the model weights, pre- and post-training software, recipes, and all data for which we hold redistribution rights."
[Ultra blog - VERBATIM, self-qualified] "Nemotron 3 Ultra is fully open - including weights, data, and recipes" BUT "much of the training data pipeline is released as permissively as possible".

## REALITY CHECK
Full corpus is NOT downloadable. Cards report far larger training totals (Nano "25T tokens",
Ultra "approximately 20T tokens", Ultra blog "10T token pre-training foundation") than the
RELEASED new dataset ("3-trillion-token"). Released data is a PORTION.

## Training code / recipe
[Repo] https://github.com/NVIDIA-NeMo/Nemotron : recipes for Nano/Super/Ultra/Nano Omni.
[Decisive reproducibility caveat - VERBATIM] "Open-Source Data Only: These recipes train exclusively on the open-sourced subset of training data. Results will differ from the tech report benchmarks, which used additional proprietary data."

## VERDICT (the decisive openness question)
Training data + recipe: PARTIALLY RELEASED. Weights + runnable recipes are open and post-training
data is genuinely CC-BY-4.0, BUT the full training corpus is not reproducible (recipes train on
the open subset only; NVIDIA's commitment is hedged to "all data for which we hold redistribution
rights"; the pretraining web corpus is under custom NVIDIA data licences). Materially more open
than the open-weights norm but does NOT reach fully_open. Recommended tier: open_weights_recipe
(tier 4) with the partial-corpus caveat explicit.
