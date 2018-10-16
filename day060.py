import tempfile
import subprocess

class FLAGS(object):
  use_tpu=False
  tpu_name=None
  # Use a local temporary path for the `model_dir`
  model_dir = tempfile.mkdtemp()
  # Number of training steps to run on the Cloud TPU before returning control.
  iterations = 50
  # A single Cloud TPU has 8 shards.
  num_shards = 8

if FLAGS.use_tpu:
    my_project_name = subprocess.check_output([
        'gcloud','config','get-value','project'])
    my_zone = subprocess.check_output([
        'gcloud','config','get-value','compute/zone'])
    cluster_resolver = tf.contrib.cluster_resolver.TPUClusterResolver(
            tpu_names=[FLAGS.tpu_name],
            zone=my_zone,
            project=my_project)
    master = tpu_cluster_resolver.get_master()
else:
    master = ''

my_tpu_run_config = tf.contrib.tpu.RunConfig(
    master=master,
    evaluation_master=master,
    model_dir=FLAGS.model_dir,
    session_config=tf.ConfigProto(
        allow_soft_placement=True, log_device_placement=True),
    tpu_config=tf.contrib.tpu.TPUConfig(FLAGS.iterations,
                                        FLAGS.num_shards),
)

# Then you must pass the tf.contrib.tpu.RunConfig to the constructor:

my_tpu_estimator = tf.contrib.tpu.TPUEstimator(
    model_fn=my_model_fn,
    config = my_tpu_run_config,
    use_tpu=FLAGS.use_tpu)