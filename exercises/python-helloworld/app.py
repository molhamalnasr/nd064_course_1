from flask import Flask
from flask import json
from datetime import datetime

import logging

app = Flask(__name__)


@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json"
    )

    app.logger.info(datetime.now().__str__() + ", Status endpoint was reached")
    return response


@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype="application/json"
    )

    app.logger.info(datetime.now().__str__() + ", Metrics endpoint was reached")
    return response


@app.route("/")
def hello():
    app.logger.info(datetime.now().__str__() + ", Main endpoint was reached")
    return "Hello World!<br>this is Molham"


if __name__ == "__main__":
    logging.basicConfig(filename="app.log", level=logging.DEBUG)

    app.run(host='0.0.0.0')
