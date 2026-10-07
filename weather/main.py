from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route("/")
def health():
    return "The service is running", 200


@app.route("/<city>")
def weather(city):
    countries = {
        "toronto": "Canada",
        "lagos": "Nigeria",
        "douala": "Cameroon",
        "london": "United Kingdom",
        "paris": "France",
        "new york": "United States",
        "accra": "Ghana",
    }

    city_key = city.lower()
    country = countries.get(city_key, "Unknown")

    fake_weather = {
        "location": {
            "name": city.title(),
            "country": country,
        },
        "current": {
            "temp_c": 8,
            "temp_f": 46.4,
            "feelslike_c": 5,
            "feelslike_f": 41,
            "condition": {
                "text": "Cloudy",
                "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
            },
        },
    }

    return jsonify(json.dumps(fake_weather))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
