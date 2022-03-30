from django.urls import include, path
from rest_framework import routers
from djangoProject.app.provider.views import ProviderViewSet
from djangoProject.app.provider.group.views import ProvidersGroupViewSet

#устанавливаем пути
router = routers.DefaultRouter()
router.register('', ProviderViewSet)
router.register('group', ProviderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]