from flask import Blueprint
from prometheus_client import Counter, Histogram, generate_latest
import time
import random
import json
import logging

main = Blueprint("main", __name__)

logging.basicConfig(level=logging.INFO)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "Request latency"
)

@main.route("/")
@REQUEST_LATENCY.time()
def index():
    REQUEST_COUNT.labels("GET", "/", "200").inc()

    log = {
        "event": "health_check",
        "status": "ok"
    }
    logging.info(json.dumps(log))

    time.sleep(random.uniform(0.1, 0.4))
    return {"status": "ok"}

@main.route("/error")
def error():
    REQUEST_COUNT.labels("GET", "/error", "500").inc()
    return {"error": "simulated error"}, 500

@main.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}
