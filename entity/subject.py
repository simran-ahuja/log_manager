from .metric import Frequency


class RequestLog(object):
    def __init__(self, url, method, timestamp, response_time, response_code):
        self.method = method
        self.url = url
        self.timestamp = timestamp
        self.response_time = response_time
        self.response_code = response_code
