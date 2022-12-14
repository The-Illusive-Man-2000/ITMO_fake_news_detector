### ITMO_fake_news_detector
С появлением большого количества различных новостных ресурсов стал, как никогда актуальным вопрос выявления фейковых новостей.
Для автоматизации этого процесса попробуем разработать модель, которая по заголовкам новостей будет их классифицировать на фейк и не фейк.
***
__Папка data:__ 

my_test.tsv  $~~~~~~~~~~~~~~~~~~~~~~~$           _Результат разбиения части обучающих данных через train_test_split_   
my_train.tsv $~~~~~~~~~~~~~~~~~~~~~$          _Результат разбиения части обучающих данных через train_test_split_    
result_bert.tsv $~~~~~~~~~~~~~~~~~$       _Предсказание, сделанное bert на test.tsv_  
test.tsv $~~~~~~~~~~~~~~~~~~~~~~~~~~~~$             _Тестовый набор данных._  
train.tsv $~~~~~~~~~~~~~~~~~~~~~~~~~~~$            _Набор данных для обучения._  
valid_bert.tsv $~~~~~~~~~~~~~~~~~$       _Предсказание, сделанное bert на my_test.tsv_  

***
__Папка experiments:__  

experiments.ipynb.  $~~~~~~~~~$  _Ноутбук с экспериментами и сравнением моделей._

Таблица сравнения моделей. 

MODEL                                       | F1 score     | 
:-------------------------------------------|:------------:|
SVC(C=20, gamma=0.1) + USE                  |  0.870       | 
BERT (cointegrated/rubert-tiny)             |  0.863       | 
SVC(C=20, gamma=0.1) + TfIdf (с очисткой)   |  0.828       | 
SVC(C=20, gamma=0.1) + TfIdf (без очистки)  |  0.814       | 

***

__Папка model:__

label_mapper.json  $~~~~~~~~~$  _Метки классов._

https://drive.google.com/file/d/1DisM5e9Bj8OJogwZ0Ga8ZWav68tmdweQ/view?usp=share_link    $~~~~~~~~~$  _Ссылка на веса модели (дообученный bert)._

***

__Папка src:__

bertclf.py   $~~~~~~~~~~~~~~~~~~~~~~~~~~$  _Создание класса для модели (bert)._  
dataset.py   $~~~~~~~~~~~~~~~~~~~~~~~~$   _Токенизация и преобразование текста._  
processing_utils.py  $~~~~~~~~~$  _Разбиение данных на тренировочный и валидационный набор, создание маппинга лейблов в id._  
run_classification.py  $~~~~~~~$  _Загрузка дообученного модели (bert). Запуск классификации._  
run_train_tiny_bert.py  $~~~~$  _Дообучение предобученной модели cointegrated/rubert-tiny._  
train_utils.py  $~~~~~~~~~~~~~~~~~~~$   _Применение модели на тестовой выборке и рассчет метрик._  

***

__Папка inference:__

result_model_proba.pickle   $~~~~~~~~~~~~~~~$  _Сохранённая модель SVC. Обучалась с параметром probability=True чтобы выдавать вероятность._  
inference_use+svc.ipynb  $~~~~~~$  _Инференс. Загрузка USE, сохранённого SVC. Запуск проверки новостей с помощью USE и SVC. Можно вводить текст с клавиатуры. Время обработки одного заголовка около 0.09 секунды (запускалось на пк с процессором core i5-760 и 12 Гб оперативной памяти)._  

***

__Папка itmo_fake_news:__

Сервис на flask.
