from rest_framework import serializers
from djangoProject.app.user.models import User
from djangoProject.app.admin.group.serializers import AdminsGroupGetSerializer
from djangoProject.app.provider.group.serializers import ProvidersGroupGetSerializer
from djangoProject.app.validators.user_id_validation import validate_user_id

# Сериализатор для GET
class PassiveIncomeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(validators=[validate_user_id])
    class Meta:
        model = User
        fields = ['id']