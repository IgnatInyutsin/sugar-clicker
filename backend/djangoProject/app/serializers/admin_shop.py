from rest_framework import serializers
from djangoProject.models import Admin

# Сериализатор для Админов
class AdminShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admin
        fields = ('name', 'cost', 'profit')