from marshmallow import Schema, fields, validate


class ReportRequestDTO(Schema):
    
    reporter_id = fields.Int(required = True)
    target_id = fields.Int(required = True)
    reason = fields.Str(validate = validate.Length(max=250))
    