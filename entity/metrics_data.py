from . import IMetricsData

from .metric import Max, Min, Sum, Frequency


class RequestMetricsData(IMetricsData):
    def __init__(self,):
        self.frequency = Frequency()
        self.max_response_time = Max()
        self.min_response_time = Min()
        self.total_response_time = Sum()

    def compute(self, subject):
        self.frequency.compute()
        self.max_response_time.compute(value=subject.response_time)
        self.min_response_time.compute(value=subject.response_time)
        self.total_response_time.compute(value=subject.response_time)

    def get_frequency(self):
        return self.frequency.get()

    def get_average_response_time(self):
        frequency = self.frequency.get()
        total = self.total_response_time.get()

        if not frequency:
            return None

        return total / frequency

    def get_min_response_time(self):
        return self.min_response_time.get()

    def get_max_response_time(self):
        return self.max_response_time.get()
