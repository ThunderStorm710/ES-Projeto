from django.contrib.auth.models import User as AuthUser
from django.db import models


class User(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
