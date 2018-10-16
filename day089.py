# The tf.data API provides a software pipelining mechanism through 
# the tf.data.Dataset.prefetch transformation
def input_fn():
  files = tf.data.Dataset.list_files("/path/to/dataset/train-*.tfrecord")
  dataset = files.interleave(tf.data.TFRecordDataset)
  dataset = dataset.shuffle(buffer_size=FLAGS.shuffle_buffer_size)
  dataset = dataset.map(map_func=parse_fn, num_parallel_calls=FLAGS.num_parallel_calls)
  dataset = dataset.batch(batch_size=FLAGS.batch_size)
  
  # the transformation uses a background thread and an internal buffer 
  # to prefetch elements from the input dataset ahead of the time they are requested
  dataset = dataset.prefetch(buffer_size=FLAGS.prefetch_buffer_size)
  return dataset