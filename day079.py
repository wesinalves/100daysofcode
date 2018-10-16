# To serve with Docker
docker run -p 8501:8501 \
  --mount type=bind,source=/path/to/my_model/,target=/models/my_model \
  -e MODEL_NAME=my_model -t tensorflow/serving
calc
# to run in the container
tensorflow_model_server --port=8500 --rest_api_port=8501 \
--model_name=my_model --model_base_path=/models/my_model