doc_type: deployment
entity: nemotron
variant/applies-to: NIM self-hosted deployment + build.nvidia.com hosted preview terms
source_url: https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/ ; https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf
document_effective_date: not shown
retrieval_date: 2026-07-31
exists: yes
retrieved: true
tag: publisher

## NIM = self-hosted deployment tooling (NOT a hosted inference provider)
[VERBATIM] https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/ : "NVIDIA NIM(TM) provides prebuilt, optimized inference microservices for rapidly deploying the latest AI models on any NVIDIA-accelerated infrastructure" ; "Deploy anywhere ... ready to run on any NVIDIA-accelerated infrastructure" across "cloud, data center, workstation, and edge".
[Data-control point - VERBATIM] you "Download and Deploy" to run NIM in "the cloud or data center of your choice," so "data never leaves your secure enclave".

AOI implication: NVIDIA is NOT added as an AOI inference-provider entry. Self-hosting via NIM
(weights + inference on your own infrastructure, no data handed to NVIDIA) supports the data_control
factor for the Nemotron entry.

## build.nvidia.com hosted PREVIEW API (LOW priority - evaluation surface, not the primary path)
Source: NVIDIA API Trial Terms of Service PDF.
[No session storage - Section 2.3, VERBATIM] "NVIDIA will not store or use User Content or Generated Content at the end of each API Service session"
[Monitoring exception - Section 2.4, VERBATIM] "NVIDIA may log and store User Content and Generated Content to monitor for security or to prevent fraud or abuse" ; Fine-Tuning API stores User Content "thirty (30) days"
[TENSION - Section 3.3, VERBATIM] NVIDIA collects "User Content and Generated Content to improve NVIDIA products and services, including AI models"

Assessment: the free build.nvidia.com preview is NOT unambiguously "no training on inputs" (2.3 no
session storage, but 3.3 reserves use of content to improve AI models). Report both. Evaluation
surface, not the primary (self-hosted NIM) deployment path.
