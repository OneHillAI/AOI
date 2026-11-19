# Sakura Cloud manual: use of closed models

- Source URL: https://manual.sakura.ad.jp/cloud/ai-engine/06-closed-model.html
- Retrieved: 2026-11-19 (by OneHill agent, curl; HTML converted to text by a local script that drops scripts, styles and tags; navigation menus trimmed)
- Language: Japanese (original). Product documentation page dated 2025-12-02 by Sakura.

## Verbatim text

```text
クローズドモデルの利用に関して 
[更新: 2025年12月2日]
クローズドモデルの利用方法 
クローズドモデルは、特定のモデル提供元が審査のうえ利用可否を判断するモデルです。
利用には 事前申請 が必要であり、 無償枠の対象外 となります。
利用を希望される場合は、以下の手順と注意事項をご確認ください。
利用にあたって 
クローズドモデルをご利用いただくには、事前の申請が必要です。
申請内容をもとにモデル提供元が利用許可を判断するため、 申請後すぐに利用を開始することはできません。
また、以下の点にご留意ください。
クローズドモデルは無償枠の対象外です。利用量に応じて料金が発生します。
クローズドモデルの申請フォームには個人情報を入力・送信しないでください。
クローズドモデル利用開始後にユーザーが推論リクエストとして入力するテキスト等のデータは、モデルの推論処理のみに使用され、モデル提供元へ送信されることはありません。
ご利用までの流れ 
AIエンジンのコントロールパネルより、 「利用可能なモデル」一覧ページ へ移動します。
申請可能なモデルから「申請」ボタンをクリックします。
申請フォームに以下を記入します。
必要事項の入力
利用規約への同意
内容を確認し、送信してください。
申請内容をもとにモデル提供元が利用可否を判断します。
原則として 7営業日前後 で結果が確定いたします。「利用可能なモデル」一覧ページにてステータスをご確認ください。
許可された場合、対象モデルに「利用可能」アイコンが表示されます。
注意事項 
クローズドモデルをご利用の際は、以下にご注意ください。
無償枠の対象外です
無償プランでは利用できず、利用量に応じて課金が発生します。
審査基準や理由は回答できません
モデル提供元の審査プロセス・判断基準・不許可理由については個別回答ができません。
個人アカウントでは利用できません
法人アカウントのみ申請可能です。
個人情報を送らないでください
申請内容に個人情報を含めないでください。
データ提供は行われません
モデル利用時のデータがモデル提供元へ送信されることはありません。
審査結果は保証されません
利用用途によっては申請が不許可となる場合があります。
```

## English reading (OneHill translation, not authoritative)

Closed models (PLaMo 3.0 Prime from Preferred Networks, cotomi v3 from NEC) need an application that the model provider approves, take about 7 business days, are not in the free plan, and are available to corporate accounts only. The page says text entered as inference requests after approval "is used only for model inference and is not sent to the model provider", and that no data is provided to the model provider. This is documentation, not a term; the binding statement is Art. 10(2) of the AI Engine terms (inputs not provided to model providers). The application form must not contain personal information.
