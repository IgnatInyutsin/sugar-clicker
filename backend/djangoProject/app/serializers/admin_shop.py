from rest_framework import serializers
from djangoProject.models import Admin

class AdminShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admin
        fields = ('name', 'cost', 'profit')