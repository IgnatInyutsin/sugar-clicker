from django.db import models
from django.core.validators import validate_email
from rest_framework.serializers import ValidationError

# Модели Django

class User(models.Model):
    name = models.CharField(max_length=256, unique=True)
    email = models.CharField(max_length=256, unique=True, validators=[validate_email])
    pass_cache = models.CharField(max_length=256)
    session_uuid = models.CharField(max_length=256)
    registration_at = models.IntegerField()
    sugar_all_time = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    last_passive_income_data = models.IntegerField()

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=256)
    cost = models.IntegerField()
    income = models.IntegerField()

    def __str__(self):
        return self.name

class Admin(models.Model):
    name = models.CharField(max_length=256)
    cost = models.IntegerField()
    profit = models.IntegerField()

    def __str__(self):
        return self.name

class ProvidersGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    count = models.IntegerField
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,)

    def __str__(self):
        return self.provider_id

class AdminsGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    __name__ = "AdminsGroup"

    def __str__(self):
        return str(self.id)