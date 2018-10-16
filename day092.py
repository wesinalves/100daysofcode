import tensorflow as tf
converter = tf.contrib.lite.TocoConverter.from_saved_model(saved_model_dir)
converter.post_training_quantize = True
tflite_quantized_model = converter.convert()
open("quantized_model.tflite", "wb").write(tflite_quantized_model)
