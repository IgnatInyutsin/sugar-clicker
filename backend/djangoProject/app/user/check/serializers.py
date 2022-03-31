from rest_framework import serializers
from djangoProject.app.user.models import User

# Сериализатор для user check
class UserCheckSerializer(serializers.HyperlinkedModelSerializer):
    session_uuid = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['session_uuid', 'id']