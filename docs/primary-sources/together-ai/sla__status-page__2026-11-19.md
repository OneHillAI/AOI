# Together AI - status page (read 2026-11-19)

Source: https://status.together.ai/ (HTTP 200; Better Stack status page). Read the rendered page, /index.json (component
availability, 90 days) and /feed.atom (incident and maintenance feed).

- "All services are online", last updated 2026-11-19 16:41 UTC. Components: Website 100%, Playground 100%, Inference
  (Vision, Chat, Images, Voice) and Together, with per-model 90-day uptime.
- Per-model 90-day availability from index.json: gpt-oss-120b 99.66%, Kimi K3 99.28%, Kimi K3.1 Pro 99.49%, GLM-5.3
  99.91%, GLM-5.2 99.85%, DeepSeek V4 Pro 0813 99.90%, DeepSeek V4.1 Flash 99.90%, MiniMax M3.1 Flash 99.95%, Qwen3.5 9B
  99.58%, Whisper Large V3 99.99%, Orpheus TTS 99.58%; several models at 100%.
- Feed holds four items: maintenance 2026-04-21 and 2026-07-02 (network maintenance, "some serverless models may
  experience degraded performance"), and two "Investigating backend provider issues" posts from 2025-01-06. No incident
  posted after January 2025 in the feed.
- The page states no SLA. The Terms (Sec 1) disclaim uptime guarantees and the docs say serverless is best-effort.
