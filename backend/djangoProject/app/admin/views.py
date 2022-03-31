from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.admin.serializers import AdminShopSerializer
from djangoProject.app.admin.models import Admin

#класс для запросов на админа, доступен только get
class AdminViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Admin.objects.all().order_by('id')
    serializer_class = AdminShopSerializer