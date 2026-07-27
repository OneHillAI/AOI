# EU AI Act - GPAI Compliance Mapping for Open-Source Models

**Version:** `1.0` · **Baseline:** July 2026
**Disclaimer:** This is engineering-and-compliance guidance, **not legal advice.**
Obligations and guidance are still being operationalised by the EU AI Office; every
entry dates its analysis and links to primary sources. Confirm with qualified counsel.

---

## 1. Why this matters to a model adopter

Most open-source LLMs are **General-Purpose AI (GPAI) models** under the EU AI Act.
The Act puts obligations on the **provider** of the GPAI model - but if you
**fine-tune, substantially modify, or place a model on the EU market under your own
name**, you can become a *provider* yourself and inherit those obligations. Even as a
pure deployer, you need the upstream documentation to do your own risk work. So a
registry that documents *whether the upstream package exists* is directly useful.

## 2. The obligation landscape (who owes what)

| Actor | Core obligations (GPAI) |
|---|---|
| **GPAI model provider** (the lab) | Art. 53: technical documentation (Annex XI), information for downstream providers (Annex XII), a **copyright policy**, and a **public summary of training content** (the AI Office template). |
| **GPAI with systemic risk** (≥ 10²⁵ FLOPs training compute, or designated) | Art. 55, **on top of** Art. 53: model evaluation & adversarial testing, systemic-risk assessment & mitigation, serious-incident tracking & reporting, cybersecurity protection. **No open-source exemption.** |
| **Downstream provider / fine-tuner** | May become a provider for the modified model; must keep documentation for *its* modifications and pass information downstream. |
| **Deployer** | Not GPAI-provider obligations per se, but transparency duties (e.g. labelling AI interactions, deepfakes) and must rely on upstream documentation for their own risk management. |

## 3. The open-source exemption - and its limits

Article 53 provides a **partial exemption** for GPAI models released under a **free and
open-source license** that makes parameters, architecture, and usage information
public - **provided the model is not monetised**. Key points:

- The exemption covers the **technical documentation to the AI Office and the
  Annex-XII information to downstream providers** - but **NOT**:
  - the obligation to put in place a **copyright policy**, and
  - the obligation to publish the **summary of training content**.
  These two apply to open-source GPAI providers as well.
- The exemption **does not apply at all** to **systemic-risk** models - a
  systemic-risk open model owes the full Article 55 set.
- A **restrictive "community license"** (acceptable-use limits, scale thresholds,
  monetisation) may **fail** the "free and open-source" test, forfeiting the
  exemption. This is analysed per-entry (see the
  [openness framework](openness-framework.md#license-classification)).

> **Registry takeaway:** for each model we record whether it *plausibly qualifies* for
> the open-source exemption, and - regardless - whether the **copyright policy** and
> **training-content summary** exist, because those are owed either way.

## 4. Timeline (as understood July 2026)

| Date | Milestone |
|---|---|
| 1 Aug 2024 | AI Act entered into force. |
| 2 Feb 2025 | Prohibited-practices and AI-literacy provisions apply. |
| 2 Aug 2025 | **GPAI obligations apply** to models placed on the market from this date; AI Office + governance operational; **GPAI Code of Practice** available as the compliance route. |
| 2 Aug 2026 | Broader high-risk / obligations phase-in continues. |
| 2 Aug 2027 | Obligations for GPAI models already on the market before Aug 2025 apply; further high-risk rules. |

The **GPAI Code of Practice** (Safety & Security, Copyright, Transparency chapters) is
the voluntary-but-load-bearing route to demonstrate compliance; signatories get a
presumption of conformity. Whether a publisher signed it is recorded per entry.

## 5. The per-model compliance record

Each model entry carries an `eu_ai_act` block:

```yaml
eu_ai_act:
  is_gpai: true
  systemic_risk:
    designated: false
    training_flops_estimate: "~3.8e25"     # note if over the 1e25 threshold
    over_threshold: true
    article_55_docs_available: partial      # yes | partial | no | n/a
  open_source_exemption:
    license_qualifies: uncertain            # yes | no | uncertain - see license classification
    rationale: "Community license has an acceptable-use policy and MAU threshold; qualification for the 'free and open-source' exemption is contested."
  provider_package:                          # what the publisher actually provides
    technical_documentation: partial         # Annex XI-grade
    downstream_information: yes               # Annex XII-grade (model card + usage)
    copyright_policy: yes
    training_content_summary: yes            # the AI Office template summary
    code_of_practice_signatory: no
  deployer_notes: >
    A fine-tuner placing this on the EU market under their own name likely becomes a
    provider for the derivative and must maintain their own Annex XI/XII docs.
  evidence:
    - {claim: "training-content summary published", source_type: publisher, url: "..."}
  last_assessed: "2026-07-25"
```

## 6. Downstream deployer checklist

A ready-to-use checklist for an organisation adopting an open model. Reproduced in the
[safe-deployment playbook](safe-deployment-playbook.md); summarised here:

```
LEGAL / REGULATORY
[ ] Confirm the license permits your specific use (commercial, scale, field-of-use)
[ ] Obtain & archive the upstream training-content summary + copyright policy
[ ] Obtain & archive the model card / Annex XII downstream information
[ ] Determine whether YOU become a "provider" (fine-tuning / rebranding / market placement)
[ ] If systemic-risk model: obtain Art. 55 evaluation & risk documentation
[ ] Record the exact artifact (source, revision, format) in your AI-BOM
[ ] Map the deployment's own risk category (is your *use* high-risk under Annex III?)
[ ] Implement transparency duties for your use (AI-interaction & synthetic-content labelling)
[ ] Keep a dated compliance file; assign an accountable owner
```

## 7. Sources (primary)

Populated per-entry; the canonical references are the **Regulation (EU) 2024/1689**
text (esp. Articles 3, 53, 55, and Annexes XI & XII), the **EU AI Office** GPAI
guidelines and training-content-summary template, and the **GPAI Code of Practice**.
Each entry links the specific documents it relies on.
