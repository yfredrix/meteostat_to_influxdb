from typing import Dict

import requests


class WeatherAPI:
    url = "https://weerlive.nl/api/json-data-10min.php"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_weather(self, location: str) -> Dict[str, str]:
        params = {"key": self.api_key, "locatie": location}
        weather_response = requests.get(url=self.url, params=params)
        if weather_response.status_code in range(200, 230):
            return weather_response.json()
        else:
            return {
                "request": "Failed",
                "status_code": weather_response.status_code,
                "body": weather_response.content,
            }
