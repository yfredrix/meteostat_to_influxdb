from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from typing import List, Dict


class InfluxClient:
    def __init__(
        self,
        url: str,
        token: str,
        org: str,
        bucket: str,
    ) -> None:
        self.org = org
        self.bucket = bucket
        self.client = InfluxDBClient(url=url, token=token, org=org)
        self.write_options = SYNCHRONOUS

    def write(self, data: Dict[str, str | List[str | float] | float]) -> None:
        with self.client.write_api(write_options=self.write_options) as write_api:
            write_api.write(self.bucket, self.org, data)
