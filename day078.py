signature_def: {
  key  : "my_classification_signature"
  value: {
    inputs: {
      key  : "inputs"
      value: {
        name: "tf_example:0"
        dtype: DT_STRING
        tensor_shape: ...
      }
    }
    outputs: {
      key  : "classes"
      value: {
        name: "index_to_string:0"
        dtype: DT_STRING
        tensor_shape: ...
      }
    }
    outputs: {
      key  : "scores"
      value: {
        name: "TopKV2:0"
        dtype: DT_FLOAT
        tensor_shape: ...
      }
    }
    method_name: "tensorflow/serving/classify"
  }
}