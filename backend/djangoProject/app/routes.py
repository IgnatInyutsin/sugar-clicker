from django.urls import include, path
from rest_framework import routers
from djangoProject.app.views.admin import AdminViewSet
from djangoProject.app.views.provider import ProviderViewSet

router = routers.DefaultRouter()
router.register('admins', AdminViewSet)
router.register('providers', ProviderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]