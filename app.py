from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS, cross_origin

import redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.

@app.route("/latest")
def latest():
    notification = r.get("latest_notification")

    print(notification)

    # deletes the key from the db
    r.delete("latest_notification")

    response = {
        "message": "Pomodoro finished!",
        "time": notification,
        "status":"ok"
    }

    if notification is None:
        return {"new": False}
    else:
        return response

@app.route("/notify", methods=["POST"])
def notify():
    time_now = datetime.now().strftime("%H:%M:%S")

    r.set("latest_notification", time_now)
    return {"status": "ok"}



