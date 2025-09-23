# Nemotron VLLM Project - NVIDIA-Nemotron-Nano-9B-v2 with Docker

This is a simple repository to launch the `nvidia/NVIDIA-Nemotron-Nano-9B-v2` model using vLLM and Docker. A GPU with VRAM greater than 24GB (e.g., NVIDIA RTX 3090) is recommended.

This repository provides a `nemo.sh` script to launch a vLLM OpenAI-compatible server for the `nvidia/NVIDIA-Nemotron-Nano-9B-v2` model.

## Requirements

*   **Docker:** Ensure Docker is installed and running on your system.
*   **NVIDIA Container Toolkit:** This is required for `--runtime=nvidia` and `--gpus all` to function correctly. Follow the official NVIDIA Docker documentation for installation.
*   **Nugging Face Token:** An environment variable `HF_TOKEN` must be set with your Hugging Face API token to access the model.
*   **CUDA_VISIBLE_DEVICES:** The `nemo.sh` script sets `CUDA_VISIBLE_DEVICES=0` to use the first GPU. Adjust if necessary.
*   **TP_SIZE:** The `nemo.sh` script sets `TP_SIZE=1` for tensor parallelism. Adjust if you have multiple GPUs and want to use tensor parallelism.

## NVIDIA Container Toolkit Installation

To enable GPU support for Docker containers, you need to install the NVIDIA Container Toolkit. The following steps are based on the procedure described in [Using Nvidia GPUs With Docker In 5 Minutes](https://dev.to/thenjdevopsguy/using-nvidia-gpus-with-docker-in-5-minutes-386g).

1.  **Install NVIDIA GPU Driver:**
    Ensure you have the correct NVIDIA GPU driver installed for your system. On Ubuntu, you can use the following package:
    ```bash
    sudo apt install nvidia-driver-535
    ```
    Once installed, use the package to install the automatic configuration for Nvidia drivers:
    ```bash
    sudo nvidia-auto-select
    ```
    You can verify the installation by running:
    ```bash
    nvidia-smi
    ```

2.  **Install Docker Engine:**
    Ensure Docker Engine (version 19.03 or later) is installed. Follow the official Docker documentation for installation if you haven't already.

3.  **Install NVIDIA Container Toolkit:**
    First, bring down the package:
    ```bash
    curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
        sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
        sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
    ```
    Next, add the package to the package manager:
    ```bash
    sudo apt-get update
    ```
    Install the toolkit:
    ```bash
    sudo apt-get install -y nvidia-container-toolkit
    ```
    Configure the NVIDIA Container Toolkit to work with the Docker engine:
    ```bash
    sudo nvidia-ctk runtime configure --runtime=docker
    ```
    Restart Docker:
    ```bash
    sudo systemctl restart docker
    ```
    You can test the installation by running a CUDA base image:
    ```bash
    docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
    ```
    You should see output similar to `nvidia-smi` specifying your Nvidia GPU.

## Environment Setup

To run the `client_test.py` script, you need to set up a Python environment and install the necessary dependencies.

1.  **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv .venv
    ```
2.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -U openai
    ```

## Usage

1.  **Set your Hugging Face Token:**
    ```bash
    export HF_TOKEN="your_hugging_face_token_here"
    ```
2.  **Make the script executable:**
    ```bash
    chmod +x nemo.sh
    ```
3.  **Run the vLLM server:**
    ```bash
    ./nemo.sh
    ```

The server will be accessible at `http://localhost:8000`.

## Testing the Client

Once the vLLM server is running, you can test it using the provided `client_test.py` script.

1.  **Ensure your virtual environment is activated** (see "Environment Setup" above).
2.  **Run the client test script:**
    ```bash
    python client_test.py
    ```
    This script will send a request to the vLLM server and print the response.