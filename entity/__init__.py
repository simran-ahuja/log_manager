from abc import ABC, abstractmethod


class ISubjectData(ABC):
    @abstractmethod
    def key(self):
        pass


class IMetric(ABC):
    @abstractmethod
    def get(self):
        pass


class IUnaryMetric(IMetric):
    @abstractmethod
    def compute(self):
        pass


class IBinaryMetric(IMetric):
    @abstractmethod
    def compute(self, value):
        pass


class IMetricsData(ABC):
    @abstractmethod
    def compute(self, subject):
        pass


class IMetricsManager(ABC):
    @abstractmethod
    def update_metrics(self, subject):
        pass
