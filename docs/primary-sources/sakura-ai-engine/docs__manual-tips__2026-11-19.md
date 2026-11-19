# Sakura Cloud manual: AI Engine Tips (service endpoint gateway, service policy)

- Source URL: https://manual.sakura.ad.jp/cloud/ai-engine/tips.html
- Retrieved: 2026-11-19 (curl; HTML to text)
- Language: Japanese. Page dated 2026-05-14.

## Verbatim text

```text
Tips 
[更新: 2026年5月14日]
さくらのAI Engine に関するTipsをまとめたページです。
サービスエンドポイントゲートウェイの設定 
 サービスエンドポイントゲートウェイ コントロールパネル操作ガイド を参考に、使用するスイッチに対してサービスエンドポイントゲートウェイを有効化します。
有効状態が「利用可能」になったことを確認し、画面右下の「編集」をクリックします。
「さくらのAI Engine」の api.ai.sakura.ad.jp にチェックを入れます。
入力内容を確認後、右下の「変更」をクリックします。
サービスポリシーの設定 
AI Engine では、サービスポリシーを設定することで、組織単位でリソース作成や操作を制御することができます。
詳細は サービスポリシー をご参照ください。
```

## English reading (OneHill translation, not authoritative)

To reach AI Engine over Sakura Cloud's private network, enable a service endpoint gateway on the switch and tick api.ai.sakura.ad.jp. AI Engine supports service policies that control resource creation and operations per organisation.
