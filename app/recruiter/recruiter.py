import socket
import json

import config
from app.data.device_registry import DeviceRegistry, Device
from app.data.status import Status, StatusParser
from app.data.short_summary import ShortSummary, ShortSummaryParser
from app.data.notify import Notification, NotificationParser
from app.data.configuration import Configuration


CONNECTION_TIMEOUT = 0.5  # 500 ms

SAX_VERSION_KEY = "version"
SAX_STATUS_KEY = "stats"
SAX_SUMMARY_KEY = "summary"
SAX_CONFIGURATION_KEY = "config"
SAX_SHORT_KEY = "lcd"
SAX_PROBLEM_HISTORY_KEY = "notify"
SAX_POOL_LIST_KEY = "pools"
SAX_DEVICES_KEY = "devs"


class Recruiter:
    def __init__(self):
        self.socket = None

    def get_device_status(self, device_id) -> Status:
        # Get list of status and filter the for the device requested
        return next(filter(lambda status: status.device.id == device_id,
                           self.get_devices_status()))

    def get_devices_status(self) -> [Status]:
        return self._get_data(SAX_STATUS_KEY, StatusParser)

    def get_configurations(self) -> [Configuration]:
        return self._get_data(SAX_CONFIGURATION_KEY, Configuration.Parser)

    def get_short_summary(self) -> [ShortSummary]:
        return self._get_data(SAX_SHORT_KEY, ShortSummaryParser)

    def get_notifications(self) -> [Notification]:
        return self._get_data(SAX_PROBLEM_HISTORY_KEY, NotificationParser)

    def _get_data(self, key, parser):
        returned_data = []
        for device in DeviceRegistry.get_devices():
            parser_instance = parser()
            self.socket = socket.socket()

            try:
                self._send_message(device, key)
            except ConnectionError as e:
                returned_data.append(parser_instance({"error": e, "device": device}))
            else:
                data = self._receive_message()

                data_instance = parser_instance(data.decode())
                data_instance.device = device

                returned_data.append(data_instance)

            self.socket.close()
        return returned_data

    def _send_message(self, device: Device, msg: bytes):
        self.socket.settimeout(CONNECTION_TIMEOUT)

        try:
            self.socket.connect((device.ip, config.EMITTER_PORT))
        except OSError:
            raise ConnectionError("Could not connect to device: {}".format(device))

        self.socket.send(json.dumps({"command": msg}).encode())

    def _receive_message(self):
        return self.socket.recv(int(16384))


if __name__ == '__main__':
    from app.data import register_tables, remove_tables
    from app import db

    register_tables(db)

    DeviceRegistry.add_device("Device1", "127.0.0.1")
    DeviceRegistry.add_device("Device2", "127.0.0.1")

    r = Recruiter()
    r.get_status()

    remove_tables(db)
