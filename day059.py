# standart Estimator
my_estimator = tf.estimator.Estimator(
  model_fn=my_model_fn)

# TPUEstimator running locally
my_tpu_estimator = tf.contrib.tpu.TPUEstimator(
    model_fn=my_model_fn,
    config=tf.contrib.tpu.RunConfig()
    use_tpu=False)