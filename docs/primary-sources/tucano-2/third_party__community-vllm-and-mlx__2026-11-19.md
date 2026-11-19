doc_type: third_party
entity: tucano-2
variant/applies-to: Tucano2-qwen-3.7B-Instruct deployment and quantization by third parties
source_url: https://huggingface.co/gutoportelaa/tucano2-3.7b-instruct-vllm-rtx3080 ; https://huggingface.co/pessini/Tucano2-qwen-3.7B-Instruct-MLX-4bit
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Extracts (VERBATIM or direct translation of the Portuguese README, author Gutemberg Portela Alves; an individual, not Polygl0t)

# Tucano2-3.7B-Instruct no vLLM: receita de deploy e medições (RTX 3080 de 10 GB)

> **Este repositório não contém pesos.** O modelo é o
> [`Polygl0t/Tucano2-qwen-3.7B-Instruct`](https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Instruct), usado sem
> alterações (Apache-2.0). Aqui estão a configuração de deploy, os scripts e os resultados de um critério de aprovação de
> qualidade e latência que o escolheu entre quatro candidatos. Baixe os pesos do repositório original.

## Configuração testada

| Item | Valor |
|---|---|
| GPU | RTX 3080, 9,64 GiB úteis, 760 GB/s (Ampere, SM 8.6) |
| Motor | vLLM 0.33.0, PyTorch 2.14, CUDA 13 |
| Precisão | bf16 (pesos de 7,06 GiB, sem quantização) |
| KV cache | 1 GiB fixo (7.280 tokens), bf16 |
| Execução | `torch.compile` + CUDA graphs, prefix caching, 8 sequências, contexto 4096 |
| Atenção | `--attention-backend TRITON_ATTN` (sem `nvcc` para o FlashInfer) |
| Raciocínio | desligado nas avaliações (`chat_template_kwargs: {"enable_thinking": false}`) |

```bash
export VLLM_USE_FLASHINFER_SAMPLER=0
vllm serve Polygl0t/Tucano2-qwen-3.7B-Instruct --served-model-name tucano2-3.7b \
  --attention-backend TRITON_ATTN --enable-prefix-caching --max-num-seqs 8 --port 8100 \
  --max-model-len 4096 --kv-cache-memory-bytes 1073741824 \
  --max-num-batched-tokens 2048 --gpu-memory-utilization 0.92
```

```bash
curl localhost:8100/v1/chat/completions -H "Content-Type: application/json" -d '{
  "model":"tucano2-3.7b","max_tokens":120,"temperature":0,
  "messages":[{"role":"user","content":"Diga olá e informe em uma frase qual modelo você é."}]}'
```

## Critério de aprovação (qualidade + latência)

- **Qualidade:** 393 questões de texto do ENEM 2022–2024 (`maritaca-ai/enem`, sem figuras), zero-shot, resposta de
  uma letra, mesmo prompt para todos os modelos.
- **Latência:** chegadas de Poisson a 0,5, 1, 2 e 4 req/s por 40 s, mistura de prompts de 128/512/1024 tokens, 128
  tokens gerados, GPU exclusiva.

| Configuração | ENEM (IC 95%) | TTFT p95 a 2 req/s | TTFT p95 a 4 req/s | VRAM |
|---|---|---|---|---|
| Llama-Poro-2-8B-Instruct, FP8 | 64,1% (59,3–68,7) | 0,38 s | 16,7 s | 9,7 GiB |
| Llama-Poro-2-8B-Instruct, W4A16 | 61,3% (56,4–66,0) | 0,29 s | 2,6 s | 8,0 GiB |
| Qwen3-8B, W4A16 (GPTQ, 256 amostras) | 67,9% (63,2–72,4) | 0,30 s | 3,5 s | 8,5 GiB |
| **Tucano2-3.7B-Instruct, bf16** | **74,6% (70,0–78,6)** | **0,22 s** | 5,7 s | 8,7 GiB |

McNemar pareado (Tucano2 contra cada um): p = 5e-5 (Poro FP8), 1e-6 (Poro W4A16), 0,008 (Qwen3-8B). Entre as
duas variantes do Poro, a diferença **não** é significativa (p = 0,145). Qwen3-8B em FP8 e Gemma-3-12B em W4A16
não couberam na GPU (ver `results/gate_candidatos/gemma3_12b_RESULTADO.txt`) e ficaram sem avaliação.

## Limitações (leia antes de usar)

- **Alucina.** Nos 8 prompts fixos (`results/evidencias/prompts_tucano.json`) inventou "canais artificiais
  construídos por um engenheiro francês" em Teresina e, ao ser perguntado quem é, disse ser baseado no mesmo
  *framework* do ChatGPT. Não use como fonte de fatos sem verificação.
- O ENEM é público e pode ter vazado para dados de treino; o número serve para **comparar** modelos nesta régua,
  não como acurácia absoluta. O PiauíBench (50 chamadas) foi inconclusivo e não está nas conclusões.
- A perplexidade (19,6 em 64 janelas de 128 tokens da Wikipédia em português) usa o tokenizador do Tucano2 e não
  é comparável à de outros modelos.
- Medições feitas em uma única GPU, uma única máquina, sem teste de longa duração.

[English reading of the table] On 393 text-only ENEM 2022-2024 questions, zero-shot, Tucano2-3.7B-Instruct in bf16 scores 74.6% (95% CI 70.0 to 78.6) against Qwen3-8B W4A16 67.9%, Llama-Poro-2-8B FP8 64.1% and W4A16 61.3%. Weights 7.06 GiB, total VRAM 8.7 GiB on an RTX 3080 (about 9.64 GiB usable), vLLM 0.33.0, context 4,096. Generation 79.4 tok/s at concurrency 1 and 436.7 tok/s at concurrency 8. The author warns the model hallucinates and that ENEM may be in training data.
[MLX 4-bit repo] pessini/Tucano2-qwen-3.7B-Instruct-MLX-4bit: card states a 4-bit MLX quantisation of the Instruct model, Apache-2.0, base architecture Qwen3-4B, 3.76B parameters, context 4,096; its benchmark table repeats the publisher's numbers (Total Avg. 53.64) and is not an independent run.
