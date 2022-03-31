from rest_framework import viewsets, mixins
from rest_framework.response import Response
from djangoProject.app.user.serializers import UserSerializer, UserBalanceSerializer, UserRegistrationSerializer
from djangoProject.app.user.models import User
from rest_framework.serializers import ValidationError
from djangoProject.app.validators.uuid_validation import validate_uuid
from rest_framework.decorators import api_view

#класс для запросов на пользователей
class UserViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    # обработка запросов про всех пользователей
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return UserBalanceSerializer
        elif self.action == "create":
            return UserRegistrationSerializer
        else:
            return UserSerializer

    # обновление баланса
    def partial_update(self, request, pk):
        # Получаем наш сериализатор
        serializer = self.get_serializer(data=request.data)
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
            user.update(balance = int(user[0].balance) + int(request.data["balance"]))
            user.update(sugar_all_time=int(user[0].sugar_all_time) + int(request.data["balance"]))

            # ответ
            return Response(status=201, data={"code": "SUCCESS_UPDATE_BALANCE", "text": "Your balance are updated"})

    # обновление баланса
    def update(self, request, pk):
        # Получаем наш сериализатор
        serializer = self.get_serializer(data=request.data)
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
            user.update(balance=int(user[0].balance) + int(request.data["balance"]))

            # ответ
            return Response(status=201, data={"code": "SUCCESS_UPDATE_BALANCE", "text": "Your balance are updated"})
