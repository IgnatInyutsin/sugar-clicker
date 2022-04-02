from djangoProject.app.admin.models import Admin
from rest_framework.serializers import ValidationError

# Валидатор id user-а, проверяющий наличие такого пользователя в базе данных

def validate_admin_id(value):
    if not Admin.objects.all().filter(id=value).exists():
        raise ValidationError([{"code": "UNDEFINED_ADMIN_ID", "text": "Admin ID is undefined"}])
    else:
        return value