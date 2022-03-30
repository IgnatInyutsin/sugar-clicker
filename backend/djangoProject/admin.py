from django.contrib import admin
from djangoProject.app.user.models import User
from djangoProject.app.admin.models import Admin, AdminsGroup
from djangoProject.app.provider.models import Provider, ProvidersGroup

#Добавляем модели на панель администратора
admin.site.register(User)
admin.site.register(Provider)
admin.site.register(Admin)
admin.site.register(ProvidersGroup)
admin.site.register(AdminsGroup)