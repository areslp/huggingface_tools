from huggingface_hub import snapshot_download
from huggingface_hub import login

snapshot_download(repo_id="meta-llama/Llama-2-7b-chat-hf", resume_download=True)
