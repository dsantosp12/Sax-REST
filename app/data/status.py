from app.data.error import Error
from app.recruiter.parser_base import ParserBase


class Status:
    def __init__(self):
        self.device = None
        self.time_elapsed = None
        self.status_code = None
        self.ghs_current = None
        self.ghs_average = None
        self.frequency = None
        self.fans = []
        self.temps = []
        self.temp_average = None
        self.temp_max = None
        self.chain_acn = []
        self.chain_acs = []

    def json_able(self):
        return {
            "device": self.device.json_able(),
            "time_elapsed": self.time_elapsed,
            "status_code": self.status_code,
            "ghs_current": self.ghs_current,
            "ghs_average": self.ghs_average,
            "frequency": self.frequency,
            "fans": self.fans,
            "temps": self.temps,
            "temp_average": self.temp_average,
            "temp_max": self.temp_max,
            "chain_acn": self.chain_acn,
            "chain_acs": self.chain_acs
        }


class StatusParser(ParserBase):
    def __init__(self):
        super().__init__()
        self.status = Status()

    def _get_data_ready(self, msg: str):
        idx = msg.find("}{")
        msg = msg[:-1]
        if idx == -1:
            raise RuntimeError("Couldn't find '}{' in the data.")

        self.data = msg[:idx + 1] + "," + msg[idx + 1:]

    def _parse_json(self):
        stats = self.data["STATS"][1]

        # Summary
        self.status.status_code = self.data["STATUS"][0]["STATUS"]
        self.status.time_elapsed = stats["Elapsed"]

        # GHS
        self.status.ghs_current = stats["GHS 5s"]
        self.status.ghs_average = stats["GHS av"]

        # Frequency
        self.status.frequency = stats["frequency"]

        # Fans
        self.status.fans.append(stats["fan1"])
        self.status.fans.append(stats["fan2"])
        self.status.fans.append(stats["fan3"])

        # Temperature
        self.status.temps.append(stats["temp1"])
        self.status.temps.append(stats["temp2"])
        self.status.temps.append(stats["temp3"])
        self.status.temp_average = stats["temp_avg"]
        self.status.temp_max = stats["temp_max"]

        # Chain
        self.status.chain_acn.append(stats["chain_acn1"])
        self.status.chain_acn.append(stats["chain_acn2"])
        self.status.chain_acn.append(stats["chain_acn3"])

        self.status.chain_acs.append(stats["chain_acs1"])
        self.status.chain_acs.append(stats["chain_acs2"])
        self.status.chain_acs.append(stats["chain_acs3"])

        return self.status

    def _handle_error(self, error):
        return type("StatusError", (Error, ), {
            "json_able": lambda cls: {
                "error": str(error.get("error")),
                "device": error.get("device").json_able()
            }
        })()
