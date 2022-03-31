from rest_framework import serializers
from djangoProject.app.user.models import User
from djangoProject.app.admin.group.serializers import AdminsGroupGetSerializer
from djangoProject.app.provider.group.serializers import ProvidersGroupGetSerializer

# Сериализатор для GET
class UserSerializer(serializers.HyperlinkedModelSerializer):
    session_uuid = serializers.CharField(write_only=True)
    pass_cache = serializers.CharField(write_only=True)
    admins = AdminsGroupGetSerializer(many=True)
    providers = ProvidersGroupGetSerializer(many=True)
    class Meta:
        model = User
        fields = ['id',
                  'name',
                  'email',
                  'session_uuid',
                  'registration_at',
                  'sugar_all_time',
                  'balance',
                  'last_passive_income_data',
                  'pass_cache',
                  'admins',
                  'providers']

# Сериализатор для POST
class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'session_uuid', 'pass_cache']

# Сериализатор для PUT и PATCH
class UserBalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['session_uuid', 'balance']