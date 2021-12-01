# Machine Translation Service
Translation flask API for the Helsinki NLP models available in the [Huggingface Transformers library](https://huggingface.co/Helsinki-NLP). 

## Usage

You can download language models using the command line utility. For example...

```
cd machine-translation-service
mkdir data
python download_models.py --source en --target fr
```

To run with Python>=3.6:

```
pip install -r requirements.txt
python app.py
```

To run with docker:

```
docker build -t machine-translation-service .
docker run -p 5000:5000 -v $(pwd)/data:/app/data -it machine-translation-service
```

The front end should then become available at http://localhost:5000.

Call the service with curl:
```
curl --location --request POST 'http://localhost:5000/translate' \
--header 'Content-Type: application/json' \
-d '{
 "text":"hello",
 "source":"en",
 "target":"fr"
}'
```
