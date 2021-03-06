import json
from json import decoder

from app.data.error import Error


class ParserBase:
    def __init__(self):
        self.data = None

    def __call__(self, data):
        if not isinstance(data, str) and data.get("error"):
            return self._handle_error(data)

        self._get_data_ready(data)

        try:
            self.data = json.loads(self.data)
        except decoder.JSONDecodeError:
            return type("CorruptedDataError", (Error,), {
                "json_able": lambda instance: {
                    "error": "Data is corrupted"
                }
            })()

        return self._parse_json()

    def _handle_error(self, error):
        raise NotImplemented

    def _get_data_ready(self, msg: str):
        raise NotImplemented

    def _parse_json(self):
        raise NotImplemented
