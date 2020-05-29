from transformers import MarianTokenizer, MarianMTModel
import os
from typing import List

class Translator():
    def __init__(self, source, target, models_dir):
        self.source = source
        self.target = target
        self.models = {}
        self.models_dir = models_dir

    def get_supported_langs(self):
        routes = [x.split('-')[-2:] for x in os.listdir(self.models_dir)]
        return routes

    def load_model(self, route):
        model = f'opus-mt-{route}'
        path = os.path.join(self.models_dir,model)
        try:
            model = MarianMTModel.from_pretrained(path)
            tok = MarianTokenizer.from_pretrained(path)
        except:
            return 0,f"Make sure you have downloaded model for {route} translation"
        self.models[route] = (model,tok)
        return 1,f"Successfully loaded model for {route} transation"

    def translate(self, text):
        route = f'{self.source}-{self.target}'
        if not self.models.get(route):
            success_code, message = self.load_model(route)
            if not success_code:
                return message

        batch = self.models[route][1].prepare_translation_batch(src_texts=[text])
        gen = self.models[route][0].generate(**batch)
        words: List[str] = self.models[route][1].batch_decode(gen, skip_special_tokens=True) 
        return words