from django.db import models
from django.core.validators import validate_email
from rest_framework.serializers import ValidationError
import time
from djangoProject.app.user.models import User

class Provider(models.Model):
    name = models.CharField(max_length=256)
    cost = models.IntegerField()
    income = models.IntegerField()

    def __str__(self):
        return self.name

class ProvidersGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    count = models.IntegerField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.provider)