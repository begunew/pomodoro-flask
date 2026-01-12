from flask import Flask
from datetime import datetime
from flask_cors import CORS, cross_origin

import redis
r = redis.Redis(host='localhost', port=6379, db=0)


app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.

time_now = ""

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/latest")
def latest():
    response = {
        "message": "Pomodoro finished!",
        "time": time_now
    }
    return response

@app.route("/notify", methods=["POST"])
def notify():
    global time_now
    time_now = datetime.now().strftime("%H:%M:%S")
    return "pomodoro completed!"



