from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return f"Hello from Flask new :) instance!  ID: {random.randint(1000,9999)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
