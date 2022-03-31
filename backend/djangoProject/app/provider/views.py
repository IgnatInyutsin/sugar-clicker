from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.provider.serializers import ProviderShopSerializer
from djangoProject.app.provider.models import Provider

#класс для запросов на провайдера, доступен только get
class ProviderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Provider.objects.all().order_by('id')
    serializer_class = ProviderShopSerializer