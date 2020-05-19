import os
from flask import Flask, request, jsonify, send_from_directory
from translate import Translator
from config import *

app = Flask(__name__)
translator = Translator(MODEL_PATH)

