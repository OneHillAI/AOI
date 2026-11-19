doc_type: marketing
entity: kimi-k3.1-pro  (NEW ENTITY candidate; also bears on the kimi-k3 successor note)
source_url: https://www.kimi.ai/blog/kimi-k3-1-pro
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Publisher's own blog, so a publisher claim, not a verified fact. Read in full as extracted page text.

## Cybersecurity section (the one place the K3 safety finding changes)

[Stated control - VERBATIM] "For the open-weight release of K3.1 Pro, we identified and removed cyber-related data from both training stages, while retaining the general-purpose coding tasks needed for model usefulness."
[Stated effect - VERBATIM] "the checkpoint without these risk-reduction measures ... solves 90.5% of problems at pass@3; the final K3.1 Pro reaches 81.0%."
[Stated position - VERBATIM] "K3.1 Pro's cyber capability remains behind that of frontier proprietary models that have been publicly available for at least three months."
[Release stance - VERBATIM] "we intend to progressively raise the cyber capability available in open weights."

Reading: this is training-data filtering that lowers cyber capability by about 9.5 points on an internal benchmark. It is not refusal training, a guard model or a safety-tuned variant, and K3.1 Pro still scores 81.0% on the internal exploit benchmark. The K3 finding (cyber capability present, no refusal) is not repealed by it.

## Availability and hosted-platform claims

[Weights - VERBATIM] "The full model weights will be released by Nov 4." The HF repo is dated 2026-11-02 and carries all 96 shards.
[Zero Data Retention - marketing, VERBATIM] "Zero Data Retention is available for API customers." This is not in the Terms of Service or the Privacy Policy as read on the same day. The binding Terms say only that customers who want restrictions on training use "may contact Moonshot AI to discuss available enterprise arrangements or separate written agreements", and the Privacy Policy says data is stored "as long as necessary". Treat Zero Data Retention as an unverified marketing claim.
[Enterprise] "Kimi Enterprise administrators can enable K3.1 Pro for their organization; access is off by default at launch."
