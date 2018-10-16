# x: an input tensor with the dimensions (N_examples, 784), 
# where 784 is the  number of pixels in a image.
# grayscale -- it would be 3 for an RGB image.
# NHWC or channels_last
with tf.name_scope('reshape'):
  x_image = tf.reshape(x, [-1, 28, 28, 1])


# NHWC or channels_last
with tf.name_scope('reshape'):
  x_image = tf.reshape(x, [-1, 1, 28, 28])