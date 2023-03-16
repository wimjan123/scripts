import os
import msgpack
import jax.numpy as jnp
from flax import traverse_util
from flax.serialization import from_bytes, to_bytes

def load_streaming_msgpack_file(file_path):
    # Set max_buffer_size to a large value, e.g., 350 GB
    max_buffer_size = 350 * 1024 * 1024 * 1024
    unpacker = msgpack.Unpacker(raw=False, max_buffer_size=max_buffer_size)

    with open(file_path, "rb") as f:
        unpacker.feed(f.read())

    flattened_train_state = {}

    for key, value in unpacker:
        value = from_bytes(jnp.ndarray, value)  # Pass jnp.ndarray as the first argument
        flattened_train_state[key] = value

    train_state = traverse_util.unflatten_dict(flattened_train_state)
    return train_state

msgpack_file = "/temp/streaming_params"
train_state = load_streaming_msgpack_file(msgpack_file)
