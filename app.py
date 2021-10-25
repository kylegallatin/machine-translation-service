import os
from flask import Flask, request, jsonify
from translate import Translator
from config import *
import cld3
import langid
import fasttext

app = Flask(__name__)
translator = Translator(MODEL_PATH)
model = fasttext.load_model('lid.176.bin')
langid.set_languages(['en', 'zh', 'hi', 'ko', 'de','fr','it', 'es'])

app.config["DEBUG"] = True # turn off in prod

@app.route('/', methods=["GET"])
def health_check():
    """Confirms service is running"""
    return "Machine translation service is up and running."

@app.route('/lang_routes', methods = ["GET"])
def get_lang_route():
    lang = request.args['lang']
    all_langs = translator.get_supported_langs()
    lang_routes = [l for l in all_langs if l[0] == lang]
    return jsonify({"output":lang_routes})

@app.route('/supported_languages', methods=["GET"])
def get_supported_languages():
    langs = translator.get_supported_langs()
    return jsonify({"output":langs})

@app.route('/translate', methods=["POST"])
def get_prediction():
    source = request.json['source']
    target = request.json['target']
    text = request.json['q']
    translation = translator.translate(source, target, text)
    return jsonify({"translatedText":translation[0]})

@app.route('/detect', methods=["POST"])
def detect_language():
    text = request.json['q']
    detection = langid.classify(text)
    #detection = model.predict(text, k=1)
    print(detection)
    return jsonify([{"language": detection[0]}])


if __name__ == '__main__':
    translator = Translator(MODEL_PATH)
    langid.set_languages(['en', 'zh', 'hi', 'ko', 'de','fr','it', 'es'])
    app.run(host="0.0.0.0", port=7000, debug=False)
