from rest_framework import serializers
from djangoProject.app.provider.models import ProvidersGroup, Provider
from djangoProject.app.user.models import User
from rest_framework.serializers import ValidationError
from djangoProject.app.validators.session_uuid_validation import validate_session_uuid
from djangoProject.app.validators.provider_id_validation import validate_provider_id


# Дополнительные сериализаторы для вложенности в POST
class UserBuyProviderSerializer(serializers.HyperlinkedModelSerializer):
    balance = serializers.IntegerField(read_only=True)
    session_uuid =  serializers.CharField(write_only=True, validators=[validate_session_uuid])
    last_passive_income_data = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'balance', 'session_uuid', 'last_passive_income_data')

class ProviderBuyProviderSerializer(serializers.HyperlinkedModelSerializer):
    cost = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(write_only=True, validators=[validate_provider_id])

    class Meta:
        model = Provider
        fields = ('id', 'cost')

# Дополнительные сериализаторы для вложенности в GET
class UserGetProviderSerializer(serializers.HyperlinkedModelSerializer):
    balance = serializers.IntegerField(read_only=True)
    last_passive_income_data = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'registration_at', 'sugar_all_time', 'balance', 'last_passive_income_data']

class ProviderGetProviderSerializer(serializers.HyperlinkedModelSerializer):
    cost = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField()

    class Meta:
        model = Provider
        fields = ('id', 'name', 'cost', 'income')


# Сериализатор для post
class ProvidersGroupSerializer(serializers.HyperlinkedModelSerializer):
    # Создаем вложенные списки
    user = UserBuyProviderSerializer()
    provider = ProviderBuyProviderSerializer()

    class Meta:
        model = ProvidersGroup
        fields = ('count', 'user', 'provider')

# Сериализатор для get
class ProvidersGroupGetSerializer(serializers.HyperlinkedModelSerializer):
    # Создаем вложенные списки
    user = UserGetProviderSerializer()
    provider = ProviderGetProviderSerializer()

    class Meta:
        model = ProvidersGroup
        fields = ('id', 'count', 'user', 'provider')