from rest_framework import serializers
from djangoProject.app.admin.models import AdminsGroup, Admin
from djangoProject.app.user.models import User
from djangoProject.app.validators.user_id_validation import validate_user_id
from djangoProject.app.validators.admin_id_validation import validate_admin_id
from rest_framework.serializers import ValidationError


# Дополнительные сериализаторы для вложенности
class UserBuyAdminSerializer(serializers.HyperlinkedModelSerializer):
    balance = serializers.IntegerField(read_only=True)
    session_uuid =  serializers.CharField(write_only=True)
    last_passive_income_data = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True, validators=[validate_user_id])

    class Meta:
        model = User
        fields = ('id', 'balance', 'session_uuid', 'last_passive_income_data')

class AdminBuyAdminSerializer(serializers.HyperlinkedModelSerializer):
    cost = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(write_only=True, validators=[validate_admin_id])

    class Meta:
        model = Admin
        fields = ('id', 'cost')

# Сериализатор для admin
class AdminsGroupSerializer(serializers.HyperlinkedModelSerializer):
    # Создаем вложенные списки
    user = UserBuyAdminSerializer()
    admin = AdminBuyAdminSerializer()

    class Meta:
        model = AdminsGroup
        fields = ('count', 'user', 'admin')