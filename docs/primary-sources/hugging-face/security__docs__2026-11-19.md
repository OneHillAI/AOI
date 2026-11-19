# Hugging Face - security documentation (re-read 2026-11-19, extracts)

Sources (all HTTP 200, read in full):
- https://huggingface.co/docs/hub/security.md
- https://huggingface.co/docs/hub/security-malware.md
- https://huggingface.co/docs/hub/security-pickle.md
- https://huggingface.co/docs/hub/security-jfrog.md
- https://huggingface.co/docs/hub/security-protectai.md
- https://huggingface.co/docs/hub/security-secrets.md
- https://huggingface.co/docs/hub/security-gpg.md
- https://huggingface.co/docs/hub/trusted-publishers.md
- https://huggingface.co/docs/hub/enterprise-advanced-security.md
- https://huggingface.co/blog/jfrog (partnership post, 2024)
- https://huggingface.co/blog/jeffboudier/soc2-iso27001-ai-compliance-guide (Hub blog community article, published 2026-05-14)

## Certifications (CORRECTION to the stored entry)

- Security overview: "Hugging Face is GDPR compliant"; DPAs and BAAs are offered "through an Enterprise Plan"; Hugging Face "is also SOC2 Type 2 certified". Security questions go to security@huggingface.co. No ISO 27001 is mentioned.
- Hub blog article of 2026-05-14 (author Jeff Boudier): states SOC 2 Type II applies to the Hub, Inference Endpoints and Inference Providers, and states ISO 27001 "is not currently held" and that Hugging Face "does not currently publish an ISO/IEC 27001 certification". A community forum thread of 2025-09-12 reaches the same answer informally.
- The stored entry said "SOC 2 and ISO 27001" (citing the JFrog blog). The JFrog blog contains neither claim. The ISO 27001 statement was wrong and is removed. SOC 2 Type 2 is claimed in HF's own docs; no report or certificate was read, so it stays a publisher claim.

## Scanning (unchanged in substance)

- Malware scan: every repository file "smaller than 2 GB" is run through ClamAV, "triggered at each commit". Files with neither an ok nor infected badge may be pending or errored. If a file is scanned as unsafe a warning message is shown to users; the docs advise the owner to remove the file. Nothing says the file is blocked from download.
- Pickle scan: the docs describe a Pickle Import scan that lists the imports in each pickled file and highlights suspicious ones, using pickletools. Disclaimer kept: "this is not 100% foolproof" and Hugging Face is "not actively auditing python packages for safety". The same page still calls safetensors something the team is "experimenting" with and recommends loading from trusted users, relying on signed commits, or loading TF or Flax weights.
- Third-party scanners: JFrog (parses code found in model files and analyses it, aimed at fewer false positives) and Protect AI Guardian (pickle, Keras and other exploits). Results are shown in the Hub UI. The JFrog partnership post says the in-house picklescan "only performs pattern matching on module names". The docs name Guardian; they do not name ModelScan.
- Secrets: TruffleHog runs on every push; email on detection of verified secrets only.
- Not documented in these pages: any blocking or quarantine of flagged files, and any scanning of Python code in repos for trust_remote_code behaviour. The Pluto report (see third_party__incidents__2026-11-19.md) says ClamAV matches known signatures and JFrog returned "not a machine-learning model" for the malicious Python file.

## Signing and publisher identity

- GPG: commits can be signed; a commit shows "Verified" when the public key is uploaded to the account and the signature checks. The docs say this "does **not** guarantee that your file is safe, but it does guarantee the origin of the file". No weight-level signing or provenance attestation is documented. The Hub blog article of 2026-05-14 likewise covers signing only for commits.
- Organisation verified badge: the only documented route found is Team and Enterprise "Advanced Security" - for an organisation with a verified domain name, requiring admin approval for new users adds "a verified badge to your organization page". That is domain verification, not an identity audit of the publisher. The stored entry's "verified_orgs: yes" is kept but this basis is recorded.
- New in the docs (not in the stored entry): Trusted Publishers lets CI push to a repo with a 1-hour OIDC-derived token instead of a stored HF token; fine-grained tokens can be scoped to specific repos and a leaked HF token can be revoked even if not yours (security-secrets doc).
- Safetensors: Hub blog 2026-04-08 says safetensors joined the PyTorch Foundation (Linux Foundation) and is "already the default format for model distribution on the Hugging Face Hub and elsewhere", with the format, APIs and Hub integration unchanged. The Hub does not block pickle uploads.
