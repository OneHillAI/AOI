# Sakura Cloud manual: chat models specification

- Source URL: https://manual.sakura.ad.jp/cloud/ai-engine/chat-models.html
- Retrieved: 2026-11-19 (by OneHill agent, curl; HTML converted to text by a local script that drops scripts, styles and tags; navigation menus trimmed)
- Language: Japanese (original). Product documentation page dated 2026-11-18 by Sakura.

## Verbatim text

```text
チャット生成モデルの仕様 
[更新: 2026年11月18日]
チャット補完API（ https://api.ai.sakura.ad.jp/v1/chat/completions ）で利用できるチャット生成モデルの仕様と、APIの互換性について説明します。
モデルごとの仕様 
モデル名
context 長
max_tokens の上限
vision
tool call
reasoning
gpt-oss-120b
131,072
32,000
✕ ※3
✓
✓
preview/gemma-4-31B-it
262,144
32,000 ※2
✓
✓
✓
llm-jp-3.1-8x13b-instruct4
4,096
※1
✕
✕
✕
preview/Phi-4-mini-instruct-cpu
4,096
※1
✕
✕
✕
preview/Qwen3-0.6B-cpu
40,960
※1
✕
✕
✕
preview/Qwen3-VL-30B-A3B-Instruct
262,144
32,000
✓（1リクエストあたり画像3枚まで）
✕
✕
preview/Qwen3.6-35B-A3B
262,144
32,000
✓
✓
✓
preview/Kimi-K2.7-Code
262,144
32,000 ※2
✓
✓
✓
preview/GLM-5.3-Flash
1,048,575
32,000
✓
✓
✓
preview/DeepSeek-V4.1-Flash-1017
1,048,575
32,000
✓
✓
✓
✓ = 対応、✕ = 非対応
※1 固定の上限はありません。「context 長 − 入力トークン数」まで指定できます。
※2 生成速度によっては、上限に達する前に処理時間の上限（約5分）で打ち切られることがあります。
※3 画像を送ってもエラーにはならず、画像は無視されます。
max_tokens の上限は指定できる最大値で、その量の生成を保証するものではありません。
API の互換性 
/v1/chat/completions は、 OpenAI Chat Completions API と互換性のある API です。
各パラメータに指定できる値は、OpenAI Chat Completions API に準じます。
ただし、すべてのパラメータの互換性を保証するものではありません。挙動はモデルによって異なる場合があります。
使えるパラメータ 
パラメータ
説明
model （必須）
使うモデルの名前
messages （必須）
会話のメッセージの配列
max_tokens
生成する最大トークン数
temperature
出力のランダム性
stream
ストリーミングで返すかどうか
tools
モデルが呼び出せる関数の定義
tool_choice
関数を呼び出すかどうかの指定
response_format
出力の形式（JSON など）
reasoning_effort
reasoning の量（ reasoning の制御 を参照）
chat_template_kwargs
モデルのチャットテンプレートに渡す値（ reasoning の制御 を参照）
OpenAI Chat Completions API との違い 
エラー（400）になるもの
入力トークン数と max_tokens の合計が context 長を超えるリクエスト
vision に対応していないモデルへの画像の入力（ gpt-oss-120b を除く）
tool call に対応していないモデルでの tools の指定
gpt-oss-120b での reasoning_effort: "none" の指定
無視されるもの （エラーにはなりません）
「使えるパラメータ」にないパラメータ
例: max_completion_tokens 、 top_p 、 top_k 、 stop 、 seed 、 n 、 logprobs
出力の長さは max_tokens で指定してください。
functions / function_call （旧形式）。 tools / tool_choice を使ってください。
gpt-oss-120b に送った画像
注意事項 
max_tokens 
生成されるトークン数の最大値は、「context 長 − 入力トークン数」「指定した max_tokens 」「モデルごとの上限」のうち最も小さい値です。
max_tokens を省略した場合も、上の最大値まで生成します。
reasoning 対応モデルでは、思考の過程に使われたトークンも max_tokens に含まれます。
処理時間の上限 
1リクエストの処理時間の上限は約5分です。ストリーミングでも同じです。
長い文章を生成すると、 max_tokens の上限に達する前に打ち切られることがあります。特に preview/gemma-4-31B-it と preview/Kimi-K2.7-Code で起こりやすくなっています。
reasoning の制御 
思考の過程は、レスポンスの message.reasoning （ストリーミングでは delta.reasoning ）に返ります。
制御の方法はモデルによって違います。
モデル名
既定の状態
無効にできるか
制御の方法
gpt-oss-120b
有効
できない
reasoning_effort に "low" / "medium" / "high" を指定して、思考の量を調整します。 "none" を指定するとエラー（400）になります。
preview/Qwen3.6-35B-A3B
有効
できる
reasoning_effort: "none" または chat_template_kwargs: {"enable_thinking": false} で無効になります。
preview/gemma-4-31B-it
無効
―
reasoning_effort に "low" / "medium" / "high" のいずれかを指定するか、 chat_template_kwargs: {"enable_thinking": true} で有効になります。
preview/Kimi-K2.7-Code
有効
できない
reasoning_effort: "none" や chat_template_kwargs: {"enable_thinking": false} は指定しないでください。思考の過程が回答本文（ content ）に混ざって返ります。
reasoning に対応していないモデルでは reasoning_effort を指定しないでください。モデルによってはエラー（400）になったり、回答の内容が変わったりします。
preview モデル 
名前が preview/ で始まるモデルは、仕様が予告なく変わったり、提供を終了したりすることがあります。
```

## English reading (OneHill translation, not authoritative)

Table of context lengths: gpt-oss-120b 131,072 tokens; Gemma 4 31B, Qwen3-VL-30B-A3B, Qwen3.6-35B-A3B, Kimi-K2.7-Code 262,144; GLM-5.3-Flash and DeepSeek-V4.1-Flash-1017 1,048,575; llm-jp-3.1-8x13b-instruct4 and Phi-4-mini 4,096; Qwen3-0.6B 40,960. Max output 32,000 tokens for most. Chat Completions is OpenAI-compatible but parameters such as top_p, top_k, stop, seed, n and logprobs are ignored. Each request is cut off after about 5 minutes. Models whose name starts with "preview/" can change or be withdrawn without notice.
