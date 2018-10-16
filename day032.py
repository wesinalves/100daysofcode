model = MyModel()
optimizer = tf.train.AdamOptimizer(learning_rate=0.001)
checkpoint_dir = '/path/to/model_dir'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")

# record state model, optimizer and global step
root = tfe.Checkpoint(optimizer=optimizer,
                      model=model,
                      optimizer_step=tf.train.get_or_create_global_step())

# to save a checkpoint
root.save(file_prefix=checkpoint_prefix)
# to load a checkpoint
root.restore(tf.train.latest_checkpoint(checkpoint_dir))