from flask import Flask
from flask import json

app = Flask(__name__)


@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route("/metrics")
def metrics():
    return "data: {UserCount: 140, UserCountActive: 23}"


@app.route("/")
def hello():
    return "Hello World!<br>this is Molham"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
