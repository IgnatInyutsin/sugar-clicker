from django.urls import include, path
from rest_framework import routers
from djangoProject.app.views.admin import AdminViewSet
from djangoProject.app.views.provider import ProviderViewSet
from djangoProject.app.views.user_registration import UserRegViewSet

#устанавливаем пути
router = routers.DefaultRouter()
router.register('admins', AdminViewSet)
router.register('providers', ProviderViewSet)
router.register('registration', UserRegViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]