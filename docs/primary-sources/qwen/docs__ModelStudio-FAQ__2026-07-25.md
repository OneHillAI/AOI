# Qwen - Alibaba Cloud Model Studio FAQ (hosted-service data posture)

- **doc_type:** docs
- **source_url:** https://www.alibabacloud.com/help/en/model-studio/faq-about-alibaba-cloud-model-studio
- **retrieval_date:** 2026-07-25
- **exists:** yes
- **retrieved:** true

## Governing clauses (verbatim)

**Data privacy / training use:**
> "Alibaba Cloud strictly protects data privacy and never uses your data for model training."

**Storage:**
Model Studio "will store data generated from model and application calls." (No retention
period is stated in the FAQ.)

**Security:**
Data is "encrypted with AES-256" in transit.

## What this grounds

- Flips the hosted-Qwen training-use posture from *documented-but-unverified* to a grounded
  **no-training** commitment (`ev-modelstudio-faq`, doc_type `docs`, retrieved).
- The FAQ points to the formal **Model Studio Service Agreement** for the binding specifics -
  exact retention period, storage region, and opt-out mechanics - which was not directly
  reachable this round. Those specifics remain `retrieved: false` (`ev-terms`); the
  training-use commitment itself is now grounded here.
