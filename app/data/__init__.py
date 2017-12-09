from .device_registry import DeviceRegistry


def register_tables(db):
    db.create_tables([
        DeviceRegistry
    ], safe=True)


def remove_tables(db):
    db.drop_tables([
        DeviceRegistry
    ], safe=True)
