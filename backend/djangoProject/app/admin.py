from django.contrib import admin
from djangoProject.models import *

#Добавляем модели на панель администратора
admin.site.register(User)
admin.site.register(Provider)
admin.site.register(Admin)
admin.site.register(ProvidersGroup)
admin.site.register(AdminsGroup)