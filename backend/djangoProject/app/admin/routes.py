from django.urls import include, path
from rest_framework import routers
from djangoProject.app.admin.views import AdminViewSet
from djangoProject.app.admin.group.views import AdminsGroupViewSet

#устанавливаем пути
router = routers.DefaultRouter()
router.register('', AdminViewSet)
router.register('group', AdminsGroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]