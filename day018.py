
# Convert the inputs to a Dataset.
# The array is sliced across the first dimension
dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

# shuffle method uses a buffer to shuffle the items as they pass through
# The repeat method restarts the Dataset when it reaches the end
# The batch method collects a number of examples and stacks them
dataset = dataset.shuffle(1000).repeat().batch(batch_size)

# Reading a csv file
# skip method to skip over first line of the file
dataset = tf.data.TextLineDataset(train_path).skip(1)
