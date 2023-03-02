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
            'moderation': json.setdefault("moderation", False),
            'max_tokens': json.setdefault("max_tokens", MAX_TOKENS),
            "model": json.setdefault("model", GPT_MODEL)}

    if not prompt:
        return {"success": False, "result": "Error reading query"}, 400
    result = model_service.predict(prompt, args)
    return {"success": True, "result": result}, 200

@app.route('/api/v1/chat', methods=['POST'])
def chat():
    json = request.json
    messages = json.get("messages")
    chat_behavior = json.get("chat_behavior")
    args = {'messages': messages, 'chat_behavior': chat_behavior}

    if not messages:
        return {"success": False, "result": "Error reading query"}, 400
    result = model_service.chat(args)
    return {"success": True, "result": result}, 200

@app.route('/api/v1/transcribe', methods=['POST'])
def transcribe():
    json = request.json
    audio_path = json.get("audio_path")
    args = {'audio_path': audio_path}

    if not audio_path:
        return {"success": False, "result": "Error reading query"}, 400
    result = model_service.transcribe(args)
    return {"success": True, "result": result}, 200


@app.route('/api/v1/image', methods=['POST'])
def image():
    json = request.json
    prompt = json.get("prompt")
    args = {'n': json.setdefault("n", 1),
            'size': json.setdefault("size", '512x512')}

    if not prompt:
        return {"success": False, "result": "Error reading query"}, 400
    result = model_service.image(prompt, args)
    return {"success": True, "result": result}, 200
