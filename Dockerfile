FROM tensorflow/serving:2.14.0

ENV MODEL_NAME=food_clf
ENV MODEL_BASE_PATH=/models
ENV TF_CPP_VMODULE=http_server=1

COPY /model /models/${MODEL_NAME}/1/

CMD tensorflow_model_server --rest_api_port=8501 --model_name=${MODEL_NAME} --model_base_path=/${MODEL_BASE_PATH}/${MODEL_NAME}
