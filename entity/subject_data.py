from . import ISubjectData


class RequestUrlMethodData(ISubjectData):
    def __init__(self, subject):
        self.url = subject.url
        self.method = subject.method

    def key(self):
        return hash((self.method, self.url))
