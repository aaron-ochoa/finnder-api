import json

from finnlib.yelp_service import YelpService


def lambda_handler(event, context):

        query_string = event["queryStringParameters"]

        lat = query_string['latitude']
        long = query_string['longitude']
        limit = query_string['limit']
        offset = query_string['offset']

        restaurants = YelpService().get_restaurants(lat, long, limit, offset)

        response = {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": { "Content-Type": "application/json" },
            "body": json.dumps(restaurants)
        }

        return response


if __name__ == '__main__':
    test_event = {
        "queryStringParameters": {
            "latitude": 33.648841,
            "longitude": -117.680715,
            "limit": 10,
            "offset": 0
        }
    }
    response = lambda_handler(test_event, None)
    print(response)
