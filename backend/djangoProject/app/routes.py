from django.urls import include, path
from rest_framework import routers
from djangoProject.app.views.admin import AdminViewSet
from djangoProject.app.views.provider import ProviderViewSet
from djangoProject.app.views.admins_group import AdminsGroupViewSet
from djangoProject.app.views.user import UserViewSet
from djangoProject.app.views.login import LoginViewSet

#устанавливаем пути
router = routers.DefaultRouter()
router.register('admin', AdminViewSet)
router.register('provider', ProviderViewSet)
router.register('admins_group', AdminsGroupViewSet)
router.register('user', UserViewSet)
router.register('login', LoginViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]