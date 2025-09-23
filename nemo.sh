export CUDA_VISIBLE_DEVICES=0
export TP_SIZE=1

docker run --runtime=nvidia --gpus all --ulimit memlock=-1 --ulimit stack=-1 \
           -v ~/.cache/huggingface:/root/.cache/huggingface \
           --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \
           --env "CUDA_VISIBLE_DEVICES=0" \
           -p 8000:8000 \
           --ipc=host \
           --name vllm-nemotron \
           vllm/vllm-openai:v0.10.1 \
           --model nvidia/NVIDIA-Nemotron-Nano-9B-v2 \
           --tensor-parallel-size ${TP_SIZE} \
           --max-num-seqs 16 \
           --max-model-len 128000 \
           --trust-remote-code
