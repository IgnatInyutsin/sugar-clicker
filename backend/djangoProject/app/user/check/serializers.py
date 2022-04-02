from rest_framework import serializers
from djangoProject.app.user.models import User
from djangoProject.app.validators.user_id_validation import validate_user_id

# Сериализатор для user check
class UserCheckSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(validators=[validate_user_id])
    class Meta:
        model = User
        fields = ['session_uuid', 'id']