from django.db import models
from django.core.validators import validate_email
from rest_framework.serializers import ValidationError
import time

class User(models.Model):
    name = models.CharField(max_length=256, unique=True)
    email = models.EmailField(max_length=256, unique=True, validators=[validate_email])
    pass_cache = models.CharField(max_length=256)
    registration_at = models.IntegerField(default=time.time)
    sugar_all_time = models.BigIntegerField(default=0)
    balance = models.BigIntegerField(default=0)
    last_passive_income_data = models.IntegerField(default=time.time)
    session_uuid = models.UUIDField(null=True)
    auth = models.UUIDField(null=True, default=None)
    is_auth = models.BooleanField(default=False)

    def __str__(self):
        return self.name