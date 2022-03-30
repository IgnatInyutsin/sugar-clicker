from django.urls import include, path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', include('djangoProject.app.admin.routes')),
    path('provider/', include('djangoProject.app.provider.routes')),
    path('user/', include('djangoProject.app.user.routes'))
]