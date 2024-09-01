import os

TOKEN = "ea19219nnska9921"
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
DATA_DIRECTORY = os.getcwd() + "/data"
DATA_IMAGE_DIRETORY = os.getcwd() + "/data/images"
BASE_URL = "https://dentalstall.com/shop"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"