from django.urls import include, path
from rest_framework import routers
from djangoProject.app.user.views import UserViewSet
from djangoProject.app.user.login.views import LoginViewSet

#устанавливаем пути
router = routers.DefaultRouter()
router.register('list',  UserViewSet)
router.register('login', LoginViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]