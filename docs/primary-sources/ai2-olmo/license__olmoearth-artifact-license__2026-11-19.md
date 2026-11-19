# Ai2 OlmoEarth Artifact License, read 2026-11-19

- **doc_type:** license
- **source_url:** https://huggingface.co/allenai/OlmoEarth-v1_3-Base/raw/main/LICENSE.txt ; https://raw.githubusercontent.com/allenai/olmoearth_pretrain/main/LICENSE
- **retrieval_date:** 2026-11-19
- **exists:** yes
- **retrieved:** true

## What was read

LICENSE.txt in OlmoEarth-v1_3-Base (7,090 bytes, md5 d5993a55300b089c730e654551d9ac5b) is byte-identical to the
one in OlmoEarth-v1_2-Base. The one in OlmoEarth-v1_2-FT-LFMC-Base differs only by a trailing newline. The
GitHub repos allenai/olmoearth_pretrain and allenai/olmoearth_projects carry a LICENSE headed "OlmoEarth
Artifact License" as well. The HF API reports gated False and `license: other` for all of them.

Governing clauses (verbatim):

> Subject to your compliance with this Agreement, Ai2 grants you permission, free of charge, to use the machine learning artifacts, materials, and documentation provided by Ai2 under this Agreement as follows (collectively, "Artifacts"): Model weights, including architecture and parameters ("Model"); Associated dataset or collection of data in connection with the Model ("Dataset"); and/or Associated software to process and run the Dataset and Model, including code in source or binary form for training, inference, and evaluation ("Code").

> 2. Use Restrictions. You will not (and will not encourage, permit, or facilitate any others to) use any portion of the Artifacts or Derivatives for the following purposes:
> (a) Any military and defense-related applications and use cases, including without limitation, for weapons development, military operations, intelligence gathering, or human surveillance and policing activities.
> (b) Any extractive activities, operations and use cases involving the removal of raw materials from the earth, including without limitation, to plan or facilitate the extraction of oil, natural gas and minerals through activities such as drilling, mining, and deforestation.

> 3(c) If you distribute any Derivatives, you may add your own intellectual property notices and apply other licenses and terms of use, provided that you include and require the use restrictions in Section 2 in all downstream distribution unless Ai2 provides written approval otherwise.

> 4. Termination. This Agreement will automatically terminate with immediate effect and without notice to you in the following circumstances: (a) Your breach of the use restrictions in Section 2 and any other terms and conditions herein; or (b) If you file, maintain, or voluntarily participate in a lawsuit ... asserting that the Artifacts ... infringe any patent ...

Other points: section 1 allows use, reproduction, modification, distribution and derivatives (including synthetic
data and distillation); section 3(a) requires citing Ai2; 3(b) requires a link or copy of the licence on
distribution; section 5 excludes patents, trademarks and third-party Contents rights; section 7 lets a separate
written agreement with Ai2 supplement or override.

The cards also say "intended for use in accordance with Ai2's Responsible Use Guidelines".

## Released with OlmoEarth

- Weights: OlmoEarth v1, v1_1, v1_2 (Nano, Tiny, Small, Base), v1_3-Base (created 2026-09-04, ViT-Base 128M
  parameters plus Perceiver and linear student), fine-tuned heads such as v1_2-FT-LFMC-Base (2026-10-23). All
  under the OlmoEarth Artifact License.
- Code: github.com/allenai/olmoearth_pretrain under the OlmoEarth Artifact License.
- Data: huggingface.co/datasets/allenai/olmoearth_pretrain_dataset under ODbL (285,288 samples, built from
  Sentinel-1/2, Landsat, USDA CDL, ERA5, OpenStreetMap, SRTM, WorldCereal, WorldCover and WRI canopy height, each
  under its own source licence). Some derived datasets are separately licensed (olmoearth_lcc apache-2.0,
  olmoearth_projects_awf apache-2.0, olmoearth-paper-embeddings cc-by-4.0).
