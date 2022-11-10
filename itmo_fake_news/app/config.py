from pathlib import Path


class Config:
    PORT_IN = 8080
    HOST_IN = '0.0.0.0'
    BASE_DIR = Path.cwd()
    LOG_FILE = BASE_DIR.joinpath("logs", f"{BASE_DIR.parts[-1]}.log")
    LOG_DIR = BASE_DIR.joinpath("logs")
    LOG_LEVEL = 'INFO'
    FLASK_DEBUG = True
    MODEL = BASE_DIR.joinpath('app', 'models', 'result_model_proba.pickle')

    deselect_stop_words = ['не']
    threshold = 0.7
