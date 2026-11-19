# marketing / publisher-blog-llm-jp-4-1

source_url: https://llm-jp.nii.ac.jp/blog/llm-jp-4-1/
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE (OneHill): publisher blog in Japanese (author Takashi Kodama and Yunang Wu, dated 2026.09.28). Treated as a publisher blog post (marketing doc_type) for grounding. Translations below are OneHill's, the original Japanese passages follow.

OneHill translation of key statements: "LLM-jp-4.1 improves the post-training of the LLM-jp-4 series, mainly STEM performance and the addition of tool calling." "In addition to the tuned models, the SFT data and DPO data used for training are also published." "In AnswerCarefully, a Japanese safety benchmark, and llm-jp-instructions, improvement was seen in LLM-jp-4.1." "The current LLM-jp post-training pipeline consists only of SFT and DPO; we plan to develop and release models that also use reinforcement learning." "LLM-jp-4.1 is the first LLM-jp series model to support tool calling." "On GPQA Diamond and AIME there was large improvement from LLM-jp-4, but a gap to existing open-weight models remains."

Original text, introduction and models:
```
LLM-jp ではオープンかつ日本語に強い大規模言語モデルの開発を進めています．2026年4月以降 llm-jp-corpus v4 および llm-jp-corpus v4.1 を用いて訓練した「LLM-jp-4」シリーズを順次公開してきました．これまでに 8B と 33B の2種類の dense モデルと 32B-A3B の MoE モデルを公開しています．
今回，新たに「LLM-jp-4.1」シリーズを公開します．LLM-jp-4.1 では，LLM-jp-4 シリーズの事後学習を改善しており，STEM 分野を中心とした性能向上や Tool Calling 機能の追加などが主な変更点です．
また，チューニング済みモデルに加えて，学習に使用した SFT データおよび DPO データも公開しています．
チューニング済みモデル
llm-jp/llm-jp-4.1-8b-thinking
llm-jp/llm-jp-4.1-32b-a3b-thinking
llm-jp/llm-jp-4.1-33b-thinking
チューニング済みモデル（量子化版）
llm-jp/llm-jp-4.1-8b-thinking-gguf
llm-jp/llm-jp-4.1-32b-a3b-thinking-gguf
llm-jp/llm-jp-4.1-33b-thinking-gguf
事後学習データセット
llm-jp/llm-jp-4.1-thinking-sft-data
llm-jp/llm-jp-4.1-8b-thinking-dpo-data
llm-jp/llm-jp-4.1-32b-a3b-thinking-dpo-data
llm-jp/llm-jp-4.1-33b-thinking-dpo-data
```
Original text, safety and quality results paragraph and conclusion:
```
LLM-jp-4 と LLM-jp-4.1 を比較すると，MT-Bench のスコアはおおむね横ばい，もしくは若干低下しています．MT-Bench は情報量の多い回答が高く評価される傾向があるため，今回の事後学習で行った回答の簡潔化がスコアに影響している可能性があります．LLM-jp-4 までは MT-Bench を主要な評価指標の一つとして用いてきましたが，スコアが頭打ちになりつつあることも踏まえ，LLM-jp-4.1 では補助的な評価指標として位置付けています．
一方，日本語安全性ベンチマークである AnswerCarefully と，日本語質問応答ベンチマークである llm-jp-instructions では，LLM-jp-4.1 で改善が見られました．llm-jp-instructions では，回答の正確性や情報量などをサブ指標として評価しています．詳細を見ると，回答の情報量は低下した一方で，正確性は向上していました．回答を簡潔にしたことで，ハルシネーションや不要な情報の生成が抑えられ，結果として回答の安全性や正確性の向上につながった可能性があります．
```
```
おわりに
本記事では，LLM-jp-4.1 シリーズの事後学習の内容と評価結果について紹介しました．
LLM-jp-4.1 では，STEM 分野を中心に性能が向上したほか，新たに Tool Calling 機能も追加しました．LLM-jp-4 と比較して高性能な既存モデルとの差を着実に縮めている一方で，AIME や GPQA などの高難度タスクには依然として改善の余地が残っています．現在の LLM-jp の事後学習パイプラインは SFT と DPO のみで構成されており，今後は強化学習も取り入れたモデルの開発・公開を進めていきたいと考えています．
LLM-jp では，今後も LLM の安全性に関する研究開発を継続して進めていきます．LLM を社会で利活用していく上では，透明性や信頼性の確保が重要であり，モデルの高度化に伴って安全性への配慮もさらに重要になります．今回公開したモデルや今後開発するモデルを活用してこれらの研究を進め，LLM の研究開発の促進に貢献していきます．
```
