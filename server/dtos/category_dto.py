from marshmallow import Schema, fields, validate

class CategoryRequestDTO(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))

class CategoryResponseDTO(Schema):
    id = fields.Integer()
    name = fields.String()
