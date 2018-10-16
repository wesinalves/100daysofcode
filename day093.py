# Config to turn on JIT compilation
config = tf.ConfigProto()
# JIT compilation is turned on
# in order to run TensorFlow computations via XLA
config.graph_options.optimizer_options.global_jit_level = tf.OptimizerOptions.ON_1
sess = tf.Session(config=config)