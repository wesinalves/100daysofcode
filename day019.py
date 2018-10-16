# Define feature columns
categorical_column_a = categorical_column_with_hash_bucket(...)
categorical_column_b = categorical_column_with_hash_bucket(...)

categorical_feature_a_x_categorical_feature_b = crossed_column(...)

# Estimator using the default optimizer.
estimator = LinearClassifier(
    feature_columns=[categorical_column_a,
                     categorical_feature_a_x_categorical_feature_b])

# Or estimator using the FTRL optimizer with regularization.
estimator = LinearClassifier(
    feature_columns=[categorical_column_a,
                     categorical_feature_a_x_categorical_feature_b],
    optimizer=tf.train.FtrlOptimizer(
      learning_rate=0.1,
      l1_regularization_strength=0.001
    ))

# Or estimator with warm-starting from a previous checkpoint.
estimator = LinearClassifier(
    feature_columns=[categorical_column_a,
                     categorical_feature_a_x_categorical_feature_b],
    warm_start_from="/path/to/checkpoint/dir")

# Remenber we need to create input functions that returns x, y 
#(where y represents label's class index).
def input_fn_train: 
  ...
def input_fn_eval:
  ... 


# Main methods of estimators
estimator.train(input_fn=input_fn_train)
estimator.evaluate(input_fn=input_fn_eval)
estimator.predict(input_fn=input_fn_predict)