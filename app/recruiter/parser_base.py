import json
from json import decoder


class ParserBase:
    def __init__(self):
        self.data = None

    def __call__(self, data):
        self._get_data_ready(data)

        try:
            self.data = json.loads(self.data)
        except decoder.JSONDecodeError:
            return None

        return self._parse_json()

    def _get_data_ready(self, msg: str):
        raise NotImplemented

    def _parse_json(self):
        raise NotImplemented
