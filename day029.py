def loss(model, x, y):
  prediction = model(x)
  return tf.losses.sparse_softmax_cross_entropy(labels=y, logits=prediction)
def grad(model, inputs, targets):
  with tf.GradientTape() as tape:
    loss_value = loss(model, inputs, targets)
  return tape.gradient(loss_value, model.variables)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
x, y = iter(dataset_train).next()
print("Initial loss: {:.3f}".format(loss(model, x, y)))
# Training loop
for (i, (x, y)) in enumerate(dataset_train):
  # Calculate derivatives of the input function with respect to its parameters.
  grads = grad(model, x, y)
  # Apply the gradient to the model
  optimizer.apply_gradients(zip(grads, model.variables),
                            global_step=tf.train.get_or_create_global_step())
  if i % 200 == 0:
    print("Loss at step {:04d}: {:.3f}".format(i, loss(model, x, y)))
print("Final loss: {:.3f}".format(loss(model, x, y)))