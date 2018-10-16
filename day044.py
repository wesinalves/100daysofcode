# model.evaluate returns the loss value & metrics values 
# for the model in test mode.
# Computation is done in batches.
mse = model.evaluate(input_test, output_test,batch_size=32)
print('Test mse:', mse)

# model.predict generates output predictions for the input samples.
# Computation is done in batches. If unspecified, it will default to 32.
target = model.predict(input_test)