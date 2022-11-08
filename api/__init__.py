# -*- encoding: utf-8 -*-

from flask import Flask, request
from flask_cors import CORS
from api.model_service import ModelService
from api.config import GPT_MODEL, TEMPERATURE, MAX_TOKENS

model_service = ModelService()

# Create App
app = Flask(__name__)

# Enable CORS
CORS(app)


@app.route('/', methods=['GET'])
def hello():
    return {
        'success': True,
        'params': {
            'temperature': TEMPERATURE,
            'max_tokens': MAX_TOKENS,
            'model': GPT_MODEL
        }
    }


@app.route('/api/v1/predict', methods=['POST'])
def predict():
    json = request.json
    prompt = json.get("prompt")
    args = {'temperature': json.setdefault("temperature", TEMPERATURE),
            'max_tokens': json.setdefault("max_tokens", MAX_TOKENS),
            "model": json.setdefault("model", GPT_MODEL)}

    if not prompt:
        return {"success": False, "result": "Error reading query"}, 400
    result = model_service.predict(prompt, args)
    return {"success": True, "result": result}, 200
