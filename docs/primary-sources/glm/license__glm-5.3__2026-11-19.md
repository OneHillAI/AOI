doc_type: license
entity: glm-5.3 (NOT part of the tracked `glm` MIT cluster; recorded here as the licence boundary)
variant/applies-to: zai-org/GLM-5.3 and zai-org/GLM-5.3-BF16 only (HF metadata license: other, license_name: glm-5.3)
source_url: https://huggingface.co/zai-org/GLM-5.3/raw/main/LICENSE (byte-identical copy in https://huggingface.co/zai-org/GLM-5.3-BF16/raw/main/LICENSE, sha1 8bc49e9ec1d18dded7ba9d185748c6904958b839)
document_effective_date: 2026 (copyright year); repo created 2026-08-25, LICENSE in the initial commit (2026-08-27); repo last modified 2026-10-14 with no LICENSE change in the commit list
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

## Governing clauses (English half, VERBATIM; the file also carries a Chinese translation after a ----- separator)

GLM-5.3 License

Copyright (c) 2026 Z.AI

Permission is hereby granted, free of charge, to any person or entity (the "Licensee") obtaining a copy of this software — including the model weights, parameters, configuration files, inference and training code, and associated documentation (collectively, the "Software") — to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software; to run, deploy, fine-tune, or otherwise modify the Software and create derivative works from it; and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. The Licensee's use of the Software must comply with applicable laws and regulations.

2. "Model as a Service" means giving a third party access to language model inference or fine-tuning (e.g., via API) in a manner that allows such third party to exercise meaningful control over the inputs, parameters, or training data. This does not include (a) end-user products with model capabilities solely embedded within specific features or harnesses, or (b) mere relaying of requests to models hosted by others.
If the Licensee or any of its affiliates operates a Model as a Service business, and the aggregate revenue of the Licensee and its affiliates exceeds 10 billion US dollars (or the equivalent in other currencies) in total over any consecutive 12 months, the Licensee must pass Z.AI's security review before using the Software or its derivative works for any commercial purpose. The scope and method of the security review shall be reasonably determined by Z.AI.

3. THE SOFTWARE AND ANY OUTPUT AND RESULTS THEREFROM ARE PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL Z.AI OR ITS AFFILIATES OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For any questions regarding this license, please contact glmlicense@z.ai.

## Reading (OneHill)
- Clause 2 is a revenue-triggered security review, not a general MaaS ban. Both conditions must hold: (a) the Licensee or an affiliate operates a "Model as a Service" business, and (b) the aggregate revenue of the Licensee and its affiliates (all revenue, not MaaS revenue only) exceeds 10 billion US dollars over any consecutive 12 months. Then the Licensee "must pass Z.AI's security review before using the Software or its derivative works for any commercial purpose", with scope and method "reasonably determined by Z.AI".
- Correction to the 2026-09-21 sweep wording: the figure is 10 billion US dollars of aggregate group revenue (Licensee plus affiliates), not a "$10B MaaS revenue" threshold. Verified verbatim here.
- The grant otherwise reads as MIT-like (use, copy, modify, merge, publish, distribute, sublicense, sell; fine-tune; derivative works). Not an OSI-approved text.
- Only GLM-5.3 and GLM-5.3-BF16 carry this licence. GLM-5.3-Flash, GLM-5.2 and GLM-5.1 ship plain MIT LICENSE files (see license__glm-5-family-and-mit-cluster__2026-11-19.md). The September sweep note that GLM-5, 5.1, 5.2, 5.3 and 5.3-Flash all carry the custom licence was wrong.
- Contact: glmlicense@z.ai (recorded, not used).
