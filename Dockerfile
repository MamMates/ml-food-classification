FROM tensorflow/serving:2.14.0

ENV MODEL_NAME=food_clf
ENV TF_CPP_VMODULE=http_server=1

COPY /model /models/${MODEL_NAME}/1/

CMD ["tensorflow_model_server", "--rest_api_port=8501", "--model_name=food_clf", "--model_base_path=/models/food_clf"]
