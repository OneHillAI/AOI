# license / Apache-2.0 as declared for Jais-3, plus the licence files that do exist

source_url: https://huggingface.co/inception42/Jais-3-32B ; https://www.apache.org/licenses/LICENSE-2.0.txt ; https://raw.githubusercontent.com/ifm-ai/xllm/main/LICENSE ; https://raw.githubusercontent.com/ifm-ai/RL360/main/LICENSE ; https://raw.githubusercontent.com/ifm-ai/gen-eval-arabic/main/LICENSE
retrieval_date: 2026-11-19
doc_type: license
exists: yes for the Apache text and for the code-repository LICENSE files; NO LICENSE file exists in any of the six Jais-3 weights repositories
retrieved: true
tag: publisher

NOTE (OneHill): none of the six inception42/Jais-3-* weights repositories contains a LICENSE or NOTICE file. Raw requests for LICENSE, LICENSE.md and NOTICE on each returned HTTP 404 on 2026-11-19. The licence of the weights therefore rests on (1) the YAML front matter `license: apache-2.0` and the hub tag license:apache-2.0 on every repo, (2) the technical report statement "Models and training code are released under the Apache 2.0 license" (Section 7.1, Table 41), and (3) the standard Apache-2.0 text. The cards have no "License" section in the body.

## Card front matter (identical in the six cards)
```
license: apache-2.0
```

## Technical report statement (arXiv 2611.10224v2, Section 7.1 and Table 41)
```
Models and training code are released under the Apache 2.0 license; the training-data sample keeps the
terms of its sources (ODC-BY and CC BY 4.0).
```
Table 41 row text (PDF text extraction): "Model weights ... hf.co/collections/IFM/jais-3 ... Apache 2.0"; "Stage checkpoints ... Same collection ... Apache 2.0"; "Training code xLLM (pretraining and SFT) and RL360 (RLVR) ... github.com/ifm-ai/xllm, github.com/ifm-ai/RL360 ... Apache 2.0"; "Training data sample ... hf.co/datasets/IFM/Jais-3-Data ... ODC-BY, CC BY 4.0"; "Evaluation code ... github.com/ifm-ai/gen-eval-arabic ... Apache 2.0"; "Training logs and configurations ... W&B project mbzuai-llm/Jais-3 ... -".

## LICENSE files in the GitHub code repositories (raw, main branch)
ifm-ai/xllm, ifm-ai/RL360 and ifm-ai/gen-eval-arabic: LICENSE is byte-identical in all three (md5 86d3f3a95c324c9479bd8986968f4327), the unmodified Apache License 2.0 text (header "Apache License Version 2.0, January 2004"; appendix boilerplate still reads "Copyright [yyyy] [name of copyright owner]"). ifm-ai/JaisVoice also carries an Apache-2.0 LICENSE (md5 2a944942e1496af1886903d274dedb13, 11,358 bytes).

## Apache License 2.0 governing clauses (apache.org text)
```
   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.
```
