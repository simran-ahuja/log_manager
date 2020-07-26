from marshmallow import Schema, fields, validate


class BaseSchema(Schema):
    class Meta:
        ordered = True


class CsvLog(BaseSchema):
    timestamp = fields.Integer(required=True)
    url = fields.String(required=True)
    method = fields.String(
        required=True, validate=validate.OneOf(["PUT", "POST", "GET", "DELETE"])
    )
    response_time = fields.Integer(required=True)
    response_code = fields.Integer(required=True)
