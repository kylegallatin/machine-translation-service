import os
from urllib.request import urlretrieve
from config import *

for model in MODELS:
    print(">>>Downloading data for % model..." % model)
    os.makedirs(os.path.join("data",model))
    for f in FILENAMES:
        print(os.path.join(HUGGINGFACE_S3_BASE_URL,model,f))
        urlretrieve(os.path.join(HUGGINGFACE_S3_BASE_URL,model,f),
                                    os.path.join(MODEL_PATH,model,f))
    print("Download complete!")