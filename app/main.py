from fastapi import FastAPI, UploadFile
from .default_response import Response
from dotenv import load_dotenv
import numpy as np
import httpx
import json
import cv2
import os


load_dotenv()
app = FastAPI()


@app.get("/")
async def root() -> Response:
    return Response.DefaultOK(data={"message": "Hello World"})


@app.post("/predict")
async def predict(file: UploadFile) -> Response:
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except BaseException:
        return Response.DefaultBadRequest()
    finally:
        file.file.close()

    try:
        image = cv2.imdecode(np.frombuffer(
            contents, np.uint8), cv2.IMREAD_COLOR)
        image = cv2.resize(image, (150, 150))
        image = image / 255.0
    except BaseException:
        return Response.DefaultBadRequest()

    input_data = json.dumps(
        {
            "instances": [image.tolist()]
        }
    )

    url = os.getenv("MODEL_ENDPOINT")

    response = httpx.post(url, data=input_data, headers={
        "content-type": "application/json"})

    predictions = json.loads(response.text)

    int_to_label = {0: 'bika_ambon', 1: 'dadar_gulung', 2: 'donat', 3: 'kue_cubit', 4: 'kue_klepon',
                    5: 'kue_lapis', 6: 'kue_lumpur', 7: 'kue_risoles', 8: 'putu_ayu', 9: 'roti'}

    pred_idx = np.argmax(predictions['predictions'][0])
    result = int_to_label[pred_idx]

    data = {
        "name": result,
        "rating": 5,
        "price": 10000
    }

    return Response.DefaultOK(
        data=data
    )
