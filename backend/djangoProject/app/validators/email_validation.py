from djangoProject.app.user.models import User
from rest_framework.serializers import ValidationError

def validate_email_in_login(value):
    # проверяем ее наличие в базе данных
    if not User.objects.all().filter(email=value).exists():
        raise ValidationError({"code": "MISSING_IN_DB_EMAIL", "text": "Email absent in database"})
    else:
        return value

def validate_auth(value):
    # проверяем активацию аккаунта
    if not User.objects.get(email=value).is_auth:
        raise ValidationError({"code": "ACCOUNT_NOT_ACTIVATED", "text": "Account is not activated"})
    else:
        return value