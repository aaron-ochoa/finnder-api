from flask import Flask
from flask import jsonify

app = Flask(__name__)

def respond(message, code, result=None):
    return jsonify({
        "message": message,
        "code": code,
        "result": result
    })

@app.route('/api/ping')
def ping():
    return respond("ping", 2000)


@app.route('/api/v1/restaurants')
def get_restaurants():
    restaurants = []
    return respond("Successful got restaurants", 2000, restaurants)
