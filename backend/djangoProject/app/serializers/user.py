from rest_framework import serializers
from djangoProject.models import User

# Сериализатор для Админов
class UserSerializer(serializers.HyperlinkedModelSerializer):
    session_uuid = serializers.CharField(write_only=True)
    pass_cache = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'session_uuid', 'registration_at', 'sugar_all_time', 'balance', 'last_passive_income_data', 'pass_cache']