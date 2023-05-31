import json
import time
from flask import Flask, jsonify


def application(environ, start_response):
    status = "200 OK"
    response_headers = [("Content-type", "application/json")]
    response = {}

    req_uri = environ["REQUEST_URI"].strip("/").split("/")
    if len(req_uri) == 2 and req_uri[0] == "hello":
        response["message"] = f"Hello, {req_uri[1]}!"
    elif len(req_uri) == 1 and req_uri[0] == "hello":
        response["message"] = "Hello, world!"
    else:
        status = "404 Not Found"
        response["error 404"] = "Page not found"

    response = json.dumps(response).encode("UTF-8")
    start_response(status, response_headers)
    return [response]


application = Flask(__name__)


@application.route("/long_task")
def long_task():
    time.sleep(120)
    return jsonify(message="We did it!")
