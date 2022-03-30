from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.serializers.admin_shop import AdminShopSerializer
from djangoProject.models import Admin

#класс для запросов на админа, доступен только get
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all().order_by('id')
    serializer_class = AdminShopSerializer
    
    def create(self, request):
        return Response(status=405,
                            data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def retrieve(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def update(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def partial_update(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def destroy(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})