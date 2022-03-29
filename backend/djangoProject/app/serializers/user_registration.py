from rest_framework import serializers
from djangoProject.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import time
from rest_framework.response import Response

# сериализатор для регистрации пользователя
class UserRegSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'pass_cache', 'session_uuid')