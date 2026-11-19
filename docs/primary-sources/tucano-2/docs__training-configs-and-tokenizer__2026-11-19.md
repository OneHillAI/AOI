doc_type: docs
entity: tucano-2
variant/applies-to: Tucano2-qwen-3.7B-Instruct and -Think (SFT and APO), config.json
source_url: https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Instruct/raw/main/training_config_sft.yaml (and training_config_apo.yaml, config.json, generation_config.json, chat_template.jinja)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Extracts (VERBATIM)


[training_config_sft.yaml, data and settings, Instruct]
# Directory settings
checkpoint_dir: "/polyglot/portuguese/checkpoints/models/Tucano2-qwen-3.7B-Instruct-SFT"
train_dataset_dir:
  # Total: ~874 million tokens (x5 epochs)
  # Coding: ~2.3 million tokens
  - /polyglot/portuguese/gigaverbo-v2-sft/code
  # Function Calling: ~17.5 million tokens
  - /polyglot/portuguese/gigaverbo-v2-sft/function_call
  # General Instruction Following: ~700 million tokens
  - /polyglot/portuguese/gigaverbo-v2-sft/general
  # Math and CoT: ~27 million tokens
  - /polyglot/portuguese/gigaverbo-v2-sft/math_cot
  # Retrieval Augmented Generation: ~2.2 million tokens
  - /polyglot/portuguese/gigaverbo-v2-sft/retrieval
  # Structured Outputs: ~35 million tokens
  - /polyglot/portuguese/gigaverbo-v2-sft/structured
  # Summarization: ~290 thousand tokens
  - /polyglot/portuguese/gigaverbo-v2-sft/summarization
  # Translation: ~5.7 million tokens
  - /polyglot/portuguese/gigaverbo-v2-sft/translation
  # Chosen Data from Preference Dataset: ~14 million tokens
  - /polyglot/portuguese/gigaverbo-v2-sft/dpo
val_dataset_dir: null
dataset_type: "jsonl"
cache_dir: "/lustre/mlnvme/data/polyglot/.cache"

# Data loading settings
pin_memory: true
num_workers_for_dataloader: 16
shuffle_dataset: true
mask_eos_token: false
mask_pad_token: true

# Training settings
total_batch_size: 524288
micro_batch_size: 4
gradient_accumulation_steps: 4
eval_micro_batch_size: null
num_train_epochs: 5
warmup_ratio: 0.1
max_learning_rate: 0.00005
min_learning_rate: 0.0
muon_learning_rate: null
weight_decay: 0.0
beta1: 0.9
beta2: 0.95
eps: 0.00000001
lr_decay_type: "cosine"
use_sqrt: false
lr_decay_iters_coef: 1.
seed: 42
max_steps: 68635
max_grad_norm: 1.0

# SFT settings
packing: false
assistant_only_loss: true

# Tokenizer and Reference model
tokenizer_name_or_path: "Polygl0t/Tucano2-qwen-3.7B-Base"
chat_template_path: null
reference_model: "Polygl0t/Tucano2-qwen-3.7B-Base"
continual_pretraining: true


[training_config_apo.yaml, data and settings, Instruct]
# Directory settings
checkpoint_dir: "/polyglot/portuguese/checkpoints/models/Tucano2-qwen-3.7B-Instruct"
train_dataset_dir:
  # Total: 28,437 samples (x5 epochs)
  # Harmfull samples (without reasoning): 4,267 samples
  - /polyglot/portuguese/gigaverbo-v2-dpo/harmfull-no-reasoning
  # Harmfull samples (with reasoning, stripped): 4,008 samples
  - /polyglot/portuguese/gigaverbo-v2-dpo/harmfull-reasoning-stripped
  # Harmless samples (without reasoning): 10,521 samples
  - /polyglot/portuguese/gigaverbo-v2-dpo/harmless-no-reasoning
  # Harmless samples (with reasoning, stripped): 9,641 samples
  - /polyglot/portuguese/gigaverbo-v2-dpo/harmless-reasoning-stripped
val_dataset_dir: null
dataset_type: "jsonl"
cache_dir: "/lustre/mlnvme/data/polyglot/.cache"

# APO settings
loss_type: "apo_zero"
dpo_beta: 0.5
precompute_ref_log_probs: true
truncation_mode: "keep_end"


[Think SFT and APO data directories] SFT: gigaverbo-v2-sft/reasoning (~34 million tokens, x5 epochs). APO: gigaverbo-v2-dpo/harmfull-reasoning (4,008 samples) and harmless-reasoning (9,641 samples), 13,649 samples x5 epochs.

[config.json, Instruct] architectures Qwen3ForCausalLM; hidden_size 2560; num_hidden_layers 36; num_attention_heads 32; num_key_value_heads 8; max_position_embeddings 4096; rope_theta 1000000; vocab_size 49152; tie_word_embeddings true; dtype bfloat16; bos_token_id 1; eos_token_id 2.

[generation_config.json, Instruct] do_sample true; max_new_tokens 1024; repetition_penalty 1.2; temperature 0.1.

[tokenizer_config.json] bos_token <|im_start|>; eos_token <|im_end|>; pad_token <|pad|>; model_max_length 4096.

[chat_template.jinja] ChatML-style: turns open with <|im_start|>role and close with <|im_end|>; a tools block renders function signatures in <tools></tools> in Portuguese and asks for <tool_call></tool_call> JSON; the Think template handles <think> and </think> reasoning content.
