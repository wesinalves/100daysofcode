import tensorflow as tf
# setting eager execution
tf.enable_eager_execution()
x = [[2.]]
m = tf.matmul(x, x)
print("hello, {}".format(m))  # => "hello, [[4.]]"