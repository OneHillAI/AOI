doc_type: security
entity: baseten
source_url: https://www.baseten.co/security-practices/
document_effective_date: "Last Updated: November 12, 2026" (stamped on the page)
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher
read_by: code session (curl, raw HTML to text); human-supervised baseline in browser-verified/ was taken 2026-09-20

## What changed against the 2026-09-20 browser-verified baseline

1. The sentence quoted in the baseline ("Unless a customer, acting through an authorized representative, requests otherwise in writing, ZDR is the default configuration for the customer's use of the inference products") is NOT in the live page. The substance is carried instead by the ZDR section below (a posture "across the below inference products") plus a new opt-out paragraph. Treat "ZDR is the default" as still supported in substance for Model APIs and Dedicated Inference, but no longer in those words on this page. docs.baseten.co/security.md (2026-11-19) still says "Synchronous requests run under ZDR by default" for Dedicated Inference.
2. New "Customer-Controlled Factors" carve-out (verbatim below).
3. Asynchronous Inference is now described as an elective feature of Dedicated Inference (it was described as a general exception before).
4. New sections: Training (Loops and Serverless Loops) retention, Baseten Sandboxes retention, Hybrid deployment option, 48-hour breach notification.
5. The "KV cache never persisted to disk" statement recorded in ev-security is not on the live page. docs.baseten.co/observability/security.md says: "Cache storage depends on your inference engine and configuration."

## Governing clauses (VERBATIM)

[ZDR Products] "Baseten adheres to a Zero Data Retention posture across the below inference products. "Zero Data Retention" or "ZDR" means that Baseten shall not (a) log, record, or store inference inputs or outputs; or (b) save inference inputs or outputs to persistent storage (e.g., hard drives, solid-state drives, cloud storage, databases) after the real-time processing required for the provision of the Services."

[Model APIs] "Baseten's Model APIs product adheres to a Zero Data Retention posture for all model inputs or outputs. Baseten will not store, retain, or otherwise make a persistent copy of model inputs or outputs during a customer's use of the Model APIs."

[Dedicated Inference] "Baseten's Dedicated Inference product adheres to a Zero Data Retention posture for Customer Model inputs or outputs. Baseten will not store, retain, or otherwise make a persistent copy of Customer Model inputs or outputs during a customer's use of the Dedicated Inference product."

[Asynchronous Inference] "Asynchronous inference is an elective feature of Dedicated Inference. If Customer elects to enable asynchronous inference, model inputs get temporarily stored and queued for the duration of the request as described in the Documentation. These model input requests can stay in queue for up to 72 hours before being processed and then deleted. Asynchronous Inference does not store the Model Outputs."

[ZDR Configuration Changes] "Customers may elect to enable logging, traffic recording, retention, abuse monitoring, or other changes to the applicable ZDR configuration for their workloads by written notice, and Baseten will promptly implement requested changes whenever technically supported for the applicable Service."

[Customer-Controlled Factors] "Baseten will not be in breach of these Security Practices (including the ZDR commitments) to the extent that any logging, retention, storage, access, use, or disclosure of Customer Content arises from (a) configurations, settings, or deployment choices made by a customer or its authorized users; (b) model runtime code, packages, dependencies, or other software provided or selected by a customer, including any vulnerability or compromise latent in a Customer Model or its supply chain; (c) a customer's election to enable any Third-Party Product; or (d) actions taken at a customer's written direction."

[Infrastructure-Only Processing] "Baseten does not use Customer Content for model training, fine-tuning, or improvement of any algorithms."

[Training retention] "Checkpoints and other Customer Models created through Loops and Serverless Loops are retained until the customer deletes them"; "For thirty (30) days after the end of a customer's subscription term, Baseten will provide the customer access to the Services to allow retrieval of Customer Content. After such thirty (30) day period, Baseten will promptly delete all remaining Customer Content in its possession." Residual copies "may remain in backups for a limited period until they are overwritten or purged".

[Audits and Certifications] "Baseten undergoes periodic SOC 2 Type II examinations conducted by an independent third-party auditor." Certifications listed on the page: SOC 2 Type II, HIPAA ("enters into Business Associate Agreements (BAAs) with qualifying customers"; "Serverless Loops is not a covered product"), GDPR (DPA at baseten.co/dpa). ISO 27001, ISO 27701, PCI DSS, FedRAMP and CSA STAR are NOT named anywhere on the page. (The separate trust centre at trust.baseten.co does list ISO 27001:2022 and PCI DSS SAQ D; see security__trust-centre__2026-11-19.md.) "Baseten Sandboxes is covered by its own SOC 2 Type II report, which may be issued in the name of Blaxel, a Baseten affiliate."

[Multi-cloud / regions] "Baseten's multi-cloud capacity management architecture distributes workloads across cloud providers and multiple regions globally, enabling cross-provider redundancy, GPU failover, and region-locking for customers with data residency or compliance requirements."

[Deployment Options] "Baseten Cloud: Fully managed, multi-cloud deployment"; "Self-Hosted: ... No Customer Content leaves the customer's environment."; "Hybrid: Combines self-hosted control with elastic spillover to Baseten Cloud".

[Incident notification] "Baseten notifies impacted customers without undue delay, and in any event within forty-eight (48) hours, of any unauthorized disclosure of their Customer Content of which Baseten becomes aware, to the extent permitted by law."

[Encryption] in transit "TLS v.1.2 or higher" (mTLS between clusters); at rest "AES-256 bit encryption (or the equivalent or better, depending on the applicable cloud service provider)". [Access] "Baseten enforces multi-factor authentication for all personnel." Quarterly access reviews. [Pen-test] "Baseten engages qualified third-party security firms for periodic penetration testing." No bug-bounty programme named.

[Sub-processors] "A list of material Infrastructure Providers and Subprocessors is maintained at https://trust.baseten.co/." "Infrastructure Providers are not Subprocessors under Baseten's DPA ... unless they have logical access to Customer Content containing personal data." "Customers will be notified at least fifteen (15) days prior to engagement of any new Subprocessor, as described in Baseten's DPA."
