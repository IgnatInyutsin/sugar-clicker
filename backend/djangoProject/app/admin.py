from django.contrib import admin
from djangoProject.models import *

admin.site.register(User)
admin.site.register(Provider)
admin.site.register(Admin)
admin.site.register(ProvidersGroup)
admin.site.register(AdminsGroup)