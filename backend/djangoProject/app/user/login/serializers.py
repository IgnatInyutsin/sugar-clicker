from rest_framework import serializers
from djangoProject.app.user.models import User
from djangoProject.app.validators.email_validation import validate_email_in_login, validate_auth

# Сериализатор для логина
class LoginSerializer(serializers.HyperlinkedModelSerializer):
    session_uuid = serializers.CharField(write_only=True)
    pass_cache = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[validate_email_in_login, validate_auth])

    class Meta:
        model = User
        fields = ['session_uuid', 'pass_cache', 'email']