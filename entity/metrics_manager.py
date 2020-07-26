from . import IMetricsManager, ISubjectData, IMetricsData
from .metrics_data import RequestMetricsData


class AggregatedData(object):
    def __init__(self, subject_data: ISubjectData, metrics_data: IMetricsData):
        self.subject_data = subject_data
        self.metrics_data = metrics_data


class RequestMetricsManager(IMetricsManager):
    def __init__(self, subject_data_cls: ISubjectData):
        self.metrics_map = {}
        self.subject_data_cls = subject_data_cls

    def update_metrics(self, subject):
        subject_data = self.subject_data_cls(subject=subject)
        key = subject_data.key()

        if not self.metrics_map.get(key):
            request_metrics = RequestMetricsData()
            self.metrics_map[key] = AggregatedData(
                subject_data=subject_data, metrics_data=request_metrics
            )

        self.metrics_map[key].metrics_data.compute(subject)
