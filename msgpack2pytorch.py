import torch
from transformers import FlaxGPTJModel, GPTJModel

# Load the Flax model
flax_model = FlaxGPTJModel.from_pretrained("/temp/flax-weights.msgpack")

# Convert Flax model to PyTorch model
pytorch_model = GPTJModel.from_pretrained("/temp/flax-weights.msgpack", from_flax=True)

# Save the PyTorch model as a binary file
pytorch_model.save_pretrained("/temp/pytorch-weights.bin")
