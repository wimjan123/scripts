import os
import msgpack
import torch
from transformers import GPTJForCausalLM, GPTJConfig

def load_streaming_msgpack_file(file_path):
    data = {}
    with open(file_path, "rb") as f:
        unpacker = msgpack.Unpacker(f, max_buffer_size=280 * 1024**3)  # Increase buffer size to 280 GB
        for key, value in unpacker:
            data[tuple(key)] = value
    return data

def unflatten_dict(dictionary):
    unflattened = {}
    for key_tuple, value in dictionary.items():
        current_level = unflattened
        for key in key_tuple[:-1]:
            if key not in current_level:
                current_level[key] = {}
            current_level = current_level[key]
        current_level[key_tuple[-1]] = value
    return unflattened

def load_flax_model_from_train_state(config_file, train_state):
    config = GPTJConfig.from_json_file(config_file)
    flax_model = GPTJForCausalLM(config)
    flax_model.params = unflatten_dict(train_state)
    return flax_model

msgpack_file = "/temp/streaming_params"
msgpack_data = load_streaming_msgpack_file(msgpack_file)

config_file = "/temp/config.json"
flax_model = load_flax_model_from_train_state(config_file, msgpack_data)

# Convert the Flax model to a PyTorch model and save it
pytorch_model = GPTJForCausalLM.from_pretrained(flax_model, from_flax=True)
pytorch_model.save_pretrained("converted_pytorch_model")
