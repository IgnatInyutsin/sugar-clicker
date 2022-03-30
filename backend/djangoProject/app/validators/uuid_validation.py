import uuid
from rest_framework.serializers import ValidationError

def validate_uuid(value):
    try:
        uuid.UUID(str(value))
        return value
    except ValueError:
        raise ValidationError([{'code': "WRONG_UUID", 'text': 'this uuid have wrong format'}])