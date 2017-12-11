from app.recruiter.parser_base import ParserBase


class ShortSummary:
    def __init__(self):
        self.device = None
        self.status_code = None
        self.ghs_current = None
        self.ghs_average = None
        self.fan_average = None
        self.temp_average = None
        self.pool = None
        self.user = None

    def json_able(self):
        return {
            "device": self.device.json_able(),
            "status_code": self.status_code,
            "ghs_current": self.ghs_current,
            "ghs_average": self.ghs_average,
            "fan_average": self.fan_average,
            "temp_average": self.temp_average,
            "pool": self.pool,
            "user": self.user
        }


class ShortSummaryParser(ParserBase):
    def __init__(self):
        super().__init__()
        self.summary = ShortSummary()

    def _parse_json(self):
        raw_summary = self.data["POOLS"][0]
        self.summary.status_code = self.data["STATUS"][0]["STATUS"]
        self.summary.ghs_current = raw_summary["GHS5s"]
        self.summary.ghs_average = raw_summary["GHSavg"]
        self.summary.fan_average = raw_summary["fan"]
        self.summary.temp_average = raw_summary["temp"]
        self.summary.pool = raw_summary["pool"]
        self.summary.user = raw_summary["user"]

        return self.summary

    def _get_data_ready(self, msg: str):
        idx = msg.find("[,")

        if idx == -1:
            raise RuntimeError("Couldn't find '[,' in the data.")

        self.data = msg[:idx+1] + msg[idx+2:]
