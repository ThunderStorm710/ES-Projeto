from django.db import models


class Specialty(models.Model):

    indicator = models.CharField(max_length=10)
