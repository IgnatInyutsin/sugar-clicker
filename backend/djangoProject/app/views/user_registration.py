from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.serializers.user_registration import UserRegSerializer
from djangoProject.models import User
from rest_framework.serializers import ValidationError
import time
from django.core import serializers
from datetime import datetime

# Класс для запросов по регистрации, доступен только POST
class UserRegViewSet(viewsets.ModelViewSet):
    #связываем с сериализатором
    queryset = User.objects.all().order_by('id')
    serializer_class = UserRegSerializer

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