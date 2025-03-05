"""User schema for serialization and validation."""
from marshmallow import Schema, fields, validate, validates, ValidationError
import re

class UserSchema(Schema):
    """Schema for User model."""
    
    id = fields.Int(dump_only=True)
    username = fields.Str(
        required=True,
        validate=[
            validate.Length(min=3, max=80),
            validate.Regexp(
                '^[a-zA-Z0-9_]+$',
                error='Username must contain only letters, numbers, and underscores'
            )
        ]
    )
    email = fields.Email(required=True)
    password = fields.Str(
        required=True,
        load_only=True,
        validate=validate.Length(min=8, max=128)
    )
    first_name = fields.Str(validate=validate.Length(max=50))
    last_name = fields.Str(validate=validate.Length(max=50))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    is_active = fields.Bool(dump_only=True)
    bio = fields.Str(validate=validate.Length(max=256))
    country = fields.Str(validate = validate.Length(max=50))
    
    @validates('password')
    def validate_password(self, value):
        """Validate password complexity.
        
        Args:
            value (str): The password to validate
            
        Raises:
            ValidationError: If password doesn't meet complexity requirements
        """
        if not re.search(r'[A-Z]', value):
            raise ValidationError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', value):
            raise ValidationError('Password must contain at least one lowercase letter')
        if not re.search(r'[0-9]', value):
            raise ValidationError('Password must contain at least one number')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValidationError('Password must contain at least one special character')


# Create schema instances
user_schema = UserSchema()
users_schema = UserSchema(many=True) 