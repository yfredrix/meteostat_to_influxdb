# Weather to influxdb
This repository contains code to upload the knmi api via weerlive.nl to an influxdb
The weather source is:
    "KNMI Weergegevens via Weerlive.nl"

## Container

The docker container requires some environment variables to function;
| Environment Variable | Meaning |
| -------------------- | ------- |
| WEATHERAPIKEY  | An api key for weerlive.nl  |
| LOCATION  | Any dutch city as a string |
| INFLUXDBHOST  | The url and port where the influxdb is hosted  |
| INFLUXDBTOKEN  | The token with which write operations will occur  |
| INFLUXDBORGANISATION  | The organization name in which the user lives  |
| INFLUXDBBUCKET  | The bucket where the data needs to be written  |