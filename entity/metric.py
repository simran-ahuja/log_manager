from . import IUnaryMetric, IBinaryMetric


class Frequency(IUnaryMetric):
    def __init__(self):
        self._frequency = 0

    def compute(self):
        self._frequency = self._frequency + 1

    def get(self):
        return self._frequency


class Sum(IBinaryMetric):
    def __init__(self):
        self._sum = 0

    def compute(self, value):
        self._sum = self._sum + value

    def get(self):
        return self._sum


class Min(IBinaryMetric):
    def __init__(self):
        self._min = None

    def compute(self, value):
        self._min = min(self._min, value) if self._min else value

    def get(self):
        return self._min


class Max(IBinaryMetric):
    def __init__(self):
        self._max = None

    def compute(self, value):
        self._max = max(self._max, value) if self._max else value

    def get(self):
        return self._max
