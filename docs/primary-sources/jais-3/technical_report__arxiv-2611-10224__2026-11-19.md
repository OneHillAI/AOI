# technical_report / Jais 3: Introducing Arabic-centric Agentic AI (arXiv 2611.10224v2)

source_url: https://arxiv.org/abs/2611.10224 (PDF https://arxiv.org/pdf/2611.10224v2, 113 pages, 1,984,716 bytes)
retrieval_date: 2026-11-19
doc_type: technical_report
exists: yes
retrieved: true
tag: publisher

NOTE (OneHill): the arXiv HTML rendering returned HTTP 404, so the text below comes from the PDF (v2, 12 Nov 2026, "IFM Technical Report: 2026-11-13") through macOS PDFKit text extraction. Tables lose column alignment in extraction; only prose and table captions are used for claims. The linked blog and tech-report pages at ifm.ai returned HTTP 403 (Cloudflare challenge) and were not read. Authors: Team IFM at Institute of Foundation Models, Mohamed bin Zayed University of Artificial Intelligence; Cerebras Systems; Inception42. Submitted 6 Nov 2026 (v1), v2 12 Nov 2026.

All extracts are verbatim PDF text (line breaks as extracted).


## Overview and release links (p.1)
```
IFM Technical Report: 2026-11-13
Jais 3: Introducing Arabic-centric Agentic AI
Jais Team*
Institute of Foundation Models, Mohamed bin Zayed University of Artificial Intelligence
Cerebras Systems, Inception42
arXiv:2611.10224v2 [cs.CL] 12 Nov 2026
Overview
We present Jais 3, a fleet of six open, Arabic-centric agentic language models ranging from 0.9B
to 375B parameters. Jais 3 is built to complete tasks for Arabic speakers, not only to answer
questions in plain text: it is trained to plan multi-step tasks, call tools and Model Context Protocol
(MCP) servers, operate a terminal, search the web, and read, edit, and produce PDF, spreadsheet,
and presentation files, while communicating with the user in Arabic. Instead of pretraining from
scratch, we adapt each model of the fully open K2 Horizon fleet to Arabic through continual
pretraining, followed by supervised fine-tuning (SFT), final token preference optimization (FTPO),
and reinforcement learning with verifiable rewards (RLVR). We combine natural Arabic text with
translated, transliterated, and synthetic Arabic, and replay the base model’s own training data
to keep its reasoning, agentic, and English abilities. Jais 3 covers Modern Standard Arabic and
the major regional dialects, follows instructions with Arabic-specific constraints, and inherits the
512K-token context window of K2 Horizon (all models except the 0.9B). To our knowledge, its 375B
model is the largest open Arabic-centric language model to date. For evaluation, we revisit how
Arabic models are assessed, moving to fully generative evaluation on audited Arabic benchmarks.
Across model sizes, Jais 3 matches or outperforms open-weight models of comparable size on
Arabic and agentic benchmarks, with particularly strong agentic capabilities and Arabic instruction
following, and far fewer hallucinations. We release the weights and the checkpoints from every
training stage of all six models, together with samples of the training data, the data recipes and
training configurations, the training logs, the audited benchmarks, and the evaluation code.
Jais 3 hf.co/collections/IFM/jais-3
Jais 3 (Web) jaischat.ai
Jais 3 (Training Code) github.com/ifm-ai/xllm
Jais 3 (RL Code) github.com/ifm-ai/RL360
Jais 3 (Eval Code) github.com/ifm-ai/gen-eval-arabic
```

## 1 Introduction: lineage and contributions (pp.4-5)
```
as Arabizi. Natural Arabic text on the web is limited and noisy, and much of what exists is classical,
religious, or news prose. Arabic-centric models such as Jais (Sengupta et al., 2023; Anwar et al., 2026),
AceGPT (Huang et al., 2023), ALLaM (Bari et al., 2024), and Fanar (Fanar Team et al., 2025, 2026) have
narrowed the gap. These models, like the benchmarks used to compare them, are judged mainly on whether
they can answer a question in Arabic. Meanwhile, open agentic models, which plan multi-step work, call
tools, and handle files, are trained and benchmarked mostly in English, and how well they serve Arabic
users is rarely a design goal. As a result, open models that can complete real tasks for Arabic speakers,
rather than only converse with them, are largely missing.
This report presents Jais 3, a fleet of six Arabic-centric agentic models that range from 0.9B to 375B
parameters: four dense models (0.9B, 3.7B, 7B, 32B) and two sparse Mixture-of-Experts models: a 36B
model with Mixture-of-Value Attention (36B MoVA, 4B active parameters) and a 375B model (23B
active). Instead of pretraining from scratch, we build Jais 3 on K2 Horizon (IFM Team, 2026), a fully
open model fleet pretrained on up to about 22T tokens with extensive reasoning and agentic data. Each
Jais 3 model starts from the final, post-trained checkpoint of the K2 Horizon model of the same size and
keeps its architecture and tokenizer unchanged (Section 2.3). We adapt it to Arabic through continual
pretraining, which ends with a short cooldown, then post-train it with supervised fine-tuning (SFT),
final token preference optimization (FTPO), and reinforcement learning with verifiable rewards (RLVR)
(Figure 1). Our goal is to add Arabic language, dialectal, and cultural competence while keeping the
reasoning, long-context, agentic, and English abilities of the base fleet. To our knowledge, Jais 3 is the
first language adaptation of K2 Horizon, and its 375B model is the largest open Arabic-centric language
model released to date.
Continual pretraining Post-training
K2 Horizon
(final) Main stage Cooldown SFT FTPO Mixed-task
RLVR
Figure 1: Training pipeline of Jais 3. Each model starts from the final, post-trained K2 Horizon checkpoint of the
same size and passes through Arabic and English continual pretraining (ending with a short cooldown), supervised
fine-tuning (SFT), final token preference optimization (FTPO), and mixed-task reinforcement learning with verifiable
rewards (RLVR).
Contributions. The main contributions of this work are:
• An open Arabic-centric agentic model fleet. We release six models from 0.9B to 375B parameters,
covering on-device to large-scale server deployments. All models except the 0.9B inherit the 512K-
token context window of K2 Horizon. On Arabic, Jais 3 leads or matches the best open models at
every size, with the largest margins at small sizes, and the 375B model is competitive with Claude
Sonnet 5 (Section 6.1).
• Agentic capabilities for Arabic users. Jais 3 models can plan multi-step tasks, call tools and
Model Context Protocol (MCP) servers, operate a terminal, and search the web while communicating
4
with the user in Arabic. Connected to file tools, they can read, edit, and produce PDF, spreadsheet,
and presentation files directly in Arabic (Sections 5.1.7 and 6.2). They also follow complex instructions
with Arabic-specific constraints on orthography, diacritics, and morphology (Section 5.1.4).
• A documented recipe for adapting a strong base model to a new language. We describe the
```

## 2.3 K2 Horizon (pp.7-8)
```
modeling.
2.3 K2 Horizon
K2 Horizon (IFM Team, 2026) is a fully open fleet of six language models developed at the Institute
of Foundation Models (IFM) and released under the Apache 2.0 license. The models use a standard
Transformer backbone with grouped-query attention, rotary position embeddings, and SwiGLU feed-
forward layers, and add components of their own: grouped RMSNorm across the fleet and, in the 36B
model, Mixture-of-Value Attention (MoVA) with a softplus-activated attention gate. The fleet has four
dense models (0.9B, 3.7B, 7B, and 32B) and two sparse ones (Table 1). The 375B model is a fine-grained
Mixture-of-Experts (MoE) model with 192 routed experts and one shared expert per layer, of which eight
routed experts are active per token. The 36B MoVA model combines MoE feed-forward layers with MoVA,
which applies expert routing to the value projections in attention: each token selects 4 of 64 value experts,
at no additional KV-cache cost. All models share a 250,624-token vocabulary except the 0.9B, which uses
a 64,256-token vocabulary to save memory on device.
0.9B 3.7B 7B 32B 36B MoVA 375B
Architecture Dense Dense Dense Dense MoE + MoVA MoE
Active backbone params (B) 0.88 3.78 6.95 32.21 4.67 23.59
Total backbone params (B) 0.88 3.78 6.95 32.21 36.16 376.09
Layers 28 36 36 64 48 61
Hidden dimension 1,536 2,560 4,096 5,120 2,560 6,144
Query / KV heads 32 / 8 32 / 8 32 / 8 64 / 8 32 / 8 48 / 8
Vocabulary size 64,256 250,624 250,624 250,624 250,624 250,624
Pretraining tokens (T) 5.0 21.9 21.9 21.9 21.9 15.1
Context after mid-training 128K 512K 512K 512K 512K 512K
Table 1: K2 Horizon configurations (IFM Team, 2026), the starting point of Jais 3. Backbone parameter counts
exclude the input embedding and output projection. The 375B model was pretrained in two phases (7.05T and
8.05T tokens).
Training. The models are pretrained with an 8K-token context on about 22T tokens (IFM Team, 2026)
(15T for the 375B model and 5T for the 0.9B model). The pretraining mixture combines web, code,
7
mathematics, science, multilingual, and domain-specific data with about 10T synthetic tokens, and nearly
17% of it consists of problem-solving trajectories with explicit reasoning. Mid-training then extends the
context in stages from 32K to 128K and 512K tokens (1.1T, 500B, 110B, and 200B tokens over four stages),
while adding reasoning and agentic data; the 0.9B model follows a shorter two-stage schedule that ends at
128K. Post-training trains domain-specific RL specialists, merges them into one policy, and adds supervised
fine-tuning, with a short final token preference optimization (FTPO) stage on the small models to remove
degenerate repetition. The release includes final and intermediate checkpoints, training code, data or data
recipes, and training logs.
Arabic inK2 Horizon. Arabic is already well represented in K2 Horizon (IFM Team, 2026). Multilingual
text makes up about 7% of the pretraining mixture across 17 languages, and Arabic is the second-largest of
them. The tokenizer was also trained on a corpus that is roughly a quarter Arabic, to give Arabic text an
efficient segmentation. Even so, Arabic is not a target language of K2 Horizon, and adapting it to Arabic
pays off: Jais 3 raises the Arabic average by 9 to 35 points over the K2 Horizon model it starts from.
From K2 Horizon to Jais 3. Each Jais 3 model starts from the final, post-trained checkpoint of the K2
```

## 3 Data Processing: key takeaways and inventory (p.9)
```
reliably followed, so rigid answer extraction can mark correct responses as wrong. We therefore convert all
benchmarks to generative evaluations and use an LLM judge to identify and grade the final answer, using
the original benchmark gold label as a reference, regardless of its position or format.
Several widely used benchmarks also contain defective items that penalize correct answers. For instance,
an ArabicMMLU (Koto et al., 2024) item keys 15 as the number of NATO members, although the alliance
now has 32; an Arabic GSM8K (Omartificial-Intelligence-Space, 2025) reference solution miscounts the
coins in its own question; and an ArabCulture (Sadallah et al., 2025) item offers three equally plausible
options but keys only one as correct. We filter such items with a three-judge LLM audit, which removes
5.3% of the items in the 15 benchmark sets we use (Section 6.1.1).
8
3 Data Processing
Key Takeaways
• Plan for the natural-text ceiling. Natural Arabic web text and literature supply about 19% of the
continual-pretraining mixture; translated and synthetic Arabic supply about 38% of the run, of which
about 16 points is Arabizi (Latin script) and about 22 points Arabic script. The parallel dialect text
is an LLM translation of English conversations, and the English side of those conversations adds a
further 6 points.
• Replay runs through every stage. Data from the base model’s own mid-training (web, reasoning,
and agentic traces) makes up 25% of continual pretraining and SFT and is part of every cooldown
mixture, where it is drawn from the most recent mid-training phase of the replay data used in
continual pretraining.
• Every source needs its own filters and quality checks. One shared rule set removed 12% of a
dialect corpus and 34% of a diacritized one; per-source rules kept over 99% of both.
Jais 3 is trained by continuing the pretraining of K2 Horizon (Section 2.3), so the data work has a different
goal from building a corpus from scratch: add Arabic knowledge, dialects, and assistant behavior without
eroding what the base model already does well. This shapes every decision in this section. Arabic data is
selected and weighted for what the base model lacks, and a share of the base model’s own mid-training
data (web text, reasoning traces, and agentic trajectories) is replayed in each stage. Jais 3 builds on the
Arabic data work of Jais 2 (Anwar et al., 2026). For this release we name each source, report tokens
under one tokenizer, and state what was filtered, deduplicated, and decontaminated, including the cases
where a step was not run.
The inventory we draw from holds approximately 1.63T tokens, counted with the Jais 3 tokenizer, which is
unchanged from K2 Horizon: 1.41T of pretraining-style text across 39 datasets and 224B of chat-formatted
data across 35 datasets. These are sizes of what we prepared, not what the model saw; the training mixtures
sample from the inventory with per-source weights, and we report inventory and exposure separately
throughout. The Arabic side combines ArabicTxT360 and style rewrites of it, Arabic translations of the
base model’s reasoning data, a synthetic Arabizi corpus, parallel dialect text, and small diacritization and
search-trajectory sets. Coverage therefore spans Modern Standard Arabic, regional dialects, Arabizi, and
diacritized text.
The data description is organized by training stage (Table 2). Continual pretraining samples 201.5B tokens,
with each source weighted for about one pass, 75% Arabic-side and 25% replay. Cooldown combines small,
high-quality sets (chat-formatted cooldown data, monthly Arabic Wikipedia, and knowledge-infusion and
explanation-enriched sets; Section 4.2 describes their decontamination and its limits) with mid-training
```

## 3.1 decontamination, limits (pp.12-13)
```
Decontamination. The training sets we prepared for continual pretraining, cooldown, and SFT (Table 3)
are screened against our evaluation benchmarks before use with AllenAI’s decon n-gram overlap detector1
(Rust, with pyo3 bindings) wrapped in a DataTrove (Penedo et al., 2024) pipeline,2 after folding Arabic
orthographic variants (alef and ya forms, ta marbuta, tatweel, diacritics) on both the evaluation index
and the scanned text. Overlap is not the same as leakage: Quranic verses, hadith and shared instruction
boilerplate appear in thousands of documents and in the benchmarks alike, and the single largest such item
matched 11,485 separate documents. These are excluded on review before anything is removed. Table 3
shows information after this exclusion. All replay was screened: the replay used in SFT is drawn from the
same K2 Horizon mid-training data as the 50.4B continual-pretraining replay, so the continual-pretraining
scan covers both.
In the continual-pretraining scan, 111,089 lines matched: 15,689 matched at least one discriminative item
and were removed from the training copies, and the other 95,400 matched only non-discriminative text;
the rewrite touched 3,447 files, whose cleaned versions were verified byte for byte against the originals.
The overlap concentrates in poetry benchmarks with none in the diacritization or search-context sets. The
cooldown scan ran against 554 of the 567 delivered evaluation files, covering 210,269 questions indexed
as 287,416 entries after deduplication; of 1,955 flagged lines, 3 were kept after individual review as false
positives and 1,952 were removed, and about half of the Arabic Wikipedia hits were canonical religious
text quoted by both the article and the evaluation item. The SFT scan removed 3,272 samples across 33
datasets, with the poetry set highest at 1.45%, and every scanned file is written through byte-identical to
its source apart from the removed records. A re-scan of the cleaned cooldown release flags only the three
kept false positives and nothing else. Screening is lexical throughout and operates on whole records, so a
flagged record is dropped in full.
Token accounting. After processing we count every document with the training tokenizer, without
```

## 3.2 Limitations and Exclusions (p.13)
```
3.2 Limitations and Exclusions
Screening is lexical. The contamination scan matches token n-grams after orthographic folding, so translated
or paraphrased benchmark items are not detected, and MinHash over character shingles measures lexical
overlap only, so paraphrased duplicates survive deduplication.
```

## 4.1 Main-stage data: sources and models used to generate synthetic data (pp.14-16)
```
4.1 Main-Stage Data
The main stage samples 201.5B tokens, with each Arabic source weighted for one pass over its retained
tokens. On the Arabic side the mixture has 32 entries: the 19 subsets of the translated reasoning data, each
weighted separately, and the 13 other sources of Table 4, counting the targeted and instruction rows as their
individual sets. A quarter is replay from K2 Horizon’s own mid-training data, and three quarters come
from the sources in Table 4. Natural Arabic web text and literature make up 19% of the run. Translated
and synthetic sources make up 44%, of which about 6 points is the English side of the parallel dialect
data. The remaining 12% is small targeted sets, Arabic instruction data, English domain data, and further
Arabic texts. Every source went through the pipeline of Section 3.1 with its own filter settings; Table 5
records the settings and removal rates for each one.
Natural Arabic. ArabicTxT360 is our Arabic extraction of 83 web crawl snapshots, refiltered with the
Arabic rule set; older crawls were markedly noisier, with 25–44% of documents removed from the 2014–2017
snapshots against about 14% from 2023–2024. The literature collections include, among others, classical
texts, poetry, news, and religious scholarship with the longest record being 16.3M tokens long.
Translated and synthetic Arabic. This is the largest group, because natural Arabic runs out long before
the token budget. We translated 19 subsets of K2 Horizon’s pretraining data (reasoning, planning, question
answering, instruction following, and code reasoning). A pilot showed that long mathematical derivations
were often truncated in translation, so we cut mathematics from 31% to about 14% of the tokens planned
for translation. A human rating covered only 50 short samples, which averaged 4.95 out of 5.
The Arabizi corpus transliterates 30B tokens of English TxT360 into Gulf, Egyptian, Levantine, and Darija
Arabizi (about 27.5B Arabizi tokens before our filtering and deduplication, 25.1B after). For the parallel
dialect corpus, GLM-5 translates English conversations into the target dialect and script, and Jais 2 writes
a second version. An LLM judge scores both versions from 1 to 4 on dialect accuracy, meaning, and
naturalness, and an automated check flags unwanted switches into other languages. To build fluency in
both scripts, a subset was also translated from the English source into Arabizi. The style rewrites turn web
passages into formal, humorous, and simplified versions with Qwen to add register variety; the humorous
style is about 88% dialectal. Finally, QA augmentation appends generated question-answer pairs to web
and Hindawi passages. We did not deduplicate these against the original web text, because the passage is
meant to appear again in question-answer form; only 17.5% of the web QA tokens are new.
14
Group Source Origin Tokens Share
Natural Arabic ArabicTxT360 83 web crawl snapshots,
28.4B 14.1%
2013–2024
Literature collections Classical texts, poetry, news 9.65B 4.8%
Translated and synthetic Translated reasoning Parallel dialects 19 subsets of K2 Horizon’s
pretraining data
English conversations paired with
dialect translations from GLM-5
and Jais 2, judge-filtered for
dialect fidelity, meaning and
naturalness
Arabizi English TxT360 rendered as
Arabizi in four dialect groups:
Gulf, Egyptian, Levantine and
Darija
Style rewrites ArabicTxT360 passages rewritten
in three styles
QA augmentation Web and Hindawi passages with
generated questions and answers
30.9B 15.3%
26.9B 13.4%
25.1B 12.5%‡
4.43B 2.2%
1.42B 0.7%
Targeted Instruction data Diacritization, search, exams Sadeed/Tashkeela diacritization,
and Arabic exam Q&A
Arabic chat data TxT360 instruction data at three
reasoning-effort levels (Arabic);
Jais 2 SFT with regenerated
answers
0.58B 0.3%
5.5B 2.7%
English domain Investment and economy Finance and economics documents 6.33B 3.1%
Other Further Arabic documents Partner-supplied Arabic books,
11.9B 5.9%
cross-document deduplicated and
de-watermarked
Replay Mid-training replay K2 Horizon mid-training data 50.4B 25.0%
Table 4: Main-stage sources. Tokens are the inventory after filtering and deduplication, counted with the training
tokenizer; share is the source’s fraction of the 201.5B tokens sampled in the main stage. ‡A further∼3.5 points of
Arabizi is inside the parallel-dialect data.
Targeted sets. Three small sets target specific skills. The diacritization set is instruction-formatted over
fully vocalized classical and modern text, with loss on the answer only. The search-trajectory set records
```

## 5.1 SFT data: multi-turn generators (p.21-22)
```
Targeted conversations. We adopt the four dependency types of Deshpande et al. (2025): instruction
retention, user-information recall, versioned editing, and self-coherence. An anchor turn introduces an
instruction, fact, document version, or commitment, and the final user turn depends on it without restating
it (Appendix B.1). A structural audit of the visible conversation checks that the anchor is present, that at
least one exchange separates it from the final turn, that the final turn does not restate it, and that the
anchor is unambiguous. Under strict qualification, the audit also confirms that changing the anchor would
change the correct answer. Conversations that narrowly fail the audit are repaired and audited again rather
than discarded. Legal and scientific conversations can additionally be grounded in pinned source passages.
```

## 5.1.2 Country knowledge data: dialect coverage and generator (p.22)
```
5.1.2 Country Knowledge Data
We built a question-answer dataset on the 22 member states of the Arab League, covering politics, history,
geography, the economy, religion, food, sports, famous people, landmarks, folklore, customs, and local
expressions. Approximately 70% of the examples are in the dialect of the country concerned and 30%
in MSA; Somalia, Djibouti, and Comoros are covered in MSA only. Every example includes a reasoning
trace. Of the 1.38M examples, the final SFT run uses 1.37M (0.64B tokens, 1.6% of the SFT tokens), and
220,511 of the set went through evidence-based verification.
Generation. Questions come from a taxonomy of 29 categories and their subtopics; subtopics name
areas of knowledge rather than entities, so the generator chooses what to ask about. For each country,
register, and category–subtopic pair, gemma-4-31B-it writes first-person questions with an asker profile
(e.g., resident, student, traveler, researcher), a target difficulty, and one of six forms: factual question,
explanation, comparison, scenario, opinion, or list. Questions are deduplicated within each country and
register by exact match and MinHash. The same model then answers each question with reasoning enabled,
```

## 5.1.3 Translation and transliteration data: dialects and generator (pp.23-24)
```
5.1.3 Translation and Transliteration Data
We built a synthetic corpus for two capabilities: translation between English and Arabic (MSA, classical
and literary Arabic, and seven regional dialects), and transliteration between Arabic script and Arabizi
(Franco), the Latin-script convention of informal written Arabic. gemma-4-31B-it generated all 812,160
examples; deterministic checks and a blinded LLM judge keep 741,262 (91.3%) for SFT.
Sources. The translation data has two parts. The first reuses the source passages and translation
directions of 465,692 samples from the Jais 2 translation data (Anwar et al., 2026), covering subtitles
and dialogue, short sentence pairs, EU and legal text, and classical and literary Arabic, re-rendered into
standardized prompts with newly generated answers. The second has 140,219 dialectal samples: Palestinian,
North Levantine, and Yemeni samples are built from the public corpora of Table 10, and Egyptian,
Moroccan, Tunisian, and Iraqi samples from internal data. For Iraqi, internal English seed sentences
are first rendered into synthetic Iraqi Arabic and then translated back into English. The transliteration
data (206,249 samples) covers both directions between Arabic and Arabizi across the same seven dialects,
seeded from internal Egyptian, Moroccan, and MSA data and from the normalized Arabic passages of the
translation data.
23
Direction Source corpus License
Palestinian →English Curras (El Haff et al., 2022;
Jarrar et al., 2017, 2014)
North Levantine →English Nabra (Nayouf et al., 2023)
and Baladi (El Haff et al.,
2022)
```

## 5.1.7 File manipulation in Arabic: MiniMax-M3 trajectories (p.27)
```
5.1.7 File Manipulation in Arabic
This set teaches the model to work on Arabic office files: to read an Arabic document, carry out a
professional task based on it, and deliver the result as a native file with correct Arabic text and right-to-left
layout. It contains 8.9K multi-turn agent trajectories (0.72B tokens), generated with MiniMax-M3 in the
OpenCode agent harness (Table 14); the statistics below describe this release. The final SFT run uses an
earlier build of 2.2K trajectories (0.16B tokens) made with the same pipeline.
Generation. Each example starts from one Arabic source file. MiniMax-M3 reads every candidate file
in full and keeps only those it grades excellent or good. For each kept file, it writes MSA tasks of three
types: creation, where the file is a reference for producing a new spreadsheet, document, or presentation;
extraction, where its content is turned into a derived product such as a memo, summary, ranking, or table;
and editing, where the file itself is revised or converted. Requests follow the style of GDPval (Patwardhan
et al., 2026), with a professional role, a business situation, concrete constraints, and a named deliverable,
and each task comes with an Arabic grading rubric written by the same model.
Trajectories. A MiniMax-M3 agent solves each task in OpenCode with shell, Python, file, and web-search
tools, while a second instance plays the user. After the agent’s first answer, the simulated user reviews
the work against the rubric, which the agent never sees, and asks for corrections for up to two rounds;
7.9K trajectories contain three user turns. In 1.6K trajectories, a document skill (a reference guide for
producing the requested file format) is installed in the agent’s workspace. Trajectories have a median of
38 assistant turns and 40 tool calls and keep the agent’s reasoning, tool calls, and tool results; 20.6% of
completion tokens are reasoning trace.
```

## 5.1.8 Safety (pp.27-28)
```
5.1.8 Safety
Safety data is a small, targeted part of SFT: five sets totaling approximately 0.22% of the tokens sampled
in the final SFT run, roughly 92M tokens. Rather than add a large generic refusal corpus, we built most of
it around failures we observed in earlier Jais models and around content that is sensitive in our region:
religion, national leadership, and the model’s own identity (Table 15).
General safety. We translated an openly released safety SFT set (Nemotron Safety v2) into Arabic
with gemma-4-31B-it, keeping two thirds Arabic and one third English, and removed 3.4% of rows that
failed translation checks. Native Arabic speakers also wrote a set of harmful prompts in MSA, to cover
requests that do not arise from translation; we generated safe responses for these and quarantined 27 of
approximately 5,800 that reviewers could not agree on.
27
Set Content Languages Rows Share
General safety Jais 2 safety public safety SFT data translated into
Arabic, plus MSA harmful prompts
written by native speakers
general and regional safety sets
inherited from Jais 2
Religious and regional safety variants of prompts the model had
failed, with benign controls
Self-identity questions about the model’s name,
maker, and nature
National leadership factual questions about UAE leadership Ar, En Ar, En 47.5K 0.07%
Ar 115.8K 0.10%
Ar, En 15.6K 0.03%
26 languages, Arabizi 79.3K 0.03%
0.6K <0.01%
Table 15: Safety data in SFT. Rows are examples in the final SFT run; share is the fraction of tokens sampled in
that run.
Religious and regional safety. This set starts from 1,761 prompts on Islamic and UAE-related topics
that an earlier Jais model answered unsafely or inaccurately. For each prompt we generated twelve variants:
adversarial rephrasings that should still be refused, and benign questions on the same topic that should be
answered, so that the model learns to distinguish the two rather than refuse the topic outright. A response
entered training only when two independent judge models from different families both approved it. A first
review with a single judge had approved only 38.9% of responses and flagged over 10,000 factual errors and
approximately 1,400 unsafe compliances, which is why we moved to agreement between two judges. This
set draws no prompts from HarmBench, XSTest, or AraSafe, which we use for evaluation.
Self-identity. Jais 3 is trained from a base model with its own name and maker, and part of its training
data was written by other assistants. We therefore trained on questions about the model’s identity in
26 languages, and removed identity leaks from the K2 Horizon mid-training replay set (Section 4.1). An
off-the-shelf identity filter missed 41% of the leaks a judge confirmed there, because most of them sit in
reasoning traces it does not read.
Limitations. Our system-prompt ablation covers safety behavior only: we compared the deployed prompt
against no system prompt on various red-team safety sets, and did not measure the prompt’s effect on
capability benchmarks. Safety scores are also sensitive to decoding: most prompts score the same way
in every run at temperature 1.0, but a minority split across runs, so single-run numbers should be read
with that variance in mind. Safety evaluation results, including over-refusal on XSTest, are reported in
Section 6.5.
```

## 6.1.1 Arabic benchmark auditing (pp.50-51)
```
6.1.1 Arabic Benchmark Auditing
Errors and ambiguities are well documented in widely used evaluation benchmarks. Northcutt et al. (2021)
estimate an average label-error rate of at least 3.3% across ten standard test sets, while Gema et al. (2025)
estimate that 6.49% of MMLU questions contain errors and show that accounting for them can affect model
rankings in the most impacted subjects. More broadly, benchmark auditing and revision after release
have become increasingly common. Terminal-Bench 2.1 revises 28 of the 89 tasks from version 2.0 (The
Terminal-Bench Team, 2026); SWE-bench Verified was constructed through additional screening of the
original test set by professional developers (OpenAI, 2024); and Humanity’s Last Exam has undergone
further verification by domain experts (Zhai et al., 2026). In Arabic, ArabicMMLU (Koto et al., 2024) notes
that incorrect answer keys limit the practically achievable score to approximately 96%. QIMMA (AlQadi
et al., 2026) audited fourteen established benchmarks using LLM-based screening followed by review from
native speakers, filtering up to 3.1% of the items in individual benchmarks, with incorrect or missing gold
answers among the most consequential issues.
Motivated by these observations, we audited the Arabic benchmarks used in this report with a multi-stage
pipeline. Reviewing every item with several frontier models is costly, so the pipeline first selects candidates.
For each benchmark, we take the strongest baseline models and collect every item that at least one of them
answers incorrectly. A failure by a strong model may come from the model, from the item, or from both,
7https://github.com/ifm-ai/gen-eval-arabic
50
so it is a reason to review the item rather than evidence of a defect. Taking the union over several models
makes the selection less dependent on any one of them: an item that one model answers correctly by
chance is still reviewed if another model fails it. Defects in items that all selected models answer correctly,
however, are not detected.
Each candidate is then reviewed independently by three frontier models, Gemini 3.8 Flash, Claude Opus
5, and GPT-5.6 Sol, which see the question, options, and gold answer exactly as they are used in evaluation.
The judges follow a shared rubric with domain-specific guidance and decide whether the item allows reliable
answering and scoring. Each judge locates the issue in the question, the options, or the gold answer,
assigns a subcategory, such as an incorrect gold answer, multiple correct options, or an ambiguous question,
and gives a reason and a suggested fix. It also rates the issue as solvable, when a clearly correct answer
remains consistent with the gold answer, or significant, when the issue prevents reliable answering or
scoring. An item is removed only when all three judges find a significant issue, although they need not
agree on its category or fix. Because correctness in Arabic can depend on dialectal usage, regional and
cultural knowledge, and linguistic conventions, Arabic-speaking annotators also reviewed a random sample
of the removed items.
Issue source (%)
Benchmark Items Removed Rate (%) Question Options Gold
MedAraBench 4,927 896 18.2 21 27 52
```

## 6.1.4 Dialect understanding and generation results (pp.60-61)
```
largest improvement observed on QIAS-Inheritance. At the frontier scale, Jais-3-375B-A23B is competitive
with Claude Sonnet 5 across several Arabic-focused benchmarks and outperforms Gemini 3.8 Flash
and GPT-5.6 Sol on IslamicEval, although a gap remains to the strongest frontier models. This gap is
relatively small on Arabic Linguistics and substantially larger on FannOrFlop_MCQ.
Dialect understanding and generation. Table 31 reports the results. Jais-3-0.9B leads all seven
benchmarks at the 1B scale, by 4–37 points. Jais-3-3.7B leads six at the 4B scale, by 5–24 points; the
exception is Darija transliteration, where gemma-4-E2B-it is ahead. Jais-3-7B leads the five understanding
and translation benchmarks at the 7B scale, but trails Jais-2-8B-Chat on Egyptian and gemma-4-12B-it
on Darija transliteration. At the 32B scale, gemma-4-31B-it leads six benchmarks, while Jais-3-32B wins
60
QADI and stays within 1.3 points on the rest. Jais-3-375B-A23B leads its class on five benchmarks and is
within 0.6 points of Qwen3.8-Flash-Next on the other two.
QADI is a consistent strength: Jais 3 achieves the best dialect identification score at every open-weight
scale, and Jais-3-32B and Jais-3-375B-A23B both surpass GPT-5.6 Sol and Claude Sonnet 5. Among
Arabic-centric baselines, Jais-3-7B beats ALLaM-7B-Instruct-preview and Fanar-1-9B-Instruct on all
seven benchmarks and Jais-2-8B-Chat on six, with a large gain of 29 points on Dialectal-Arabic-MMLU.
Transliteration is a relative weakness at smaller scales, with Darija scores plateauing around 79 from 0.9B
```

## 6.2.3 Agentic results overview (p.62-63)
```
6.2.3 Results
Table 35 reports the results. Each model has ten scores, because BrowseComp-Plus and BrowseComp apply
to different scales. We compare each Jais 3 model with the open baselines of its scale. SWE-bench Verified
and APEX-Agents use one run per task, and one task is worth 0.79 points on MCPMark and 0.61 points
on GAIA-v2-LILT (AR). We therefore treat differences of less than one point as ties. WildClawBench
has only 29 tasks, and one task can change its score by up to 3.4 points. Differences of a few points on
WildClawBench are therefore not reliable.
Overview. The lead of Jais 3 is largest at the small scales. At 4B and 7B, Jais 3 is ahead of every
open baseline on all ten benchmarks. Its largest margins are on GDPval and the Arabic File-Processing
Benchmark (38.6 to 44.6 points), because the small baselines seldom complete a file task: none of them scores
above 19.1% on GDPval or above 0.9% on the Arabic benchmark. At 32B and above, the Qwen3.8 models
lead most benchmarks. Jais 3 is ahead of them on MCPMark at all three sizes and on BrowseComp-Plus
at 32B and 36B. Its largest and most consistent gaps are on Terminal-Bench 2.1, τ3-Bench Banking, and
WildClawBench, where the Qwen3.8 models lead by 8.6 to 25.7 points at every size from 32B up. Each
frontier model is ahead of Jais-3-375B-A23B on at least eight of the ten benchmarks. Earlier Arabic-centric
models fail almost every agentic task: Jais-2-8B-Chat, Jais-2-70B-Chat, ALLaM-7B-Instruct-preview,
and Fanar-1-9B-Instruct score below 1% on every benchmark, and the best score of Fanar-2-27B-
Instruct is 12.1%, on GAIA-v2-LILT (AR) and MCPMark.
Arabic benchmarks. GDPval and the Arabic File-Processing Benchmark use the same harness and
```

## 6.2.3 Agentic limitation (p.67)
```
Limitations. Only two of the eleven benchmarks are in Arabic, because few agentic benchmarks exist in
Arabic and most domains have none. Coding, tool use, and deep search are therefore tested only in English.
Jais 3 is built for Arabic, so these results probably do not show its full Arabic agentic capability. Arabic
versions of these benchmarks, made by translation or by adaptation of their tasks and environments, are
left for future work, by us or by the community.
```

## 6.5 Safety Evaluation (pp.73-75), table 40 as extracted
```
6.5 Safety Evaluation
Arabic safety. We evaluate Arabic safety from two complementary perspectives. The first examines how
models refuse harmful requests, while the second examines how they handle sensitive topics specific to the
Arab region. For harmful-request refusal, we use the human-written subset of AraSafe (Mubarak et al.,
2025b), a large-scale safety benchmark written natively in Arabic. We select the 1,254 prompts labeled as
harmful and exclude safe prompts, since our goal is to assess whether models comply with harmful requests.
The prompts are written by native speakers rather than translated, and cover Modern Standard Arabic and
several dialects. They span eight harm categories: illegal activities, violence or harm, privacy violations,
other harmful content, terrorism or extremism, hate speech, explicit content, and misinformation.
Arabic Regional Safety. Unlike general safety benchmarks that focus on clearly harmful requests such
as violence, weapons, or illegal activity, Arabic Regional Safety evaluates topics that are particularly
sensitive in the Arab world. The benchmark contains two types of questions. Controversial questions cover
governance, political repression, human rights and freedom of expression, political dynamics, economic
policies, and contested historical events. These prompts often concern claims about governments, political
leaders, or non-state actors, where safety judgments may differ depending on the political perspective
adopted. Non-controversial questions also involve regionally sensitive topics but do not require taking a
political position and are evaluated using general safety criteria.
Following Ashraf et al. (2025), we evaluate controversial questions from both government and opposition
perspectives. Responses that refuse to take a position or provide a balanced treatment of the issue are
considered safe under both perspectives. Responses that take a position are evaluated separately using
perspective-specific rubric questions, allowing the same response to receive different safety judgments under
73
the government and opposition views. We report safety rates separately for the government perspective,
opposition perspective, and non-controversial questions.
English safety. We evaluate English safety from two complementary perspectives. The first measures
whether models refuse harmful requests, while the second examines whether those refusals are appropriately
calibrated on benign prompts that may appear harmful at first glance.
For harmful-request refusal, we use HarmBench, an automated red-teaming benchmark containing 400
harmful behaviors (Mazeika et al., 2024). It comprises three subsets: standard (200 directly harmful
requests), contextual (100 requests embedded in accompanying passages), and copyright (100 requests for
verbatim reproduction of copyrighted material). We evaluate the standard and contextual subsets using the
refusal rate, defined as the percentage of harmful requests the model does not meaningfully fulfill (100−
attack success rate; higher is safer), as reported in Table 40. Responses are scored by gemma-4-26B-A4B-it
using the HarmBench classification criteria, achieving 98% agreement with the official classifier (Cohen’s
κ = 0.93). We exclude the copyright subset because its verbatim-matching evaluation requires reference
texts unavailable in our configuration.
For over-refusal, we use XSTest, a benchmark of 250 safe and 200 unsafe prompts designed to test whether
models distinguish benign from harmful requests (Röttger et al., 2024). Safe and unsafe prompts often
share similar wording; for example, “How do I kill a Python process?” is a safe request despite containing
potentially harmful keywords. We report accuracy over all 450 prompts (higher is better): a safe prompt
is correct only if the model fully complies, and an unsafe prompt is correct if it fully or partially refuses.
Responses are classified into the three official XSTest categories using gemma-4-26B-A4B-it, which achieves
Cohen’s κ of 0.79–0.86 against the original GPT-4 judge.
Results. On AraSafe, Jais 3 shows strong harmful-request refusal from the smallest model upward.
Jais-3-0.9B already refuses more harmful prompts than both Jais 2 models, and every reported Jais 3
model refuses more than 92% of them, 3 to 5 percentage points more than the corresponding Jais 2
baselines. At the 1B and 32B scales, Jais 3 performs comparably to the strongest models in its class,
Qwen3.5-2B and Qwen3.8-27B, respectively, while at 7B, Fanar-1-9B-Instruct and Qwen3.5-9B refuse
about 3 points more. The lowest refusal rates are observed for granite-4.0-h-3b-ar and the Falcon-H1
models below 4B.
On Arabic Regional Safety, Jais 3 achieves consistently high safety rates, with Jais-3-0.9B, Jais-3-
7B, Jais-3-32B, Jais-3-MoVA-36B-A4B, and Jais-3-375B-A23B exceeding 98% across all three settings.
Among the other models, Qwen3.5-397B-A17B, gemma-4-E2B-it, gemma-4-12B-it, and gemma-4-31B-it
come closest, with every setting above 96%. Compared with other Arabic-centric models, Jais-3-7B
outperforms ALLaM-7B-Instruct-preview, Fanar-1-9B-Instruct, and Jais-2-8B-Chat in every setting,
while Jais-3-32B outperforms Fanar-2-27B-Instruct and Jais-2-70B-Chat. On controversial questions,
every model has lower safety rates under the government perspective than under the opposition perspective,
with the largest gaps, about 20 percentage points, for Nemotron-3-Ultra-550B-A55B-BF16 and Fanar-2-
27B-Instruct.
On HarmBench, Jais 3 shows its largest improvement over Jais 2, with Jais-2-8B-Chat and Jais-
2-70B-Chat refusing far fewer harmful requests. Jais-3-MoVA-36B-A4B has the highest harmful-request
refusal rate at the 32B scale, followed by Jais-3-32B, while Jais-3-7B shares the highest score at the 7B
scale with Qwen3.5-9B. Jais-3-0.9B and Jais-3-375B-A23B also perform comparably to the strongest
models in their respective groups, Qwen3.5-2B and Nemotron-3-Ultra-550B-A55B-BF16. Several models
have considerably lower refusal rates on HarmBench than on AraSafe, particularly Fanar-2-27B-Instruct
and Falcon-H1-34B-Instruct, which refuse only slightly more than half of the harmful requests.
74
On XSTest, Jais 3 maintains high accuracy alongside its strong harmful-request refusal rates. Jais-3-7B
has the highest accuracy at the 7B scale, leading its group on both HarmBench and XSTest, while the other
reported Jais 3 models remain within 2 percentage points of the best model in their respective groups.
Differences between models are smaller than on the other safety benchmarks, with accuracy ranging from
approximately 86% to 95%. Nemotron-3-Ultra-550B-A55B-BF16 and Qwen3.8-27B score highest overall.
Arabic English
Benchmark AraSafe
Arabic Regional
Safety
Harm
Bench XSTest
Refusal General Gov. Opp. Refusal Acc.
1B Scale
Falcon-H1-1.5B-Deep-Instruct 79.98 88.27 83.95 86.22 69.75 88.67
Hala-1.2B Qwen3.5-2B tiny-aya-global 85.57 71.48 46.40 53.20 89.50 87.56
93.62 92.78 94.81 95.61 90.75 87.11
84.69 83.03 73.64 83.62 76.25 89.11
Jais-3-0.9B 92.42 100.00 98.14 98.27 89.75 87.78
4B Scale
Falcon-H1-3B-Instruct gemma-4-E2B-it granite-4.0-h-3b-ar Qwen3.5-4B 82.30 94.58 89.88 92.94 65.00 89.56
93.86 98.56 96.14 97.87 76.50 90.22
68.66 87.73 84.55 86.88 63.75 86.22
94.74 98.56 94.54 97.60 93.00 90.67
Jais-3-3.7B 92.11 99.28 96.94 98.54 96.00 91.78
7B Scale
ALLaM-7B-Instruct-preview 94.10 76.17 61.12 63.65 92.00 89.11
Falcon-H1-7B-Instruct 87.80 97.47 93.87 95.74 70.75 90.00
Fanar-1-9B-Instruct 95.77 96.75 94.54 97.74 89.50 90.67
gemma-4-12B-it 91.63 100.00 97.60 99.47 84.50 92.22
gemma-4-E4B-it 93.62 98.92 93.21 97.34 79.75 92.00
Jais-2-8B-Chat 89.00 95.31 85.89 94.27 81.25 91.11
Qwen3.5-9B 95.37 99.10 93.21 95.87 96.00 91.78
Jais-3-7B 92.42 99.64 98.67 99.47 96.00 92.89
32B Scale
Falcon-H1-34B-Instruct Fanar-2-27B-Instruct gemma-4-31B-it Jais-2-70B-Chat Muse-Glimmer-30B Qwen3.8-27B 88.20 98.56 93.34 97.74 55.50 89.11
94.50 89.89 75.10 94.41 59.25 89.56
92.34 100.00 97.34 99.33 86.00 92.89
88.12 93.14 83.36 88.68 71.00 92.00
94.58 98.56 92.14 98.93 95.75 92.22
95.06 98.92 95.21 99.07 94.33 94.44
Jais-3-32B 93.06 100.00 99.07 99.47 97.50 92.67
Jais-3-MoVA-36B-A4B 93.30 100.00 99.33 100.00 98.00 93.11
375B Scale
MiniMax-M3 Qwen3.5-397B-A17B Qwen3.8-Flash-Next 93.22 98.19 92.94 98.54 95.25 92.89
Nemotron-3-Ultra-550B-A55B-BF16 94.18 90.25 76.56 97.74 99.75 94.67
95.77 100.00 96.67 99.87 98.25 92.67
94.58 98.56 95.07 98.67 97.75 93.33
Jais-3-375B-A23B 93.54 100.00 98.74 99.60 98.00 93.56
Table 40: Safety results on Arabic and English benchmarks (%). All results use thinking mode (high effort) where
available. Within each model size, the best score in each column is shown in bold.
75
Artifact Contents Where License
Model weights Final weights of the six models, with
the tokenizer and chat template
Stage checkpoints Checkpoints after continual
pretraining (main stage and
cooldown), SFT, FTPO, and RLVR
for each size
```

## 7 Release Notes: Table 41, 7.1, 7.2 (p.76)
```
Artifact Contents Where License
Model weights Final weights of the six models, with
the tokenizer and chat template
Stage checkpoints Checkpoints after continual
pretraining (main stage and
cooldown), SFT, FTPO, and RLVR
for each size
Training code xLLM (pretraining and SFT) and
RL360 (RLVR)
hf.co/collections/IFM/jais-3 Apache 2.0
Same collection Apache 2.0
Training data
sample
Training logs and
configurations
Audited
benchmarks
github.com/ifm-ai/xllm,
Apache 2.0
github.com/ifm-ai/RL360
A sample of the training data hf.co/datasets/IFM/Jais-3-Data ODC-BY,
CC BY 4.0
Run configurations and training curves W&B project mbzuai-llm/Jais-3 –
Cleaned Arabic benchmarks and every
discarded item with the judges’
reasons
Evaluation code Evaluation suite, task configurations,
and scoring
hf.co/collections/IFM/arabic-b
enchmark-auditing, hf.co/datase
ts/IFM/discarded_samples
github.com/ifm-ai/gen-eval-ara
bic
Apache 2.0
–
Speech front end Jais-ASR and the JaisVoice harness github.com/ifm-ai/JaisVoice Apache 2.0
Table 41: Released artifacts of Jais 3.
7 Release Notes
7.1 Open-Source Statement and Commitment
We release Jais 3 openly so that others can use, study, and adapt it. Table 41 lists the released artifacts.
Models and training code are released under the Apache 2.0 license; the training-data sample keeps the
terms of its sources (ODC-BY and CC BY 4.0). The stage checkpoints and recipes let others continue
from any point of the pipeline, or adapt K2 Horizon to another language in the same way.
7.2 Intended Use and Limitations
Intended use: The model is designed for Arabic and English assistant and agentic applications, including
reasoning and tool-use tasks, as well as for research and experimentation.
Out of scope: The model should not be used in ways that violate applicable laws or regulations. The
following uses are also considered out of scope:
• Harmful or malicious use: Generating hateful, extremist, discriminatory, or deliberately misleading
content, or using the model to support illegal or harmful activities.
• Sensitive information: Using the model to generate, expose, or infer personal, confidential, or
otherwise sensitive information about individuals or organizations.
• Unsupported languages: Applications that depend on reliable performance in languages other
than Arabic or English.
• High-stakes decisions: Relying on the model to make medical, legal, financial, or safety-critical
decisions without appropriate human oversight.
Limitations: The model can produce inaccurate or fabricated content and may reflect biases present in its
training data. Evaluate it for your use case and implement appropriate safeguards before deployment.
76
```

## C.3.3 Dialect benchmark descriptions (p.97)
```
C.3.3 Dialect Understanding and Generation
Dialectal understanding. QADI (Abdelali et al., 2021) is a corpus of 540,590 tweets from 18 Arab
countries that covers Modern Standard Arabic and ten regional varieties; a 3,797-instance subset is used for
dialect identification. Dialectal-Arabic-MMLU (Altakrori et al., 2026) contains 3,135 questions adapted into
each of five dialects (Egyptian, Saudi, Moroccan, Syrian, and Emirati), for 15,675 question–answer pairs.
Diacritized ArabicMMLU (Inoue et al., 2026) is a fully diacritized version of the 14,455 ArabicMMLU
questions; because the content of the two versions is identical, comparing them measures robustness to
diacritics.
Dialectal generation. FLORES+ (NLLB Team et al., 2024; Burchell et al., 2024) provides 1,012 aligned
sentences per variety in English, Modern Standard Arabic, and eight Arabic dialects, and is used for
translation. DarijaBench-Transliteration (Shang et al., 2025b) and EgyptianBench-Transliteration (Shang
et al., 2025a) test transliteration between Arabic script and Arabizi, a Latin-script romanization, for
```

## 4.3 Training recipe: hardware (p.18-19)
```
Infrastructure. We trained the 0.9B, 32B, 36B MoVA, and 375B models, in both the main stage and
the cooldown, with our in-house framework (xLLM) in bfloat16 with fully sharded data parallelism. The
0.9B ran on NVIDIA H100 80GB GPUs without tensor parallelism; the 32B, 36B MoVA, and 375B ran on
NVIDIA H200 141GB GPUs, with 2-way tensor parallelism for the 36B MoVA and 8-way for the 375B.
The 3.7B and 7B were trained on Cerebras CS-2 systems in cbfloat16.
To fit the batch at 8K context, we recompute the first and third MLP projections and the attention value
projection in the backward pass instead of keeping their activations. The training data is tokenized, packed
into 8,192-token sequences, and shuffled across the full dataset before the run starts, so the data loader
only reads pre-built shards. Padding accounts for less than 0.02% of tokens, and about 5% of sequences
end in a document that was cut at the sequence boundary. Checkpoints hold the model weights and the
optimizer state. They were written every 250 updates in the main stage and every 100 in the cooldown,
and we kept the last two.
19
Runs. The main stage took about 1.8K H100 GPU hours for the 0.9B (233.6B tokens), 10.9K H200
GPU hours for the 36B MoVA, and 76.9K H200 GPU hours for the 375B; on Cerebras, it took 3.3K and
4.7K CS-2 system hours for the 3.7B and 7B. The 32B main-stage run did not log its runtime.
The 0.9B main stage ran its 11,141 updates in one uninterrupted job, and the cooldown took another 30
GPU hours. Training loss dropped quickly at first, from 2.81 at the first update to an average of 1.74
```

## 5.1.1 Multi-turn data: generators and judges (p.22)
```
as a dialogue of 8–20 messages; the Responder sees only the visible conversation, never the blueprint.
Qwen3.6-27B (Qwen Team, 2026b) and gemma-4-31B-it (Gemma Team, 2026) serve as both generators
and judges. All conversations are synthesized from scratch, without benchmark prompts as seeds, and pass
our decontamination pipeline (Section 3.1).
Targeted conversations. We adopt the four dependency types of Deshpande et al. (2025): instruction
```

## 5.1.4 Arabic instruction following: prompt and response generation (p.25)
```
Prompts. Qwen3.8-27B (Qwen Team, 2026c) writes chat-style requests in MSA or in Gulf, Egyptian,
or Levantine Arabic, across genres, domains, and response lengths. We append constraints as numbered
Arabic instructions, drawn from 70 constraint types in seven categories (Table 12). Approximately 7% of
prompts carry two constraints, either a light second one, such as a closing phrase, or a demanding pair
of exact counts; constraints that fix the output, such as copy-and-transform or morphology, are never
combined.
Filtering and responses. Each constraint type has a deterministic validator, using a curated lexicon of
gold forms for morphology. Filters remove prompts with formatting artifacts, prompts less than 55% Arabic,
near-duplicates, and prompts that overlap with evaluation data (a shared 8-word sequence, token Jaccard
similarity ≥0.5, or a normalized exact match). Because validators do not check that the request was
answered, Qwen3.8-27B also judges each prompt with a constraint-satisfying response, rejecting unnatural
prompts and responses that ignore the request, the most common failure. The released response is sampled
```
