# Machine Translation Service
Translation flask API for the Helsinki NLP models available in the [Huggingface Transformers library](https://huggingface.co/Helsinki-NLP). 

## Usage

First create the directory where you want to store models (and change `MODEL_PATH` in `config.py` accordingly). Then you can download models using the command line utility. For example...

```
mkdir data
python download_models.py --source en --target jap
```

To run with Python>=3.6:

```
pip install -r requirements.txt
python app.py
```

To run with docker:

```
docker build -t machine-translation-service .
docker run -p 5000:5000 -v /path/to/models:/app/data -it machine-translation-service
```

The front end should then become available at http://localhost:5000.

Call the service with curl:
```
curl --location --request POST 'http://localhost:5000/translate' \
--header 'Content-Type: application/json' \
--data-raw '{
 "text":"hello",
 "source":"en",
 "target":"fr"
}'
```
