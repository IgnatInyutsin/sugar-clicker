from rest_framework import serializers
from djangoProject.models import Provider

class ProviderShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('name', 'cost', 'income')