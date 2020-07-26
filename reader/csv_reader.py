import csv
from marshmallow import ValidationError
from . import IReader
from errors import ReaderException


class CSVReader(IReader):
    def __init__(self, schema):
        self.schema = schema

    def read(self, file="./input/input.csv"):
        try:
            with open(file) as csvfile:
                rows = csv.DictReader(csvfile)
                return self.schema(many=True).load(rows)

        except Exception as exc:
            raise ReaderException(f"Failed to read records from csv {str(exc)}")
