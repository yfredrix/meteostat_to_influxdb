FROM python:3.10-slim-bullseye

RUN pip install influxdb-client requests pytz

COPY crontab /etc/cron.d/crontab

WORKDIR /weather_app
COPY weatherApi_to_influx /weather_app

ENV WEATHERAPIKEY=demo
ENV LOCATION=Amsterdam
ENV INFLUXDBHOST=http://localhost:8550
ENV INFLUXDBORGANISATION=Default
ENV INFLUXDBBUCKET=Weather

RUN crontab /etc/cron.d/crontab
CMD ["cron", "-f"]
