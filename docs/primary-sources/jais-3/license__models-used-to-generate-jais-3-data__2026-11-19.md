# license / licences of other models that the Jais 3 report says generated or judged training data

source_url: https://huggingface.co/MiniMaxAI/MiniMax-M3/raw/main/LICENSE ; https://huggingface.co/api/models/<repo> for MiniMaxAI/MiniMax-M3, zai-org/GLM-5, google/gemma-4-31B-it, Qwen/Qwen3.8-27B, Qwen/Qwen3.6-27B, inception42/Jais-2-8B-Chat ; https://huggingface.co/Qwen/Qwen3.8-27B/raw/main/LICENSE ; https://huggingface.co/zai-org/GLM-5/raw/main/README.md
retrieval_date: 2026-11-19
doc_type: license
exists: yes
retrieved: true for the MiniMax-M3 LICENSE text and the Qwen3.8-27B LICENSE header; metadata only for the others
tag: publisher

NOTE (OneHill): the technical report says these models produced or judged parts of the Jais 3 training data: MiniMax-M3 generated 2.2K agent trajectories in the final SFT run (and 8.9K in the released set); GLM-5 translated English conversations into dialects; gemma-4-31B-it generated translation, transliteration, country-knowledge, robustness and other SFT data and judged data; Qwen3.8-27B and Qwen3.6-27B generated and judged instruction-following, long-context, multi-turn and style-rewrite data; Jais 2 wrote a second dialect translation. The report does not discuss whether any of these licences restrict use of their outputs for training. This file records what each licence says on its face. It does not decide whether any clause reaches Jais 3.

## MiniMax-M3 (MiniMaxAI/MiniMax-M3): MINIMAX COMMUNITY LICENSE (raw LICENSE, 3,339 bytes, verbatim)
HF metadata: license other, license_name minimax-community, gated false.
```
MINIMAX COMMUNITY LICENSE
Copyright (c) 2026 MiniMax
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software for non-commercial purposes, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or provide copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
2. If the Software (or any derivative works thereof) is used for any Commercial Use for your products or services: 
  1. you shall prominently display “Built with MiniMax M3” on a related website, user interface, blogpost, about page or product documentation. 
  2. you shall obtain a separate, prior written authorization from MiniMax by contacting api@minimax.io with the subject line “M3 licensing - authorization request”, if such products and services generate more than 20 million US dollars (or equivalent in other currencies) in yearly revenue; otherwise, you only need to send a one-time notice to api@minimax.io with the subject “M3 licensing — notice”.
3. “Commercial Use” means any use of the Software or any derivative work thereof that is primarily intended for commercial advantage or monetary compensation, which includes, without limitation: (i) offering products or services to third parties for a fee, which utilize, incorporate, or rely on the Software or its derivatives, (ii) the commercial use of APIs provided by or for the Software or its derivatives, including to support or enable commercial products, services, or operations, whether in a cloud-based, hosted, or other similar environment, and (iii) the deployment or provision of the Software or its derivatives that have been subjected to post-training, fine-tuning, instruction-tuning, or any other form of modification, for any commercial purpose.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Appendix: Prohibited Uses 
You agree you will not use, or allow others to use, the Software or any derivatives of the Software to:
1. Generate or disseminate content prohibited by applicable laws or regulations.
2. Assist with, engage in or otherwise support any military purpose.
3. Exploit, harm, or attempt to exploit or harm minors.
4. Generate or disseminate false or misleading information with the intent to cause harm.
5. Promote discrimination, hate speech, or harmful behavior against individuals or groups based on race or ethnic origin, religion, disability, age, nationality and national origin, veteran status, sexual orientation, gender or gender identity, caste, immigration status, or any other characteristic that is associated with systemic discrimination or marginalization.
```
OneHill observation: the grant is for non-commercial purposes and conditions commercial use of the Software or its derivative works. The text does not mention model outputs, synthetic data or training other models on outputs.

## Other models (metadata and, where noted, licence header)
- google/gemma-4-31B-it: card licence apache-2.0, license_link https://ai.google.dev/gemma/docs/gemma_4_license, gated false, no LICENSE file in repo. The Gemma 4 licence page text is stored in docs/primary-sources/gemma-4/license__gemma-4-apache-2.0__2026-11-19.md.
- Qwen/Qwen3.8-27B: card licence apache-2.0; raw LICENSE begins "Apache License / Version 2.0, January 2004". Qwen/Qwen3.6-27B: card licence apache-2.0, LICENSE file present (not opened).
- zai-org/GLM-5: card licence mit (metadata only; no LICENSE file in the repo, see docs/primary-sources/glm/license__glm-5-family-and-mit-cluster__2026-11-19.md).
- inception42/Jais-2-8B-Chat: card licence apache-2.0, gated auto, no LICENSE file.
- Also named by the report: Nemotron Safety v2 (translated into Arabic for SFT; licence not opened), TxT360 and TxT360-3efforts (LLM360; IFM/TxT360-v2 is cc-by-4.0 per hub metadata; the Jais-3-Data card says TxT360-3efforts is released under CC BY 4.0), Common Crawl (Terms of Use).
