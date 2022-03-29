from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.serializers.provider_shop import ProviderShopSerializer
from djangoProject.models import Provider

#класс для запросов на провайдера, доступен только get
class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all().order_by('id')
    serializer_class = ProviderShopSerializer

    def create(self, request):
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