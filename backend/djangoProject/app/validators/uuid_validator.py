import re
from rest_framework.serializers import ValidationError

# Валидация uuid

def validate_uuid(value):
    if re.match(r"^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$", value):
        return value
    else:
        raise ValidationError([{'err_code': 'INVALID_UUID', 'text': 'UUID is invalid'}])