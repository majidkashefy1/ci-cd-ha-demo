from flask import Flask
from prometheus_client import start_http_server, Counter
import random

app = Flask(__name__)
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return f"Hello from Flask instance. ID: {random.randint(1000,9999)}"

if __name__ == '__main__':
    start_http_server(8000)  #
    app.run(host='0.0.0.0', port=5000)
