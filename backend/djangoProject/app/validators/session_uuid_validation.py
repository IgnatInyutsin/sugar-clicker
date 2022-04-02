import uuid
from rest_framework.serializers import ValidationError
from djangoProject.app.user.models import User

def validate_session_uuid(value):
    if not User.objects.all().filter(session_uuid=value).exists():
        raise ValidationError([{"code": "SESSION_UUID_UNDEFINED", "text": "session_uuid in undefinded"}])
    else:
        return value