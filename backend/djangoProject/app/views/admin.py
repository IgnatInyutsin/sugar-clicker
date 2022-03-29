from rest_framework import viewsets
from djangoProject.app.serializers.admin_shop import AdminShopSerializer
from djangoProject.models import Admin

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all().order_by('id')
    serializer_class = AdminShopSerializer