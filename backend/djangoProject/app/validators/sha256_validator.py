import re
import sys
from rest_framework.serializers import ValidationError

# Валидатор для проверки, действительно ли это хэш SHA256

def validate_sha256(value):
    # Действителен, если является 16-ричным числом и по количеству байт равен 32
    if re.match(r'(0x)?[A-Fa-f0-9]+', value) and sys.getsizeof(value) == 32:
        return value
    # Иначе отдаем сообщение об ошибке
    else:
        raise ValidationError([{'err_code': 'INVALID_PASSWORD_CACHE', 'text': 'Password hash is invalid'}])