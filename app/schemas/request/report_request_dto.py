from marshmallow import EXCLUDE, Schema, fields, validate


class ReportRequestDTO(Schema):
    class Meta:
        unknown = EXCLUDE 
    
    reporter_id = fields.Int(required = True)
    target_id = fields.Int(required = True)
    reason = fields.Str(validate = validate.Length(max=250))
    
    