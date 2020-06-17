import os
import argparse
import urllib
from urllib.request import urlretrieve
from config import *

parser = argparse.ArgumentParser()
parser.add_argument("--source", type=str, help="source language code")
parser.add_argument(
    "--target", type=str, help="sum the integers (default: find the max)"
)


def download_language_model(source, target):
    model = f"opus-mt-{source}-{target}"
    print(">>>Downloading data for %s to %s model..." % (source, target))
    os.makedirs(os.path.join("data", model))
    for f in FILENAMES:
        try:
            print(os.path.join(HUGGINGFACE_S3_BASE_URL, model, f))
            urlretrieve(
                "/".join([HUGGINGFACE_S3_BASE_URL, model, f]),
                os.path.join(MODEL_PATH, model, f),
            )
            print("Download complete!")
        except urllib.error.HTTPError:
            print("Error retrieving model from url. Please confirm model exists.")
            os.rmdir(os.path.join("data", model))
            break


if __name__ == "__main__":
    args = parser.parse_args()
    download_language_model(args.source, args.target)
