from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.serializers.user import UserSerializer
from djangoProject.models import User

#класс для запросов на провайдера, доступен только get
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def create(self, request):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def destroy(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})