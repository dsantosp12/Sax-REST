from app.recruiter.parser_base import ParserBase


class Notification:
    def __init__(self):
        self.device = None
        self.status_code = None
        self.last_well = None
        self.last_not_well = None
        self.reason_not_well = None
        self.thread_fail_init = None
        self.thread_zero_hash = None
        self.thread_fail_queue = None
        self.device_no_start = None
        self.device_over_heat = None
        self.device_comms_error = None

    def json_able(self):
        return {
            "device": self.device.json_able(),
            "status_code": self.status_code,
            "last_well": self.last_well,
            "last_not_well": self.last_not_well,
            "reason_not_well": self.reason_not_well,
            "thread_fail_init": self.thread_fail_init,
            "thread_zero_hash": self.thread_zero_hash,
            "thread_fail_queue": self.thread_fail_queue,
            "device_no_start": self.device_no_start,
            "device_over_heat": self.device_over_heat,
            "device_comms_error": self.device_comms_error
        }


class NotificationParser(ParserBase):
    def __init__(self):
        super().__init__()
        self.notification = Notification()

    def _get_data_ready(self, msg: str):
        # Data isn't corrupt for this message. Nothing to do here.
        self.data = msg

    def _parse_json(self):
        raw_notification = self.data["NOTIFY"][0]

        self.notification.status_code = self.data["STATUS"][0]["STATUS"]
        self.notification.last_well = raw_notification["Last Well"]
        self.notification.last_not_well = raw_notification["Last Not Well"]
        self.notification.reason_not_well = raw_notification["Reason Not Well"]
        self.notification.thread_fail_init = raw_notification["*Thread Fail Init"]
        self.notification.thread_zero_hash = raw_notification["*Thread Zero Hash"]
        self.notification.thread_fail_queue = raw_notification["*Thread Fail Queue"]
        self.notification.device_no_start = raw_notification["*Dev Nostart"]
        self.notification.device_over_heat = raw_notification["*Dev Over Heat"]
        self.notification.device_comms_error = raw_notification["*Dev Comms Error"]

        return self.notification
