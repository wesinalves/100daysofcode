# Serialize a model to JSON format
json_string = model.to_json()

# Recreate the model (freshly initialized)
fresh_model = keras.models.from_json(json_string)

# Serializes a model to YAML format
yaml_string = model.to_yaml()

# Recreate the model
fresh_model = keras.models.from_yaml(yaml_string)