from rest_framework import viewsets
from djangoProject.app.serializers.provider_shop import ProviderShopSerializer
from djangoProject.models import Provider

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all().order_by('id')
    serializer_class = ProviderShopSerializer