from flask import Blueprint, jsonify


routes = Blueprint("routes", __name__)


@routes.route("/")
def health():
    return jsonify({"status": "ok"})


@routes.route("/metrics")
def metrics():
    return jsonify({"message": "metrics endpoint"})


@routes.route("/error")
def error():
    raise Exception("Simulated internal server error")
