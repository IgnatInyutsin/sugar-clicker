from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.serializers.user_registration import UserRegSerializer
from djangoProject.models import User
from rest_framework.serializers import ValidationError
import time
from django.core import serializers

# Класс для запросов по регистрации, доступен только POST
class UserRegViewSet(viewsets.ModelViewSet):
    #связываем с сериализатором
    queryset = User.objects.all().order_by('id')
    serializer_class = UserRegSerializer

    # метод POST
    def create(self, request):
        # Получаем наш сериализатор
        serializer = self.get_serializer(data=request.data)
        # Проверяем, все ли поля прошли валидацию
        if serializer.is_valid(raise_exception=True):
            # Если да - сохраняем пользователя
            user = User(
                email=request.data['name'],
                name=request.data['name'],
                pass_cache=request.data['pass_cache'],
                session_uuid=request.data['session_uuid'],
                registration_at=time.time(),
                last_passive_income_data=time.time()
            )
            user.save()
            return Response(status=201, data={"code": "SUCCESS_ADD_USER", "text": "User is created"})

        # Иначе возвращаем сообщение о всех ошибках
        raise ValidationError(serializer.errors)

    def list(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})
    def retrieve(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def update(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def partial_update(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def destroy(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})