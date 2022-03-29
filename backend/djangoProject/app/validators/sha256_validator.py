import re
import sys
from rest_framework.serializers import ValidationError

# Валидатор для проверки, действительно ли это хэш SHA256

def sha256_validator(value):
    # Действителен, если является 16-ричным числом и по количеству байт равен 32
    if re.match(r'(0x)?[A-Fa-f0-9]+', value) and sys.getsizeof(value) == 32:
        return value
    # Иначе отдаем сообщение об ошибке
    else:
        raise ValidationError(['Password hash is invalid'])