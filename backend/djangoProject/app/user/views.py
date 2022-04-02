from rest_framework import viewsets, mixins
from rest_framework.response import Response
from djangoProject.app.user.serializers import UserSerializer, UserBalanceSerializer, UserRegistrationSerializer
from djangoProject.app.user.models import User
from rest_framework.serializers import ValidationError
from rest_framework.decorators import api_view
from django.core.mail import send_mail
import uuid
import os
from django.db import transaction

#класс для запросов на пользователей
class UserViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    # обработка запросов про всех пользователей
    queryset = User.objects.all().filter(is_auth=True).order_by('id')
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return UserBalanceSerializer
        elif self.action == "create":
            return UserRegistrationSerializer
        else:
            return UserSerializer

    # регистрация
    def create(self, request, pk=None):
        # Получаем наш сериализатор
        serializer = self.get_serializer(data=request.data)
        # Проверяем, все ли поля прошли валидацию
        if serializer.is_valid(raise_exception=True):
            # Генерируем аутенфикатор
            auth = uuid.uuid4()
            # Создаем пользователя
            user = User(
                name=request.data["name"],
                email=request.data["email"],
                pass_cache=request.data["pass_cache"],
                auth=auth
            )
            user.save()

            #отправляем на почту сообщение
            send_mail('Аутентификация в SUGAR CLICKER',
                        'http://' + request.get_host() + '/api/user/auth/' + str(auth) + '/ перейдите по этой ссылке, '
                                                                             'чтобы подтвердить принадлежность этой почты к аккаунту SUGAR CLICK',
                        os.environ.get("EMAIL"),
                        [request.data["email"]],
                        fail_silently=False)

            #возвращаем сообщение об удачной регистрации
            return Response(status=201, data={"code": "SUCCESSFULL_REGISTRATION_USER", "text": "User is created, please, check you email"})

        raise ValidationError(serializer.errors)

    # обновление баланса
    @transaction.atomic
    def partial_update(self, request, pk):
        # Получаем наш сериализатор
        serializer = self.get_serializer(data={
            "id": pk,
            "session_uuid": request.data.get("session_uuid", False),
            "balance": request.data.get("balance", False)
        })
        # Проверяем, все ли поля прошли валидацию
        if serializer.is_valid(raise_exception=True):
            # проверяем наличие пользователя с этим id
            if not User.objects.all().filter(id=pk).exists():
                raise ValidationError([{"code": "UNDEFINED_USER", "text": "user is wrong"}])

            # проверяем соответствие с сессией пользователя под этим id
            if str(User.objects.get(id=pk).session_uuid) != request.data['session_uuid']:
                raise ValidationError([{"code": "WRONG_SESSION_UUID", "text": "my_session_uuid is wrong"}])

            # если прошел валидацию обновляем баланс
            user = User.objects.all().filter(id=pk)
            user.update(balance = int(user[0].balance) + int(request.data["balance"]),
                        sugar_all_time=int(user[0].sugar_all_time) + int(request.data["balance"]))

            # ответ
            return Response(status=201, data={"code": "SUCCESS_UPDATE_BALANCE", "text": "Your balance are updated"})

        raise ValidationError(serializer.errors)

    # обновление баланса
    @transaction.atomic
    def update(self, request, pk):
        # Получаем наш сериализатор
        serializer = self.get_serializer(data={
            "id": pk,
            "session_uuid": request.data.get("session_uuid", False),
            "balance": request.data.get("balance", False)
        })
        # Проверяем, все ли поля прошли валидацию
        if serializer.is_valid(raise_exception=True):
            # проверяем наличие пользователя с этим id
            if not User.objects.all().filter(id=pk).exists():
                raise ValidationError([{"code": "UNDEFINED_USER", "text": "user is wrong"}])

            # проверяем соответствие с сессией пользователя под этим id
            if str(User.objects.get(id=pk).session_uuid) != request.data['session_uuid']:
                raise ValidationError([{"code": "WRONG_SESSION_UUID", "text": "my_session_uuid is wrong"}])

            # если прошел валидацию обновляем баланс
            user.update(balance=int(user[0].balance) + int(request.data["balance"]),
                        sugar_all_time=int(user[0].sugar_all_time) + int(request.data["balance"]))

            # ответ
            return Response(status=201, data={"code": "SUCCESS_UPDATE_BALANCE", "text": "Your balance are updated"})

        raise ValidationError(serializer.errors)
