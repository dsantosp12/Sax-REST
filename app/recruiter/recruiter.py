import socket

import config
from app.data.device_registry import DeviceRegistry, Device
from app.data.status import Status
from app.data.configuration import Configuration


SAX_STATUS_KEY = b"STATUS"
SAX_CONFIGURATION_KEY = b"CONFIGURATION"


class Recruiter:
    def __init__(self):
        self.socket = None

    def get_status(self) -> [Status]:
        return self._get_data(SAX_STATUS_KEY, Status.Parser())

    def get_configurations(self):
        return self._get_data(SAX_CONFIGURATION_KEY, Configuration.Parser())

    def _get_data(self, key, parser):
        returned_status = []
        for device in DeviceRegistry.get_devices():
            self.socket = socket.socket()
            status = self._send_message(device, key, parser)
            returned_status.append(status)

    def _send_message(self, device: Device, msg: bytes, parser) -> Status:
        self.socket.connect((device.ip, config.EMITTER_PORT))
        self.socket.send(msg)
        data = self.socket.recv(int(1E6))
        self.socket.close()

        return parser((device, data))


if __name__ == '__main__':
    from app.data import register_tables, remove_tables
    from app import db

    register_tables(db)

    DeviceRegistry.add_device("Device1", "127.0.0.1")
    DeviceRegistry.add_device("Device2", "127.0.0.1")

    r = Recruiter()
    r.get_status()

    remove_tables(db)
