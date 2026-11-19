# Groq - status page, security page, platform and trust centre (read 2026-11-19)

## Status page - https://groqstatus.com/ (status.groq.com redirects here; incident.io; HTTP 200)
- "We're fully operational. We're not aware of any issues affecting our systems."
- Aug 2026 - Nov 2026 uptime: API 100%; Production (6 components: llama-3.1-8b-instant, llama-3.3-70b-versatile,
  gpt-oss-120b, gpt-oss-20b, whisper-large-v3, whisper-large-v3-turbo) 100%; Preview Models (7
  components) 99.98%, with minimax-m2.7 at 99.96%; Website 100%. Earlier passes recorded no status page.
- No SLA statement on the page. /history returned 404.

## Security page - https://groq.com/security ("Updated May 2026")
- "Groq operates a private vulnerability disclosure program through HackerOne". Not a public bug bounty.
- Points to the Groq Trust Center for the security programme and compliance documentation.

## Platform page - https://groq.com/platform (marketing)
- "Now operating 13 data centers across four continents": US-1 Liberty Lake, US-2 St Paul, US-3 Dallas, US-4
  Houston, CA-1 Kamloops, CA-2 Vaudreuil-Dorion, CA-3 Calgary, EU-1 Vantaa (Finland), AU-1 Sydney, EU-2 London,
  SA-1 Riyadh. (The 2025 newsroom post on Helsinki now returns 404.)
- Product ladder: GroqMetal "Dedicated bare-metal infrastructure", GroqCore (inference stack), GroqAssured
  (enterprise governance). Homepage and platform copy now mention LPX racks connecting to NVIDIA hardware
  "when released". No public contract terms for dedicated offerings.

## Trust centre - https://trust.groq.com/ and /subprocessors
Both return a ~7 KB single-page-app shell whose visible text is only "Groq Trust Center". Content needs
JavaScript; retrieved: false. The sub-processor list, the SOC 2 claim and any certificate were NOT read in
this pass, so no score rests on them being re-confirmed.
