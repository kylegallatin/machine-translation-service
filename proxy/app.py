import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

app.config["DEBUG"] = True # turn off in prod

@app.route('/', methods=["GET"])
def health_check():
    """Confirms service is running"""
    return "Machine translation service is up and running."

@app.route('/lang_routes', methods = ["GET"])
def get_lang_route():
    lang = request.args['lang']
    all_langs = [x.split('-')[-2:] for x in os.listdir(os.environ.get("MODEL_PATH"))]
    lang_routes = [l for l in all_langs if l[0] == lang]
    return jsonify({"output":lang_routes})

@app.route('/supported_languages', methods=["GET"])
def get_supported_languages():
    langs = [x.split('-')[-2:] for x in os.listdir(os.environ.get("MODEL_PATH"))]
    return jsonify({"output":langs})

@app.route('/translate', methods=["POST"])
def get_prediction():
    source = request.json['source']
    target = request.json['target']
    text = request.json['text'].encode("utf-8")
    route = f'{source}_{target}'

    headers = {
    'Content-Type': 'application/json'
    }

    r = requests.post(f"http://machine-translation-service_{route}_1:5000/translate", headers = headers, data='{"text":'+text+'}')
    print(r.content)
    translation = str(r.content)
    return jsonify({"output":translation})

app.run(host="0.0.0.0")