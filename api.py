import json

from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
import request

from encoder import encode_text
from schema import Predict
from utils.logger import create_logger
from utils.constants import SENTIMENT_SERVER

app = FastAPI()

logger = create_logger()

@app.post('/sentiment/predict')
async def predict(body: Predict) -> Response:
    """Predict the sentiment of a given text on scale from 0 to 4."""

    body = json.loads(body.json())
    logger.info(f'Recieved request: {body}')
    payload = {"signature_name": "serving_default", "instances": encode_text(body['text'])}
    
    headers = {"content-type": "application/json"}
    json_response = requests.post(SENTIMENT_SERVER, data=payload, headers=headers)

    prediction = "Uncertain"
    _prediction = [round(i, 3) for i in softmax(json.loads(json_response.text)['predictions'][0])]
    logger.info(f'Prediction: {_prediction}')
    if max(_prediction) >= body['confidence_threshold']:
        prediction = np.argmax(_prediction)

    result = {'text': body['text'], 'sentiment': prediction}
    logger.info(f'Returned result: {result}')

    return JSONResponse(content=result)

