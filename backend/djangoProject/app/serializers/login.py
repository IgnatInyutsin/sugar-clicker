from rest_framework import serializers
from djangoProject.models import User

# Сериализатор для логина
class LoginSerializer(serializers.HyperlinkedModelSerializer):
    session_uuid = serializers.CharField(write_only=True)
    pass_cache = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['session_uuid', 'pass_cache']