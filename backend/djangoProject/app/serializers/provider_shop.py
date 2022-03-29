from rest_framework import serializers
from djangoProject.models import Provider

# Сериализатор для Поставщиков
class ProviderShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('name', 'cost', 'income')