# To test your setup
from tensorflow.python.lib.io import file_io

print file_io.stat('s3://bucketname/path/')

# <tensorflow.python.pywrap_tensorflow_internal.FileStatistics; 
# proxy of <Swig Object of type 'tensorflow::FileStatistics *' 
# at 0x10c2171b0> >

# Reading Data
filenames = ["s3://bucketname/path/to/file1.tfrecord",
             "s3://bucketname/path/to/file2.tfrecord"]

dataset = tf.data.TFRecordDataset(filenames)