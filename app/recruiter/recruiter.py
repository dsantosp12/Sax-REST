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
        returned_data = []
        for device in DeviceRegistry.get_devices():
            self.socket = socket.socket()

            try:
                self._send_message(device, key)
            except ConnectionError as e:
                returned_data.append(parser({"error": e, "device": device}))
            else:
                data = self._receive_message()

                returned_data.append(parser(data))

            self.socket.close()
        return returned_data

    def _send_message(self, device: Device, msg: bytes):
        try:
            self.socket.connect((device.ip, config.EMITTER_PORT))
        except OSError:
            raise ConnectionError("Couldn't connect to device: {}".format(device))

        self.socket.send(msg)

    def _receive_message(self):
        return self.socket.recv(int(1E6))



if __name__ == '__main__':
    from app.data import register_tables, remove_tables
    from app import db

    register_tables(db)

    DeviceRegistry.add_device("Device1", "127.0.0.1")
    DeviceRegistry.add_device("Device2", "127.0.0.1")

    r = Recruiter()
    r.get_status()

    remove_tables(db)
