from transformers import GPTJConfig, FlaxGPTJModel

def load_flax_model_from_train_state(config_file, train_state):
    # Load the model config
    config = GPTJConfig.from_json_file(config_file)
    
    # Create the Flax model
    flax_model = FlaxGPTJModel(config)
    
    # Set the Flax model weights from the train state
    flax_model.params = train_state.params

    return flax_model

config_file = "/temp/config.json"
flax_model = load_flax_model_from_train_state(config_file, train_state)
