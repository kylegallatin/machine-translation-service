from transformers import MarianTokenizer, MarianMTModel
import os
from typing import List
src = 'en'  # source language
trg = 'ja'  # target language
sample_text = "How are you?"
mname = f'Helsinki-NLP/opus-mt-{src}-{trg}'

model = MarianMTModel.from_pretrained("/Users/gallak12/machine-translation-service/data/opus-mt-en-jap")
tok = MarianTokenizer.from_pretrained("/Users/gallak12/machine-translation-service/data/opus-mt-en-jap")
batch = tok.prepare_translation_batch(src_texts=[sample_text])  # don't need tgt_text for inference
gen = model.generate(**batch)  # for forward pass: model(**batch)
words: List[str] = tok.batch_decode(gen, skip_special_tokens=True)  # returns "Where is the the bus stop ?"
print(words)