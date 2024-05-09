from django.db import models


class Doctor(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    specialty = models.CharField(max_length=255, null=True, blank=True)

