from datetime import datetime
from weather import WeatherAPI
from influxdb import InfluxClient
import os
import logging

location = os.getenv("LOCATION")

weatherAPI = WeatherAPI(os.getenv("WEATHERAPIKEY"))
influx = InfluxClient(
    os.getenv("INFLUXDBHOST"),
    os.getenv("INFLUXDBTOKEN"),
    os.getenv("INFLUXDBORGANISATION"),
    os.getenv("INFLUXDBBUCKET"),
)

weather = weatherAPI.get_weather(location)

if "request" in weather:
    logging.error("Request failed")


data_to_write = {
    "measurement": "weather",
    "tags": {"location": location},
    "fields": weather["liveweer"][0],
    "time": datetime.now(),
}
influx.write(influx.convert_to_point(data_to_write))
