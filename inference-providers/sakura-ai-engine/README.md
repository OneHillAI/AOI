# Sakura Internet AI Engine - OneHill Inference-Provider Dossier

> **Score: computed by scripts/score.py** · HQ: Japan · EU region: no (Japan-only processing claimed, not contracted) · Trains on inputs: never (inputs only, per terms Art. 10(2))
> Last verified: 2026-11-19
>
> _The binding terms were read in full in Japanese. The terms bar use of inputs and training on them, but they do not promise zero retention, they do not fix a data location, and there is no DPA or SLA. Marketing says more than the contract does._

**Hard flags:** none

---

## 1. What it serves and how it's priced

A shared API (OpenAI-compatible and Anthropic-compatible) over mostly open-weight models: gpt-oss-120b, Qwen3,
Gemma 4, Kimi, GLM, DeepSeek, llm-jp, Whisper and embeddings, plus two closed Japanese models (PLaMo, cotomi) by
application. Prices are published in yen per 10,000 tokens with a free allowance. A dedicated "Private Edition"
hosts your own model on a dedicated GPU platform for Japanese corporations only.

## 2. Data governance - where your prompts go

Terms Art. 10(1): inputs and outputs are "in principle not stored", but may be kept encrypted for an undefined
period for maintenance and fault handling. Art. 10(2): Sakura does not use inputs, does not give them to third
parties including model providers, and inputs are not used for AI training by Sakura or the model provider.
**Contradiction:** the product pages say "not stored at all", "not cached" and "ZDR". The terms do not.

## 3. Compliance and certifications

ISO 27001, ISO 27017, ISO 27018, ISMAP, Privacy Mark and an independent SOC 3 (data centre) are held, but their
registered scopes name Sakura Cloud or the Ishikari data centre, not AI Engine. No DPA or sub-processor list was
found. SOC 2 reports exist on request and were not read.

## 4. Residency and sovereignty

Sakura's FAQ says model execution, communication and storage are completed in Japan. **None of the three terms
documents says so**, and the basic terms say referenced web pages are not part of the contract. No data centre is
named. Japanese law and Tokyo courts govern. As a Japanese company Sakura carries no US CLOUD Act exposure, but its
terms import US export-control lists.

## 5. Reliability and lock-in

AI Engine is outside the SLA, Private Edition is best effort unless an SLA is written, and no AI Engine status
history was found. Most models are public previews that can end without notice. No minimum term, but all RAG
documents must be deleted before cancelling.

## 6. Sources and evidence

See [`entry.yaml`](entry.yaml) for the evidence list and
[`docs/primary-sources/sakura-ai-engine/`](../../docs/primary-sources/sakura-ai-engine/) for the verbatim Japanese
text with OneHill's English readings (not lawyer-checked).

---

_Scored against [provider rubric v1.2](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
