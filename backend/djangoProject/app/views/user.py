from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.serializers.user import UserSerializer
from djangoProject.models import User
from rest_framework.serializers import ValidationError

#класс для запросов на пользователей
class UserViewSet(viewsets.ModelViewSet):
    # обработка запросов про всех пользователей
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def destroy(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def partial_update(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def update(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})
