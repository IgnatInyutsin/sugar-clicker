from django.urls import include, path
from rest_framework import routers
from djangoProject.app.user.views import UserViewSet
from djangoProject.app.user.check.views import UserCheckViewSet
from djangoProject.app.user.login.views import LoginViewSet
from djangoProject.app.user.passive_income.views import PassiveIncomeViewSet

#устанавливаем пути
router = routers.DefaultRouter()
router.register('list',  UserViewSet)
router.register('login', LoginViewSet)
router.register('check', UserCheckViewSet)
router.register('passive_income', PassiveIncomeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]