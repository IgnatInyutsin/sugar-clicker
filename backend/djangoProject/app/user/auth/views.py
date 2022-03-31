from rest_framework import viewsets, mixins
from rest_framework.response import Response
from djangoProject.app.user.models import User
from djangoProject.app.provider.models import ProvidersGroup, Provider
from djangoProject.app.admin.models import Admin, AdminsGroup
from rest_framework.serializers import ValidationError
from djangoProject.app.validators.uuid_validation import validate_uuid
from rest_framework.decorators import api_view
from djangoProject.app.user.serializers import UserSerializer
import time
import uuid

class AuthViewSet(mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def retrieve(self, request, pk):
        # проверка на соответствие auth-токена
        if not User.objects.all().filter(auth=pk).exists():
            raise ValidationError("Токен не действителен")
        else:
            User.objects.all().filter(auth=pk).update(auth=None, is_auth=True)
            return Response(data="Активация прошла успешно! Вы можете зайти в свой аккаунт.")