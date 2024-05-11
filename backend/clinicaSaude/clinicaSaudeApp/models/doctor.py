from django.db import models
from . import fk
from .specialty import Specialty


class Doctor(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    specialty = fk(Specialty)

