# license / apache-2.0-llm-jp-4.1

source_url: https://huggingface.co/llm-jp/llm-jp-4.1-33b-thinking ; https://www.apache.org/licenses/LICENSE-2.0.txt ; https://github.com/llm-jp/scripts
retrieval_date: 2026-11-19
exists: yes (as card declaration and standard text; no LICENSE file in the model repo)
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE (OneHill): the Hugging Face model repositories contain NO LICENSE file. A direct request for https://huggingface.co/llm-jp/llm-jp-4.1-33b-thinking/raw/main/LICENSE on 2026-11-19 returned HTTP 404. The file list from the Hugging Face API for llm-jp-4.1-33b-thinking, 8b-thinking and 32b-a3b-thinking holds only README.md, chat_template.jinja, config.json, generation_config.json, llmjp4_harmony.py, llmjp4_tokenizer.py, the safetensors shards and tokenizer files. The grant therefore rests on three statements by the publisher: the model card YAML front matter `license: apache-2.0` (hub tag license:apache-2.0), the model card section "License" linking the Apache text, and the technical report section 2.4. The licence text itself is the standard Apache-2.0 text.

## Model card statement (llm-jp-4.1-33b-thinking, 8b-thinking, 32b-a3b-thinking: identical)
```
---
license: apache-2.0
---
...
## License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
```

## Technical report 2.4 (arXiv 2610.19331)
```
We release the LLM-jp-4 models under the Apache License 2.0, a standard open-source license.
```
The report adds that the absence of use restrictions in the licence "does not imply that the societal impacts of model use are unimportant" and that responsibilities "include avoiding uses that infringe intellectual property rights or human rights, contribute to defamation, involve professional judgments without appropriate qualifications or expert oversight, or otherwise violate applicable laws and regulations." These are described as responsibilities distinct from the licence; they are not licence terms.

## Apache-2.0 text, https://www.apache.org/licenses/LICENSE-2.0.txt (retrieved 2026-11-19, 11358 bytes)
Sections 2, 3, 7 and 8 (governing grant and disclaimers):
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
```
```
   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.
```

## Companion code repositories
https://raw.githubusercontent.com/llm-jp/scripts/main/LICENSE is the Apache License, Version 2.0 (full text). GitHub API licence field: llm-jp/scripts Apache-2.0, llm-jp/llm-jp-4-cookbook Apache-2.0, llm-jp/llm-jp-judge Apache-2.0, llm-jp/llm-jp-tokenizer Apache-2.0, llm-jp/llm-jp-4-vl Apache-2.0. llm-jp/Megatron-LM (fork) and llm-jp/swallow-evaluation-instruct report NOASSERTION (not read).
