x = tf.zeros(tf.constant([1,2,3])+1)

print(x.shape)
# TensorShape([Dimension(None), Dimension(None), Dimension(None)])

x.set_shape([2,3,4])

# In many cases the batch size is the only unknown dimension

params = {'batch_size':32}

ds = tf.data.Dataset.from_tensors([0, 1, 2])

ds = ds.repeat().batch(params['batch-size'])

print(ds)
#BatchDataset shapes: (?, 3), types: tf.int32>

# The most straightforward fix is to apply tf.contrib.data.batch_and_drop_remainder

params = {'batch_size':32}

ds = tf.data.Dataset.from_tensors([0, 1, 2])

ds = ds.repeat().apply(tf.contrib.data.batch_and_drop_remainder(params['batch-size']))

print(ds)
# <_RestructuredDataset shapes: (32, 3), types: tf.int32>