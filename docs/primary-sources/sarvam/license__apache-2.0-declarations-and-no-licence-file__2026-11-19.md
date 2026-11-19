# license / Apache-2.0 declared on every Sarvam weights repo; no LICENSE file

source_url: https://huggingface.co/sarvamai/<repo>/raw/main/LICENSE (HTTP 404) ; https://www.apache.org/licenses/LICENSE-2.0.txt
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE (OneHill): none of the weights repositories contains a LICENSE file. A request for raw/main/LICENSE on 2026-11-19 returned HTTP 404 for sarvam-30b, sarvam-105b, sarvam-105b-1711, sarvam-105b-1711-bf16, sarvam-105b-fp8, sarvam-30b-fp8, sarvam-105b-gguf and sarvam-30b-gguf. The file listings from the Hugging Face API hold only README.md, config and tokenizer files, custom Python files and weights. The grant therefore rests on three publisher statements: the card front matter `license: apache-2.0` (hub tag license:apache-2.0), the card sentence below, and the publisher blog.

Card sentence (sarvam-105b and sarvam-30b, same wording with the model name changed):
```
Sarvam-105B is open-sourced under the **Apache License**. For more details, see our [blog](https://www.sarvam.ai/blogs/sarvam-30b-105b).
```
NOTE: the card sentence names 'the Apache License' without a version number and links no licence text. Apache-2.0 is the SPDX identifier in the front matter.

Blog sentence (publisher blog, conclusion):
```
Combined with Apache 2.0 open-source availability, these models serve as foundational infrastructure for sovereign AI development.
```

Sibling contrast: the separate repository sarvamai/prism (a Sarvam-105B LoRA fine-tune) does carry a LICENSE file (HTTP 200, standard Apache-2.0 text). The weights repos in this entry do not.

Standard Apache-2.0 text read from apache.org (sections that matter):
```
   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. ... perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work ...

   7. Disclaimer of Warranty. ... Licensor provides the Work ... on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND ...
```

NOTE: no Sarvam document read for this entry (Terms of Service v2.0, EULA, Privacy Policy) mentions the Apache-2.0 weights or carves them out. See terms__sarvam-terms-of-service-v2.0 and terms__sarvam-eula.
