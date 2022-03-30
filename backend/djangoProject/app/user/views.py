from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.user.serializer import UserSerializer
from djangoProject.app.user.models import User
from rest_framework.serializers import ValidationError
from djangoProject.app.validators.uuid_validation import validate_uuid

#класс для запросов на пользователей
class UserViewSet(viewsets.ModelViewSet):
    # обработка запросов про всех пользователей
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def destroy(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    # обновление баланса
    def partial_update(self, request, pk=None):
        pk = int(request.path[15:].replace('/', ''))
        # проверяем наличие пользователя с этим id
        if not User.objects.all().filter(id=pk).exists():
            raise ValidationError([{"code": "UNDEFINED_USER", "text": "user is wrong"}])

        # проверяем uuid
        try:
            validate_uuid(request.data['my_session_uuid'])
        except ValidationError:
            raise ValidationError([{"code": "INVALID_SESSION_UUID", "text": "UUID is invalid"}])

        # если сессия есть - проверяем ее соответствие с сессией пользователя под этим id
        if str(User.objects.get(id=pk).session_uuid) != request.data["my_session_uuid"]:
            raise ValidationError([{"code": "WRONG_SESSION_UUID_UNDEFINED", "text": "my_session_uuid is wrong"}])

        # проверяем наличие поля плюса к балансу
        if not "plus_balance" in request.data:
            raise ValidationError([{"code": "UNDEFINED_PLUS_BALANCE", "text": "plus_balance is undefined"}])

        if not isinstance(request.data["plus_balance"], int):
            raise ValidationError([{"code": "INVALID_PLUS_BALANCE", "text": "plus_balance is invalid"}])

        # если прошел валидацию обновляем баланс
        user = User.objects.all().filter(id=pk)
        user.update(balance = int(user[0].balance) + int(request.data["plus_balance"]))

        # ответ
        return Response(status=201, data={"code": "SUCCESS_UPDATE_BALANCE", "text": "Your balance are updated"})



        # если действителен, то создадим кл

    def update(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})
