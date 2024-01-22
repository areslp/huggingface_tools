from huggingface_hub import snapshot_download
from huggingface_hub import login

# ref : https://huggingface.co/docs/huggingface_hub/guides/download

# login, set enviroment variable HF_TOKEN
login()

local_dir = '.'
local_dir_use_symlinks = False
snapshot_download(repo_id="meta-llama/Llama-2-7b-chat-hf", resume_download=True, local_dir=local_dir, local_dir_use_symlinks=local_dir_use_symlinks)
