from rest_framework import viewsets, mixins
from rest_framework.response import Response
from djangoProject.app.user.check.serializers import UserCheckSerializer
from djangoProject.app.user.models import User
from rest_framework.serializers import ValidationError
from django.core.validators import validate_email
from django.core import serializers

# класс для запросов на проверку пользователя
class UserCheckViewSet(mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    # обработка запросов про всех пользователей
    queryset = User.objects.all().order_by('id')
    serializer_class = UserCheckSerializer

    def partial_update(self, request, pk):
        # Получаем наш сериализатор
        if pk.isdigit():
            serializer = self.get_serializer(data={
                "session_uuid": request.data.get("session_uuid", False),
                "id": int(pk)
            })
            # Проверяем, все ли поля прошли валидацию
            if serializer.is_valid(raise_exception=True):
                # соответствие session_id
                if str(User.objects.get(id=pk).session_uuid) == request.data['session_uuid']:
                    return Response(status=200, data={"code": "TRUE_CHECK", "text": "This session_id is valid"})
                else:
                    raise ValidationError({code: "FALSE_CHECK", "text": "This session_id is non-valid"})

            raise ValidationError(serializer.errors)

        else: raise ValidationError([{"code": "ID_IS_ONLY_NUMBER", "text": "ID is only number!"}])
