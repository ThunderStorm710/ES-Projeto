from django.contrib.auth.models import User as AuthUser
from django.db import models
from backend.clinicaSaude.clinicaSaudeApp.models import fk


class User(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
