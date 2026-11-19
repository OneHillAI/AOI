# Gemma 4: Public Summary of Training Content for General-Purpose AI models (EU AI Act Article 53(1)(d) template)

source_url: https://storage.googleapis.com/transparencyreport/report-downloads/pdf-report-nn_2026-7-31_2026-7-31_en_v1.pdf
retrieval_date: 2026-11-19
doc_type: docs
retrieved: true
note: 8-page PDF (214 KB) from Google's transparency report storage, found through a secondary blog (discuss.pytorch.kr, not relied on). Text extracted with macOS PDFKit and the checkbox states read from page images, because the text layer drops tick marks. A sibling PDF named in the same blog (pdf-report-ii_2026-7-2, said to be the Gemini 3 Pro summary) returned HTTP 404 and was not read.

Document facts: title "Public Summary of Training Content for General-Purpose AI models"; "Version of the Summary: v1"; "Last update: 31 July 2026"; provider "Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Ireland"; authorised representative field blank; versioned model name "The Gemma 4 family of models"; placement on the Union market "April 2026".

## 1.2 Model identification (verbatim)

```
Model dependencies: Gemma 4 is not a modification or a fine-tune of a prior model. Each subsequent model in the Gemma 4 family is based on Gemma 4 (see each model card for individual model details). The Gemma 4 family includes models such as: Gemma 4 E2B, Gemma 4 E4B, Gemma 4 12B, Gemma 4 26B A4B, Gemma 4 31B.
```

## 1.3 Training data size (ticked boxes read from the page images)

```
Text:  More than 10 trillion tokens
Image: More than 1 billion images
Audio: More than 1 million hours
Video: More than 1 million hours
Latest date of data acquisition/collection: The knowledge cut-off date for Gemma 4 is January 2025. We may periodically update models after this date.
Other relevant characteristics: The pre-training dataset was a large-scale, diverse collection of data encompassing a wide range of domains and modalities, which included publicly-available web-documents, code, images, audio (including speech and other audio types), and video. The post-training dataset included different types of instruction tuning data, reinforcement learning data, and human-preference data.
```

Reading note: the size bands are the summary's own, for the whole family. The model card and technical report give no token count.

## 2 Data sources (ticked boxes: Yes unless stated)

```
2.1 Publicly available datasets: Yes (Text, Image, Video, Audio ticked).
    "List of large publicly available datasets: Our publicly available datasets include data across various sectors such as educational, government, legal, and research sectors comprising a wide variety of media types and languages."  (no dataset is named)
2.2.1 Datasets commercially licensed by rightsholders: Yes (Text, Image, Video, Audio ticked).
2.2.2 Private datasets obtained from other third parties: Yes (Text, Image, Video, Audio ticked).
    "None of the private datasets subject to section 2.2.2 are publicly known."
    "Datasets cover subject areas including educational materials, scientific reasoning, and mathematics."
2.3 Crawlers used: Yes (Text, Image, Video, Audio ticked).
    "Google's common crawlers obey robots.txt rules when crawling automatically."  (the crawler list is a link to a general Google crawler page; no domain names are listed)
2.4 User data:
    "Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model?" Yes
    "Was data collected from user interactions with the provider's other services or products used to train the model?" Yes (Text, Image, Video, Audio ticked)
    "In accordance with Google's relevant terms of service, privacy policy, and service-specific policies, and pursuant to user consent where legally required, we use data collected from users of Google products and services - such as user chats with Gemini Apps - to train AI models."
2.5 Synthetic data: Yes (Text, Image, Audio ticked; Video not ticked)
    "We have relied on the externally available Gemini 3 family of models to generate synthetic data."
    "We may use fine-tuned versions of internal models and non-GPAI models to generate synthetic data for training."
2.6 Other sources: Yes
    "It includes datasets that Google acquires or generates in the course of its business operations, or directly from its workforce."
```

(The dash in the user-data sentence is an em dash in the PDF; written here as a hyphen.)

## 3 Data processing

```
3.1 "Are you a Signatory to the Code of Practice for general-purpose AI models that includes commitments to respect reservations of rights from the TDM exception or limitation?" Yes
"Data filtering and preprocessing included techniques such as deduplication, honoring robots.txt, safety filtering in-line with Google's commitment to advancing AI safely and responsibly, and quality filtering to mitigate risks and improve training data reliability. Specifically, our Google-Extended control lets web publishers manage whether content Google crawls from their sites may be used for training Gemini models that power Gemini Apps and Gemini Enterprise Agent Platform, for grounding in Gemini Apps, and for the Grounding with Google Search feature on Gemini Enterprise Agent Platform."
3.2 Removal of illegal content: "As described above, data filtering and preprocessing included techniques such as safety filtering ... This process may involve filtering irrelevant or harmful content ... including filtering content that is pornographic, violent, or violative of child sexual abuse material (CSAM) laws."
```

Reading notes by OneHill:
- This answers the question of whether Google published an Article 53(1)(d) training-content summary for Gemma 4: it did, as a v1 template filled in and dated 31 July 2026. It names no dataset and no domain, so it supports a "public summary exists" statement, not reproducibility.
- The summary says user-interaction data from Google products (it names Gemini Apps chats) was used in training. The Gemma 4 model card describes the pre-training data only as web documents, code, mathematics, images and audio, and does not mention user data. This is a provenance and privacy point a downstream deployer should know; the licence does not address it.
- The summary says synthetic data came from the Gemini 3 family (a proprietary Google model family). The Gemma 4 licence is Apache 2.0 and contains no restriction tied to that.
- Google's Google-Extended opt-out is described as governing Gemini training; the page does not say it governs Gemma training separately.
