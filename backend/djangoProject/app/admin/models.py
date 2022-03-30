from django.db import models
from django.core.validators import validate_email
from rest_framework.serializers import ValidationError
import time
from djangoProject.app.user.models import User

class Admin(models.Model):
    name = models.CharField(max_length=256)
    cost = models.IntegerField()
    profit = models.IntegerField()

    def __str__(self):
        return self.name

class AdminsGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    __name__ = "AdminsGroup"

    def __str__(self):
        return str(self.id)