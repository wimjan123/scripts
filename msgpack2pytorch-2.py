import msgpack
import msgpack_numpy as m
from transformers import GPT2Config
from custom_functions import load_streaming_msgpack_file, load_flax_model_from_train_state

m.patch()

msgpack_file = "/temp/streaming_params"
config_file = "/temp/config.json"

# Load the msgpack file
msgpack_data = load_streaming_msgpack_file(msgpack_file)

# Load the Flax model from the train state
flax_model = load_flax_model_from_train_state(config_file, msgpack_data)
