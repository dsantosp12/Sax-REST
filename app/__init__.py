from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from peewee import SqliteDatabase

import config

app = Flask(__name__)
app.config.from_object(config)

# Allow cross origin request to the UI client only
cors = CORS(app, resources={r"/*": {"origins": "*"}})

db = SqliteDatabase(config.DATABASE_URI)

from app.recruiter.recruiter import Recruiter
from app.data.device_registry import DeviceRegistry


# @app.before_request
# def check_authorization():
#     request_token = request.headers.get("Authorization")
#
#     if not request_token == app.config.get("AUTH_TOKEN"):
#         abort(401)


#
# Devices Status Endpoints
#
@app.route("/devices/status")
@app.route("/devices/status/<int:device_id>")
def get_devices_status(device_id=None):
    recruiter = Recruiter()

    if device_id:
        devices_status = recruiter.get_device_status(device_id).json_able()
    else:
        devices_status = [status.json_able()
                          for status in recruiter.get_devices_status()]

    return jsonify(devices_status)


@app.route("/devices/status/short")
def get_devices_status_short():
    recruiter = Recruiter()
    devices_status = [status.json_able()
                      for status in recruiter.get_short_summary()]

    return jsonify(devices_status)


#
# Devices Create and Get Endpoints
#
@app.route("/devices", methods=['POST'])
def create_devices():
    device_json = request.get_json()

    device_name = None
    device_ip = None

    try:
        device_name = device_json["device_name"]
        device_ip = device_json["device_ip"]
    except KeyError:
        abort(400)

    new_device = DeviceRegistry.add_device(device_name, device_ip)

    return jsonify(new_device.json_able())


@app.route("/devices", methods=['GET'])
def get_devices():
    devices = [device.json_able() for device in DeviceRegistry.get_devices()]

    return jsonify(devices)


#
# Devices Notification Endpoint
#
@app.route("/devices/notifications")
def get_notifications():
    recruiter = Recruiter()
    notifications = [notification.json_able() for notification in recruiter.get_notifications()]

    return jsonify(notifications)
