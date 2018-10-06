#service
import requests
from os import environ as env

class YelpService:

    url = "https://api.yelp.com/v3"

    def __init__(self):
        self.client_id = env.get("YELP_CLIENT_ID")
        self.secret = env.get("YELP_SECRET")

    def get_restaurants(self, lat, long, limit, offset):
        querystring = {
            "latitude":lat,
            "longitude":long,
            "categories":"restaurants",
            "limit": limit,
            "offset": offset
        }


        response = requests.request("GET", "{}/businesses/search".format(self.url), headers=self._get_headers(), params=querystring)
        print(response.json())
        restaurants = response.json()["businesses"]
        results = []

        for restaurant in restaurants:
            details = self._get_restaurant_details(restaurant["id"])
            restaurant["photos"] = details["photos"]
            results.append(restaurant)

        return results

    def _get_restaurant_details(self, id):

        response = requests.request("GET", "{}/businesses/{}".format(self.url, id), headers=self._get_headers())

        return response.json()

    def _get_headers(self):

        return {
            'Authorization': "Bearer {}".format(self.secret)
        }
