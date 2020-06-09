# Machine Translation Service
Translation flask API for the Helenski NLP models available in the [Huggingface Transformers library](https://huggingface.co/Helsinki-NLP). 

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

First build the `translation_base` image locally.
```
cd
docker build -t translation_base
```
Then run the service using docker-compose:
```
docker-compose up
```

The API should then become available at http://localhost:5000.