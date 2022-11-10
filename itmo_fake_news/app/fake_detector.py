import re

import tensorflow as tf

from app import Config
from app import my_model_svc
from app import nlp
from app import use


# Функция для удаления пунктуации и чисел.
def text_process(text):
    text = text.lower()
    # удаляем пунктуацию
    text = re.sub(r'[^\w0-9\s]', '', text)
    # удаляем числа
    text = re.sub(r'\d+', '', text)

    return text


# Процедура удаления стоп-слов.
def remove_stop_words(text):
    # токенизация текста
    doc = nlp(text)

    clean_text = []

    for token in doc:
        if not token.is_stop:
            clean_text.append(token.text)
    return ' '.join(clean_text)


# Функция предобработки текста
def preprocessing(text):
    text_preprocessing = remove_stop_words(text_process(text))
    return text_preprocessing


# Функция для предсказания является заголовок новости фейком или нет.
def predict_fake(news):
    model = my_model_svc
    processed = preprocessing(news)
    embedding = use(processed)
    embedding = tf.reshape(embedding, (1, -1)).numpy()
    proba = round(model.predict_proba(embedding)[0][1], 4)
    return True if proba >= Config.threshold else False
