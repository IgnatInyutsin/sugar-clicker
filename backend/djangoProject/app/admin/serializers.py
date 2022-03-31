from rest_framework import serializers
from djangoProject.app.admin.models import Admin

# Сериализатор для Админов
class AdminShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'name', 'cost', 'profit')