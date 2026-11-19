# Assess - Sakura Internet AI Engine

_Should we route our data through this provider? Data governance, compliance, residency, security,
pricing and reliability live here. The binding documents are in Japanese and the Japanese text governs
(basic terms Art. 3(1)). English readings below are OneHill's own and have not been checked by a Japanese
lawyer._

<!-- item: data-governance -->
## Data governance - retention, ZDR and training

The AI Engine terms commit Sakura in writing not to use your inputs, not to give them to third parties
(model providers included) and not to train on them, but they do not promise zero retention.

Article 10(1) (第10条第1項) of the AI Engine service terms reads, in OneHill's translation: inputs and
outputs are "in principle not stored" (原則として保存されません), but may be stored "for a certain period"
(一定期間) in Sakura's facilities for maintenance or fault handling, are then kept encrypted, and are deleted
after that period and not stored permanently. The "certain period" is not defined in any of the three terms
documents. Article 10(2) reads: Sakura does not use input information and does not provide it to third
parties "including, but not limited to, model providers", and input information is not used for AI
training by Sakura or the model provider. The sentence covers inputs. Outputs are not named in it.

Translation uncertainty: 恒常的には is read as "not on a standing basis"; 一定期間 could also be read as "a
fixed period", which still leaves the length open.

**Contradiction with marketing.** The product page, FAQ and Private Edition page say input and response data
are "not stored at all", that prompts are "not cached", and that the service is "ZDR (Zero Data
Retention)". Article 10(1) permits temporary encrypted storage for an undefined period, so zero retention
is a marketing claim and not a contract term. The manual adds that documents uploaded to the RAG feature are
kept until you delete them, a case the terms do not address. For Private Edition, article 9(4) says Sakura
does not handle input and output "in principle", with exceptions for fault investigation, support you ask
for, and legal or other justifiable reasons (正当な理由, open-ended).

<!-- item: data-ownership -->
## Data and IP ownership

Nothing in the terms takes a licence over your inputs or outputs. Article 10(3) says you may use outputs
freely as long as you stay within each model provider's licence. The two closed models narrow that: the
PLaMo licence bars entering personal information (Art. 4(7)), fine-tuning, and using outputs to train other
language models (Art. 3(2)), and the cotomi conditions bar distillation and derived models (Art. 2(8), 2(9)).

There is no mutual confidentiality clause naming customer data. What exists is the express duty in article
10(2) (inputs only) and the statutory secrecy of communications in basic terms article 24(1). Article 24(2)
allows disclosure to courts and regulators, and article 24(3) allows disclosure of information within your
secrecy of communications to third parties where you commit a prohibited act. Basic terms article 17(2)
says Sakura does not involve itself in your data and is not liable for its leakage or loss, subject to
article 29. Under Private Edition, rights in your model stay with you (article 8(4)) and Sakura may not use
the model to train its own or anyone else's AI (article 9(2)).

<!-- item: residency -->
## Residency and jurisdiction

Japan-only processing is claimed but not contracted. The top-page FAQ says model execution, communication and
storage are completed entirely on cloud infrastructure in Japan, and the manual says requests are processed
in domestic data centres. None of the three terms documents contains a location clause. Basic terms article
2(5) (in OneHill's reading) says websites designated in the terms are not part of the terms unless expressly
stated. No data centre is named for AI Engine, and there is no region choice in the API.

The contract is under Japanese law (article 32) with the Tokyo District Court as the exclusive first-instance
court for your claims, and Sakura may choose arbitration in Tokyo before one arbitrator it selects, in
Japanese (article 33(2)). Sakura is a Japanese company, so the US CLOUD Act does not apply to it as a US
company. The terms do import US export control: users on the Japanese METI Foreign End User List, the US BIS
lists or from embargoed countries are barred (AI Engine terms articles 3 and 12). Applicants must live in a
"designated country" (basic terms article 5(3)), and the list was not found.

<!-- item: compliance -->
## Compliance and attestations

Sakura holds real, independently audited certifications, but none of the scopes read names AI Engine.
ISMS ISO/IEC 27001 (ICMS-SR0063) is a company-level certificate valid to 2027-04-12. The ISMS cloud
security certificate (ISO 27017 based), the ISO/IEC 27018 certificate and the ISMAP registration (C21-0030-2)
all name Sakura Cloud (Tokyo and Ishikari regions). PCI DSS covers physical requirements 9 and 12 only. A
public SOC 3 report from an independent auditor (security and availability, 2025-06-01 to 2026-05-31,
opinion dated 2026-07-31) covers the Ishikari data centre, not AI Engine. SOC 2 Type 2 (data centre) and
SOC 2 Type 1 (Sakura Cloud) reports are disclosed on request and were not read.

No DPA, GDPR addendum or sub-processor list was found. The privacy policy concerns personal information
Sakura collects about its own customers and staff and says nothing about AI Engine inputs. The check sheet
(updated 2026-11-13) says billing, invoicing and customer support are outsourced, without naming
contractors. The transparency report omits AI Engine. Compliance is therefore scored on what ties to this
service, not on the company's full certificate list.

<!-- item: security -->
## Security controls

Documented for AI Engine: temporarily kept inputs and outputs are encrypted (article 10(1)); access is by
account token; the Sakura Cloud service endpoint gateway gives a private route to the API; service policies
control resources per organisation. Not found for AI Engine: tenant-isolation description, a penetration-test
statement, a bug-bounty or vulnerability-disclosure policy, and an incident history. Sakura's cloud security
policy describes full virtualisation for customer-created servers, which is a different product. Private
Edition dedicates the named GPU platform, but article 2(2) says VM, storage, API and network exclusivity is
not guaranteed unless agreed.

<!-- item: pricing -->
## Pricing and cost model

Pay-as-you-go in yen, tax included, per 10,000 tokens (gpt-oss-120b: 0.15 yen input, 0.75 yen output),
per 60 seconds of audio, per 10,000 mora of speech and per 100 RAG chunks. A free foundation-model plan gives
a monthly request allowance (3,000 chat requests). Payment is by credit card unless Sakura approves otherwise
(article 6), billed in yen on the 10th of the next month. RAG storage bills until every document is deleted.
Private Edition is a flat monthly fee per GPU on quote with a two-month or one-year initial term. No
comparison with other providers was made in this pass.

<!-- item: reliability -->
## Reliability posture

AI Engine is outside Sakura's SLA, per the manual ("品質保証（SLA）の適用対象外です"). Private Edition
article 11 gives best effort unless an SLA is written into the service site, order form or another document.
The only remedy found is basic terms article 29(3): if a continuously provided service is wholly unusable
for 24 hours or more for a reason attributable to Sakura, compensation of actual ordinary damage on request,
capped at one thirtieth of one month's basic fee per whole day of outage, or a term extension when the sum is
under 10,000 yen. How that applies to a usage-billed service is not stated. Sakura's public status page lists
Sakura Cloud components and not AI Engine, so no uptime history was found.
