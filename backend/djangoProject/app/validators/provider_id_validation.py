from djangoProject.app.provider.models import Provider
from rest_framework.serializers import ValidationError

# Валидатор id user-а, проверяющий наличие такого пользователя в базе данных

def validate_provider_id(value):
    if not Provider.objects.all().filter(id=value).exists():
        raise ValidationError([{"code": "UNDEFINED_PROVIDER_ID", "text": "Provider ID is undefined"}])
    else:
        return value