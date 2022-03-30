from djangoProject.app.user.models import User
from rest_framework.serializers import ValidationError

# Валидатор id user-а, проверяющий наличие такого пользователя в базе данных

def validate_user_id(value):
    if User.objects.all().filter(id=value).exists():
        ValidationError([{"code": "UNDEFINED_USER_ID", "text": "User ID is undefined"}])
    else:
        return value