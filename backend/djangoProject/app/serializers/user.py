from rest_framework import serializers
from djangoProject.models import User

# Сериализатор для Админов
class UserSerializer(serializers.HyperlinkedModelSerializer):
    session_uuid = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'pass_cache', 'session_uuid', 'registration_at', 'sugar_all_time', 'balance', 'last_passive_income_data']