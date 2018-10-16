# to launch a cluster with two servers running on localhost:2222 and localhost:2223

# In task 0:
cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})

server = tf.train.Server(cluster, job_name="local", task_index=0)

# In task 1:
cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})

server = tf.train.Server(cluster, job_name="local", task_index=1)