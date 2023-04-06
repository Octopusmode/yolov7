import torch

torch.cuda.empty_cache()

torch.cuda.memory_summary(device=0, abbreviated=False)