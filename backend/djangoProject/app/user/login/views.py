from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.user.login.serializer import LoginSerializer
from djangoProject.app.user.models import User
from rest_framework.serializers import ValidationError
from django.core.validators import validate_email
from django.core import serializers

#класс для запросов на пользователей
class LoginViewSet(viewsets.ModelViewSet):
    # обработка запросов про всех пользователей
    queryset = User.objects.all().order_by('id')
    serializer_class = LoginSerializer

    def partial_update(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def create(self, request):
        # Получаем наш сериализатор
        serializer = self.get_serializer(data=request.data)
        # Проверяем, все ли поля прошли валидацию
        if serializer.is_valid(raise_exception=True):
            # проверяем существование почты
            if not "email" in request.data:
                raise ValidationError([{"code": "MISSING_EMAIL", "text": "Email absent in you request"}])

            # валидация email
            try:
                validate_email(request.data["email"])
            except ValidationError:
                raise ValidationError([{"code": "EMAIL_WRONG_FORMAT", "text": "Wrong format of email"}])

            # проверяем ее наличие в базе данных
            if not User.objects.all().filter(email=request.data["email"]).exists():
                raise ValidationError([{"code": "MISSING_IN_DB_EMAIL", "text": "Email absent in database"}])

            # проверяем соответствие кэшей пароля
            if User.objects.get(email=request.data["email"]).pass_cache != request.data["pass_cache"]:
                raise ValidationError([{"code": "WRONG_PASSWORD", "text": "Password is wrong"}])

            # если прошли проверки, то меняем session_id и возвращаем обновленного пользователя
            User.objects.all().filter(email=request.data["email"]).update(session_uuid=request.data["session_uuid"])
            return Response(status=201, data={"code": "SUCCESS_LOGIN", "text": "Login is success!", "user_id": User.objects.all().filter(email=request.data["email"])[0].id})

        # Если не прошли валидацию сериалайзера - возвращаем 400
        raise ValidationError(serializer.errors)

    def list(self, request):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def retrieve(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def update(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def destroy(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})