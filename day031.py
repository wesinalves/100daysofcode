# In eager execution, variables are objects.

with tf.device("gpu:0"):

  v = tfe.Variable(tf.random_normal([1000, 1000]))

  v = None  # v no longer takes up GPU memory