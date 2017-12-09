import datetime
import types

from peewee import *

from app import db


class Device:
    """
        Device is the DTO that for the representation of a device in the system.

        device_name:    Is the name of the device given by the user.
        device_ip:      Is the local IP of the device where the system will connect to.
    """
    def __init__(self, name: str, ip: str, date: datetime.datetime):
        if not isinstance(date, datetime.date):
            raise TypeError("Date must be a datetime.date type")
        self.name = name
        self.ip = ip
        self.date = date

    def json_able(self):
        return {
            "device_name": self.name,
            "device_ip": self.ip
        }

    def __repr__(self):
        return "Device: %s IP: %s" % (self.name, self.ip)


class DeviceRegistry(Model):
    """
        Device Registry is table with all the registered devices in the system.

        device_name:    Is the name of the device given by the user.
        device_ip:      Is the local IP of the device where the system will connect to.
        added_on:       Stores the date that the device was added to the registry.
    """

    device_name = CharField()
    device_ip = CharField()
    added_on = DateField(default=datetime.datetime.now())

    class Meta:
        database = db

    def __repr__(self):
        return "Device: %s IP: %s" % (self.device_name, self.device_ip)

    @classmethod
    def get_devices(cls) -> types.GeneratorType:
        for device in DeviceRegistry.select():
            yield Device(device.device_name, device.device_ip, device.added_on)

    @classmethod
    def add_device(cls, name: str, ip: str) -> Device:
        device = DeviceRegistry()
        device.device_name = name
        device.device_ip = ip
        device.save()

        return Device(name, ip, datetime.datetime.now())
