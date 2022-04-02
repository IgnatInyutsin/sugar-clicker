from rest_framework import serializers
from djangoProject.app.user.models import User

# Сериализатор для user check
class AuthSerializer(serializers.HyperlinkedModelSerializer):
    auth = serializers.UUIDField()
    class Meta:
        model = User
        fields = ['auth']