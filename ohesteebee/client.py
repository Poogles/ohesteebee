"""Ohessteebee client."""
import requests
from typing import Dict

PutDict = Dict[str, str]

class Ohessteebee:

    def __init__(self, endpoint, port=4242):
        self.session = requests.Session()
        self.req_path = "http://{endpoint}:{port}".format(
            endpoint=endpoint, port=port)

    def _generate_put_dict(metric: str, timestamp: int, value: int, **kwargs) -> PutDict:
        if kwargs:
            tags = {**kwargs}
        else:
            tags = {}

        response = {
            "metric": metric,
            "timestamp": timestamp,
            "value": value,
            "tags": tags
        }

        return response

    def query(self, metric: str, start_date=None, end_date=None):
        """Get metric from OSTB."""
        path = "/api/query"
        api_url = self.req_path + path
        self.session.get(api_url)

    def put(self, metric: str, timestamp: int, **kwargs):
        """Put metric into OSTB."""
        path = "/api/put"
        api_url = self.req_path + path

        data = self._generate_put_dict()
        self.sesion.post(api_url)
