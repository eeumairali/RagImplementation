
# Conda Installation Guide

## Step 1: Download Conda
Visit the official [Anaconda website](https://www.anaconda.com/products/distribution#download-section) and download the installer for your operating system.

## Step 2: Install Conda
- **Windows**: Run the `.exe` installer and follow the prompts.
- **macOS/Linux**: Run the following commands in your terminal:
  ```bash
  bash ~/Downloads/Anaconda3-latest-Linux-x86_64.sh
  ```

## Step 3: Verify Installation
After installation, verify by typing:
```bash
conda --version
```

## Step 4: Create a New Environment
```bash
conda create -n RagEnv python=3.8
conda activate RagEnv
pip install farm-haystack[all] transformers
# implement code and adjust in django

```

You're all set!
