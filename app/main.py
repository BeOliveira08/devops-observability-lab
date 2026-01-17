from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest
import time
import random

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "Request latency"
)

@app.route("/")
@REQUEST_LATENCY.time()
def index():
    REQUEST_COUNT.labels("GET", "/", "200").inc()
    time.sleep(random.uniform(0.1, 0.5))
    return {"status": "ok"}

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}
