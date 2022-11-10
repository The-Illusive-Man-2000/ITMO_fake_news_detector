import logging.config
import pickle

import spacy
import tensorflow_hub as hub
import tensorflow_text
from flask import Flask

from app.config import Config


def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s in '%(module)s' at line %(lineno)d: %(message)s ")
    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    rotateHandler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1048576, backupCount=10)
    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(rotateHandler)
    l.addHandler(streamHandler)
    return l


my_model_svc = pickle.load(open(Config.MODEL, 'rb'))
# Загружаем модель из spacy.
nlp = spacy.load('ru_core_news_sm')
# Удаляем частице "не" из списка стоп-слов.
for w in Config.deselect_stop_words:
    nlp.vocab[w].is_stop = False

# # Загружаем модель USE
use = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3")

app = Flask(__name__)
