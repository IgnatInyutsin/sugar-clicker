from rest_framework import serializers
from djangoProject.app.user.models import User

# Сериализатор для пользователей
class UserSerializer(serializers.HyperlinkedModelSerializer):
    session_uuid = serializers.CharField(write_only=True)
    pass_cache = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'session_uuid', 'registration_at', 'sugar_all_time', 'balance', 'last_passive_income_data', 'pass_cache']

# Сериализатор для PUT и PATCH
class UserBalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['session_uuid', 'balance']