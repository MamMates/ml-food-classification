FROM tensorflow/serving

ENV MODEL_NAME=food_clf
ENV MODEL_BASE_PATH=/models

COPY . /models/${MODEL_NAME}/1/

EXPOSE 8501

CMD tensorflow_model_server --model_name=${MODEL_NAME} --model_base_path=/${MODEL_BASE_PATH}/${MODEL_NAME} --rest_api_port=8501