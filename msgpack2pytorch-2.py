import msgpack
import msgpack_numpy as m
from transformers import GPTJConfig, FlaxGPTJModel 

m.patch()

def load_streaming_msgpack_file(file_path):
    data = {}
    with open(file_path, "rb") as f:
        unpacker = msgpack.Unpacker(f)
        for key, value in unpacker:
            data[tuple(key)] = value
    return data


def load_flax_model_from_train_state(config_file, train_state):
    config = GPTJConfig.from_json_file(config_file)
    flax_model = FlaxGPTJModel(config)
    flax_model.params = train_state["params"]
    return flax_model

msgpack_file = "/temp/streaming_params"
config_file = "/temp/config.json"

# Load the msgpack file
msgpack_data = load_streaming_msgpack_file(msgpack_file)

# Load the Flax model from the train state
flax_model = load_flax_model_from_train_state(config_file, msgpack_data)
