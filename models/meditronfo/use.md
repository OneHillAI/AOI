# Use - MeditronFO (Apertus-70B-MeditronFO / Apertus-8B-MeditronFO)

_What can it do and how do we use it? Capabilities, context window, prompt format and language coverage. Remember the boundary from the assess domain: research and evaluation use, not patient decisions._

<!-- item: capabilities -->
## Capabilities & modalities

Text in, text out, English medical content. The fine-tuning corpus covers four kinds of material: public medical exam and patient-question datasets (MedMCQA, MedQA, AfriMed-QA, HealthSearchQA, LiveQA-Med), synthetic exam-style questions, questions generated from 14,192 clinical practice guidelines, and open-ended adversarial clinical vignettes modelled on clinician-written MOOVE cases (`ev-data-card`). Compared with its Apertus-Instruct base, the 70B gains 9.2 points on MedQA, 7.4 on MedMCQA, 4.3 on MedXpertQA, 9.9 on HealthBench and 0.2 on PubMedQA (`ev-card-70b`). The 8B gains on MedQA and MedMCQA but loses 2.9 points on PubMedQA (`ev-card-8b`). It is weaker at general instruction following than its base (`ev-project-page`). No image or audio input.

<!-- item: context-window -->
## Context window & long-context behaviour

`config.json` sets 65,536 positions with llama3-style rope scaling (factor 8 from an original 8,192) for both sizes (`ev-hf-meta`). The fine-tuning packed sequences of 8,192 tokens and the card's generation defaults are 8,192 new tokens (`ev-card-70b`). The publisher reports no long-context evaluation of the fine-tune, so do not assume the base model's long-context quality survived. Clinical records, long guidelines or multi-document prompts should be tested against your own cases first.

<!-- item: chat-template -->
## Prompt format & chat template

Both repositories ship a `chat_template.jinja` (`ev-hf-meta`). Use `tokenizer.apply_chat_template(messages, add_generation_prompt=True, ...)` as the card does, with a single user turn and no system prompt; the AutoMOOVE answering setup also used the vignette alone with no system prompt (`ev-card-70b`, `ev-github-readme`). Sample with temperature 0.7 as in the card and generation config, which is what the benchmark numbers used for open-ended tasks; the multiple-choice benchmarks were decoded greedily (`ev-card-70b`).

<!-- item: languages -->
## Language coverage

The cards tag English only, and the corpus is English (`ev-card-70b`, `ev-data-card`). The Apertus base is advertised as multilingual with support for over 1,000 languages (`ev-base-card`), but the paper and cards report no multilingual medical evaluation, so treat any non-English clinical use as untested.

<!-- tool-use and structured-output are `gap` items in entry.yaml - see their gap_reason. -->
