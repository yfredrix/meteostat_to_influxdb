from typing import Dict, List
from datetime import datetime, date
from pytz import timezone

import requests


class WeatherAPI:
    url = "https://weerlive.nl/api/json-data-10min.php"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_weather(self, location: str) -> Dict[str, str]:
        params = {"key": self.api_key, "locatie": location}
        weather_response = requests.get(url=self.url, params=params)
        if weather_response.status_code in range(200, 230):
            return self.converted_weather(weather_response.json(), date.today())
        else:
            return {
                "request": "Failed",
                "status_code": weather_response.status_code,
                "body": weather_response.content,
            }

    def converted_weather(
        self, weather: Dict[str, List[Dict[str, str]]], current_day: date
    ) -> Dict[str, List[Dict[str, str | float]]]:
        conversion_level = weather["liveweer"][0]
        for item in conversion_level:
            if ":" in conversion_level[item]:
                hour, minute = conversion_level[item].split(":")
                conversion_level[item] = (
                    timezone("Europe/Amsterdam")
                    .localize(
                        datetime(
                            current_day.year,
                            current_day.month,
                            current_day.day,
                            int(hour),
                            int(minute),
                        )
                    )
                    .isoformat()
                )
            try:
                conversion_level[item] = float(conversion_level[item])
            except ValueError:
                conversion_level[item] = conversion_level[item]
        return weather
