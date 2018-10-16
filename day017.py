# Configuring checkpoint
my_checkpointing_config = tf.estimator.RunConfig(
    save_checkpoints_secs = 15*60,  # Save checkpoints every 15 minutes.
    keep_checkpoint_max = 10,       # Retain the 10 most recent checkpoints.
)

# Taking DNNClassifier as axample
# sets the model_dir argument to the models/iris directory:
classifier = tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    hidden_units=[10, 10],
    n_classes=3,
    model_dir='models/iris')

# the first call to train adds checkpoints 
# and other files to the model_dir directory
classifier.train(
        input_fn=lambda:train_input_fn(train_x, train_y, batch_size=100),
                steps=200)