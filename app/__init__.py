import json

from flask import Flask, request, abort, jsonify
from peewee import SqliteDatabase

import config

app = Flask(__name__)
app.config.from_object(config)

db = SqliteDatabase(config.DATABASE_URI)

from app.recruiter.recruiter import Recruiter
from app.data.device_registry import DeviceRegistry


@app.route("/devices/status")
def get_devices_status():
    recruiter = Recruiter()
    devices_status = recruiter.get_status()

    return json.dumps(devices_status)


@app.route("/devices", methods=['POST'])
def create_devices():
    device_json = request.get_json()

    device_name = None
    device_ip = None

    try:
        device_name = device_json["device_name"]
        device_ip = device_json["device_ip"]
    except:
        abort(400)

    new_device = DeviceRegistry.add_device(device_name, device_ip)

    return jsonify(new_device.json_able())


@app.route("/devices", methods=['GET'])
def get_devices():
    devices = [device.json_able() for device in DeviceRegistry.get_devices()]

    return jsonify(devices)
