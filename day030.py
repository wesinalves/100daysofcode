class Model(tf.keras.Model):
  def __init__(self):
    super(Model, self).__init__()
    self.W = tfe.Variable(5., name='weight')
    self.B = tfe.Variable(10., name='bias')
  def call(self, inputs):
    return inputs * self.W + self.B
# The loss function to be optimized
def loss(model, inputs, targets):
  error = model(inputs) - targets
  return tf.reduce_mean(tf.square(error))
def grad(model, inputs, targets):
  with tf.GradientTape() as tape:
    loss_value = loss(model, inputs, targets)
  return tape.gradient(loss_value, [model.W, model.B])