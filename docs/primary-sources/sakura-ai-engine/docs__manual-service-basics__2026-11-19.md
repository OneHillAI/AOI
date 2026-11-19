# Sakura Cloud manual: AI Engine service basics (サービス基本情報)

- Source URL: https://manual.sakura.ad.jp/cloud/ai-engine/01-basics.html
- Retrieved: 2026-11-19 (by OneHill agent, curl; HTML converted to text by a local script that drops scripts, styles and tags; navigation menus trimmed)
- Language: Japanese (original). Product documentation page dated 2026-11-11 by Sakura. Not part of the contract.

## Verbatim text

```text
サービス基本情報 
[更新: 2026年11月11日]
概要 
「さくらのAI Engine」は従量課金型で様々な生成AIモデルを使える基盤プラットフォームサービスです。
対応しているLLMモデルはすべてさくらインターネットによりホスティングされているため、データはすべてお客様とさくらインターネット間の通信だけで完結し、チャット補完などに使われるデータはLLMモデルなどの学習に使われることのない、データ安全性の高いサービスです。
機能説明 
さくらのAI Engine は大きく4つの機能を提供しています。
チャット補完
ドキュメント管理とRAG (Retrieval-Augmented Generation)
音声の文字起こし
音声合成
注意事項 
ご利用いただく前に、以下の点にご注意ください。
品質保証（SLA）の適用対象外です。
LLM に対して「モデル名」や「内部仕様」を問い合わせた場合でも、実際に稼働しているモデル名と一致した回答が得られない場合があります。
基盤モデル無償プランにおいても、RAG (Retrieval-Augmented Generation) をご利用開始、すべてのドキュメントを削除するまで課金対象となりますのでご注意ください。
すべてのアカウントトークンとすべてのドキュメントを削除しないとプランの解約はできません。
サポート範囲は お客様サポート の「弊社・お客様の責任分界点」に準じます。
データの取り扱い 
さくらのAI Engine へのリクエストは、国内のデータセンターで処理されます。
チャット補完、ベクトル埋め込み、音声の文字起こし、音声合成のリクエストで送信された入力内容（プロンプトや音声データなど）および応答内容は保存されません。
ドキュメント管理とRAGの機能でアップロードしたドキュメントは、お客様が削除するまで保存されます。
料金体系 
料金については サービスサイト を参照ください。
さくらのAI Engine では、無償分を除き、API呼び出しごとの従量課金が基本です。
コスト予測をしやすいGPU専有モデルをご希望の場合、 さくらのAIサービスサイト内 お問合せフォームからお問い合わせください。
サポート 
ご不明点やお困りの際は、 会員メニュー内のメールサポート より、サービス情報として「さくらのAI Engine」を選択してお問い合わせください。
```

## English reading (OneHill translation, not authoritative)

- Notes before use: "Not covered by quality assurance (SLA)." A model asked for its name or internal specification may answer with a name that differs from the model actually running. The free foundation-model plan still bills RAG while any document exists. The plan cannot be cancelled until all account tokens and all documents are deleted.
- Overview: "All supported LLMs are hosted by Sakura Internet, so data stays entirely within communication between the customer and Sakura Internet, and data used for chat completion is not used to train LLMs."
- Data handling: "Requests to AI Engine are processed in domestic (Japanese) data centres. Input content (prompts, audio data and so on) and response content sent in chat completion, vector embedding, transcription and speech synthesis requests are not stored. Documents uploaded for document management and RAG are stored until the customer deletes them."
- Plain consequence: this is a product-documentation statement, not a contract term. It says "not stored" without the maintenance-retention qualification of Art. 10(1) of the terms. It also confirms that uploaded RAG documents are stored indefinitely until deleted, a case the terms do not address.
