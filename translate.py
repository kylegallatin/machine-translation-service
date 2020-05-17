from transformers import MarianTokenizer, MarianMTModel
import os
from typing import List

src = 'en'  # source language
trg = 'ja'  # target language
sample_text = "How are you?"
mname = f'Helsinki-NLP/opus-mt-{src}-{trg}'

class Translator():
    def __init__(self, models_dir):
        self.models = {}
        self.models_dir = models_dir

    def load_model(self, route):
        model = f'opus-mt-{route}'
        path = os.path.join(self.models_dir,model)
        try:
            model = MarianMTModel.from_pretrained(path)
            tok = MarianTokenizer.from_pretrained(path)
        except:
            print(f"Make sure you have download model for {source} -> {target} translation")
        self.models[route] = (model,tok)
        print(f"Successfully loaded model for {source} -> {target} transation")

    def translate(self, source, target, text):
        route = f'{source}-{target}'
        if not self.models.get(route):
            self.load_model(route)

        batch = self.models[route][1].prepare_translation_batch(src_texts=[text])
        gen = self.models[route][0].generate(**batch)
        words: List[str] = tok.batch_decode(gen, skip_special_tokens=True) 
        return words