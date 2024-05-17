from django.db import models
from . import fk
from .user import User
from .appointment import Appointment


class Payment(models.Model):

    appointment = fk(Appointment)
    patient = fk(User)
    value = models.FloatField()
    date = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)


