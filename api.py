from flask import Flask
from flask import jsonify
from yelp_service import YelpService
from flask import request

app = Flask(__name__)

yelp = YelpService()

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
    lat = request.args['latitude']
    long = request.args['longitude']
    limit = request.args['limit']
    offset = request.args['offset']
    restaurants = yelp.get_restaurants(lat, long, limit, offset)
    return respond("Successful got restaurants", 2000, restaurants)
