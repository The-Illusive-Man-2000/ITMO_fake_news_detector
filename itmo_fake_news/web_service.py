from flask import jsonify


from app import Config
from app import app
from app.fake_detector import predict_fake
from app import setup_logger

log_web = setup_logger(logger_name='tm_nalog3_api', log_file=Config.LOG_FILE, level=Config.LOG_LEVEL)
log_web.info('Starting tm_nalog3_api web-service')


@app.route('/fakeNews/v1/detect/<title>', methods=["GET"])
def make_detection(title):
    try:
        result, proba = predict_fake(title)
        resp_json = {'code': 200,
                     'message': '',
                     'data': {'if_fake': result, 'fake_proba': proba}}
    except Exception as exc:
        log_web.error(exc, exc_info=True)
        resp_json = {'code': 500,
                     'message': 'Ошибка детекции, обратитесь к адинимтратору системы',
                     'data': {'if_fake': None, 'fake_proba': None}}
    return jsonify(resp_json)


if __name__ == '__main__':
    app.run(port=Config.PORT_IN, host=Config.HOST_IN, debug=Config.FLASK_DEBUG, threaded=True)
